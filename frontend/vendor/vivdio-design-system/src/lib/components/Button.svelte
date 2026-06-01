<script lang="ts">
  import type { Snippet } from 'svelte';
  import { t } from '../i18n.js';

  type Variant = 'primary' | 'secondary' | 'ghost' | 'danger';

  interface Props {
    variant?: Variant;
    type?: 'button' | 'submit' | 'reset';
    disabled?: boolean;
    loading?: boolean;
    href?: string;
    class?: string;
    children?: Snippet;
    onclick?: (e: MouseEvent) => void;
    'aria-label'?: string;
  }

  let {
    variant = 'primary',
    type = 'button',
    disabled = false,
    loading = false,
    href,
    class: className = '',
    children,
    onclick,
    'aria-label': ariaLabel
  }: Props = $props();

  const isDisabled = $derived(disabled || loading);
  const classes = $derived(
    `vd-btn vd-btn--${variant} ${className}`.trim()
  );
</script>

{#if href && !isDisabled}
  <a {href} class={classes} role="button" aria-label={ariaLabel} onclick={onclick}>
    {#if loading}<span class="vd-sr-only">{t('button.loading')}</span>{/if}
    {@render children?.()}
  </a>
{:else}
  <button
    {type}
    class={classes}
    disabled={isDisabled}
    aria-disabled={isDisabled}
    aria-busy={loading}
    aria-label={ariaLabel}
    {onclick}
  >
    {#if loading}<span class="vd-sr-only">{t('button.loading')}</span>{/if}
    {@render children?.()}
  </button>
{/if}
