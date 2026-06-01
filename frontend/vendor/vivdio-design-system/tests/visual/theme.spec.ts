import { test, expect } from '@playwright/test';

/**
 * Smoke visual: tokens aplicados via data-theme (rodar com app piloto ou Storybook futuro).
 * Por ora valida HTML estático mínimo servido localmente se VIVDIO_VISUAL_URL estiver setado.
 */
const base = process.env.VIVDIO_VISUAL_URL;

test.describe('design tokens', () => {
  test.skip(!base, 'defina VIVDIO_VISUAL_URL (ex. https://vitrine.vivdio.com)');

  test('página carrega sem texto de credencial vazado', async ({ page }) => {
    await page.goto(base!);
    const html = await page.content();
    expect(html).not.toMatch(/FAL_API_KEY|GOOGLE_CLIENT_SECRET|demo@study\.dev/);
  });

  test('snapshot da home', async ({ page }) => {
    await page.goto(base!);
    await expect(page).toHaveScreenshot('home.png', { maxDiffPixelRatio: 0.02 });
  });
});
