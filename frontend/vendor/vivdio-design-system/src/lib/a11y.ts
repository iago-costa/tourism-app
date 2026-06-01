/** Generate stable id for aria-labelledby / aria-describedby */
let idCounter = 0;

export function uniqueId(prefix = 'vd'): string {
  idCounter += 1;
  return `${prefix}-${idCounter}`;
}

export function trapFocus(container: HTMLElement): () => void {
  const focusable =
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
  const nodes = () =>
    Array.from(container.querySelectorAll<HTMLElement>(focusable)).filter(
      (el) => !el.hasAttribute('disabled') && el.offsetParent !== null
    );

  function onKeydown(e: KeyboardEvent) {
    if (e.key !== 'Tab') return;
    const list = nodes();
    if (list.length === 0) return;
    const first = list[0];
    const last = list[list.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }

  container.addEventListener('keydown', onKeydown);
  const list = nodes();
  list[0]?.focus();
  return () => container.removeEventListener('keydown', onKeydown);
}
