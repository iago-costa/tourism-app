<script lang="ts">
  import { onMount } from 'svelte';
  import type { Snippet } from 'svelte';
  import { getStoredTheme, initTheme, type ThemeMode } from '../theme.js';

  interface Props {
    initial?: ThemeMode;
    children?: Snippet;
  }

  let { initial, children }: Props = $props();

  onMount(() => initTheme(initial ?? getStoredTheme()));
</script>

{@render children?.()}
