export type ContactConfig = {
  email: string | null;
  phone: string | null;
  github: { url: string; label: string };
};
export const contacts: ContactConfig = {
  email: null,
  phone: null,
  github: { url: 'https://github.com/KA71337', label: 'GitHub profilinə keç' },
};
export const site = {
  name: 'KYAMICH', author: 'Kamil', url: 'https://kyamich.dev', language: 'az',
  title: 'KYAMICH — Biznesiniz üçün müasir veb-saytlar',
  description: 'Kamil tərəfindən bizneslər üçün müasir, sürətli və mobil cihazlara uyğun veb-saytlar. Real layihələr, düşünülmüş dizayn. Adətən 200–300 ₼.',
  price: { min: 200, max: 300, currency: '₼' },
  nav: [{ href: '#isler', label: 'İşlər' }, { href: '#xidmetler', label: 'Xidmətlər' }, { href: '#haqqimda', label: 'Haqqımda' }, { href: '#elaqe', label: 'Əlaqə' }],
} as const;
