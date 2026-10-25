import { ImageResponse } from 'next/og';
export const alt = 'KYAMICH — Biznesiniz üçün müasir veb-saytlar';
export const size = {width: 1200, height: 630};
export const contentType = 'image/png';
export default function Image() {
  return new ImageResponse(<div style={{width: '100%', height: '100%', background: '#141615', color: '#f1f1e8', padding: '60px 72px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between'}}>
    <div style={{display: 'flex', justifyContent: 'space-between', fontSize: 30}}><span style={{color: '#d1ff5f'}}>KYAMICH /</span><span>kyamich.dev</span></div>
    <div style={{display: 'flex', flexDirection: 'column', fontSize: 82, fontWeight: 700, letterSpacing: '-4px', lineHeight: 1.08}}><span>Biznesiniz üçün</span><span style={{color: '#d1ff5f'}}>müasir veb-saytlar.</span></div>
    <div style={{display: 'flex', justifyContent: 'space-between', borderTop: '1px solid #42473e', paddingTop: 26, fontSize: 24}}><span>Dizayn. Kod. Xarakter.</span><span>Kamil / Web developer</span></div>
  </div>, size);
}
