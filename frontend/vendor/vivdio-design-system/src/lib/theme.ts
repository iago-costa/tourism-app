export type ThemeMode = 'light' | 'dark' | 'system';

const STORAGE_KEY = 'vivdio-theme';

export function getStoredTheme(): ThemeMode {
  if (typeof localStorage === 'undefined') return 'system';
  const v = localStorage.getItem(STORAGE_KEY);
  if (v === 'light' || v === 'dark' || v === 'system') return v;
  return 'system';
}

export function resolveTheme(mode: ThemeMode): 'light' | 'dark' {
  if (mode === 'light' || mode === 'dark') return mode;
  if (typeof matchMedia === 'undefined') return 'light';
  return matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

export function applyTheme(mode: ThemeMode): 'light' | 'dark' {
  const resolved = resolveTheme(mode);
  if (typeof document !== 'undefined') {
    document.documentElement.setAttribute('data-theme', resolved);
  }
  return resolved;
}

export function setTheme(mode: ThemeMode): void {
  if (typeof localStorage !== 'undefined') {
    localStorage.setItem(STORAGE_KEY, mode);
  }
  applyTheme(mode);
}

export function initTheme(mode: ThemeMode = getStoredTheme()): () => void {
  applyTheme(mode);
  if (mode !== 'system' || typeof matchMedia === 'undefined') {
    return () => {};
  }
  const mq = matchMedia('(prefers-color-scheme: dark)');
  const handler = () => applyTheme('system');
  mq.addEventListener('change', handler);
  return () => mq.removeEventListener('change', handler);
}
