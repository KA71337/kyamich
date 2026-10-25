import type { Metadata, Viewport } from 'next';
import localFont from 'next/font/local';
const manrope = localFont({ src: '../../node_modules/@fontsource-variable/manrope/files/manrope-latin-wght-normal.woff2', variable: '--font-manrope', display: 'swap', adjustFontFallback: 'Arial' });
const manropeExt = localFont({ src: '../../node_modules/@fontsource-variable/manrope/files/manrope-latin-ext-wght-normal.woff2', variable: '--font-manrope-ext', display: 'swap', adjustFontFallback: false });
const space = localFont({ src: '../../node_modules/@fontsource-variable/space-grotesk/files/space-grotesk-latin-wght-normal.woff2', variable: '--font-space', display: 'swap', adjustFontFallback: 'Arial' });
const spaceExt = localFont({ src: '../../node_modules/@fontsource-variable/space-grotesk/files/space-grotesk-latin-ext-wght-normal.woff2', variable: '--font-space-ext', display: 'swap', adjustFontFallback: false });
import './globals.css';
import { site, contacts } from '@/config/site';
export const metadata: Metadata = {
  metadataBase: new URL(site.url), title: site.title, description: site.description,
  applicationName: site.name, authors: [{ name: site.author, url: contacts.github.url }],
  alternates: { canonical: '/', languages: { az: '/' } },
  openGraph: { type: 'website', url: '/', title: site.title, description: site.description, siteName: site.name, locale: 'az_AZ', images: [{ url: '/opengraph-image', width: 1200, height: 630, alt: 'KYAMICH — Biznesiniz üçün müasir veb-saytlar' }] },
  twitter: { card: 'summary_large_image', title: site.title, description: site.description, images: ['/opengraph-image'] },
  robots: { index: true, follow: true }, icons: { icon: '/icon.svg' },
};
export const viewport: Viewport = { themeColor: '#141615', colorScheme: 'dark' };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="az" className={`${manrope.variable} ${manropeExt.variable} ${space.variable} ${spaceExt.variable}`}><body><a className="skip-link" href="#main">Məzmuna keç</a>{children}</body></html>;
}
