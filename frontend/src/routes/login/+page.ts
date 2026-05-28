import type { PageLoad } from './$types';
import { fetchAuthConfig } from '$lib/auth-config';

export const load: PageLoad = async () => {
	const authConfig = await fetchAuthConfig();
	return { authConfig };
};
