const ACCESS_KEY = "tourism_access_token";
const REFRESH_KEY = "tourism_refresh_token";

export function saveTokens(accessToken: string, refreshToken: string) {
  localStorage.setItem(ACCESS_KEY, accessToken);
  localStorage.setItem(REFRESH_KEY, refreshToken);
}

export function readAccessToken() {
  return localStorage.getItem(ACCESS_KEY) || "";
}

export function readRefreshToken() {
  return localStorage.getItem(REFRESH_KEY) || "";
}

export function clearTokens() {
  localStorage.removeItem(ACCESS_KEY);
  localStorage.removeItem(REFRESH_KEY);
}
