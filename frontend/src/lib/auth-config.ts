import { redirect } from '@sveltejs/kit';
import { getApiBase } from '$lib/api/base';

export type AuthConfig = {
	allow_password_auth: boolean;
	google_oauth_configured: boolean;
	social_oauth_per_user: boolean;
};

function normalizeAuthConfig(raw: Partial<AuthConfig>): AuthConfig {
	const allowPassword = raw.allow_password_auth ?? false;
	return {
		allow_password_auth: allowPassword,
		google_oauth_configured: raw.google_oauth_configured ?? !allowPassword,
		social_oauth_per_user: raw.social_oauth_per_user ?? !allowPassword
	};
}

/** @deprecated Use fetchAuthConfig() — kept for tests; do not gate UI on DEV alone. */
export const isPasswordAuthEnabled = import.meta.env.DEV;

const PRODUCTION_AUTH_CONFIG: AuthConfig = {
	allow_password_auth: false,
	google_oauth_configured: true,
	social_oauth_per_user: true
};

export async function fetchAuthConfig(): Promise<AuthConfig> {
	try {
		const base = getApiBase();
		const prefix = base.endsWith('/api/v1') ? base : `${base}/api/v1`;
		const path = prefix.endsWith('/auth/config') ? prefix : `${prefix}/auth/config`;
		const res = await fetch(path);
		if (!res.ok) {
			throw new Error('Failed to load auth config');
		}
		return res.json();
	} catch {
		if (import.meta.env.PROD) {
			return normalizeAuthConfig(PRODUCTION_AUTH_CONFIG);
		}
		return normalizeAuthConfig({ allow_password_auth: true });
	}
}

/** Redirect to /login when password auth is disabled (production). */
export async function loadAuthConfigOrRedirectPassword(): Promise<AuthConfig> {
	const config = await fetchAuthConfig();
	if (!config.allow_password_auth) {
		throw redirect(302, '/login');
	}
	return config;
}
