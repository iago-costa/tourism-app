import { redirect } from '@sveltejs/kit';

export type AuthConfig = {
	allow_password_auth: boolean;
	google_oauth_configured: boolean;
	social_oauth_per_user: boolean;
};

/** @deprecated Use fetchAuthConfig() — kept for tests; do not gate UI on DEV alone. */
export const isPasswordAuthEnabled = import.meta.env.DEV;

export async function fetchAuthConfig(): Promise<AuthConfig> {
	const res = await fetch('/api/v1/auth/config');
	if (!res.ok) {
		throw new Error('Failed to load auth config');
	}
	return res.json();
}

/** Redirect to /login when password auth is disabled (production). */
export async function loadAuthConfigOrRedirectPassword(): Promise<AuthConfig> {
	const config = await fetchAuthConfig();
	if (!config.allow_password_auth) {
		throw redirect(302, '/login');
	}
	return config;
}
