#!/usr/bin/env python3
"""Gera os SVGs do perfil. Rodar na raiz do repo: python3 tools/gerar.py"""
import random, pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"
F = "font-family=\"'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif\""
COB, HERO, TINTA, PAPEL = "#2B3BFF", "#2433E0", "#0B1240", "#F4F6FF"
SOL, CORAL, MENTA, WORK = "#FFD23F", "#FF5D73", "#2EE6A8", "#0B3B40"
EASE = "cubic-bezier(.23,1,.32,1)"

def larg(txt, fs, k=.6):
    return len(txt) * fs * k

def salvar(nome, w, h, rotulo, corpo):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
           f'role="img" aria-label="{rotulo}">\n{corpo}\n</svg>\n')
    (OUT / nome).write_text(svg, encoding="utf-8")

def pixels(w, h, seed, livre=lambda x, y: True, prob=.2, viva=.4):
    r = random.Random(seed); s = []
    for x in range(3, w, 30):
        for y in range(3, h, 30):
            if r.random() > prob or not livre(x, y):
                continue
            if r.random() < viva:
                c = r.choice([SOL, CORAL, MENTA])
                s.append(f'<rect class="b" x="{x}" y="{y}" width="24" height="24" rx="5" fill="{c}" style="animation-delay:{r.uniform(0, 6):.2f}s"/>')
            else:
                s.append(f'<rect x="{x}" y="{y}" width="24" height="24" rx="5" fill="{PAPEL}" opacity=".07"/>')
    return "".join(s)

# ---------------------------------------------------------------- banner
def banner():
    W, H = 1200, 400
    frases = ["CRM e funil de vendas", "dashboards com dados reais", "agenda online",
              "relatório com assinatura", "firmware para ESP32"]
    rot = "".join(
        f'<text class="r" x="124" y="316" font-size="27" font-weight="800" fill="{SOL}" style="animation-delay:{i*2.4:.1f}s">{t}</text>'
        for i, t in enumerate(frases))
    # janela do sistema
    wx, wy, ww, wh = 700, 62, 430, 276
    cx, cy = wx + 104, wy + 52            # area de conteudo
    kpis = [("128", "leads", COB), ("R$ 48k", "em propostas", "#0F9B6E"), ("92%", "no prazo", CORAL)]
    k = ""
    for i, (n, l, c) in enumerate(kpis):
        x = cx + i * 104
        k += (f'<rect x="{x}" y="{cy}" width="96" height="58" rx="9" fill="#fff" stroke="{TINTA}" stroke-opacity=".12"/>'
              f'<text x="{x+11}" y="{cy+28}" font-size="19" font-weight="800" fill="{c}">{n}</text>'
              f'<text x="{x+11}" y="{cy+46}" font-size="10.5" font-weight="600" fill="{TINTA}" opacity=".6">{l}</text>')
    alt = [34, 52, 44, 70, 60, 86, 98]
    by = cy + 190
    barras = ""
    for i, a in enumerate(alt):
        c = MENTA if i == len(alt) - 1 else COB
        barras += f'<rect class="bar" x="{cx+14+i*25}" y="{by-a}" width="17" height="{a}" rx="4" fill="{c}" style="animation-delay:{i*.12:.2f}s"/>'
    lista = ""
    for i in range(4):
        y = cy + 96 + i * 25
        lista += (f'<circle cx="{cx+222}" cy="{y}" r="6" fill="{TINTA}" fill-opacity=".12"/>'
                  f'<circle class="ok" cx="{cx+222}" cy="{y}" r="6" fill="{MENTA}" style="animation-delay:{i*.9:.1f}s"/>'
                  f'<rect x="{cx+236}" y="{y-4}" width="{[62,48,70,40][i]}" height="8" rx="4" fill="{TINTA}" fill-opacity=".18"/>')
    menu = "".join(
        f'<rect x="{wx+16}" y="{wy+56+i*26}" width="{[56,44,52,38,48][i]}" height="10" rx="5" fill="{MENTA if i == 1 else PAPEL}" opacity="{1 if i == 1 else .28}"/>'
        for i in range(5))
    janela = f'''<g transform="rotate(-4 {wx+ww/2} {wy+wh/2})"><g class="jan">
<rect x="{wx+12}" y="{wy+12}" width="{ww}" height="{wh}" rx="16" fill="{TINTA}"/>
<g clip-path="url(#j)">
<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="{PAPEL}"/>
<rect x="{wx}" y="{wy}" width="{ww}" height="36" fill="#fff"/>
<rect x="{wx}" y="{wy+36}" width="88" height="{wh}" fill="{TINTA}"/>
{menu}
<circle cx="{wx+20}" cy="{wy+18}" r="5.5" fill="{CORAL}"/><circle cx="{wx+38}" cy="{wy+18}" r="5.5" fill="{SOL}"/><circle cx="{wx+56}" cy="{wy+18}" r="5.5" fill="{MENTA}"/>
<rect x="{wx+120}" y="{wy+9}" width="200" height="18" rx="9" fill="{TINTA}" fill-opacity=".08"/>
{k}
<rect x="{cx}" y="{cy+70}" width="200" height="132" rx="9" fill="#fff" stroke="{TINTA}" stroke-opacity=".12"/>
<rect x="{cx+208}" y="{cy+70}" width="104" height="132" rx="9" fill="#fff" stroke="{TINTA}" stroke-opacity=".12"/>
{barras}{lista}
</g>
<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" rx="16" fill="none" stroke="{TINTA}" stroke-width="3"/>
</g></g>'''
    def adesivo(x, y, txt, cor, ang, atraso, fg=TINTA):
        w = larg(txt, 17) + 34
        return (f'<g transform="rotate({ang} {x+w/2} {y+19})"><g class="p" style="animation-delay:{atraso}s">'
                f'<rect x="{x+4}" y="{y+4}" width="{w:.0f}" height="38" rx="19" fill="{TINTA}"/>'
                f'<rect x="{x}" y="{y}" width="{w:.0f}" height="38" rx="19" fill="{cor}" stroke="{TINTA}" stroke-width="2.5"/>'
                f'<text x="{x+w/2:.0f}" y="{y+25}" text-anchor="middle" font-size="17" font-weight="800" fill="{fg}">{txt}</text></g></g>')
    ades = (adesivo(640, 286, "ESP32", SOL, -8, 0) + adesivo(1040, 30, "Next.js", MENTA, 7, -1.6)
            + adesivo(1020, 322, "PostgreSQL", CORAL, 5, -3.1))
    corpo = f'''<style>
.b{{opacity:.14;animation:pisca 6s ease-in-out infinite}}
@keyframes pisca{{0%,100%{{opacity:.14}}20%{{opacity:.95}}40%{{opacity:.14}}}}
.e{{animation:entra 1s {EASE} both}}
@keyframes entra{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:none}}}}
.r{{opacity:0;animation:troca 12s {EASE} infinite}}
@keyframes troca{{0%{{opacity:0;transform:translateY(12px)}}3%,17%{{opacity:1;transform:none}}20%,100%{{opacity:0;transform:translateY(-12px)}}}}
.jan{{animation:chega 1.2s {EASE} .3s both}}
@keyframes chega{{from{{opacity:0;transform:translate(40px,24px)}}to{{opacity:1;transform:none}}}}
.bar{{transform-box:fill-box;transform-origin:bottom;animation:cresce 6s {EASE} infinite}}
@keyframes cresce{{0%{{transform:scaleY(.12)}}22%,86%{{transform:scaleY(1)}}100%{{transform:scaleY(.12)}}}}
.ok{{opacity:0;animation:marca 6s linear infinite}}
@keyframes marca{{0%,14%{{opacity:0}}18%,88%{{opacity:1}}94%,100%{{opacity:0}}}}
.p{{animation:flutua 5s ease-in-out infinite}}
@keyframes flutua{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-7px)}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.b{{opacity:.5}}.r{{opacity:0}}.r:first-of-type{{opacity:1}}.ok{{opacity:1}}}}
</style>
<defs><clipPath id="c"><rect width="{W}" height="{H}" rx="24"/></clipPath>
<clipPath id="j"><rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" rx="16"/></clipPath>
<linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{HERO}"/><stop offset=".5" stop-color="{HERO}" stop-opacity=".9"/><stop offset="1" stop-color="{HERO}" stop-opacity="0"/></linearGradient></defs>
<g clip-path="url(#c)" {F}>
<rect width="{W}" height="{H}" fill="{HERO}"/>
{pixels(W, H, 7)}
<rect width="760" height="{H}" fill="url(#g)"/>
<g class="e"><rect x="56" y="46" width="{larg("SISTEMAS WEB · DO PROTÓTIPO AO DEPLOY", 13, .68)+44:.0f}" height="32" rx="16" fill="{TINTA}" fill-opacity=".45"/>
<rect x="70" y="56" width="12" height="12" rx="3.5" fill="{SOL}"/>
<text x="92" y="67" font-size="13" font-weight="700" letter-spacing="1.3" fill="{PAPEL}">SISTEMAS WEB · DO PROTÓTIPO AO DEPLOY</text></g>
<text class="e" style="animation-delay:.12s" x="52" y="174" font-size="102" font-weight="800" letter-spacing="-3.5" fill="{PAPEL}">Lorran</text>
<text class="e" style="animation-delay:.24s" x="52" y="262" font-size="102" font-weight="800" letter-spacing="-3.5" fill="{SOL}">Rodrigues</text>
<g class="e" style="animation-delay:.45s"><text x="56" y="316" font-size="27" font-weight="600" fill="{PAPEL}">Faço</text>{rot}
<text x="56" y="356" font-size="19" font-weight="500" fill="{PAPEL}" opacity=".82">Transformo papel, planilha e grupo de WhatsApp em sistema.</text></g>
{janela}
{ades}
</g>'''
    salvar("banner.svg", W, H, "Lorran Rodrigues, desenvolvedor de sistemas web", corpo)

# ---------------------------------------------------------------- numeros
def numeros():
    W, H, g = 1200, 172, 18
    cw = (W - 2 * g) / 3
    dados = [("20", "sistemas construídos", "do agendamento ao CRM", COB, PAPEL, SOL),
             ("5", "demos no ar", "abra e teste agora", TINTA, MENTA, MENTA),
             ("89", "projetos com ESP32", "quando o problema sai da tela", CORAL, TINTA, TINTA)]
    s = ""
    for i, (n, t, sub, bg, cn, px) in enumerate(dados):
        x = i * (cw + g)
        ft = TINTA if bg == CORAL else PAPEL
        deco = "".join(
            f'<rect class="q" x="{x+cw-34-dx*26:.0f}" y="{16+dy*26}" width="20" height="20" rx="5" fill="{px}" style="animation-delay:{(dx+dy)*.5+i*.3:.1f}s"/>'
            for dx, dy in [(0, 0), (1, 0), (0, 1), (3, 0)])
        nx = x + 30
        tx = nx + larg(n, 84, .58) + 18
        s += (f'<g class="c" style="animation-delay:{i*.14:.2f}s"><rect x="{x:.0f}" y="0" width="{cw:.0f}" height="{H}" rx="22" fill="{bg}"/>{deco}'
              f'<text x="{nx:.0f}" y="112" font-size="84" font-weight="800" letter-spacing="-3" fill="{cn}">{n}</text>'
              f'<text x="{tx:.0f}" y="86" font-size="21" font-weight="800" fill="{ft}">{t}</text>'
              f'<text x="{tx:.0f}" y="111" font-size="15" font-weight="500" fill="{ft}" opacity=".75">{sub}</text></g>')
    corpo = f'''<style>.c{{animation:sobe .9s {EASE} both}}@keyframes sobe{{from{{opacity:0;transform:translateY(16px)}}to{{opacity:1;transform:none}}}}
.q{{opacity:.16;animation:q 4s ease-in-out infinite}}@keyframes q{{0%,100%{{opacity:.16}}30%{{opacity:.7}}60%{{opacity:.16}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style>
<g {F}>{s}</g>'''
    salvar("numeros.svg", W, H, "20 sistemas construídos, 5 demos no ar, 89 projetos com ESP32", corpo)

# ---------------------------------------------------------------- workito
def workito():
    W, H = 1200, 432
    seg = ""
    for i in range(7):
        x = 56 + i * 64
        seg += f'<rect x="{x}" y="222" width="56" height="10" rx="5" fill="{PAPEL}" fill-opacity=".14"/>'
        if i < 5:
            seg += f'<rect class="seg" x="{x}" y="222" width="56" height="10" rx="5" fill="{MENTA}" style="animation-delay:{.4+i*.18:.2f}s"/>'
    # funil
    fx, fy, cw, ch, gap = 608, 48, 170, 216, 12
    cols = [("LEAD", "8", [1, 2]), ("PROPOSTA", "3", [1]), ("GANHO", "5", [1, 2])]
    fun = ""
    for i, (nome, qt, slots) in enumerate(cols):
        x = fx + i * (cw + gap)
        ganho = i == 2
        fun += (f'<rect x="{x}" y="{fy}" width="{cw}" height="{ch}" rx="14" fill="{PAPEL}" fill-opacity=".06"/>'
                f'<text x="{x+14}" y="{fy+27}" font-size="12" font-weight="700" letter-spacing="1.5" fill="{MENTA if ganho else PAPEL}" opacity="{1 if ganho else .7}">{nome}</text>'
                f'<rect x="{x+cw-40}" y="{fy+12}" width="26" height="20" rx="10" fill="{PAPEL}" fill-opacity=".12"/>'
                f'<text x="{x+cw-27}" y="{fy+26}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{PAPEL}">{qt}</text>'
                f'<rect x="{x+12}" y="{fy+44}" width="{cw-24}" height="44" rx="8" fill="none" stroke="{PAPEL}" stroke-opacity=".16" stroke-dasharray="4 4"/>')
        for sl in slots:
            y = fy + 44 + sl * 54
            fun += (f'<rect x="{x+12}" y="{y}" width="{cw-24}" height="44" rx="8" fill="{MENTA if ganho else PAPEL}" fill-opacity="{.16 if ganho else .1}"/>'
                    f'<rect x="{x+24}" y="{y+12}" width="{[0, 78, 60][sl]}" height="7" rx="3.5" fill="{PAPEL}" fill-opacity=".4"/>'
                    f'<rect x="{x+24}" y="{y+26}" width="{[0, 46, 54][sl]}" height="6" rx="3" fill="{PAPEL}" fill-opacity=".2"/>')
    passo = cw + gap
    fun += (f'<g class="card"><rect x="{fx+16}" y="{fy+48}" width="{cw-24}" height="44" rx="8" fill="#062528"/>'
            f'<rect x="{fx+12}" y="{fy+44}" width="{cw-24}" height="44" rx="8" fill="{SOL}"/>'
            f'<rect class="ganho" x="{fx+12}" y="{fy+44}" width="{cw-24}" height="44" rx="8" fill="{MENTA}"/>'
            f'<text x="{fx+24}" y="{fy+62}" font-size="11" font-weight="700" fill="{TINTA}" opacity=".7">Padaria Central</text>'
            f'<text x="{fx+24}" y="{fy+79}" font-size="14" font-weight="800" fill="{TINTA}">R$ 12.400</text></g>')
    # modulos
    prontos = ["Funil de vendas", "Leads", "Comunicação", "Propostas", "Atividades", "Dashboard", "Planilhas"]
    breve = ["Análise de documentos", "Análise de feedback"]
    def linha(itens, y, cor, tracejado, t0):
        s, x = "", 176
        for i, t in enumerate(itens):
            w = round(larg(t, 14.5, .56) + 34)
            d = f'style="animation-delay:{t0+i*.9:.1f}s"'
            s += (f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="17" fill="{PAPEL}" fill-opacity=".05" stroke="{PAPEL}" stroke-opacity=".3"{" stroke-dasharray=\"5 4\"" if tracejado else ""}/>'
                  f'<rect class="on" x="{x}" y="{y}" width="{w}" height="34" rx="17" fill="{cor}" {d}/>'
                  f'<text x="{x+w/2}" y="{y+22}" text-anchor="middle" font-size="14.5" font-weight="600" fill="{PAPEL}">{t}</text>'
                  f'<text class="on" x="{x+w/2}" y="{y+22}" text-anchor="middle" font-size="14.5" font-weight="700" fill="{TINTA}" {d}>{t}</text>')
            x += w + 10
        return s
    mods = (f'<text x="56" y="325" font-size="12" font-weight="700" letter-spacing="1.5" fill="{MENTA}">NO MVP</text>'
            + linha(prontos, 304, MENTA, False, 0)
            + f'<text x="56" y="371" font-size="12" font-weight="700" letter-spacing="1.5" fill="{SOL}">EM BREVE</text>'
            + linha(breve, 350, SOL, True, 6.3))
    corpo = f'''<style>
.on{{opacity:0;animation:acende 8.1s linear infinite}}
@keyframes acende{{0%{{opacity:0}}1%,11.11%{{opacity:1}}12.11%,100%{{opacity:0}}}}
.card{{transform-box:fill-box;transform-origin:center;animation:anda 6s cubic-bezier(.77,0,.175,1) infinite}}
@keyframes anda{{0%,18%{{transform:translate(0,0)}}30%{{transform:translate({passo/2}px,-14px) rotate(-4deg)}}40%,58%{{transform:translate({passo}px,0)}}70%{{transform:translate({passo*1.5}px,-14px) rotate(4deg)}}80%,100%{{transform:translate({passo*2}px,0)}}}}
.ganho{{opacity:0;animation:cor 6s linear infinite}}
@keyframes cor{{0%,76%{{opacity:0}}82%,100%{{opacity:1}}}}
.seg{{animation:seg .5s {EASE} both}}
@keyframes seg{{from{{opacity:0;transform:translateX(-10px)}}}}
.pulso{{animation:pulso 1.6s ease-in-out infinite}}
@keyframes pulso{{50%{{opacity:.3}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.card{{transform:translate({passo}px,0)}}}}
</style>
<defs><radialGradient id="l" cx=".85" cy="0" r=".9"><stop offset="0" stop-color="{MENTA}" stop-opacity=".2"/><stop offset="1" stop-color="{MENTA}" stop-opacity="0"/></radialGradient></defs>
<rect width="{W}" height="{H}" rx="24" fill="{WORK}"/>
<rect width="{W}" height="{H}" rx="24" fill="url(#l)"/>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="23" fill="none" stroke="{MENTA}" stroke-opacity=".35" stroke-width="2"/>
<g {F}>
<rect x="56" y="48" width="150" height="28" rx="14" fill="{MENTA}"/><circle class="pulso" cx="74" cy="62" r="4" fill="{TINTA}"/>
<text x="86" y="67" font-size="13" font-weight="700" letter-spacing="1.4" fill="{TINTA}">EM DESTAQUE</text>
<text x="53" y="146" font-size="68" font-weight="800" letter-spacing="-2" fill="{PAPEL}">Workito</text>
<text x="58" y="178" font-size="18.5" fill="{PAPEL}" opacity=".85">CRM completo para equipes de vendas</text>
<text x="56" y="212" font-size="12" font-weight="700" letter-spacing="1.5" fill="{PAPEL}" opacity=".7">PROGRESSO DO MVP</text>
<text x="496" y="212" text-anchor="end" font-size="13" font-weight="700" fill="{MENTA}">5 de 7 fases</text>
{seg}
<text x="56" y="262" font-size="14.5" fill="{PAPEL}" opacity=".65">Dados isolados por empresa · 5 perfis de acesso</text>
{fun}
<rect x="56" y="284" width="{W-112}" height="1" fill="{PAPEL}" fill-opacity=".12"/>
{mods}
</g>'''
    salvar("workito.svg", W, H, "Workito, CRM SaaS em construção, 5 de 7 fases. No MVP: funil de vendas, leads, comunicação, propostas, atividades, dashboard e planilhas. Em breve: análise de documentos e de feedback", corpo)

# ---------------------------------------------------------------- stack
def stack():
    W, H = 1200, 196
    grupos = [("WEB", MENTA, ["TypeScript", "JavaScript", "React", "Next.js", "Tailwind"]),
              ("DADOS E INFRA", SOL, ["PostgreSQL", "Prisma", "Python", "Docker"]),
              ("HARDWARE", CORAL, ["ESP32", "Arduino", "C++", "LVGL 9"])]
    s = ""
    colw = (W - 96) / 3
    for gi, (nome, cor, itens) in enumerate(grupos):
        x0 = 48 + gi * colw
        s += (f'<rect x="{x0:.0f}" y="40" width="10" height="10" rx="3" fill="{cor}"/>'
              f'<text x="{x0+18:.0f}" y="50" font-size="12.5" font-weight="700" letter-spacing="1.6" fill="{cor}">{nome}</text>')
        x, y = x0, 70
        for t in itens:
            w = round(larg(t, 15, .58) + 32)
            if x + w > x0 + colw - 24:
                x, y = x0, y + 44
            s += (f'<rect x="{x:.0f}" y="{y}" width="{w}" height="34" rx="10" fill="{PAPEL}" fill-opacity=".08" stroke="{PAPEL}" stroke-opacity=".16"/>'
                  f'<text x="{x+w/2:.0f}" y="{y+22}" text-anchor="middle" font-size="15" font-weight="600" fill="{PAPEL}">{t}</text>')
            x += w + 8
        if gi:
            s += f'<rect x="{x0-22:.0f}" y="36" width="1" height="{H-72}" fill="{PAPEL}" fill-opacity=".12"/>'
    corpo = f'<rect width="{W}" height="{H}" rx="24" fill="{TINTA}"/><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="23" fill="none" stroke="{PAPEL}" stroke-opacity=".14" stroke-width="2"/><g {F}>{s}</g>'
    salvar("stack.svg", W, H, "Web: TypeScript, JavaScript, React, Next.js, Tailwind. Dados e infra: PostgreSQL, Prisma, Python, Docker. Hardware: ESP32, Arduino, C++, LVGL 9", corpo)

# ---------------------------------------------------------------- cta
def cta():
    W, H = 1200, 168
    px = "".join(f'<rect x="{x}" y="{y}" width="24" height="24" rx="5" fill="{TINTA}" opacity="{o}"/>'
                 for x, y, o in [(783, 3, .08), (813, 33, .14), (753, 123, .08), (783, 141, .12), (843, 3, .06), (723, 3, .05)])
    corpo = f'''<style>.s{{animation:vai 1.6s ease-in-out infinite}}@keyframes vai{{50%{{transform:translateX(6px)}}}}@media (prefers-reduced-motion:reduce){{.s{{animation:none}}}}</style>
<defs><clipPath id="c"><rect width="{W}" height="{H}" rx="24"/></clipPath></defs>
<g clip-path="url(#c)" {F}><rect width="{W}" height="{H}" fill="{SOL}"/>{px}
<text x="56" y="82" font-size="40" font-weight="800" letter-spacing="-1.2" fill="{TINTA}">Seu processo ainda vive no papel?</text>
<text x="58" y="118" font-size="19" font-weight="500" fill="{TINTA}" opacity=".8">Me conta como é hoje. Eu mostro como fica em sistema.</text>
<rect x="886" y="58" width="262" height="64" rx="32" fill="#0B1240" opacity=".25"/>
<rect x="880" y="52" width="262" height="64" rx="32" fill="{TINTA}"/>
<text x="924" y="91" font-size="20" font-weight="700" fill="{PAPEL}">Falar comigo</text>
<text class="s" x="1066" y="92" font-size="24" font-weight="700" fill="{SOL}">→</text></g>'''
    salvar("cta.svg", W, H, "Seu processo ainda vive no papel? Falar comigo", corpo)

# ---------------------------------------------------------------- botoes
def botao(nome, txt, bg, fg, borda, ponto=None):
    w = round(larg(txt, 17, .6) + (62 if ponto else 48)); h = 48
    tx = 44 if ponto else 24
    p = (f'<circle class="d" cx="26" cy="24" r="5.5" fill="{ponto}"/>' if ponto else "")
    corpo = (f'<style>.d{{animation:d 1.6s ease-in-out infinite}}@keyframes d{{50%{{opacity:.3}}}}</style>'
             f'<rect x="1.5" y="1.5" width="{w-3}" height="{h-3}" rx="{(h-3)/2}" fill="{bg}" stroke="{borda}" stroke-width="2"/>{p}'
             f'<text x="{tx}" y="30" {F} font-size="17" font-weight="700" fill="{fg}">{txt}</text>')
    salvar(nome, w, h, txt, corpo)

OUT.mkdir(exist_ok=True)
banner(); numeros(); workito(); stack(); cta()
botao("btn-portfolio.svg", "Ver o portfólio →", SOL, TINTA, TINTA)
botao("btn-demos.svg", "5 demos no ar", TINTA, PAPEL, MENTA, MENTA)
print("ok")
