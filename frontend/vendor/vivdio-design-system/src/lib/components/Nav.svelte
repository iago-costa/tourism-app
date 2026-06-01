<script lang="ts">
  import type { Snippet } from 'svelte';
  import { t } from '../i18n.js';

  interface Props {
    brand?: Snippet;
    class?: string;
    children?: Snippet;
    mobileOpen?: boolean;
    onmenuclick?: () => void;
  }

  let {
    brand,
    class: className = '',
    children,
    mobileOpen = false,
    onmenuclick
  }: Props = $props();
</script>

<nav
  class={className}
  aria-label="Principal"
  style="position: sticky; top: 0; z-index: var(--vd-z-dropdown); border-bottom: 1px solid var(--vd-color-border); background: var(--vd-color-bg-elevated);"
>
  <div class="vd-container vd-cluster" style="min-height: var(--vd-touch-min); justify-content: space-between; padding-block: var(--vd-space-2);">
    <div class="vd-cluster">
      {#if onmenuclick}
        <button
          type="button"
          class="vd-btn vd-btn--ghost"
          aria-expanded={mobileOpen}
          aria-controls="vd-nav-links"
          aria-label={t('nav.menu')}
          onclick={onmenuclick}
          style="display: inline-flex; min-width: var(--vd-touch-min);"
        >
          ☰
        </button>
      {/if}
      {@render brand?.()}
    </div>
    <div
      id="vd-nav-links"
      class="vd-nav-links vd-cluster"
      style="gap: var(--vd-space-4);"
      hidden={onmenuclick && !mobileOpen ? true : undefined}
    >
      {@render children?.()}
    </div>
  </div>
</nav>

