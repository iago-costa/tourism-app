import { browser } from '$app/environment';
import { env } from '$env/dynamic/public';

declare global {
	interface Window {
		VIVDIO_CHASKIQ?: { appId: string; domain: string };
		chaskiqSettings?: { app_id: string; domain: string };
	}
}

/** Load Chaskiq messenger when PUBLIC_CHASKIQ_APP_KEY is set. */
export function initChaskiq(): void {
	if (!browser) return;
	const appId = env.PUBLIC_CHASKIQ_APP_KEY?.trim();
	if (!appId) return;

	window.VIVDIO_CHASKIQ = {
		appId,
		domain: env.PUBLIC_CHASKIQ_DOMAIN?.trim() || 'https://support.vivdio.com'
	};

	if (document.querySelector('script[data-vivdio-chaskiq]')) return;

	const s = document.createElement('script');
	s.src = '/vivdio-chaskiq.js';
	s.defer = true;
	s.setAttribute('data-vivdio-chaskiq', '1');
	document.body.appendChild(s);
}
