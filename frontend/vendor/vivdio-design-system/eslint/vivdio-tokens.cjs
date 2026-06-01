/**
 * ESLint rule: discourage hardcoded hex colors in frontend when Vivdio DS is adopted.
 * Enable in consuming apps: plugins: { 'vivdio-ds': require('@vivdio/design-system/eslint/vivdio-tokens') }
 */
module.exports = {
  rules: {
    'vivdio/prefer-design-tokens': {
      meta: {
        type: 'suggestion',
        docs: {
          description: 'Prefer var(--vd-*) tokens over raw hex in styles'
        }
      },
      create(context) {
        const hex = /#[0-9a-fA-F]{3,8}\b/;
        return {
          Literal(node) {
            if (typeof node.value !== 'string' || !hex.test(node.value)) return;
            if (!/\.(svelte|css)$/.test(context.filename)) return;
            context.report({
              node,
              message: 'Use var(--vd-color-*) design tokens instead of hardcoded hex.'
            });
          }
        };
      }
    }
  }
};
