'use client';
import { useEffect, useRef, useState } from 'react';
import { ArrowUpRight, Menu, X } from 'lucide-react';
import { site } from '@/config/site';

export function Navigation() {
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState('');
  const toggle = useRef<HTMLButtonElement>(null);
  const panel = useRef<HTMLDivElement>(null);
  const close = () => { setOpen(false); toggle.current?.focus(); };
  useEffect(() => {
    const observer = new IntersectionObserver((entries) => {
      for (const entry of entries) if (entry.isIntersecting) setActive(`#${entry.target.id}`);
    }, { rootMargin: '-15% 0px -55% 0px' });
    site.nav.forEach(({ href }) => { const el = document.querySelector(href); if (el) observer.observe(el); });
    return () => observer.disconnect();
  }, []);
  useEffect(() => {
    if (!open) return;
    const previous = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    panel.current?.querySelector<HTMLAnchorElement>('a')?.focus();
    function onKey(event: KeyboardEvent) {
      if (event.key === 'Escape') { setOpen(false); toggle.current?.focus(); }
      if (event.key === 'Tab') {
        const links = Array.from(panel.current?.querySelectorAll<HTMLAnchorElement>('a') ?? []);
        const first = toggle.current;
        const last = links.at(-1);
        if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last?.focus(); }
        if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first?.focus(); }
      }
    }
    const media = matchMedia('(min-width: 800px)');
    const onResize = () => { if (media.matches) setOpen(false); };
    media.addEventListener('change', onResize);
    document.addEventListener('keydown', onKey);
    return () => { document.body.style.overflow = previous; document.removeEventListener('keydown', onKey); media.removeEventListener('change', onResize); };
  }, [open]);
  return <header className="site-header">
    <div className="header-inner">
      <a className="wordmark" href="#baslangic" aria-label="KYAMICH — başlanğıca qayıt" onClick={() => setOpen(false)}>kyamich<span className="logo-dot">.</span><span className="logo-slash">/</span></a>
      <nav className="desktop-nav" aria-label="Əsas naviqasiya">{site.nav.map(item => <a key={item.href} href={item.href} aria-current={active === item.href ? 'location' : undefined}>{item.label}</a>)}</nav>
      <a className="header-cta" href="#elaqe">Birlikdə yaradaq <ArrowUpRight size={16} aria-hidden="true" /></a>
      <button className="menu-toggle" ref={toggle} aria-expanded={open} aria-controls="mobile-menu" aria-label={open ? 'Menyunu bağla' : 'Menyunu aç'} onClick={() => setOpen(!open)}>{open ? <X aria-hidden="true" /> : <Menu aria-hidden="true" />}</button>
    </div>
    <div id="mobile-menu" className="mobile-panel" ref={panel} hidden={!open}><nav aria-label="Mobil naviqasiya">{site.nav.map((item, index) => <a key={item.href} href={item.href} onClick={close}><span>0{index + 1}</span>{item.label}<ArrowUpRight aria-hidden="true" /></a>)}</nav><p>Biznesiniz üçün düşünülmüş veb-saytlar.</p></div>
  </header>;
}
