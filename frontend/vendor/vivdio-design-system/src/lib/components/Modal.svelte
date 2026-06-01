<script lang="ts">
  import { onMount } from 'svelte';
  import type { Snippet } from 'svelte';
  import { trapFocus } from '../a11y.js';
  import { t } from '../i18n.js';
  import Button from './Button.svelte';

  interface Props {
    open?: boolean;
    title: string;
    class?: string;
    children?: Snippet;
    onclose?: () => void;
  }

  let { open = $bindable(false), title, class: className = '', children, onclose }: Props = $props();

  let panelEl = $state<HTMLDivElement | null>(null);
  let releaseFocus: (() => void) | undefined;

  $effect(() => {
    if (!open) {
      releaseFocus?.();
      releaseFocus = undefined;
      return;
    }
    if (panelEl) {
      releaseFocus = trapFocus(panelEl);
    }
    return () => releaseFocus?.();
  });

  function close() {
    open = false;
    onclose?.();
  }

  function onBackdrop(e: MouseEvent) {
    if (e.target === e.currentTarget) close();
  }

  function onKeydown(e: KeyboardEvent) {
    if (e.key === 'Escape') close();
  }

  onMount(() => {
    if (typeof document === 'undefined') return;
    const handler = (e: KeyboardEvent) => {
      if (open && e.key === 'Escape') close();
    };
    document.addEventListener('keydown', handler);
    return () => document.removeEventListener('keydown', handler);
  });
</script>

{#if open}
  <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
  <div
    class="vd-modal-backdrop {className}"
    role="presentation"
    onclick={onBackdrop}
    onkeydown={onKeydown}
    style="position: fixed; inset: 0; z-index: var(--vd-z-modal); display: flex; align-items: flex-end; justify-content: center; padding: var(--vd-space-4); background: var(--vd-color-overlay);"
  >
    <div
      bind:this={panelEl}
      role="dialog"
      aria-modal="true"
      aria-labelledby="vd-modal-title"
      style="width: 100%; max-width: 32rem; max-height: 90dvh; overflow: auto; border-radius: var(--vd-radius-2xl); background: var(--vd-color-bg-elevated); padding: var(--vd-space-6); box-shadow: var(--vd-shadow-lg);"
    >
      <div class="vd-cluster" style="justify-content: space-between; margin-bottom: var(--vd-space-4);">
        <h2 id="vd-modal-title" style="margin: 0; font-size: var(--vd-text-xl); color: var(--vd-color-fg);">{title}</h2>
        <Button variant="ghost" aria-label={t('modal.close')} onclick={close}>×</Button>
      </div>
      {@render children?.()}
    </div>
  </div>
{/if}
