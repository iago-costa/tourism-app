<script lang="ts">
  import { onMount } from "svelte";
  import { goto } from "$app/navigation";
  import { page } from "$app/stores";
  import { saveTokens } from "$lib/auth";

  let message = "Conectando com Google...";

  onMount(async () => {
    const code = $page.url.searchParams.get("code");
    if (!code) {
      message = "Código de autorização ausente";
      return;
    }
    const res = await fetch("/api/v1/auth/google/callback", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code }),
    });
    const data = await res.json();
    if (data.access_token) {
      saveTokens(data.access_token, data.refresh_token || data.access_token);
      goto("/");
      return;
    }
    message = data.detail || "Falha na autenticação Google";
  });
</script>

<main>
  <p>{message}</p>
  {#if message !== "Conectando com Google..."}
    <a href="/login">Voltar ao login</a>
  {/if}
</main>
