// N.A.R. Complexe — interactions légères, sans dépendance
(function () {
  const header = document.querySelector('.header');
  const onScroll = () => header && header.classList.toggle('scrolled', window.scrollY > 20);
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });

  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav');
  if (burger && nav) {
    burger.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
      burger.querySelector('path').setAttribute('d', open ? 'M6 6l12 12M18 6L6 18' : 'M4 7h16M4 12h16M4 17h16');
      document.body.style.overflow = open ? 'hidden' : '';
    });
    const closeNav = () => { nav.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); burger.querySelector('path').setAttribute('d', 'M4 7h16M4 12h16M4 17h16'); document.body.style.overflow = ''; };
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', closeNav));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeNav(); });
    window.addEventListener('resize', () => { if (window.innerWidth > 1024) closeNav(); });
  }

  // Apparition au défilement
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  document.querySelectorAll('.rv').forEach(el => io.observe(el));

  // Lightbox galerie
  const lb = document.querySelector('.lightbox');
  if (lb) {
    const img = lb.querySelector('img');
    document.querySelectorAll('[data-lightbox]').forEach(a => a.addEventListener('click', ev => {
      ev.preventDefault(); img.src = a.getAttribute('href'); img.alt = a.querySelector('img')?.alt || ''; lb.classList.add('on');
    }));
    const close = () => lb.classList.remove('on');
    lb.addEventListener('click', e => { if (e.target !== img) close(); });
    lb.querySelector('button').addEventListener('click', close);
    document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  }

  // Formulaire entreprise : envoi via WhatsApp (aucun serveur nécessaire)
  const form = document.querySelector('#form-b2b');
  if (form) form.addEventListener('submit', e => {
    e.preventDefault();
    const f = new FormData(form);
    const msg = `Bonjour N.A.R. Complexe,%0A%0ADemande d'offre entreprise%0A` +
      `Société : ${f.get('societe')}%0AContact : ${f.get('nom')}%0A` +
      `Téléphone : ${f.get('tel')}%0AE-mail : ${f.get('email')}%0A` +
      `Participants : ${f.get('taille')}%0ADate souhaitée : ${f.get('date') || 'à définir'}%0A` +
      `Activités : ${f.getAll('activites').join(', ') || 'à définir'}%0A%0A${f.get('message') || ''}`;
    window.open('https://wa.me/212602587922?text=' + msg, '_blank');
  });

  // Vidéo du hero : lecture silencieuse quand visible
  const v = document.querySelector('.reel video');
  if (v) {
    const vo = new IntersectionObserver(es => es.forEach(x => x.isIntersecting ? v.play().catch(() => {}) : v.pause()), { threshold: .3 });
    vo.observe(v);
  }
})();
