import { describe, expect, it } from 'vitest';
import { setLocale, t } from './i18n.js';

describe('i18n', () => {
  it('returns pt messages by default', () => {
    expect(t('pwa.offline')).toContain('offline');
  });

  it('switches locale', () => {
    setLocale('en');
    expect(t('pwa.offline')).toBe('You are offline');
    setLocale('pt');
  });
});
