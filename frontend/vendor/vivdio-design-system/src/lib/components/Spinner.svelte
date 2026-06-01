<script lang="ts">
  interface Props {
    size?: number;
    label?: string;
    class?: string;
  }

  let { size = 24, label = 'Loading', class: className = '' }: Props = $props();
</script>

<div
  class={className}
  role="status"
  aria-live="polite"
  aria-label={label}
  style="display: inline-block; width: {size}px; height: {size}px;"
>
  <svg
    width={size}
    height={size}
    viewBox="0 0 24 24"
    fill="none"
    aria-hidden="true"
    class="vd-spinner__svg"
  >
    <circle cx="12" cy="12" r="10" stroke="var(--vd-color-border)" stroke-width="3" />
    <path
      d="M12 2a10 10 0 0 1 10 10"
      stroke="var(--vd-color-primary)"
      stroke-width="3"
      stroke-linecap="round"
    />
  </svg>
</div>

