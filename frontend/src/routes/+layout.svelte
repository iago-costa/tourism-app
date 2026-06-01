<script lang="ts">
  import '../app.css';
  import { ThemeProvider, OfflineIndicator, InstallPrompt } from '@vivdio/design-system';

  let { children } = $props();
</script>

<ThemeProvider>
  <OfflineIndicator />
  <InstallPrompt storageKey="tourism-pwa-install" />
  {@render children()}
</ThemeProvider>
