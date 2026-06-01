<script lang="ts">
  import type { Snippet } from 'svelte';

  interface Props {
    href?: string;
    class?: string;
    children?: Snippet;
    onclick?: () => void;
  }

  let { href, class: className = '', children, onclick }: Props = $props();
</script>

<li
  style="border-radius: var(--vd-radius-lg); border: 1px solid var(--vd-color-border); background: var(--vd-color-bg-elevated); min-height: var(--vd-touch-min);"
>
  {#if href}
    <a
      {href}
      class={className}
      style="display: flex; align-items: center; padding: var(--vd-space-3) var(--vd-space-4); color: inherit; text-decoration: none; min-height: var(--vd-touch-min);"
    >
      {@render children?.()}
    </a>
  {:else}
    <button
      type="button"
      class={className}
      style="display: flex; width: 100%; align-items: center; padding: var(--vd-space-3) var(--vd-space-4); background: transparent; border: none; color: inherit; cursor: pointer; min-height: var(--vd-touch-min); text-align: left;"
      {onclick}
    >
      {@render children?.()}
    </button>
  {/if}
</li>
