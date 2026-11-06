# -*- coding: utf-8 -*-
"""Génère les pages HTML du nouveau site N.A.R. Complexe (statique)."""
import os, json
OUT = os.path.dirname(os.path.abspath(__file__))
ROBOTS = os.environ.get("NAR_ROBOTS","noindex, nofollow")
TEL = "+212 6 02 58 79 22"; TEL_RAW = "+212602587922"; WA = "https://wa.me/212602587922"
WAZE = "https://www.waze.com/en/live-map/directions/ma/marrakech-safi/n.a.r-complexe-sportif-location-quad-cross-raptor-buggy-waterkarting-paintball-karting-marrakech?place=ChIJ9RRt12yLrw0RAxssu5ktRnk"
MAPS = "https://maps.google.com/?cid=8738722265252502275"
MAP_EMBED = "https://www.google.com/maps?q=N.A.R+Complexe+Sportif+Marrakech&output=embed"
ADDR = "Route de Casablanca, Douar Berhmoun, 40000 Marrakech"

SVG = {
 "wa": '<svg viewBox="0 0 24 24"><path d="M20.5 3.5A11.9 11.9 0 0 0 12 0C5.4 0 .1 5.3.1 11.9c0 2.1.6 4.1 1.6 5.9L0 24l6.3-1.7a12 12 0 0 0 5.7 1.5c6.6 0 11.9-5.3 11.9-11.9 0-3.2-1.2-6.2-3.4-8.4ZM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 0 1 2.1 12C2.1 6.5 6.5 2 12 2c2.6 0 5.1 1 7 2.9a9.8 9.8 0 0 1 2.9 7c0 5.5-4.5 9.9-9.9 9.9Zm5.4-7.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5.3-.5v-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4Z"/></svg>',
 "tel": '<svg viewBox="0 0 24 24"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2Z"/></svg>',
 "waze": '<svg viewBox="0 0 24 24"><path d="M12 2a9 9 0 0 0-9 9c0 1.6.4 3 1.1 4.3L2 21l3.8-1.3A9 9 0 1 0 12 2Zm-3 7.5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Zm6 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2Zm-6.6 4.3c.2-.4.7-.5 1-.3 1.6 1.2 3.6 1.2 5.2 0 .3-.2.8-.1 1 .3.2.3.1.8-.2 1a5.8 5.8 0 0 1-6.8 0c-.3-.2-.4-.7-.2-1Z"/></svg>',
 "ig": '<svg viewBox="0 0 24 24"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10Zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4ZM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4ZM21.9 7.9c-.1-1.6-.4-3-1.6-4.2S17.7 2.2 16.1 2.1C14.5 2 9.5 2 7.9 2.1c-1.6.1-3 .4-4.2 1.6S2.2 6.3 2.1 7.9C2 9.5 2 14.5 2.1 16.1c.1 1.6.4 3 1.6 4.2s2.6 1.5 4.2 1.6c1.6.1 6.6.1 8.2 0 1.6-.1 3-.4 4.2-1.6s1.5-2.6 1.6-4.2c.1-1.6.1-6.6 0-8.2Zm-2.3 10a3.3 3.3 0 0 1-1.8 1.8c-1.3.5-4.3.4-5.8.4s-4.5.1-5.8-.4a3.3 3.3 0 0 1-1.8-1.8C3.9 16.6 4 13.6 4 12s-.1-4.5.4-5.8a3.3 3.3 0 0 1 1.8-1.8C7.5 3.9 10.5 4 12 4s4.5-.1 5.8.4a3.3 3.3 0 0 1 1.8 1.8c.5 1.3.4 4.3.4 5.8s.1 4.5-.4 5.9Z"/></svg>',
 "tt": '<svg viewBox="0 0 24 24"><path d="M16.6 5.8A4.3 4.3 0 0 1 15.5 3h-3.1v12.4a2.6 2.6 0 0 1-2.6 2.5 2.6 2.6 0 0 1-2.6-2.6 2.6 2.6 0 0 1 3.4-2.5V9.7a5.7 5.7 0 0 0-6.5 5.6A5.7 5.7 0 0 0 9.8 21a5.7 5.7 0 0 0 5.7-5.7V9a7.3 7.3 0 0 0 4.3 1.4V7.3s-1.9.1-3.2-1.5Z"/></svg>',
 "snap": '<svg viewBox="0 0 24 24"><path d="M12 2c3.3 0 5.6 2.5 5.6 5.8v2.4c.4.2.9 0 1.3-.1.5-.1.9.2.9.6 0 .5-.6.8-1.2 1-.4.2-1 .3-1.1.7-.1.3.1.6.2.8 1 1.8 2.5 2.8 4 3.1.3.1.4.3.3.6-.3.6-1.4.9-2.4 1.1-.1.2-.2.8-.4 1-.2.2-.6.1-1.1 0-.8-.1-1.8-.2-2.8.5-.9.6-1.7 1.5-3.3 1.5s-2.4-.9-3.3-1.5c-1-.7-2-.6-2.8-.5-.5.1-.9.2-1.1 0-.2-.2-.3-.8-.4-1-1-.2-2.1-.5-2.4-1.1-.1-.3 0-.5.3-.6 1.5-.3 3-1.3 4-3.1.1-.2.3-.5.2-.8-.1-.4-.7-.5-1.1-.7-.6-.2-1.2-.5-1.2-1 0-.4.4-.7.9-.6.4.1.9.3 1.3.1V7.8C6.4 4.5 8.7 2 12 2Z"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s7-6.3 7-11.5A7 7 0 0 0 5 9.5C5 14.7 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3 4 6v6c0 5 3.4 8.4 8 9 4.6-.6 8-4 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/></svg>',
 "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2 4 14h7l-1 8 9-12h-7l1-8Z"/></svg>',
 "kid": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="7" r="3"/><path d="M6 21v-3a6 6 0 0 1 12 0v3"/></svg>',
 "pool": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 16c2 1.5 4 1.5 6 0s4-1.5 6 0 4 1.5 6 0M3 20c2 1.5 4 1.5 6 0s4-1.5 6 0 4 1.5 6 0M8 12V5a2 2 0 0 1 4 0M14 12V5a2 2 0 0 1 4 0"/></svg>',
}

NAV = [("index.html","Accueil"),("activites.html","Activités"),("tarifs.html","Tarifs"),("galerie.html","Galerie"),("entreprises.html","Entreprises"),("a-propos.html","À propos"),("contact.html","Contact")]

def header(active):
    links = "".join('<a href="%s"%s>%s</a>' % (h, ' class="active"' if h==active else '', t) for h,t in NAV)
    links += '<a href="franchise.html"%s class="nav-ext">Devenez franchisé</a>' % (' aria-current="page"' if active=="franchise.html" else '') 
    return f'''<header class="header"><div class="wrap">
  <a class="brand" href="index.html" aria-label="N.A.R. Complexe Sportif, accueil"><img src="assets/img/logo.png" alt="N.A.R. Complexe Sportif Marrakech" width="160" height="62"></a>
  <nav class="nav" aria-label="Menu principal">{links}<a class="btn btn-wa btn-sm nav-cta" href="{WA}" target="_blank" rel="noopener">{SVG["wa"]} WhatsApp</a></nav>
  <button class="burger" aria-label="Ouvrir le menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></header>'''

def footer():
    return f'''<footer class="footer"><div class="wrap">
 <div class="cols">
  <div><a class="brand" href="index.html"><img src="assets/img/logo.png" alt="N.A.R. Complexe Sportif"></a>
   <p>Complexe de loisirs motorisés et nautiques à Marrakech : quad, buggy, Can-Am, moto-cross, karting, water karting, paintball, stand de tir et supercars. Ouvert 7j/7, sans réservation.</p>
   <div class="socials">
    <a href="https://www.instagram.com/n.a.r_complexe/" target="_blank" rel="noopener" aria-label="Instagram">{SVG["ig"]}</a>
    <a href="https://www.tiktok.com/@n.a.r_complexe" target="_blank" rel="noopener" aria-label="TikTok">{SVG["tt"]}</a>
    <a href="https://www.snapchat.com/add/narcomplexe" target="_blank" rel="noopener" aria-label="Snapchat">{SVG["snap"]}</a>
   </div></div>
  <div><h4>Activités</h4><ul>
   <li><a href="activites.html#quad">Quad &amp; Raptor</a></li><li><a href="activites.html#canam">Buggy &amp; Can-Am</a></li><li><a href="activites.html#cross">Moto-cross</a></li>
   <li><a href="activites.html#karting">Karting</a></li><li><a href="activites.html#waterkarting">Water karting</a></li><li><a href="activites.html#paintball">Paintball &amp; tir</a></li><li><a href="activites.html#supercars">Supercars</a></li></ul></div>
  <div><h4>Le complexe</h4><ul>
   <li><a href="tarifs.html">Tarifs &amp; packs</a></li><li><a href="tarifs.html#excursions">Excursions</a></li><li><a href="galerie.html">Galerie</a></li>
   <li><a href="entreprises.html">Offres entreprises</a></li><li><a href="a-propos.html">À propos</a></li><li><a href="contact.html">Contact &amp; accès</a></li><li><a href="franchise.html">Devenez franchisé Water Karting</a></li></ul></div>
  <div><h4>Coordonnées</h4><ul>
   <li><a href="tel:{TEL_RAW}">{TEL}</a></li><li>{ADDR}</li><li><strong>7j/7 · 9h00 – 22h00</strong></li>
   <li><a href="{WAZE}" target="_blank" rel="noopener">Itinéraire Waze</a> · <a href="{MAPS}" target="_blank" rel="noopener">Google Maps</a></li></ul></div>
 </div>
 <div class="legal"><span>© 2026 N.A.R. Complexe Sportif – Marrakech</span><span><a href="mentions-legales.html">Mentions légales</a><a href="mentions-legales.html#donnees">Confidentialité</a></span></div>
</div></footer>
<div class="float">
 <a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{SVG["wa"]}</a>
 <div class="float-socials">
  <a href="https://www.instagram.com/n.a.r_complexe/" target="_blank" rel="noopener" aria-label="Instagram">{SVG["ig"]}</a>
  <a href="https://www.tiktok.com/@n.a.r_complexe" target="_blank" rel="noopener" aria-label="TikTok">{SVG["tt"]}</a>
  <a href="https://www.snapchat.com/add/narcomplexe" target="_blank" rel="noopener" aria-label="Snapchat">{SVG["snap"]}</a>
 </div>
 <a class="tel" href="tel:{TEL_RAW}" aria-label="Appeler">{SVG["tel"]}</a>
 <a class="wz" href="{WAZE}" target="_blank" rel="noopener" aria-label="Itinéraire Waze">{SVG["waze"]}</a>
</div>'''

JSONLD = json.dumps({
 "@context":"https://schema.org","@type":"SportsActivityLocation","name":"N.A.R. Complexe Sportif",
 "url":"https://www.narcomplexesportif.com/","telephone":TEL_RAW,"image":"https://www.narcomplexesportif.com/assets/img/p-canam-desert.jpg",
 "address":{"@type":"PostalAddress","streetAddress":"Route de Casablanca, Douar Berhmoun","postalCode":"40000","addressLocality":"Marrakech","addressCountry":"MA"},
 "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"09:00","closes":"22:00"}],
 "priceRange":"100 DH - 4500 DH","sameAs":["https://www.instagram.com/n.a.r_complexe/","https://www.tiktok.com/@n.a.r_complexe","https://www.snapchat.com/add/narcomplexe"]
}, ensure_ascii=False)

def page(fname, title, desc, body, active=None):
    html = f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{ROBOTS}">
<link rel="canonical" href="https://www.narcomplexesportif.com/{fname if fname!="index.html" else ""}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:image" content="assets/img/p-canam-desert.jpg">
<link rel="icon" href="assets/img/logo-footer.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;700;800&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css?v=2">
<script type="application/ld+json">{JSONLD}</script>
</head><body>
{header(active or fname)}
<main>
{body}
</main>
{footer()}
<div class="lightbox" role="dialog" aria-label="Photo agrandie"><button aria-label="Fermer">×</button><img alt=""></div>
<script src="assets/app.js?v=2" defer></script>
</body></html>'''
    with open(os.path.join(OUT,fname),"w",encoding="utf-8") as f: f.write(html)

def page_head(crumb, h1, p, img):
    return f'''<section class="page-head"><img src="assets/img/{img}" alt="" aria-hidden="true"><div class="wrap">
 <div class="crumbs"><a href="index.html">Accueil</a> / {crumb}</div><h1>{h1}</h1><p>{p}</p></div></section>'''

def cta_band(title="Prêt à rouler ?", text="Sans réservation, 7 jours sur 7, de 9h à 22h. Venez quand vous voulez, on s'occupe du reste.", img="p-desert-buggies.jpg"):
    return f'''<section><div class="wrap"><div class="cta-band rv"><img class="bg" src="assets/img/{img}" alt="">
 <div><span class="eyebrow">N.A.R. Complexe</span><h2>{title}</h2><p class="lead" style="margin-top:.8rem">{text}</p></div>
 <div class="actions"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{SVG["wa"]} Écrire sur WhatsApp</a><a class="btn btn-ghost" href="tel:{TEL_RAW}">{SVG["tel"]} {TEL}</a></div>
</div></div></section>'''

# ----------------------------------------------------------- DONNÉES
ACTS = [
 dict(id="quad", t="Quad", img="v-quad.png", chip=None, price="100", unit="dès · 30 min",
      s="Kawasaki automatiques 300 et 450 cc : balade dans le désert, la palmeraie ou l'Atlas. Accessible à tous, équipement fourni."),
 dict(id="raptor", t="Raptor 700", img="v-raptor700.png", chip="Édition spéciale", price="800", unit="dès · 30 min",
      s="Le quad sportif par excellence. Puissance et sensations fortes pour les pilotes qui en veulent plus."),
 dict(id="canam", t="Can-Am Maverick", img="v-canam-r.png", chip="Exclusivité Maroc", price="500", unit="dès · 30 min",
      s="Maverick XRS Turbo, Maverick R Turbo 2 et 4 places. Les SSV les plus puissants du marché, en exclusivité au Maroc."),
 dict(id="cross", t="Moto-cross", img="v-cross.png", chip="Modèles 2025", price="800", unit="dès · 30 min",
      s="Yamaha YZ, Honda CRF, Kawasaki KX millésime 2025. Protections complètes fournies."),
 dict(id="buggy", t="Buggy", img="v-canam.png", chip=None, price="300", unit="1 heure",
      s="Du buggy classique au buggy de course, pour une virée tout-terrain accessible et ludique."),
 dict(id="karting", t="Rallye-karting", img="v-kart.png", chip=None, price="200", unit="15 min",
      s="Un circuit de karting au cœur du désert. Chronos, dépassements et podium entre amis."),
 dict(id="waterkarting", t="Water karting", img="v-waterkart.png", chip="1er circuit au Maroc", price="800", unit="15 min",
      s="Un kart qui flotte ! Le premier circuit de water karting d'Afrique, pour toute la famille. Concept disponible en franchise."),
 dict(id="paintball", t="Paintball & stand de tir", img="v-paintball.png", chip=None, price="200", unit="100 balles",
      s="Terrain de paintball aménagé et stand de tir équipé. Affrontez vos amis ou travaillez votre précision."),
 dict(id="supercars", t="Supercars · Test drive", img="v-huracan.png", chip="Immersion pilotage", price="2000", unit="15 min",
      s="Lamborghini Huracán EVO Spyder, Aventador S, Urus, Ferrari 488 Spider, Porsche 911 Turbo S. Au volant, dans le désert de Marrakech."),
]

TARIFS = [
 ("Quad & moto enfant", "Circuit encadré et sécurisé", "v-quad.png", [("10 tours","100"),("20 tours","200"),("30 tours","300")], None),
 ("Quad automatique 300 cc", "Idéal débutants et balades", "v-quad.png", [("30 min","100"),("1 h","150"),("2 h","190"),("3 h","250")], None),
 ("Quad Kawasaki 450 cc", "Automatique sport", "v-quad.png", [("30 min","300"),("1 h","600"),("2 h","800"),("3 h","900")], None),
 ("Raptor 700", "Édition spéciale", "v-raptor.png", [("30 min","800"),("1 h","1600"),("2 h","1900"),("3 h","2400")], None),
 ("Moto-cross", "YZF · CRF · KXF · YZ 2025", "v-cross.png", [("30 min","800"),("1 h","1600"),("2 h","1900"),("3 h","2400")], None),
 ("Buggy", "Tout-terrain classique ou sportif", "v-canam.png", [("1 h","300"),("2 h","500")], None),
 ("Can-Am Maverick XRS Turbo RR", "2 places", "v-canam.png", [("30 min","500"),("1 h","900"),("2 h","1300"),("3 h","1600")], None),
 ("Can-Am Maverick R XRS Turbo", "2 places · full équipé", "v-canam-r.png", [("30 min","1450"),("1 h","2900"),("2 h","3900"),("3 h","4500")], "featured"),
 ("Can-Am Maverick R 2024 XRS Turbo", "4 places · full équipé", "v-canam-r.png", [("30 min","1450"),("1 h","2900"),("2 h","3900"),("3 h","4500")], None),
 ("Test drive supercars", "Porsche 911 · Huracán · Aventador · 488 · Urus", "v-huracan.png", [("15 min","2000"),("30 min","3000"),("1 h","4000")], None),
 ("Water karting", "Session sur le circuit aquatique", "v-waterkart.png", [("15 min","800"),("30 min","1200")], None),
 ("Rallye-karting", "Session chronométrée", "v-kart.png", [("15 min","200")], None),
 ("Paintball / stand de tir", "Équipement complet fourni", "v-paintball.png", [("100 balles","200")], None),
]

PACKS = [
 ("Pack 1","900",False,[("Jet ski ou water karting · 15 min",0),("Karting · 15 min",0),("Accès piscine offert",1),("Thé marocain offert",1)]),
 ("Pack 2","1400",True,[("Jet ski ou water karting · 15 min",0),("Quad · 1 h",0),("Karting · 15 min",0),("Accès piscine offert",1),("Thé marocain offert",1)]),
 ("Pack 3","4500",False,[("Quad, moto-cross, Raptor ou buggy · 1 h",0),("Ferrari, Lamborghini ou Porsche · 30 min",0),("Stand de tir · 100 balles",0),("Karting · 15 min",0),("Jet ski ou water karting · 15 min",0),("Accès piscine offert",1),("Thé marocain offert",1)]),
]

EXCU = [
 ("30 min","Bas de l'Atlas",["Visite du bas de l'Atlas de Marrakech"],None),
 ("1 h","Palmeraie ou désert",["Visite de la palmeraie","ou visite du désert de Marrakech"],"Pause thé & msemen offerte"),
 ("2 h","Panorama 360°",["Haut de l'Atlas, vue panoramique","Désert de Marrakech","Palmeraie"],"Pause thé & msemen offerte"),
 ("3 h","La grande boucle",["Haut de l'Atlas, vue panoramique","Désert de Marrakech","Palmeraie","Pause thé & msemen"],"Barbecue offert"),
]

GALLERY = [("p-canam-desert.jpg","Can-Am Maverick dans le désert de Marrakech"),("p-groupe-quad.jpg","Groupe d'amis en quad Kawasaki"),("p-drone.jpg","Vue aérienne du complexe : circuit de water karting et karting"),
 ("p-paintball-groupe.jpg","Équipe de paintball devant les Can-Am"),("p-enfants-mascottes.jpg","Activités enfants avec mascottes"),("p-desert-buggies.jpg","Convoi de buggies dans le désert"),
 ("p-canam-jaune.jpg","Can-Am Maverick jaune"),("p-groupe-drapeau.jpg","Groupe avec le drapeau marocain sur le circuit"),("p-flotte.jpg","La flotte de Can-Am"),
 ("p-famille.jpg","Famille devant un Can-Am"),("p-paintball-terrain.jpg","Terrain de paintball"),("p-pilote.jpg","Pilote sur Can-Am X RS"),
 ("p-terrasse.jpg","Terrasse ombragée du complexe"),("p-casque.jpg","Casque racing et jet ski"),("p-canam-flotte.jpg","Can-Am alignés devant la piste"),
 ("p-panneau.jpg","Panneau d'entrée du complexe"),("p-13.jpg","Au complexe"),("p-14.jpg","Au complexe"),("p-15.jpg","Au complexe"),("p-16.jpg","Au complexe"),("p-17.jpg","Au complexe"),("p-18.jpg","Au complexe"),("p-24.jpg","Au complexe"),("p-25.jpg","Au complexe")]

def act_card(a):
    chip = f'<span class="chip">{a["chip"]}</span>' if a.get("chip") else ""
    photo = " photo" if a.get("photo") else ""
    return f'''<a class="card rv" href="activites.html#{a["id"]}">{chip}<div class="media{photo}"><img src="assets/img/{a["img"]}" alt="{a["t"]}" loading="lazy"></div>
 <div class="body"><h3>{a["t"]}</h3><p>{a["s"]}</p><div class="price"><span><b>{a["price"]} DH</b> <small>{a["unit"]}</small></span><span class="more">Découvrir</span></div></div></a>'''

def tarif_card(t):
    name,sub,img,rows,cls = t
    trs = "".join(f"<tr><td>{d}</td><td>{p}<small>DH</small></td></tr>" for d,p in rows)
    return f'''<div class="tarif rv{(' '+cls) if cls else ''}"><div class="top"><img src="assets/img/{img}" alt=""><div><h3>{name}</h3><small>{sub}</small></div></div><table>{trs}</table></div>'''

def pack_card(p):
    n,amt,hot,items = p
    lis = "".join('<li%s>%s</li>' % (' class="gift"' if g else '', i) for i,g in items)
    tag = '<span class="tag">Le plus choisi</span>' if hot else ""
    return f'''<div class="pack rv{' hot' if hot else ''}" data-n="{n[-1]}"><div class="ph"><h3>{n}</h3>{tag}</div><div class="amount">{amt}<small>DH</small></div><ul>{lis}</ul>
 <a class="btn btn-red" href="{WA}?text=Bonjour, je souhaite réserver le {n} ({amt} DH)." target="_blank" rel="noopener">Réserver ce pack</a></div>'''

def packs_section(alt=True):
    return f'''<section id="packs" class="{'alt' if alt else ''}"><div class="wrap">
 <div class="sec-head rv"><div><span class="eyebrow">Formules tout compris</span><h2>Les packs <span class="accent">N.A.R.</span></h2></div><p>Plusieurs activités enchaînées, piscine et thé marocain offerts. La façon la plus simple de tout tester en une journée.</p></div>
 <div class="packs">{"".join(pack_card(p) for p in PACKS)}</div></div></section>'''

def excursions_section():
    cards = ""
    for d,t,items,gift in EXCU:
        lis = "".join(f"<li>{i}</li>" for i in items)
        g = f'<span class="gift">★ {gift}</span>' if gift else ""
        cards += f'<div class="ex rv"><div class="d">{d}</div><h3>{t}</h3><ul>{lis}</ul>{g}</div>'
    return f'''<section id="excursions" class="sand-bg"><div class="wrap">
 <div class="sec-head rv"><div><span class="eyebrow">Quad · Raptor · Can-Am · buggy</span><h2>Les <span class="sand">excursions</span></h2></div><p>Chaque location de 30 minutes à 3 heures inclut un itinéraire guidé. Accès piscine gratuit, service photographe et vidéo drone disponibles.</p></div>
 <div class="excu">{cards}</div></div></section>'''

# ----------------------------------------------------------- ACCUEIL
home = f'''
<section class="hero"><div class="hero-bg"><img src="assets/img/p-canam-desert.jpg" alt="" fetchpriority="high"></div>
 <div class="wrap">
  <div>
   <div class="hero-badges"><span class="badge"><i></i>Ouvert aujourd'hui · 9h – 22h</span><span class="badge">Sans réservation</span><span class="badge">Marrakech</span></div>
   <h1><span>Le désert,</span><span class="thin">à pleine vitesse.</span></h1>
   <p class="lead">Quad, Can-Am, buggy, moto-cross, karting, water karting, paintball, stand de tir et supercars : le plus grand complexe de loisirs motorisés de Marrakech, à 20 minutes du centre.</p>
   <div class="hero-actions"><a class="btn btn-red" href="tarifs.html">Voir les tarifs</a><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{SVG["wa"]} Réserver sur WhatsApp</a></div>
   <div class="hero-stats"><div class="stat"><b>+110</b><span>véhicules</span></div><div class="stat"><b>7j/7</b><span>9h – 22h</span></div><div class="stat"><b>1<sup>er</sup></b><span>circuit water karting d'Afrique</span></div><div class="stat"><b>9</b><span>activités sur place</span></div></div>
  </div>
  <div class="reel"><video muted loop playsinline preload="metadata" poster="assets/reel-poster.jpg"><source src="assets/reel.mp4" type="video/mp4"></video><span class="tag">● Live du complexe</span></div>
 </div>
</section>
<div class="ticker" aria-hidden="true"><div class="track"><span>Ouvert 7j/7 de 9h à 22h</span><span>Sans réservation</span><span>Route de Casablanca · Marrakech</span><span>Can-Am Maverick R en exclusivité au Maroc</span><span>Ouvert 7j/7 de 9h à 22h</span><span>Sans réservation</span><span>Route de Casablanca · Marrakech</span><span>Can-Am Maverick R en exclusivité au Maroc</span></div></div>

<section id="activites"><div class="wrap">
 <div class="sec-head rv"><div><span class="eyebrow">9 activités, un seul lieu</span><h2>Choisissez votre <span class="accent">dose d'adrénaline</span></h2></div><p>Du quad enfant sur circuit encadré à la Lamborghini dans le désert : il y a une machine pour chaque pilote.</p></div>
 <div class="grid grid-3">{"".join(act_card(a) for a in ACTS)}</div>
</div></section>

<section class="alt"><div class="wrap">
 <div class="sec-head rv"><div><span class="eyebrow">Pourquoi N.A.R.</span><h2>Pensé pour <span class="sand">toute la famille</span></h2></div></div>
 <div class="why">
  <div class="why-item rv"><div class="ic">{SVG["bolt"]}</div><h3>Zéro réservation</h3><p>Arrivez quand vous voulez, 7 jours sur 7 de 9h à 22h. Les machines sont prêtes.</p></div>
  <div class="why-item rv"><div class="ic">{SVG["shield"]}</div><h3>Sécurité d'abord</h3><p>Casques, protections, briefing et accompagnateurs expérimentés qui connaissent la région.</p></div>
  <div class="why-item rv"><div class="ic">{SVG["kid"]}</div><h3>Espace enfants</h3><p>Quads, motos et karts enfants sur circuit encadré. Les petits aventuriers ont leur piste.</p></div>
  <div class="why-item rv"><div class="ic">{SVG["pool"]}</div><h3>Piscine & détente</h3><p>Accès piscine gratuit, terrasse ombragée, granitas et thé marocain entre deux sessions.</p></div>
 </div>
</div></section>

{packs_section(alt=False)}
{excursions_section()}

<section><div class="wrap"><div class="split">
 <div class="rv"><span class="eyebrow">Le complexe</span><h2>Un terrain de jeu <span class="accent">unique en Afrique</span></h2>
  <p class="lead" style="margin-top:1rem">Sur la route de Casablanca, aux portes du désert de Marrakech, N.A.R. Complexe réunit un circuit de karting, le premier circuit de water karting du continent, un terrain de paintball, un stand de tir et plus de 110 véhicules tout-terrain.</p>
  <ul class="checks"><li>Départ d'excursions vers la palmeraie, le désert et l'Atlas</li><li>Service photographe et vidéo drone pour repartir avec vos images</li><li>Offres entreprises : séminaires, team building, incentives</li></ul>
  <a class="btn btn-ghost" href="a-propos.html">Découvrir le complexe</a></div>
 <div class="pic wide rv"><img src="assets/img/p-drone.jpg" alt="Vue aérienne du complexe N.A.R." loading="lazy"><div class="caption"><b>Vue du ciel</b><span>Circuit karting et plan d'eau du water karting</span></div></div>
</div></div></section>

<section class="alt"><div class="wrap">
 <div class="sec-head rv"><div><span class="eyebrow">Galerie</span><h2>Ça s'est passé <span class="sand">chez nous</span></h2></div><a class="btn btn-ghost btn-sm" href="galerie.html">Toute la galerie</a></div>
 <div class="strip rv">{"".join(f'<a href="assets/img/{f}" data-lightbox><img src="assets/img/{f}" alt="{a}" loading="lazy"></a>' for f,a in GALLERY[:6])}</div>
</div></section>

<section><div class="wrap"><div class="split rev">
 <div class="pic rv"><img src="assets/img/p-paintball-groupe.jpg" alt="Équipe en séminaire au complexe" loading="lazy"></div>
 <div class="rv"><span class="eyebrow">Entreprises</span><h2>Team building <span class="accent">hors norme</span></h2>
  <p class="lead" style="margin-top:1rem">Tarifs préférentiels pour les groupes et les sociétés. Paintball par équipes, challenge karting, raid en Can-Am puis barbecue : nous construisons la journée avec vous.</p>
  <div class="hero-actions" style="margin-top:1.6rem"><a class="btn btn-red" href="entreprises.html">Demander une offre</a></div></div>
</div></div></section>

<section class="alt" id="infos"><div class="wrap">
 <div class="sec-head rv"><div><span class="eyebrow">Infos pratiques</span><h2>Venir au <span class="sand">complexe</span></h2></div></div>
 <div class="info-cards rv">
  <div class="info"><div class="ic">{SVG["clock"]}</div><div><h3>Horaires</h3><p>Tous les jours, 9h00 – 22h00<br>Sans réservation</p></div></div>
  <div class="info"><div class="ic">{SVG["pin"]}</div><div><h3>Adresse</h3><p>{ADDR}</p><a href="{WAZE}" target="_blank" rel="noopener" class="sand">Ouvrir dans Waze →</a></div></div>
  <div class="info"><div class="ic">{SVG["phone"]}</div><div><h3>Contact</h3><p><a href="tel:{TEL_RAW}">{TEL}</a><br><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a> · Instagram · TikTok</p></div></div>
 </div>
 <div class="map rv" style="margin-top:1.4rem"><iframe src="{MAP_EMBED}" loading="lazy" title="Carte N.A.R. Complexe" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</div></section>
'''
page("index.html","N.A.R. Complexe Sportif – Quad, buggy, karting, water karting et supercars à Marrakech",
     "Le plus grand complexe de loisirs motorisés de Marrakech : location quad, Can-Am, buggy, moto-cross, karting, water karting, paintball, stand de tir et test drive supercars. Ouvert 7j/7 de 9h à 22h, sans réservation.", home)

# ----------------------------------------------------------- ACTIVITÉS
DETAILS = {
 "quad":("Quad","v-quad.png",False,"Marrakech se découvre en quad. Nous mettons à votre disposition une gamme de quads Kawasaki automatiques, 300 cc pour les débutants et 450 cc sport pour les plus exigeants, ainsi que des quads enfants sur circuit encadré.","Équipement complet fourni, casque compris, et briefing détaillé avant le départ. Les excursions vous emmènent dans la palmeraie, le désert ou jusqu'au haut de l'Atlas selon la durée choisie.",["Dès 100 DH","30 min à 3 h","Enfants bienvenus","Automatique"]),
 "raptor":("Raptor 700 édition spéciale","v-raptor700.png",False,"Pour l'ultime expérience tout-terrain, le Yamaha Raptor 700 répond à votre soif d'adrénaline. Puissance et performance pour les pilotes confirmés.","Nos Raptor sont entretenus et inspectés régulièrement. Sans réservation : vivez l'excitation quand bon vous semble.",["Dès 800 DH","30 min à 3 h","Pilotes confirmés"]),
 "canam":("Can-Am Maverick","v-canam-r.png",False,"Maverick XRS Turbo RR 2 places, Maverick R XRS Turbo 2 places et Maverick R 2024 4 places full équipés : les SSV les plus puissants du marché, en exclusivité au Maroc.","Partez en famille ou entre amis dans le même véhicule, dunes et pistes du désert de Marrakech au programme.",["Dès 500 DH","2 ou 4 places","Exclusivité Maroc","Turbo"]),
 "cross":("Moto-cross","v-cross.png",False,"Yamaha YZ, Honda CRF et Kawasaki KX millésime 2025. Une flotte pensée pour les amateurs de sensations fortes et d'exploration.","Une heure intense ou trois heures d'exploration : les tarifs flexibles s'adaptent à votre envie. Casque, protections et tout l'équipement sont fournis.",["Dès 800 DH","Modèles 2025","Protections fournies"]),
 "buggy":("Buggy","v-canam.png",False,"Du buggy tout-terrain classique au buggy de course plus sportif, adapté à tous les niveaux. Une façon originale et passionnante de découvrir la région.","Véhicules soigneusement entretenus et inspectés pour garantir une expérience optimale.",["Dès 300 DH","1 h ou 2 h","Tous niveaux"]),
 "karting":("Rallye-karting","v-kart.png",False,"Un circuit de karting de pointe au cœur de la Ville Rouge. Vitesse, excitation et action à l'état pur dans un environnement divertissant et compétitif.","Sessions de 15 minutes chronométrées, idéales pour un challenge entre amis ou collègues. Karts enfants disponibles.",["200 DH / 15 min","Chronométré","Enfants bienvenus"]),
 "waterkarting":("Water karting","v-waterkart.png",False,"Un kart qui flotte sur l'eau : la toute dernière génération WATERKART, sur le premier circuit de water karting d'Afrique. Le mélange parfait de sensations fortes et de rires.","Gilets de sauvetage et casques fournis. Ouvert à tous les membres de la famille, des plus jeunes aux plus âgés. Jet ski également disponible dans nos packs.",["Dès 800 DH","15 ou 30 min","Toute la famille","1er en Afrique"]),
 "paintball":("Paintball & stand de tir","v-paintball.png",False,"Le paintball chez nous, c'est l'adrénaline à l'état pur : terrain aménagé, obstacles, équipement complet. Affrontez vos amis dans des batailles épiques.","Notre stand de tir bien équipé offre une expérience de précision pour les amateurs. Encadrement par des professionnels.",["200 DH / 100 balles","Par équipes","Encadré"]),
 "supercars":("Supercars · immersion pilotage","v-aventador.png",False,"Lamborghini Huracán EVO Spyder, Lamborghini Aventador S, Lamborghini Urus, Ferrari 488 Spider et Porsche 911 Turbo S 992 : prenez le volant pour un test drive dans le désert de Marrakech.","Sessions de 15 minutes à 1 heure, accompagné d'un instructeur. Une expérience inoubliable à offrir ou à s'offrir.",["Dès 2000 DH","15 min à 1 h","Avec instructeur"]),
}
acts_html = ""
for a in ACTS:
    t,img,photo,p1,p2,meta = DETAILS[a["id"]]
    acts_html += f'''<article class="act" id="{a["id"]}"><div class="act-media{' photo' if photo else ''} rv"><img src="assets/img/{img}" alt="{t}" loading="lazy"></div>
 <div class="rv"><span class="eyebrow">{a["t"]}</span><h3>{t}</h3><p>{p1}</p><p style="margin-top:.8rem">{p2}</p>
 <div class="meta">{"".join(f"<span>{m}</span>" for m in meta)}</div>
 <div class="hero-actions"><a class="btn btn-red btn-sm" href="tarifs.html">Voir les tarifs</a><a class="btn btn-wa btn-sm" href="{WA}?text=Bonjour, je souhaite des informations sur : {t}" target="_blank" rel="noopener">{SVG["wa"]} Réserver</a>{'<a class="btn btn-ghost btn-sm" href="franchise.html">Devenez franchisé</a>' if a["id"]=="waterkarting" else ''}</div></div></article>'''
subnav = "".join(f'<a href="#{a["id"]}">{a["t"]}</a>' for a in ACTS)
page("activites.html","Activités – Quad, Can-Am, buggy, moto-cross, karting, water karting, paintball, supercars | N.A.R. Complexe Marrakech",
     "Toutes les activités du complexe N.A.R. à Marrakech : quad, Raptor, Can-Am Maverick, buggy, moto-cross, karting, water karting, paintball, stand de tir et test drive supercars.",
     page_head("Activités","Nos <span class='accent'>activités</span>","Neuf façons de faire monter l'adrénaline, sur terre, sur l'eau et sur circuit. Toutes accessibles sans réservation.","p-flotte.jpg")
     + f'<div class="subnav"><div class="wrap">{subnav}</div></div><section style="padding-top:0"><div class="wrap">{acts_html}</div></section>' + cta_band())

# ----------------------------------------------------------- TARIFS
tarifs_body = page_head("Tarifs","Tarifs <span class='sand'>2026</span>","Ouvert 7j/7 sans réservation, de 9h à 22h, dans la joie et la bonne humeur. Prix en dirhams, équipement de sécurité inclus.","p-canam-jaune.jpg") + f'''
<div class="subnav"><div class="wrap"><a href="#location">Location</a><a href="#excursions">Excursions</a><a href="#packs">Packs</a><a href="#supercars">Supercars</a><a href="#affiche">Affiche officielle</a></div></div>
<section id="location"><div class="wrap">
 <div class="sec-head rv"><div><span class="eyebrow">Location à la durée</span><h2>Quads, SSV, motos <span class="accent">& circuits</span></h2></div><p>Casque et équipement fournis. Accès piscine gratuit. Service photographe et vidéo drone en option.</p></div>
 <div class="tarif-grid">{"".join(tarif_card(t) for t in TARIFS)}</div>
 <p class="form-note" style="margin-top:1.4rem">Rafraîchissements disponibles sur place (NAR Food). Tarifs indicatifs susceptibles d'évoluer, confirmez par WhatsApp.</p>
</div></section>
{excursions_section()}
{packs_section(alt=False)}
<section id="supercars" class="alt"><div class="wrap"><div class="split">
 <div class="rv"><span class="eyebrow">Test drive</span><h2>Immersion <span class="sand">pilotage</span></h2>
  <p class="lead" style="margin-top:1rem">Porsche 911 Carrera 4S, Lamborghini Huracán EVO Spyder, Lamborghini Aventador S, Ferrari 488 Spider, Lamborghini Urus. Une expérience inoubliable dans le désert de Marrakech.</p>
  <div class="tarif rv" style="margin-top:1.5rem;max-width:420px"><table><tr><td>15 min</td><td>2000<small>DH</small></td></tr><tr><td>30 min</td><td>3000<small>DH</small></td></tr><tr><td>1 h</td><td>4000<small>DH</small></td></tr></table></div></div>
 <div class="grid grid-2 rv"><div class="render"><img src="assets/img/v-huracan.png" alt="Lamborghini Huracán EVO Spyder" loading="lazy"><span>Lamborghini Huracán EVO Spyder</span></div><div class="render"><img src="assets/img/v-ferrari.png" alt="Ferrari 488 Spider" loading="lazy"><span>Ferrari 488 Spider</span></div><div class="render"><img src="assets/img/v-aventador.png" alt="Lamborghini Aventador S" loading="lazy"><span>Lamborghini Aventador S</span></div><div class="render"><img src="assets/img/v-urus.png" alt="Lamborghini Urus" loading="lazy"><span>Lamborghini Urus</span></div></div>
</div></div></section>
<section id="affiche"><div class="wrap">
 <div class="sec-head rv"><div><span class="eyebrow">À télécharger</span><h2>L'affiche <span class="accent">officielle</span></h2></div><p>La grille complète au format image, pratique à partager sur WhatsApp.</p></div>
 <div class="grid grid-2 rv"><a href="assets/img/tarifs-affiche.jpg" data-lightbox><img src="assets/img/tarifs-affiche.jpg" alt="Affiche des tarifs N.A.R. Complexe" style="border-radius:14px" loading="lazy"></a><a href="assets/img/tarifs-packs.jpg" data-lightbox><img src="assets/img/tarifs-packs.jpg" alt="Affiche des packs N.A.R. Complexe" style="border-radius:14px" loading="lazy"></a></div>
</div></section>
''' + cta_band("Une question sur les tarifs ?","Écrivez-nous sur WhatsApp, on vous répond rapidement et on vous conseille la formule adaptée à votre groupe.")
page("tarifs.html","Tarifs 2026 – Location quad, Can-Am, buggy, karting, water karting, packs | N.A.R. Complexe Marrakech",
     "Tous les tarifs du complexe N.A.R. à Marrakech : quad dès 100 DH, Can-Am Maverick, Raptor 700, moto-cross, karting, water karting, paintball, test drive supercars et packs tout compris. Sans réservation.", tarifs_body)

# ----------------------------------------------------------- GALERIE
gal = "".join(f'<a href="assets/img/{f}" data-lightbox class="rv"><img src="assets/img/{f}" alt="{a}" loading="lazy"></a>' for f,a in GALLERY)
page("galerie.html","Galerie photos – N.A.R. Complexe Sportif Marrakech",
     "Explorez N.A.R. Complexe en images : quad, Can-Am, karting, water karting, paintball, activités enfants et vue aérienne du complexe à Marrakech.",
     page_head("Galerie","En <span class='accent'>images</span>","Parcourez la galerie et plongez dans l'univers du complexe, où le sport motorisé et l'aquatique se rencontrent.","p-groupe-drapeau.jpg")
     + f'<section style="padding-top:2rem"><div class="wrap"><div class="masonry">{gal}</div><p class="form-note" style="margin-top:2rem">Suivez-nous sur <a class="sand" href="https://www.instagram.com/n.a.r_complexe/" target="_blank" rel="noopener">Instagram</a>, <a class="sand" href="https://www.tiktok.com/@n.a.r_complexe" target="_blank" rel="noopener">TikTok</a> et <a class="sand" href="https://www.snapchat.com/add/narcomplexe" target="_blank" rel="noopener">Snapchat</a> pour les vidéos du jour.</p></div></section>' + cta_band())

# ----------------------------------------------------------- ENTREPRISES
acts_opts = "".join(f'<label style="display:flex;gap:.5rem;align-items:center;font-size:.95rem;color:#ddd"><input type="checkbox" name="activites" value="{a["t"]}" style="width:auto"> {a["t"]}</label>' for a in ACTS)
b2b = page_head("Entreprises","Offres <span class='sand'>entreprises</span>","Séminaires, team building, incentives : des tarifs préférentiels et un programme sur mesure pour renforcer la cohésion de vos équipes.","p-paintball-groupe.jpg") + f'''
<section><div class="wrap"><div class="split" style="align-items:start">
 <div class="rv"><span class="eyebrow">Zoom sur l'offre B2B</span><h2>Des moments <span class="accent">mémorables</span> pour vos équipes</h2>
  <p class="lead" style="margin:1rem 0">Chez N.A.R. Complexe, nous savons l'importance du bien-être des collaborateurs et de la cohésion d'équipe. Nous proposons des tarifs préférentiels aux entreprises qui souhaitent offrir à leurs équipes des expériences sportives et aquatiques uniques.</p>
  <ul class="checks"><li>Challenge karting chronométré avec podium</li><li>Tournoi de paintball par équipes</li><li>Raid en quad ou Can-Am vers la palmeraie ou l'Atlas, pause thé et barbecue</li><li>Water karting et piscine pour la détente</li><li>Terrasse privatisable, restauration sur place</li><li>Service photographe et vidéo drone pour vos réseaux</li></ul>
  <div class="info-cards" style="grid-template-columns:1fr 1fr"><div class="info"><div class="ic">{SVG["phone"]}</div><div><h3>Par téléphone</h3><a href="tel:{TEL_RAW}">{TEL}</a></div></div><div class="info"><div class="ic">{SVG["clock"]}</div><div><h3>Réponse</h3><p>Sous 24 h ouvrées</p></div></div></div></div>
 <div class="rv" style="background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:2rem">
  <h3 style="margin-bottom:.4rem">Demander une offre personnalisée</h3><p class="form-note" style="margin-bottom:1.4rem">Remplissez le formulaire, il s'ouvre dans WhatsApp prérempli : vous n'avez plus qu'à l'envoyer.</p>
  <form id="form-b2b" class="form">
   <div class="field"><label for="societe">Société</label><input id="societe" name="societe" required placeholder="Nom de l'entreprise"></div>
   <div class="field"><label for="nom">Votre nom</label><input id="nom" name="nom" required placeholder="Prénom Nom"></div>
   <div class="field"><label for="tel">Téléphone</label><input id="tel" name="tel" type="tel" required placeholder="+212 6 …"></div>
   <div class="field"><label for="email">E-mail</label><input id="email" name="email" type="email" placeholder="vous@societe.com"></div>
   <div class="field"><label for="taille">Nombre de participants</label><select id="taille" name="taille"><option>5 – 10</option><option>10 – 20</option><option>20 – 50</option><option>50 et plus</option></select></div>
   <div class="field"><label for="date">Date souhaitée</label><input id="date" name="date" type="date"></div>
   <div class="field full"><label>Activités envisagées</label><div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem;margin-top:.3rem">{acts_opts}</div></div>
   <div class="field full"><label for="message">Message</label><textarea id="message" name="message" placeholder="Objectif de la journée, budget, contraintes…"></textarea></div>
   <div class="full"><button class="btn btn-wa" type="submit" style="width:100%;justify-content:center">{SVG["wa"]} Envoyer ma demande</button></div>
  </form></div>
</div></div></section>
<section class="alt"><div class="wrap"><div class="strip rv">{"".join(f'<a href="assets/img/{f}" data-lightbox><img src="assets/img/{f}" alt="{a}" loading="lazy"></a>' for f,a in [GALLERY[3],GALLERY[7],GALLERY[8],GALLERY[2],GALLERY[10],GALLERY[0]])}</div></div></section>'''
page("entreprises.html","Offres entreprises – Team building & séminaires à Marrakech | N.A.R. Complexe",
     "Tarifs préférentiels pour les entreprises : team building karting, paintball, raid en quad ou Can-Am, water karting, barbecue. Demandez une offre personnalisée.", b2b)

# ----------------------------------------------------------- À PROPOS
about = page_head("À propos","Notre <span class='accent'>oasis sportive</span>","Bienvenue dans notre complexe, où l'aventure et la sécurité vont de pair. Pionniers exclusifs en Afrique, nous vous proposons des expériences uniques.","p-drone.jpg") + f'''
<section><div class="wrap"><div class="split">
 <div class="rv"><span class="eyebrow">N.A.R. Complexe</span><h2>Vivez l'aventure <span class="sand">en toute sécurité</span></h2>
  <p class="lead" style="margin-top:1rem">Notre équipe expérimentée assure votre sécurité lors de toutes nos activités tout-terrain : quad, buggy, moto-cross, karting et water karting. Nous organisons également des excursions dans la palmeraie et le désert de Marrakech.</p>
  <p style="margin-top:.8rem">Que vous représentiez une entreprise à la recherche d'activités B2B captivantes ou que vous soyez un particulier en quête d'aventures inoubliables, chaque expérience est conçue pour offrir un mélange parfait d'aventure, de sécurité et de plaisir.</p></div>
 <div class="pic rv"><img src="assets/img/p-groupe-quad.jpg" alt="Groupe d'amis en quad" loading="lazy"></div>
</div></div></section>
<section class="alt"><div class="wrap"><div class="why">
 <div class="why-item rv"><div class="ic">{SVG["shield"]}</div><h3>L'équipe</h3><p>Des professionnels chevronnés qui connaissent la région. Instructions détaillées et équipement complet avant chaque sortie.</p></div>
 <div class="why-item rv"><div class="ic">{SVG["kid"]}</div><h3>Activités enfants</h3><p>Pistes de quad, de moto et de kart conçues pour les enfants, encadrées par des professionnels qualifiés.</p></div>
 <div class="why-item rv"><div class="ic">{SVG["pool"]}</div><h3>Pause fraîcheur</h3><p>Granitas aux multiples saveurs, thé marocain, piscine et terrasse ombragée quand la chaleur est à son comble.</p></div>
 <div class="why-item rv"><div class="ic">{SVG["bolt"]}</div><h3>+110 véhicules</h3><p>Kawasaki, Yamaha, Honda, Can-Am, WATERKART… une flotte entretenue et inspectée régulièrement.</p></div>
</div></div></section>
<section><div class="wrap"><div class="split rev">
 <div class="pic rv"><img src="assets/img/p-enfants-mascottes.jpg" alt="Activités enfants avec mascottes" loading="lazy"></div>
 <div class="rv"><span class="eyebrow">Petits aventuriers</span><h2>Les enfants ont <span class="accent">leur piste</span></h2>
  <p class="lead" style="margin-top:1rem">N.A.R. Complexe propose des activités spécialement conçues pour les enfants : quads, motos et karts adaptés, sur un circuit encadré et sécurisé. Nous croyons en l'importance de les initier à ces activités passionnantes tout en garantissant leur sécurité.</p>
  <div class="hero-actions" style="margin-top:1.4rem"><a class="btn btn-ghost" href="tarifs.html">Tarifs enfants dès 100 DH</a></div></div>
</div></div></section>
<section class="alt"><div class="wrap"><div class="sec-head rv"><div><span class="eyebrow">Questions fréquentes</span><h2>Bon à <span class="sand">savoir</span></h2></div></div>
<div class="faq rv">
 <details><summary>Faut-il réserver ?</summary><p>Non. Le complexe est ouvert 7 jours sur 7 de 9h à 22h, sans réservation. Pour les groupes et les entreprises, un message WhatsApp nous aide à tout préparer.</p></details>
 <details><summary>L'équipement est-il fourni ?</summary><p>Oui : casques, protections, gilets de sauvetage pour le water karting, et un briefing détaillé avant chaque activité.</p></details>
 <details><summary>Les enfants peuvent-ils participer ?</summary><p>Oui. Quads, motos et karts enfants sont disponibles sur un circuit dédié et encadré, dès 100 DH les 10 tours.</p></details>
 <details><summary>Où se trouve le complexe ?</summary><p>{ADDR}, aux portes du désert. Cliquez sur le bouton Waze en bas de page pour l'itinéraire.</p></details>
 <details><summary>Peut-on manger sur place ?</summary><p>Oui : rafraîchissements, granitas, thé marocain et restauration NAR Food. Les excursions de 1h et plus incluent une pause thé et msemen, et la formule 3h un barbecue.</p></details>
</div></div></section>''' + cta_band()
page("a-propos.html","À propos – N.A.R. Complexe Sportif, Marrakech","Découvrez N.A.R. Complexe : équipe, sécurité, activités enfants, pause fraîcheur et questions fréquentes. Ouvert 7j/7 de 9h à 22h.", about)

# ----------------------------------------------------------- CONTACT
contact = page_head("Contact","Contact <span class='sand'>& accès</span>","Une question, un groupe, une surprise à organiser ? Le plus rapide reste WhatsApp.","p-panneau.jpg") + f'''
<section style="padding-top:2rem"><div class="wrap">
 <div class="info-cards rv">
  <div class="info"><div class="ic">{SVG["phone"]}</div><div><h3>Téléphone & WhatsApp</h3><p><a href="tel:{TEL_RAW}">{TEL}</a></p><a class="btn btn-wa btn-sm" style="margin-top:.8rem" href="{WA}" target="_blank" rel="noopener">{SVG["wa"]} Écrire</a></div></div>
  <div class="info"><div class="ic">{SVG["pin"]}</div><div><h3>Adresse</h3><p>{ADDR}</p><p style="margin-top:.6rem"><a class="sand" href="{WAZE}" target="_blank" rel="noopener">Waze →</a> &nbsp; <a class="sand" href="{MAPS}" target="_blank" rel="noopener">Google Maps →</a></p></div></div>
  <div class="info"><div class="ic">{SVG["clock"]}</div><div><h3>Horaires</h3><p>Lundi – dimanche<br>9h00 – 22h00<br><strong>Sans réservation</strong></p></div></div>
 </div>
 <div class="map rv" style="margin-top:1.4rem;aspect-ratio:16/8"><iframe src="{MAP_EMBED}" loading="lazy" title="Carte N.A.R. Complexe" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
 <div class="socials rv" style="margin-top:1.6rem"><a href="https://www.instagram.com/n.a.r_complexe/" target="_blank" rel="noopener" aria-label="Instagram">{SVG["ig"]}</a><a href="https://www.tiktok.com/@n.a.r_complexe" target="_blank" rel="noopener" aria-label="TikTok">{SVG["tt"]}</a><a href="https://www.snapchat.com/add/narcomplexe" target="_blank" rel="noopener" aria-label="Snapchat">{SVG["snap"]}</a></div>
</div></section>'''
page("contact.html","Contact & accès – N.A.R. Complexe Sportif Marrakech","Contactez N.A.R. Complexe à Marrakech : +212 6 02 58 79 22, WhatsApp, itinéraire Waze et Google Maps. Route de Casablanca, Douar Berhmoun. Ouvert 7j/7 de 9h à 22h.", contact)

# ----------------------------------------------------------- MENTIONS
ml = page_head("Mentions légales","Mentions <span class='sand'>légales</span>","Informations légales et politique de confidentialité du site narcomplexesportif.com.","p-terrasse.jpg") + f'''
<section style="padding-top:1rem"><div class="wrap prose">
 <h2>1. Présentation du site</h2><p><strong>Propriétaire :</strong> N.A.R. Complexe – {ADDR}.<br><strong>Responsable de publication :</strong> N.A.R. Complexe – {TEL}.<br><strong>Hébergeur :</strong> Namecheap.</p>
 <h2>2. Accès au site</h2><p>Le présent site est accessible 24 heures sur 24 et 7 jours sur 7, à l'exception des cas de force majeure, difficultés informatiques, maintenance, difficultés liées à la structure des réseaux de communication ou difficultés d'ordre technique.</p>
 <h2>3. Conditions générales d'utilisation</h2><p>La navigation sur ce site est soumise à la réglementation en vigueur et aux présentes conditions d'accès et d'utilisation.</p>
 <h2 id="donnees">4. Collecte et protection des données</h2><p>Nous collectons vos données personnelles uniquement lorsque vous nous contactez (formulaire, WhatsApp, téléphone) afin de répondre à votre demande. Conformément à la loi n° 09-08 promulguée par le Dahir 1-09-15 du 18 février 2009, relative à la protection des personnes physiques à l'égard du traitement des données à caractère personnel, vous bénéficiez d'un droit d'accès, de rectification et d'opposition aux informations qui vous concernent. Pour l'exercer, contactez-nous au {TEL}.</p>
 <h2>5. Cookies</h2><p>Ce site n'utilise pas de cookies de suivi publicitaire. Les services tiers intégrés (carte Google Maps, polices Google Fonts) peuvent déposer leurs propres cookies selon leurs politiques respectives. Vous pouvez vous y opposer en désactivant cette fonction dans les préférences de votre navigateur.</p>
 <h2>6. Limitation de responsabilité</h2><p>N.A.R. Complexe ne saurait être tenu responsable des dommages directs ou indirects résultant de l'utilisation ou de l'impossibilité d'utiliser les éléments de ce site. Les tarifs affichés sont indicatifs et peuvent évoluer sans préavis.</p>
 <h2>7. Propriété intellectuelle</h2><p>L'ensemble des contenus (textes, photos, vidéos, logo) est la propriété de N.A.R. Complexe ou de ses partenaires. Toute reproduction est interdite sans autorisation préalable.</p>
</div></section>'''
page("mentions-legales.html","Mentions légales – N.A.R. Complexe Sportif","Mentions légales et politique de confidentialité du site N.A.R. Complexe Sportif, Marrakech.", ml)
print("pages générées :", [f for f in os.listdir(OUT) if f.endswith('.html')])

# ----------------------------------------------------------- FRANCHISE
fr = page_head("Franchise","Devenez <span class='sand'>franchisé</span> Water Karting","Le premier circuit de water karting d'Afrique est né chez N.A.R. Complexe. Importez le concept dans votre ville : nous vous accompagnons de l'étude du site à l'ouverture.","p-drone.jpg") + f'''
<section><div class="wrap"><div class="split" style="align-items:start">
 <div class="rv"><span class="eyebrow">Le concept</span><h2>Un kart qui flotte, <span class="accent">un succès qui se duplique</span></h2>
  <p class="lead" style="margin:1rem 0">Le water karting combine la vitesse du karting et la fraîcheur d'un plan d'eau. Accessible à toute la famille, sans permis, il attire touristes et locaux toute l'année dans les climats chauds.</p>
  <ul class="checks"><li>Karts WATERKART dernière génération, gilets et casques fournis</li><li>Circuit aquatique modulable, installation sur bassin existant ou créé</li><li>Formation des équipes, procédures de sécurité et d'exploitation</li><li>Identité de marque, supports marketing et visibilité réseaux</li><li>Accompagnement au lancement puis suivi régulier</li></ul>
  <div class="info-cards" style="grid-template-columns:1fr 1fr"><div class="info"><div class="ic">{SVG["phone"]}</div><div><h3>Par téléphone</h3><a href="tel:{TEL_RAW}">{TEL}</a></div></div><div class="info"><div class="ic">{SVG["clock"]}</div><div><h3>Réponse</h3><p>Sous 48 h ouvrées</p></div></div></div></div>
 <div class="rv" style="background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:2rem">
  <h3 style="margin-bottom:.4rem">Demander le dossier franchise</h3><p class="form-note" style="margin-bottom:1.4rem">Vos coordonnées sont envoyées directement à l'équipe N.A.R. Complexe par e-mail.</p>
  <div class="form-msg ok" hidden>✓ Merci, votre demande a bien été envoyée. Nous revenons vers vous rapidement.</div>
  <div class="form-msg err" hidden>Le message n'a pas pu être envoyé. Vérifiez les champs obligatoires ou contactez-nous par téléphone.</div>
  <form id="form-franchise" class="form" method="post" action="https://www.narcomplexesportif.com/wp-admin/admin-post.php">
   <input type="hidden" name="action" value="nar_franchise"><input type="text" name="site_web" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
   <div class="field"><label for="f-nom">Nom et prénom *</label><input id="f-nom" name="nom" required></div>
   <div class="field"><label for="f-societe">Société</label><input id="f-societe" name="societe"></div>
   <div class="field"><label for="f-tel">Téléphone *</label><input id="f-tel" name="tel" type="tel" required></div>
   <div class="field"><label for="f-email">E-mail *</label><input id="f-email" name="email" type="email" required></div>
   <div class="field"><label for="f-lieu">Ville / pays du projet *</label><input id="f-lieu" name="lieu" required placeholder="Ex. : Agadir, Maroc"></div>
   <div class="field"><label for="f-budget">Budget envisagé</label><select id="f-budget" name="budget"><option>Non défini</option><option>Moins de 500 000 DH</option><option>500 000 – 1 000 000 DH</option><option>1 000 000 – 2 000 000 DH</option><option>Plus de 2 000 000 DH</option></select></div>
   <div class="field full"><label for="f-message">Votre projet</label><textarea id="f-message" name="message" placeholder="Terrain ou plan d'eau disponible, calendrier, expérience dans les loisirs…"></textarea></div>
   <div class="full"><button class="btn btn-red" type="submit" style="width:100%;justify-content:center">Envoyer ma demande</button></div>
  </form></div>
</div></div></section>
<section class="alt"><div class="wrap"><div class="strip rv">{"".join(f'<a href="assets/img/{f}" data-lightbox><img src="assets/img/{f}" alt="{a}" loading="lazy"></a>' for f,a in [GALLERY[2],GALLERY[13],GALLERY[0],GALLERY[8],GALLERY[7],GALLERY[5]])}</div></div></section>'''
page("franchise.html","Devenez franchisé Water Karting – N.A.R. Complexe Marrakech","Ouvrez un circuit de water karting dans votre ville avec le concept N.A.R. Complexe, pionnier en Afrique. Demandez le dossier franchise.", fr)

page("404.html","Page introuvable – N.A.R. Complexe","Cette page n'existe pas.", page_head("Erreur","Page <span class='accent'>introuvable</span>","Cette page n'existe pas ou a été déplacée. Retournez à l'accueil ou écrivez-nous sur WhatsApp.","p-desert-buggies.jpg") + cta_band("On vous remet sur la piste ?","Toutes les activités, tarifs et infos pratiques sont sur l'accueil."), active="index.html")
pages=["","activites.html","tarifs.html","galerie.html","entreprises.html","franchise.html","a-propos.html","contact.html","mentions-legales.html"]
open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>https://www.narcomplexesportif.com/{u}</loc></url>\n" for u in pages)+"</urlset>\n")
open(os.path.join(OUT,"robots.txt"),"w").write("User-agent: *\nAllow: /\nSitemap: https://www.narcomplexesportif.com/sitemap.xml\n")
