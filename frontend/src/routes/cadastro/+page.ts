import type { PageLoad } from './$types';
import { loadAuthConfigOrRedirectPassword } from '$lib/auth-config';

export const load: PageLoad = async () => {
	const authConfig = await loadAuthConfigOrRedirectPassword();
	return { authConfig };
};
