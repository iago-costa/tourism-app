<script lang="ts">
  import type { Snippet } from 'svelte';

  type Tone = 'neutral' | 'success' | 'warning' | 'danger' | 'info';

  interface Props {
    tone?: Tone;
    class?: string;
    children?: Snippet;
  }

  let { tone = 'neutral', class: className = '', children }: Props = $props();

  const bg = $derived({
    neutral: 'var(--vd-color-bg-muted)',
    success: 'var(--vd-color-success)',
    warning: 'var(--vd-color-warning)',
    danger: 'var(--vd-color-danger)',
    info: 'var(--vd-color-info)'
  }[tone]);

  const fg = $derived({
    neutral: 'var(--vd-color-fg-muted)',
    success: 'var(--vd-color-on-success)',
    warning: 'var(--vd-color-on-warning)',
    danger: 'var(--vd-color-on-danger)',
    info: 'var(--vd-color-on-info)'
  }[tone]);
</script>

<span class="vd-badge {className}" style="background: {bg}; color: {fg};">
  {@render children?.()}
</span>
