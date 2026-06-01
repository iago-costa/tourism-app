<script lang="ts">
  import type { HTMLInputAttributes } from 'svelte/elements';

  interface Props {
    id?: string;
    name?: string;
    type?: string;
    value?: string;
    placeholder?: string;
    required?: boolean;
    disabled?: boolean;
    autocomplete?: HTMLInputAttributes['autocomplete'];
    label?: string;
    error?: string;
    hint?: string;
    class?: string;
    oninput?: (e: Event) => void;
  }

  let {
    id,
    name,
    type = 'text',
    value = $bindable(''),
    placeholder = '',
    required = false,
    disabled = false,
    autocomplete,
    label,
    error,
    hint,
    class: className = '',
    oninput
  }: Props = $props();

  const inputId = $derived(id ?? name ?? undefined);
  const describedBy = $derived(
    [error ? `${inputId}-error` : null, hint ? `${inputId}-hint` : null]
      .filter(Boolean)
      .join(' ') || undefined
  );
</script>

<div class="vd-stack" style="gap: var(--vd-space-2);">
  {#if label && inputId}
    <label for={inputId} style="font-size: var(--vd-text-sm); font-weight: var(--vd-font-medium); color: var(--vd-color-fg);">
      {label}
      {#if required}<span aria-hidden="true"> *</span>{/if}
    </label>
  {/if}
  <input
    id={inputId}
    {name}
    {type}
    bind:value
    {placeholder}
    {required}
    {disabled}
    {autocomplete}
    class="vd-input {className}"
    aria-invalid={error ? 'true' : undefined}
    aria-describedby={describedBy}
    {oninput}
  />
  {#if hint && inputId}
    <p id="{inputId}-hint" style="font-size: var(--vd-text-xs); color: var(--vd-color-fg-subtle); margin: 0;">{hint}</p>
  {/if}
  {#if error && inputId}
    <p id="{inputId}-error" role="alert" style="font-size: var(--vd-text-xs); color: var(--vd-color-danger); margin: 0;">{error}</p>
  {/if}
</div>
