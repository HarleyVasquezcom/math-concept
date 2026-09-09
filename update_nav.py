with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Make switcher prominent and visible in fixed top header
old_nav = """<nav>
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

new_nav = """<nav>
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
  <div class="lang-switcher" style="display: flex; gap: 4px; align-items: center; background: rgba(255, 255, 255, 0.06); padding: 4px 10px; border-radius: 20px; border: 1px solid var(--border-strong);">
    <span style="font-size: 11px; color: var(--accent); margin-right: 4px;"><i class="fas fa-globe"></i></span>
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

if old_nav in html:
    html = html.replace(old_nav, new_nav)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Nav updated with globe icon and pill bar styling")
else:
    print("Could not locate old_nav block")
