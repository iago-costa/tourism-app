import { clearTokens, readAccessToken, readRefreshToken, saveTokens } from "$lib/auth";

async function tryRefreshToken(): Promise<string> {
  const refreshToken = readRefreshToken();
  if (!refreshToken) return "";
  const response = await fetch("/api/v1/auth/refresh", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh_token: refreshToken }),
  });
  if (!response.ok) {
    clearTokens();
    return "";
  }
  const data = await response.json();
  const newAccess = data.access_token || "";
  if (newAccess) saveTokens(newAccess, refreshToken);
  return newAccess;
}

export async function apiFetch(url: string, init: RequestInit = {}): Promise<Response> {
  const headers = new Headers(init.headers || {});
  const accessToken = readAccessToken();
  if (accessToken) headers.set("Authorization", `Bearer ${accessToken}`);
  let response = await fetch(url, { ...init, headers });
  if (response.status !== 401 || !accessToken) return response;

  const refreshedToken = await tryRefreshToken();
  if (!refreshedToken) return response;

  headers.set("Authorization", `Bearer ${refreshedToken}`);
  response = await fetch(url, { ...init, headers });
  return response;
}
