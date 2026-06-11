<script lang="ts">
  import { onMount } from 'svelte';
  import { initChaskiq } from '$lib/vivdio-chaskiq';
  import '../app.css';
  import { ThemeProvider, OfflineIndicator, InstallPrompt } from '@vivdio/design-system';

  onMount(() => initChaskiq());

  let { children } = $props();
</script>

<ThemeProvider>
  <OfflineIndicator />
  <InstallPrompt storageKey="tourism-pwa-install" />
  {@render children()}
</ThemeProvider>
