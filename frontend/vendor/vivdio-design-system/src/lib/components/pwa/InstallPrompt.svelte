<script lang="ts">
  import { onMount } from 'svelte';
  import { t } from '../../i18n.js';
  import Button from '../Button.svelte';
  import Card from '../Card.svelte';

  interface BeforeInstallPromptEvent extends Event {
    prompt: () => Promise<void>;
    userChoice: Promise<{ outcome: 'accepted' | 'dismissed' }>;
  }

  interface Props {
    storageKey?: string;
  }

  let { storageKey = 'vivdio-pwa-install-dismissed' }: Props = $props();

  let deferred = $state<BeforeInstallPromptEvent | null>(null);
  let visible = $state(false);

  onMount(() => {
    if (localStorage.getItem(storageKey)) return;

    const handler = (e: Event) => {
      e.preventDefault();
      deferred = e as BeforeInstallPromptEvent;
      visible = true;
    };
    window.addEventListener('beforeinstallprompt', handler);
    return () => window.removeEventListener('beforeinstallprompt', handler);
  });

  async function install() {
    if (!deferred) return;
    await deferred.prompt();
    visible = false;
    deferred = null;
  }

  function dismiss() {
    visible = false;
    localStorage.setItem(storageKey, '1');
  }
</script>

{#if visible}
  <div
    role="region"
    aria-label={t('pwa.install.title')}
    style="position: fixed; bottom: var(--vd-space-4); left: var(--vd-space-4); right: var(--vd-space-4); z-index: var(--vd-z-toast); max-width: 24rem; margin-inline: auto;"
  >
    <Card title={t('pwa.install.title')}>
      <div class="vd-cluster" style="margin-top: var(--vd-space-3);">
        <Button variant="primary" onclick={install}>{t('pwa.install.action')}</Button>
        <Button variant="ghost" onclick={dismiss}>{t('pwa.install.dismiss')}</Button>
      </div>
    </Card>
  </div>
{/if}
