<script lang="ts">
  import type { Snippet } from 'svelte';

  interface Props {
    title?: string;
    class?: string;
    children?: Snippet;
    header?: Snippet;
    footer?: Snippet;
  }

  let { title, class: className = '', children, header, footer }: Props = $props();
</script>

<article class="vd-card {className}" style="padding: var(--vd-space-6);">
  {#if header}
    <header style="margin-bottom: var(--vd-space-4);">{@render header()}</header>
  {:else if title}
    <h2 style="font-size: var(--vd-text-lg); font-weight: var(--vd-font-semibold); margin: 0 0 var(--vd-space-4); color: var(--vd-color-fg);">
      {title}
    </h2>
  {/if}
  <div>{@render children?.()}</div>
  {#if footer}
    <footer style="margin-top: var(--vd-space-4); padding-top: var(--vd-space-4); border-top: 1px solid var(--vd-color-border);">
      {@render footer()}
    </footer>
  {/if}
</article>
