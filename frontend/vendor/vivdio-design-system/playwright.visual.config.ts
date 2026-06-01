import { defineConfig, devices } from '@playwright/test';

/**
 * Visual regression for design system — run from consuming app or Storybook when added.
 * npx playwright test -c playwright.visual.config.ts
 */
export default defineConfig({
  testDir: './tests/visual',
  snapshotDir: './tests/visual/snapshots',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  use: {
    trace: 'on-first-retry'
  },
  projects: [
    { name: 'Mobile Chrome', use: { ...devices['Pixel 5'] } },
    { name: 'Mobile Safari', use: { ...devices['iPhone 12'] } },
    { name: 'Desktop Chrome', use: { ...devices['Desktop Chrome'] } }
  ]
});
