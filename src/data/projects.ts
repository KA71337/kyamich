export type Project = {
  id: string; number: string; name: string; url: string; domain: string;
  category: string; description: string; technologies: readonly string[];
  image: string; alt: string; width: number; height: number; accent: string;
};
export const projects: readonly Project[] = [
  {id: 'nerj', number: '01', name: 'NERJ METAL', url: 'https://nerjmetal.com/', domain: 'nerjmetal.com', category: 'İstehsal · Korporativ sayt', description: 'Paslanmaz polad istehsalçısının məhsullarını və sənaye həllərini təqdim edən korporativ sayt.', technologies: ['Next.js', 'React'], image: '/projects/nerj-metal-cover.webp', alt: 'NERJ METAL saytının real görüntüsü: tünd fonda paslanmaz polad istehsalı və məhsullar', width: 1440, height: 1000, accent: 'lime'},
  {id: 'talsan', number: '02', name: 'TALSAN POWER', url: 'https://talsanpower.com/', domain: 'talsanpower.com', category: 'Enerji · Məhsul və xidmət kataloqu', description: 'Generator, stabilizator və tənzimləyici satışı ilə texniki servisi bir araya gətirən sayt.', technologies: ['Next.js', 'React'], image: '/projects/talsan-power-cover.webp', alt: 'TALSAN POWER saytının real görüntüsü: enerji avadanlıqları, sarı vurğular və generator', width: 1440, height: 1000, accent: 'yellow'},
  {id: 'ayva', number: '03', name: 'AYVA TECH', url: 'https://www.ayvatech.az/', domain: 'ayvatech.az', category: 'Elektronika · Məhsul kataloqu', description: 'Elektronika məhsullarını aydın kateqoriyalar və rahat vizual naviqasiya ilə təqdim edən kataloq.', technologies: ['HTML', 'CSS', 'JavaScript'], image: '/projects/ayva-tech-gallery-cover.webp', alt: 'AYVA TECH saytının real məhsul qalereyası: elektronika və kompüter avadanlıqları', width: 1440, height: 1000, accent: 'blue'},
];
export const services = [
  {number: '01', title: 'Korporativ saytlar', text: 'Şirkətinizi, fəaliyyətinizi və xidmətlərinizi aydın şəkildə təqdim edən saytlar.', detail: 'Şirkətlər və istehsalçılar üçün'},
  {number: '02', title: 'Biznes üçün lendinqlər', text: 'Bir xidmətə və ya təklifə fokuslanan, ziyarətçiyə növbəti addımı göstərən səhifələr.', detail: 'Bir məqsəd. Dəqiq təqdimat.'},
  {number: '03', title: 'Brend təqdimatı', text: 'Brendinizin xarakterini rəqəmsal mühitə daşıyan, vizual bütövlüyə malik saytlar.', detail: 'Dizayn və məzmun bir yerdə'},
] as const;
export const process = [
  {title: 'Müzakirə', text: 'Biznesinizi, məqsədinizi və sayt üçün ehtiyaclarınızı aydınlaşdırırıq.'},
  {title: 'Dizayn və struktur', text: 'Səhifələrin məntiqini və brendinizə uyğun vizual istiqaməti müəyyən edirik.'},
  {title: 'Hazırlanma', text: 'Dizaynı sürətli, istifadəsi rahat və adaptiv veb-sayta çevirirəm.'},
  {title: 'Yoxlama və təhvil', text: 'Mobil və masaüstü görünüşü, keçidləri və əsas funksiyaları yoxlayırıq.'},
] as const;
