<script lang="ts">
  import { onMount } from 'svelte';
  import { t } from '../../i18n.js';
  import Button from '../Button.svelte';
  import Card from '../Card.svelte';

  interface Props {
    onrequest?: () => void | Promise<void>;
    dismissedKey?: string;
  }

  let { onrequest, dismissedKey = 'vivdio-push-dismissed' }: Props = $props();
  let visible = $state(false);

  onMount(() => {
    if (typeof Notification === 'undefined') return;
    if (Notification.permission !== 'default') return;
    if (localStorage.getItem(dismissedKey)) return;
    visible = true;
  });

  async function enable() {
    await onrequest?.();
    visible = false;
  }

  function dismiss() {
    visible = false;
    localStorage.setItem(dismissedKey, '1');
  }
</script>

{#if visible}
  <div
    role="region"
    aria-label={t('pwa.push.title')}
    style="position: fixed; top: var(--vd-space-4); left: var(--vd-space-4); right: var(--vd-space-4); z-index: var(--vd-z-toast); max-width: 24rem; margin-inline: auto;"
  >
    <Card>
      <p style="margin: 0 0 var(--vd-space-3); font-size: var(--vd-text-sm); color: var(--vd-color-fg-muted);">
        {t('pwa.push.title')}
      </p>
      <div class="vd-cluster">
        <Button variant="primary" onclick={enable}>{t('pwa.push.enable')}</Button>
        <Button variant="ghost" onclick={dismiss}>{t('pwa.install.dismiss')}</Button>
      </div>
    </Card>
  </div>
{/if}
