import { browser } from '$app/environment';

/** API base: browser uses same-origin proxy; SSR needs absolute URL. */
export function getApiBase(): string {
	const explicit = import.meta.env.VITE_API_URL as string | undefined;
	if (explicit) return explicit.replace(/\/$/, '');

	if (browser) return '';

	const internal =
		typeof process !== 'undefined' && process.env.API_INTERNAL_URL
			? process.env.API_INTERNAL_URL
			: '';
	if (internal) return internal.replace(/\/$/, '');

	const origin = typeof process !== 'undefined' && process.env.ORIGIN ? process.env.ORIGIN : '';
	if (origin) return `${origin.replace(/\/$/, '')}/api/v1`;

	return 'https://tourism.vivdio.com/api/v1';
}
