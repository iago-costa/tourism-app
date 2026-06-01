/** Tailwind v3 preset — maps Vivdio tokens to theme.extend */
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--vd-font-sans)'],
        display: ['var(--vd-font-display)']
      },
      colors: {
        vd: {
          bg: 'var(--vd-color-bg)',
          elevated: 'var(--vd-color-bg-elevated)',
          muted: 'var(--vd-color-bg-muted)',
          fg: 'var(--vd-color-fg)',
          'fg-muted': 'var(--vd-color-fg-muted)',
          border: 'var(--vd-color-border)',
          primary: 'var(--vd-color-primary)',
          'primary-hover': 'var(--vd-color-primary-hover)',
          success: 'var(--vd-color-success)',
          warning: 'var(--vd-color-warning)',
          danger: 'var(--vd-color-danger)',
          info: 'var(--vd-color-info)'
        }
      },
      borderRadius: {
        vd-sm: 'var(--vd-radius-sm)',
        vd-md: 'var(--vd-radius-md)',
        vd-lg: 'var(--vd-radius-lg)',
        vd-xl: 'var(--vd-radius-xl)',
        'vd-2xl': 'var(--vd-radius-2xl)'
      },
      boxShadow: {
        'vd-sm': 'var(--vd-shadow-sm)',
        'vd-md': 'var(--vd-shadow-md)',
        'vd-lg': 'var(--vd-shadow-lg)',
        'vd-focus': 'var(--vd-shadow-focus)'
      },
      spacing: {
        'vd-1': 'var(--vd-space-1)',
        'vd-2': 'var(--vd-space-2)',
        'vd-4': 'var(--vd-space-4)',
        'vd-6': 'var(--vd-space-6)',
        'vd-8': 'var(--vd-space-8)'
      },
      minHeight: {
        touch: 'var(--vd-touch-min)'
      },
      minWidth: {
        touch: 'var(--vd-touch-min)'
      }
    }
  }
};
