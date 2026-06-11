"""Lightweight in-memory rate limit for auth POST endpoints (no extra deps)."""

from __future__ import annotations

import time
from collections import defaultdict

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

_AUTH_PATH_MARKERS = (
    "/login",
    "/register",
    "/forgot-password",
    "/reset-password",
)


class AuthRateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app,
        *,
        enabled: bool = True,
        limit: int = 30,
        window_seconds: int = 60,
    ) -> None:
        super().__init__(app)
        self._enabled = enabled
        self._limit = limit
        self._window = window_seconds
        self._hits: dict[str, list[float]] = defaultdict(list)

    def _client_key(self, request: Request) -> str:
        forwarded = request.headers.get("x-forwarded-for", "").split(",")[0].strip()
        if forwarded:
            return forwarded
        if request.client:
            return request.client.host
        return "unknown"

    async def dispatch(self, request: Request, call_next) -> Response:
        if not self._enabled or request.method.upper() != "POST":
            return await call_next(request)

        path = request.url.path.lower()
        if not any(marker in path for marker in _AUTH_PATH_MARKERS):
            return await call_next(request)

        now = time.monotonic()
        key = f"{self._client_key(request)}:{path}"
        window_start = now - self._window
        recent = [t for t in self._hits[key] if t >= window_start]
        if len(recent) >= self._limit:
            return JSONResponse(status_code=429, content={"detail": "Too many requests"})
        recent.append(now)
        self._hits[key] = recent
        return await call_next(request)
