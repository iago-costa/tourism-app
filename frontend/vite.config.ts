import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vite";
import { vivdioPwa } from '@vivdio/design-system/vite/pwa';

export default defineConfig(({ mode }) => ({
  plugins: [sveltekit(), vivdioPwa({ name: 'Tourism', themeColor: '#14b8a6' })],
	ssr: {
		noExternal: ['@vivdio/design-system']
	},
  build: { sourcemap: false },
  esbuild: { drop: mode === 'production' ? ['console', 'debugger'] : [] }
}));
