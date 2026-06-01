import { describe, expect, it, beforeEach, afterEach } from 'vitest';
import { applyTheme, resolveTheme, setTheme, getStoredTheme } from './theme.js';

describe('theme', () => {
  beforeEach(() => {
    localStorage.clear();
    document.documentElement.removeAttribute('data-theme');
  });

  afterEach(() => {
    localStorage.clear();
  });

  it('resolveTheme respects explicit modes', () => {
    expect(resolveTheme('light')).toBe('light');
    expect(resolveTheme('dark')).toBe('dark');
  });

  it('applyTheme sets data-theme on document', () => {
    applyTheme('dark');
    expect(document.documentElement.getAttribute('data-theme')).toBe('dark');
  });

  it('setTheme persists preference', () => {
    setTheme('light');
    expect(getStoredTheme()).toBe('light');
    expect(localStorage.getItem('vivdio-theme')).toBe('light');
  });
});
