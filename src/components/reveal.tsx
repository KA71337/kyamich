'use client';
import { useEffect } from 'react';
/** Progressive enhancement: content is always visible without JavaScript. */
export function RevealEffects() {
  useEffect(() => {
    const media = matchMedia('(prefers-reduced-motion: reduce)');
    if (media.matches) return;
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(({ target, isIntersecting }) => {
        if (!isIntersecting) return;
        target.animate([{ opacity: 0.35, transform: 'translateY(22px)' }, { opacity: 1, transform: 'translateY(0)' }], { duration: 600, easing: 'cubic-bezier(.2,.7,.2,1)' });
        observer.unobserve(target);
      });
    }, { threshold: 0.08 });
    document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el));
    const disable = () => { if (media.matches) { observer.disconnect(); document.getAnimations().forEach(animation => animation.finish()); } };
    media.addEventListener('change', disable);
    return () => { observer.disconnect(); media.removeEventListener('change', disable); };
  }, []);
  return null;
}
