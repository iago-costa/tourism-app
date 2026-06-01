import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vite";

export default defineConfig(({ mode }) => ({
  plugins: [sveltekit()],
	ssr: {
		noExternal: ['@vivdio/design-system']
	},
  build: { sourcemap: false },
  esbuild: { drop: mode === 'production' ? ['console', 'debugger'] : [] }
}));
