<script lang="ts">
  import { goto } from '$app/navigation';
  import { saveTokens } from '$lib/auth';
  import { Button, Input, Card } from '@vivdio/design-system';
  import type { PageData } from './$types';

  let { data }: { data: PageData } = $props();

  let email = $state('');
  let password = $state('');
  let message = $state('');
  let googleLoading = $state(false);

  async function loginWithGoogle() {
    googleLoading = true;
    try {
      const res = await fetch('/api/v1/auth/google/start');
      const payload = await res.json();
      if (!res.ok || !payload.authorize_url) {
        message = payload.detail || 'Não foi possível iniciar o login.';
        googleLoading = false;
        return;
      }
      window.location.href = payload.authorize_url;
    } catch {
      message = 'Falha ao iniciar login com Google';
      googleLoading = false;
    }
  }

  async function submit(event: SubmitEvent) {
    event.preventDefault();
    const res = await fetch('/api/v1/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    const payload = await res.json();
    const token = payload.access_token || '';
    const refresh = payload.refresh_token || token;
    if (token) {
      saveTokens(token, refresh);
      goto('/');
      return;
    }
    message = payload.detail || 'Falha no login';
  }
</script>

<main class="vd-page">
  <Card title="Login">
    <div class="vd-stack" style="gap: var(--vd-space-4);">
      <Button variant="primary" onclick={loginWithGoogle} loading={googleLoading} type="button">
        {googleLoading ? 'Redirecionando…' : 'Entrar com Google'}
      </Button>

      {#if data.authConfig.allow_password_auth}
        <form onsubmit={submit} class="vd-stack" style="gap: var(--vd-space-3);">
          <Input label="E-mail" type="email" bind:value={email} required autocomplete="email" />
          <Input
            label="Senha"
            type="password"
            bind:value={password}
            required
            autocomplete="current-password"
          />
          <Button variant="secondary" type="submit">Entrar com e-mail</Button>
        </form>
        <p style="font-size: var(--vd-text-sm); margin: 0;">
          <a href="/cadastro">Criar conta</a>
        </p>
      {/if}

      {#if message}
        <p class="vd-msg" role="alert">{message}</p>
      {/if}
    </div>
  </Card>
</main>
