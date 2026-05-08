<script lang="ts">
  let token = "";
  let newPassword = "";
  let message = "";

  async function submit(event: SubmitEvent) {
    event.preventDefault();
    const res = await fetch("/api/v1/auth/reset-password", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ token, new_password: newPassword }),
    });
    const data = await res.json();
    message = data.message || data.detail || "Senha atualizada";
  }
</script>

<main>
  <h1>Redefinir senha</h1>
  <form on:submit={submit}>
    <input bind:value={token} required placeholder="Token recebido por email" />
    <input type="password" bind:value={newPassword} required placeholder="Nova senha" />
    <button type="submit">Salvar nova senha</button>
  </form>
  <p>{message}</p>
</main>
