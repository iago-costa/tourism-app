/* Theme & i18n */
export {
  applyTheme,
  getStoredTheme,
  initTheme,
  resolveTheme,
  setTheme,
  type ThemeMode
} from './theme.js';
export { getLocale, setLocale, t, type Locale, type MessageKey } from './i18n.js';
export { trapFocus, uniqueId } from './a11y.js';

/* Components — tree-shake via direct imports */
export { default as Button } from './components/Button.svelte';
export { default as Input } from './components/Input.svelte';
export { default as Textarea } from './components/Textarea.svelte';
export { default as Card } from './components/Card.svelte';
export { default as Modal } from './components/Modal.svelte';
export { default as Nav } from './components/Nav.svelte';
export { default as List } from './components/List.svelte';
export { default as ListItem } from './components/ListItem.svelte';
export { default as Badge } from './components/Badge.svelte';
export { default as Spinner } from './components/Spinner.svelte';
export { default as ThemeProvider } from './components/ThemeProvider.svelte';
export { default as ThemeToggle } from './components/ThemeToggle.svelte';
export { default as OfflineIndicator } from './components/pwa/OfflineIndicator.svelte';
export { default as InstallPrompt } from './components/pwa/InstallPrompt.svelte';
export { default as PushNotificationBanner } from './components/pwa/PushNotificationBanner.svelte';
