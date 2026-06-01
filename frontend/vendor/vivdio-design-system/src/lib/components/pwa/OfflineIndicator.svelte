<script lang="ts">
  import { onMount } from 'svelte';
  import { t } from '../../i18n.js';
  import Badge from '../Badge.svelte';

  interface Props {
    syncing?: boolean;
  }

  let { syncing = false }: Props = $props();
  let online = $state(true);

  onMount(() => {
    online = navigator.onLine;
    const on = () => (online = true);
    const off = () => (online = false);
    window.addEventListener('online', on);
    window.addEventListener('offline', off);
    return () => {
      window.removeEventListener('online', on);
      window.removeEventListener('offline', off);
    };
  });
</script>

{#if !online}
  <div
    role="status"
    aria-live="polite"
    style="position: fixed; bottom: var(--vd-space-4); left: var(--vd-space-4); right: var(--vd-space-4); z-index: var(--vd-z-toast); display: flex; justify-content: center;"
  >
    <Badge tone="warning">
      {syncing ? t('pwa.offline.syncing') : t('pwa.offline')}
    </Badge>
  </div>
{/if}
