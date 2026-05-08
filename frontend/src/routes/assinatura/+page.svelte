<script lang="ts">
  import { apiFetch } from "$lib/api";
  import { readAccessToken } from "$lib/auth";

  let email = "";
  let accessToken = readAccessToken();
  let message = "";
  let subscriptionStatus = "";

  async function checkout(event: SubmitEvent) {
    event.preventDefault();
    const res = await fetch("/api/v1/billing/checkout", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ customer_email: email }),
    });
    const data = await res.json();
    if (data.checkout_url) {
      window.location.href = data.checkout_url;
      return;
    }
    message = data.detail || data.message || "Falha ao iniciar checkout";
  }

  async function loadSubscriptionStatus() {
    const res = await apiFetch("/api/v1/billing/me");
    const data = await res.json();
    subscriptionStatus = data.subscription?.status || "sem assinatura";
    if (data.detail) {
      message = data.detail;
    }
    accessToken = readAccessToken();
  }
</script>

<main>
  <h1>Assinatura Tourism</h1>
  <form on:submit={checkout}>
    <input type="email" bind:value={email} required placeholder="seu@email.com" />
    <button type="submit">Assinar com Stripe</button>
  </form>
  <hr />
  <input bind:value={accessToken} placeholder="Access token para consultar assinatura" />
  <button on:click={loadSubscriptionStatus}>Ver status da assinatura</button>
  <p>Status: {subscriptionStatus}</p>
  <p>{message}</p>
</main>
