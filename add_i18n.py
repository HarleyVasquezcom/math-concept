import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add styles for lang-btn hover/active
style_addition = """
.lang-switcher {
  display: flex;
  gap: 4px;
  align-items: center;
}
.lang-btn {
  background: transparent;
  border: 1px solid var(--border-strong);
  color: var(--fg-dim);
  padding: 4px 8px;
  border-radius: 6px;
  cursor: pointer;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  transition: all 0.2s;
}
.lang-btn:hover {
  border-color: var(--accent);
  color: var(--fg);
}
.lang-btn.active {
  background: var(--bg-card);
  border-color: var(--accent);
  color: var(--accent);
  font-weight: 600;
}
"""

html = html.replace("</style>", style_addition + "\n</style>")

# Update nav bar
nav_old = """<nav>
  <div class="logo">
    <span class="logo-mark">∠</span>
    AXIOMA
  </div>
  <div class="nav-links">
    <a href="#playground" data-num="01">Playground</a>
    <a href="#plots" data-num="02">Plots</a>
    <a href="#quiz" data-num="03">Quiz</a>
    <a href="#solutions" data-num="04">Solutions</a>
  </div>
  <a href="#hero" class="btn-secondary" style="padding: 8px 18px; font-size: 13px;">
    Begin
    <i class="fas fa-arrow-right" style="font-size: 11px;"></i>
  </a>
</nav>"""

nav_new = """<nav>
  <div class="logo">
    <span class="logo-mark">∠</span>
    AXIOMA
  </div>
  <div class="nav-links">
    <a href="#playground" data-num="01" data-i18n="nav_playground">Playground</a>
    <a href="#plots" data-num="02" data-i18n="nav_plots">Plots</a>
    <a href="#quiz" data-num="03" data-i18n="nav_quiz">Quiz</a>
    <a href="#solutions" data-num="04" data-i18n="nav_solutions">Solutions</a>
  </div>
  <div class="lang-switcher">
    <button class="lang-btn" data-lang="es">ES</button>
    <button class="lang-btn active" data-lang="en">EN</button>
    <button class="lang-btn" data-lang="de">DE</button>
    <button class="lang-btn" data-lang="pt">PT</button>
    <button class="lang-btn" data-lang="fr">FR</button>
    <button class="lang-btn" data-lang="it">IT</button>
  </div>
  <a href="#hero" class="btn-secondary" style="padding: 8px 18px; font-size: 13px;">
    <span data-i18n="nav_begin">Begin</span>
    <i class="fas fa-arrow-right" style="font-size: 11px;"></i>
  </a>
</nav>"""

html = html.replace(nav_old, nav_new)

# Add i18n script before </body>
i18n_js = """
/* ============================================
   6-LANGUAGE I18N SWITCHER (ES, EN, DE, PT, FR, IT)
   ============================================ */
const translations = {
  en: {
    nav_playground: "Playground",
    nav_plots: "Plots",
    nav_quiz: "Quiz",
    nav_solutions: "Solutions",
    nav_begin: "Begin",
    hero_badge: "LIVE · INTERACTIVE · MATHEMATICS",
    hero_title: 'Mathematics,<br><em>made tangible.</em>',
    hero_p: "Pull a vertex. Bend a curve. Watch the numbers answer back in real time. AXIOMA is a handcrafted field guide to the shapes, functions, and logic that quietly run the world.",
    hero_cta1: 'Open the playground <i class="fas fa-arrow-right" style="font-size: 12px;"></i>',
    hero_cta2: "See a worked solution",
    sec1_num: "01 — PLAYGROUND",
    sec1_title: 'Drag the <em>vertices</em>.<br>Read the triangle.',
    sec1_kicker: "Every side length, every interior angle, the area — all of it recomputed the instant you move a point. Geometry as a living instrument.",
    sec2_num: "02 — PLOTS",
    sec2_title: 'A polynomial<br><em>that obeys your fingers.</em>',
    sec2_kicker: "Four coefficients, four sliders. As you move them, the curve redraws, the roots migrate, and the extrema hunt for new hiding places along the x-axis.",
    sec3_num: "03 — QUIZ",
    sec3_title: 'Five questions.<br><em>Immediate feedback.</em>',
    sec3_kicker: "Pick an answer and the card flashes mint when you're right, coral when you're not. No grades, no timers — just the quiet satisfaction of knowing.",
    sec4_num: "04 — SOLUTIONS",
    sec4_title: 'One problem.<br><em>Revealed step by step.</em>',
    sec4_kicker: "Mathematics is mostly about the path, not the answer. Walk through the quadratic formula one move at a time — at your own pace."
  },
  es: {
    nav_playground: "Patio de juegos",
    nav_plots: "Gráficas",
    nav_quiz: "Cuestionario",
    nav_solutions: "Soluciones",
    nav_begin: "Comenzar",
    hero_badge: "MATEMÁTICAS · EN VIVO · INTERACTIVAS",
    hero_title: 'Matemáticas,<br><em>hechas tangibles.</em>',
    hero_p: "Arrastra un vértice. Curva una función. Observa cómo los números responden en tiempo real. AXIOMA es una guía interactiva de formas y lógica.",
    hero_cta1: 'Abrir patio de juegos <i class="fas fa-arrow-right" style="font-size: 12px;"></i>',
    hero_cta2: "Ver solución detallada",
    sec1_num: "01 — PATIO DE JUEGOS",
    sec1_title: 'Arrastra los <em>vértices</em>.<br>Lee el triángulo.',
    sec1_kicker: "Cada lado, ángulo interior y área se recalculan al instante en que mueves un punto. Geometría viva.",
    sec2_num: "02 — GRÁFICAS",
    sec2_title: 'Un polinomio<br><em>que obedece tus dedos.</em>',
    sec2_kicker: "Cuatro coeficientes, cuatro deslizadores. La curva se redibuja, las raíces migran y los extremos se recalculan.",
    sec3_num: "03 — CUESTIONARIO",
    sec3_title: 'Cinco preguntas.<br><em>Retroalimentación inmediata.</em>',
    sec3_kicker: "Elige una respuesta y la tarjeta se ilumina en menta si es correcta o coral si no lo es.",
    sec4_num: "04 — SOLUCIONES",
    sec4_title: 'Un problema.<br><em>Revelado paso a paso.</em>',
    sec4_kicker: "Recorre la fórmula cuadrática movimiento a movimiento, a tu propio ritmo."
  },
  de: {
    nav_playground: "Spielwiese",
    nav_plots: "Graphen",
    nav_quiz: "Quiz",
    nav_solutions: "Lösungen",
    nav_begin: "Starten",
    hero_badge: "LIVE · INTERAKTIV · MATHEMATIK",
    hero_title: 'Mathematik,<br><em>greifbar gemacht.</em>',
    hero_p: "Ziehe an einem Eckpunkt. Biege eine Kurve. Erlebe Mathematik in Echtzeit. AXIOMA ist ein interaktiver Leitfaden für Formen und Logik.",
    hero_cta1: 'Spielwiese öffnen <i class="fas fa-arrow-right" style="font-size: 12px;"></i>',
    hero_cta2: "Musterlösung ansehen",
    sec1_num: "01 — SPIELWIESE",
    sec1_title: 'Eckpunkte <em>ziehen</em>.<br>Dreieck ablesen.',
    sec1_kicker: "Seitenlängen, Innenwinkel und Flächeninhalt werden sofort neu berechnet. Geometrie als lebendiges Instrument.",
    sec2_num: "02 — GRAPHEN",
    sec2_title: 'Ein Polynom,<br><em>das deinen Fingern gehorcht.</em>',
    sec2_kicker: "Vier Koeffizienten, vier Regler. Wenn du sie bewegst, zeichnet sich die Kurve neu.",
    sec3_num: "03 — QUIZ",
    sec3_title: 'Fünf Fragen.<br><em>Sofortiges Feedback.</em>',
    sec3_kicker: "Wähle eine Antwort und die Karte leuchtet grün oder rot auf.",
    sec4_num: "04 — LÖSUNGEN",
    sec4_title: 'Ein Problem.<br><em>Schritt für Schritt erklärt.</em>',
    sec4_kicker: "Gehe die quadratische Lösungsformel Schritt für Schritt durch."
  },
  pt: {
    nav_playground: "Laboratório",
    nav_plots: "Gráficos",
    nav_quiz: "Questionário",
    nav_solutions: "Soluções",
    nav_begin: "Começar",
    hero_badge: "AO VIVO · INTERATIVO · MATEMÁTICA",
    hero_title: 'Matemática,<br><em>feita tangível.</em>',
    hero_p: "Mova um vértice. Dobre uma curva. Veja os números responderem em tempo real. AXIOMA é um guia interativo de formas e lógica.",
    hero_cta1: 'Abrir laboratório <i class="fas fa-arrow-right" style="font-size: 12px;"></i>',
    hero_cta2: "Ver solução passo a passo",
    sec1_num: "01 — LABORATÓRIO",
    sec1_title: 'Arraste os <em>vértices</em>.<br>Leia o triângulo.',
    sec1_kicker: "Comprimentos, ângulos e área são recalculados instantaneamente ao mover um ponto.",
    sec2_num: "02 — GRÁFICOS",
    sec2_title: 'Um polinômio<br><em>que obedece aos seus dedos.</em>',
    sec2_kicker: "Quatro coeficientes, quatro controles. A curva se desenha em tempo real.",
    sec3_num: "03 — QUESTIONÁRIO",
    sec3_title: 'Cinco perguntas.<br><em>Feedback imediato.</em>',
    sec3_kicker: "Escolha uma resposta e veja a confirmação visual instantânea.",
    sec4_num: "04 — SOLUÇÕES",
    sec4_title: 'Um problema.<br><em>Revelado passo a passo.</em>',
    sec4_kicker: "Acompanhe a fórmula de Bhaskara passo a passo, no seu próprio ritmo."
  },
  fr: {
    nav_playground: "Espace interactif",
    nav_plots: "Graphiques",
    nav_quiz: "Quiz",
    nav_solutions: "Solutions",
    nav_begin: "Commencer",
    hero_badge: "EN DIRECT · INTERACTIF · MATHÉMATIQUES",
    hero_title: 'Les mathématiques,<br><em>rendues tangibles.</em>',
    hero_p: "Déplacez un sommet. Incurvez une fonction. Observez les nombres répondre en temps réel. AXIOMA est un guide vivant des formes et de la logique.",
    hero_cta1: 'Ouvrir l\'espace interactif <i class="fas fa-arrow-right" style="font-size: 12px;"></i>',
    hero_cta2: "Voir une solution guidée",
    sec1_num: "01 — ESPACE INTERACTIF",
    sec1_title: 'Faites glisser les <em>sommets</em>.<br>Lisez le triangle.',
    sec1_kicker: "Longueur des côtés, angles et surface sont recalculés instantanément dès que vous déplacez un point.",
    sec2_num: "02 — GRAPHIQUES",
    sec2_title: 'Un polynôme<br><em>à portée de main.</em>',
    sec2_kicker: "Quatre coefficients, quatre curseurs. La courbe se redessine en temps réel.",
    sec3_num: "03 — QUIZ",
    sec3_title: 'Cinq questions.<br><em>Retour immédiat.</em>',
    sec3_kicker: "Sélectionnez une réponse et découvrez le résultat en direct.",
    sec4_num: "04 — SOLUTIONS",
    sec4_title: 'Un problème.<br><em>Révélé étape par étape.</em>',
    sec4_kicker: "Parcourez la formule quadratique pas à pas, à votre rythme."
  },
  it: {
    nav_playground: "Laboratorio",
    nav_plots: "Grafici",
    nav_quiz: "Quiz",
    nav_solutions: "Soluzioni",
    nav_begin: "Inizia",
    hero_badge: "LIVE · INTERATTIVO · MATEMATICA",
    hero_title: 'Matematica,<br><em>resa tangibile.</em>',
    hero_p: "Trascina un vertice. Piega una curva. Guarda i numeri rispondere in tempo reale. AXIOMA è una guida interattiva a forme e logica.",
    hero_cta1: 'Apri il laboratorio <i class="fas fa-arrow-right" style="font-size: 12px;"></i>',
    hero_cta2: "Vedi soluzione guidata",
    sec1_num: "01 — LABORATORIO",
    sec1_title: 'Trascina i <em>vertici</em>.<br>Leggi il triangolo.',
    sec1_kicker: "Lati, angoli e area ricalcolati all'istante quando muovi un punto.",
    sec2_num: "02 — GRAFICI",
    sec2_title: 'Un polinomio<br><em>ai tuoi comandi.</em>',
    sec2_kicker: "Quattro coefficienti, quattro cursori. La curva si ridisegna in tempo reale.",
    sec3_num: "03 — QUIZ",
    sec3_title: 'Cinque domande.<br><em>Feedback immediato.</em>',
    sec3_kicker: "Scegli una risposta per ricevere subito un riscontro visivo.",
    sec4_num: "04 — SOLUZIONI",
    sec4_title: 'Un problema.<br><em>Rivelato passo dopo passo.</em>',
    sec4_kicker: "Esplora la formula risolutiva per equazioni di secondo grado passo dopo passo."
  }
};

function switchLanguage(lang) {
  if (!translations[lang]) return;
  const t = translations[lang];

  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });

  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.dataset.i18n;
    if (t[key]) el.innerHTML = t[key];
  });

  showToast('Language changed to ' + lang.toUpperCase());
}

document.addEventListener('click', e => {
  const btn = e.target.closest('.lang-btn');
  if (btn) {
    switchLanguage(btn.dataset.lang);
  }
});
"""

# Inject data-i18n tags on elements
html = html.replace('LIVE · INTERACTIVE · MATHEMATICS', '<span data-i18n="hero_badge">LIVE · INTERACTIVE · MATHEMATICS</span>')
html = html.replace('<h1>Mathematics,<br><em>made tangible.</em></h1>', '<h1 data-i18n="hero_title">Mathematics,<br><em>made tangible.</em></h1>')
html = html.replace('<p>Pull a vertex. Bend a curve. Watch the numbers answer back in real time. AXIOMA is a handcrafted field guide to the shapes, functions, and logic that quietly run the world.</p>', '<p data-i18n="hero_p">Pull a vertex. Bend a curve. Watch the numbers answer back in real time. AXIOMA is a handcrafted field guide to the shapes, functions, and logic that quietly run the world.</p>')

# Section headers
html = html.replace('<div class="section-num">01 — PLAYGROUND</div>', '<div class="section-num" data-i18n="sec1_num">01 — PLAYGROUND</div>')
html = html.replace('<h2 class="section-title">Drag the <em>vertices</em>.<br>Read the triangle.</h2>', '<h2 class="section-title" data-i18n="sec1_title">Drag the <em>vertices</em>.<br>Read the triangle.</h2>')

html = html.replace('<div class="section-num">02 — PLOTS</div>', '<div class="section-num" data-i18n="sec2_num">02 — PLOTS</div>')
html = html.replace('<h2 class="section-title">A polynomial<br><em>that obeys your fingers.</em></h2>', '<h2 class="section-title" data-i18n="sec2_title">A polynomial<br><em>that obeys your fingers.</em></h2>')

html = html.replace('<div class="section-num">03 — QUIZ</div>', '<div class="section-num" data-i18n="sec3_num">03 — QUIZ</div>')
html = html.replace('<h2 class="section-title">Five questions.<br><em>Immediate feedback.</em></h2>', '<h2 class="section-title" data-i18n="sec3_title">Five questions.<br><em>Immediate feedback.</em></h2>')

html = html.replace('<div class="section-num">04 — SOLUTIONS</div>', '<div class="section-num" data-i18n="sec4_num">04 — SOLUTIONS</div>')
html = html.replace('<h2 class="section-title">One problem.<br><em>Revealed step by step.</em></h2>', '<h2 class="section-title" data-i18n="sec4_title">One problem.<br><em>Revealed step by step.</em></h2>')

html = html.replace('</script>', i18n_js + '\n</script>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("add_i18n.py executed successfully")
