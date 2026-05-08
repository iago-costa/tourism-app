<script lang="ts">
  const apiBase = "/api/v1";
</script>

<main>
  <h1>Tourism Web</h1>
  <p>Frontend web em SvelteKit alinhado ao padrao do Universal Study.</p>
  <ul>
    <li><a href={`${apiBase}/auth/google/start`}>Entrar com Google</a></li>
    <li><a href="/cadastro">Criar conta</a></li>
    <li><a href="/login">Entrar com email</a></li>
    <li><a href="/assinatura">Assinaturas (Stripe)</a></li>
    <li><a href="/recuperar-conta">Recuperar conta</a></li>
    <li><a href="/redefinir-senha">Redefinir senha</a></li>
  </ul>
</main>
