<script lang="ts">
  let email = "";
  let message = "";

  async function submit(event: SubmitEvent) {
    event.preventDefault();
    const res = await fetch("/api/v1/auth/recover-account", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email }),
    });
    const data = await res.json();
    message = data.message || "Solicitacao enviada";
  }
</script>

<main>
  <h1>Recuperar conta</h1>
  <form on:submit={submit}>
    <input type="email" bind:value={email} required placeholder="seu@email.com" />
    <button type="submit">Enviar email de recuperacao</button>
  </form>
  <p>{message}</p>
</main>
