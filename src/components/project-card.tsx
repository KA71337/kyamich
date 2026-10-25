import Image from 'next/image';
import { ArrowUpRight } from 'lucide-react';
import type { Project } from '@/data/projects';
export function ProjectCard({ project }: { project: Project }) {
  return <article className={`project-card project-${project.id}`} data-reveal>
    <a className={`project-visual accent-${project.accent}`} href={project.url} target="_blank" rel="noopener noreferrer" aria-label={`${project.name} — sayta bax (yeni pəncərə)`}>
      <div className="window-bar"><span className="window-dots"><i /><i /><i /></span><span>{project.domain}</span><ArrowUpRight size={14} aria-hidden="true" /></div>
      <div className="project-image"><Image src={project.image} width={project.width} height={project.height} alt={project.alt} sizes={project.id === 'nerj' ? '(max-width: 799px) 92vw, 88vw' : '(max-width: 799px) 92vw, 44vw'} quality={85} /></div>
      <span className="project-visit">Sayta bax <ArrowUpRight size={20} aria-hidden="true" /></span>
    </a>
    <div className="project-info"><div><p className="eyebrow">{project.number} / {project.category}</p><h3><a href={project.url} target="_blank" rel="noopener noreferrer">{project.name}<ArrowUpRight aria-hidden="true" /></a></h3></div><p className="project-description">{project.description}</p></div>
    <ul className="tech-tags" aria-label="Təsdiqlənmiş texnologiyalar">{project.technologies.map(tech => <li key={tech}>{tech}</li>)}</ul>
  </article>;
}
