<script lang="ts">
  import { getStoredTheme, setTheme, type ThemeMode } from '../theme.js';
  import { t } from '../i18n.js';
  import Button from './Button.svelte';

  let mode = $state<ThemeMode>('system');

  $effect(() => {
    if (typeof localStorage !== 'undefined') {
      mode = getStoredTheme();
    }
  });

  const cycle: ThemeMode[] = ['light', 'dark', 'system'];

  function next() {
    const i = cycle.indexOf(mode);
    const nextMode = cycle[(i + 1) % cycle.length];
    mode = nextMode;
    setTheme(nextMode);
  }

  const label = $derived(
    mode === 'light' ? t('theme.light') : mode === 'dark' ? t('theme.dark') : t('theme.system')
  );
</script>

<Button variant="ghost" aria-label={label} onclick={next}>
  {mode === 'dark' ? '🌙' : mode === 'light' ? '☀️' : '◐'}
</Button>
