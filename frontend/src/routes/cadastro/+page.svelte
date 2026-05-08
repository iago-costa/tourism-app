<script lang="ts">
  let email = "";
  let fullName = "";
  let password = "";
  let message = "";

  async function submit(event: SubmitEvent) {
    event.preventDefault();
    const res = await fetch("/api/v1/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, full_name: fullName, password }),
    });
    const data = await res.json();
    message = data.message || data.detail || "Cadastro finalizado";
  }
</script>

<main>
  <h1>Criar conta</h1>
  <form on:submit={submit}>
    <input bind:value={fullName} placeholder="Nome completo" />
    <input type="email" bind:value={email} required placeholder="Email" />
    <input type="password" bind:value={password} required placeholder="Senha" />
    <button type="submit">Cadastrar</button>
  </form>
  <p>{message}</p>
</main>
