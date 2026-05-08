<script lang="ts">
  import { apiFetch } from "$lib/api";
  import { clearTokens, readAccessToken, readRefreshToken, saveTokens } from "$lib/auth";

  let email = "";
  let password = "";
  let token = readAccessToken();
  let refreshToken = readRefreshToken();
  let message = "";

  async function submit(event: SubmitEvent) {
    event.preventDefault();
    const res = await fetch("/api/v1/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    const data = await res.json();
    token = data.access_token || "";
    refreshToken = data.refresh_token || "";
    if (token && refreshToken) saveTokens(token, refreshToken);
    message = token ? "Login realizado" : data.detail || "Falha no login";
  }

  async function refreshAccessToken() {
    const res = await fetch("/api/v1/auth/refresh", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ refresh_token: refreshToken }),
    });
    const data = await res.json();
    token = data.access_token || token;
    if (token && refreshToken) saveTokens(token, refreshToken);
    message = data.access_token ? "Access token renovado" : data.detail || "Falha ao renovar token";
  }

  async function logout() {
    const res = await fetch("/api/v1/auth/logout", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ refresh_token: refreshToken }),
    });
    const data = await res.json();
    token = "";
    refreshToken = "";
    clearTokens();
    message = data.message || "Logout realizado";
  }

  async function loadProfile() {
    const res = await apiFetch("/api/v1/auth/me");
    const data = await res.json();
    message = data.email ? `Sessao ativa: ${data.email}` : data.detail || "Sem sessao";
    token = readAccessToken();
  }
</script>

<main>
  <h1>Login</h1>
  <form on:submit={submit}>
    <input type="email" bind:value={email} required placeholder="Email" />
    <input type="password" bind:value={password} required placeholder="Senha" />
    <button type="submit">Entrar</button>
  </form>
  <p>{message}</p>
  {#if token}<code>{token}</code>{/if}
  <div>
    <button type="button" on:click={refreshAccessToken} disabled={!refreshToken}>Renovar token</button>
    <button type="button" on:click={logout} disabled={!refreshToken}>Logout</button>
    <button type="button" on:click={loadProfile} disabled={!token}>Ver perfil</button>
  </div>
</main>
