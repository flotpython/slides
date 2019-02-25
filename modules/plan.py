from IPython.display import HTML

PLAN = [
    "introduction",                             # 01
    ("types de base", [                         # 02
        "nombres: <code>int</code>, <code>float</code>, <code>complex</code>, <code>bool</code>",
        "séquences: <code>str</code>, <code>bytes</code>",
        "containers: <code>list</code>, <code>tuple</code>, <code>set</code>, <code>dict</code>",
        "fichier",
        "références partagées",
    ]),
    ("syntaxe et instructions", [               # 03
        "syntaxe & opérateurs",
        "instructions",
        "itérations",
    ]),
    ("fonctions", [
        "déclaration, passage de paramètres",   # 04
        "portée des variables",
        "objets fonction et lambdas",
    ]),
    ("modules & packages", [                    # 05
        "modules",
        "packages",
    ]),
    ("classes", [                               # 06
        "encapsulation",
        "héritage",
        "surcharge des opérateurs",
    ]),
    ("compléments", [                           # 07
        "exceptions",
        "librairies utiles",
        "outils utiles",
        "type hints",
        "asyncio",
        # "regexps",          # vide pour l'instant
    ]),
    ("sujets avancés", [                        # 08
        "context managers",
        "méthodes statiques et de classe",
        "décorateurs",
        "espaces de nommage",
        "protocole d'accès aux attributs",
        "générateurs",
        "métaclasses",
    ]),
#    ("autres", [
#        "",
#    ]),
#    "librairies de base",
]


def span(text, bold, strike):
    class_ = ''
    if bold or strike:
        class_ += ' class="'
    if bold:
        class_ += ' plan-bold'
    if strike:
        class_ += ' plan-strike'
    if bold or strike:
        class_ += '"'
    return (f"<span{class_}>{text}</span>")


def plan(title, subtitle=None, level=2):
    result = f"<h{level} class='plan'>plan du cours</h{level}>"
    result += "<ul class='plan'>"
    done = True
    for item in PLAN:
        # are there subsections ?
        if isinstance(item, str):
            pl_title, pl_subtitles = item, []
        else:
            pl_title, pl_subtitles = item
        # is this the current topic ?
        cur_title = title.lower() in pl_title
        if cur_title:
            done = False
        # write section
        result += f"<li>{span(pl_title, bold=cur_title, strike=done)}"
        # if we've asked for subsections, only detail
        # the current section
        subdone = True
        if subtitle and cur_title and pl_subtitles:
            result += "<ul class='subplan'>"
            for pl_subtitle in pl_subtitles:
                cur_subtitle = subtitle.lower() in pl_subtitle
                if cur_subtitle:
                    subdone = False
                item = span(pl_subtitle, bold=cur_subtitle, strike=subdone)
                result += f"<li>{item}</li>"
            result += "</ul>"
        # close section
        result +="</li>"
    result += "</ul>"
    return HTML(result)
