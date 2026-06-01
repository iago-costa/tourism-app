export type Locale = 'pt' | 'en';

export type MessageKey =
  | 'button.loading'
  | 'input.required'
  | 'modal.close'
  | 'nav.menu'
  | 'pwa.offline'
  | 'pwa.offline.syncing'
  | 'pwa.install.title'
  | 'pwa.install.action'
  | 'pwa.install.dismiss'
  | 'pwa.push.title'
  | 'pwa.push.enable'
  | 'theme.light'
  | 'theme.dark'
  | 'theme.system';

const messages: Record<Locale, Record<MessageKey, string>> = {
  pt: {
    'button.loading': 'Carregando…',
    'input.required': 'Campo obrigatório',
    'modal.close': 'Fechar',
    'nav.menu': 'Menu',
    'pwa.offline': 'Você está offline',
    'pwa.offline.syncing': 'Sincronizando quando a conexão voltar…',
    'pwa.install.title': 'Instale o app na tela inicial',
    'pwa.install.action': 'Instalar',
    'pwa.install.dismiss': 'Agora não',
    'pwa.push.title': 'Ative notificações para não perder atualizações',
    'pwa.push.enable': 'Ativar',
    'theme.light': 'Tema claro',
    'theme.dark': 'Tema escuro',
    'theme.system': 'Tema do sistema'
  },
  en: {
    'button.loading': 'Loading…',
    'input.required': 'Required field',
    'modal.close': 'Close',
    'nav.menu': 'Menu',
    'pwa.offline': 'You are offline',
    'pwa.offline.syncing': 'Will sync when back online…',
    'pwa.install.title': 'Install this app on your home screen',
    'pwa.install.action': 'Install',
    'pwa.install.dismiss': 'Not now',
    'pwa.push.title': 'Enable notifications to stay updated',
    'pwa.push.enable': 'Enable',
    'theme.light': 'Light theme',
    'theme.dark': 'Dark theme',
    'theme.system': 'System theme'
  }
};

let currentLocale: Locale = 'pt';

export function setLocale(locale: Locale): void {
  currentLocale = locale;
}

export function getLocale(): Locale {
  return currentLocale;
}

export function t(key: MessageKey, locale: Locale = currentLocale): string {
  return messages[locale][key] ?? messages.pt[key] ?? key;
}
