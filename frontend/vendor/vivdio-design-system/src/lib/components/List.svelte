<script lang="ts">
  import type { Snippet } from 'svelte';

  interface Props {
    ordered?: boolean;
    class?: string;
    children?: Snippet;
  }

  let { ordered = false, class: className = '', children }: Props = $props();
</script>

<svelte:element
  this={ordered ? 'ol' : 'ul'}
  class={className}
  style="list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: var(--vd-space-2);"
>
  {@render children?.()}
</svelte:element>
