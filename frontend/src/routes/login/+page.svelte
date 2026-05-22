<script lang="ts">
  import { goto } from "$app/navigation";
  import { saveTokens } from "$lib/auth";
  import { isPasswordAuthEnabled } from "$lib/auth-config";

  let email = "";
  let password = "";
  let message = "";
  let googleLoading = false;

  async function loginWithGoogle() {
    googleLoading = true;
    try {
      const res = await fetch("/api/v1/auth/google/start");
      const data = await res.json();
      if (!res.ok || !data.authorize_url) {
        message = data.detail || "Google OAuth não disponível";
        googleLoading = false;
        return;
      }
      window.location.href = data.authorize_url;
    } catch {
      message = "Falha ao iniciar login com Google";
      googleLoading = false;
    }
  }

  async function submit(event: SubmitEvent) {
    event.preventDefault();
    const res = await fetch("/api/v1/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    const data = await res.json();
    const token = data.access_token || "";
    const refresh = data.refresh_token || token;
    if (token) {
      saveTokens(token, refresh);
      goto("/");
      return;
    }
    message = data.detail || "Falha no login";
  }
</script>

<main>
  <h1>Login</h1>

  <button type="button" on:click={loginWithGoogle} disabled={googleLoading}>
    {googleLoading ? "Redirecionando..." : "Entrar com Google"}
  </button>

  {#if isPasswordAuthEnabled}
    <form on:submit={submit}>
      <input type="email" bind:value={email} required placeholder="Email" />
      <input type="password" bind:value={password} required placeholder="Senha" />
      <button type="submit">Entrar com e-mail</button>
    </form>
    <p><a href="/cadastro">Criar conta</a></p>
  {/if}

  {#if message}<p>{message}</p>{/if}
</main>
