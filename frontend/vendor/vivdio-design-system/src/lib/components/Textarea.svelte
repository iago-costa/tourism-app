<script lang="ts">
  import type { HTMLTextareaAttributes } from 'svelte/elements';

  interface Props {
    id?: string;
    name?: string;
    value?: string;
    placeholder?: string;
    required?: boolean;
    disabled?: boolean;
    rows?: number;
    label?: string;
    error?: string;
    class?: string;
    oninput?: (e: Event) => void;
  }

  let {
    id,
    name,
    value = $bindable(''),
    placeholder = '',
    required = false,
    disabled = false,
    rows = 4,
    label,
    error,
    class: className = '',
    oninput
  }: Props = $props();

  const areaId = $derived(id ?? name ?? undefined);
</script>

<div class="vd-stack" style="gap: var(--vd-space-2);">
  {#if label && areaId}
    <label for={areaId} style="font-size: var(--vd-text-sm); font-weight: var(--vd-font-medium);">
      {label}
    </label>
  {/if}
  <textarea
    id={areaId}
    {name}
    bind:value
    {placeholder}
    {required}
    {disabled}
    {rows}
    class="vd-input {className}"
    style="min-height: auto; resize: vertical;"
    aria-invalid={error ? 'true' : undefined}
    {oninput}
  ></textarea>
  {#if error}
    <p role="alert" style="font-size: var(--vd-text-xs); color: var(--vd-color-danger); margin: 0;">{error}</p>
  {/if}
</div>
