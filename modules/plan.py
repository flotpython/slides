from IPython.display import HTML

plan_style = """
<style>
h1.plan, h2.plan, h3.plan {
    text-align: center;
    padding-bottom: 30px;
}

.plan-bold {
    font-weight: bold;
    font-style: italic;
    background-color: #eee;
}

ul.plan>li>span.plan-bold {
    font-size: 110%;
    padding: 4px;
}

ul.plan>li>ul.subplan>li>span.plan-bold {
    padding: 2px 4px;
}

.plan-strike {
    opacity: 0.4;
/*    text-decoration: line-through; */
}

div.plan-container {
    display: grid;
    grid-template-columns: 50% 50%;
}
</style>
"""

# a None section is meant as a separator

PLAN = {
    'header': "plan du cours",
    'outline': [
        "introduction",                             # 01
        ("types de base", [                         # 02
            "nombres&nbsp;:<code>int</code>, <code>float</code>, "
                "<code>complex</code>, <code>bool</code>", # pylint: disable=c0330
            "séquences & chaines&nbsp;:<code>str</code>",
            "containers&nbsp;:<code>list</code>, <code>tuple</code>, "
                "<code>set</code>, <code>dict</code>",  # pylint: disable=c0330
            "références partagées",
            "fichiers",
            "données brutes&nbsp;:<code>bytes</code>",
            "expressions régulières, module <code>re</code>",
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
        None,
        ("classes", [                               # 06
            "intro et exemples",
            "surcharge des opérateurs",
            "classes et attributs",
            "classes - avancé",
        ]),
        ("compléments", [                           # 07
            "exceptions",
            "librairies utiles",
            "outils utiles",
            "type hints",
            "asyncio",
            "nouvelles releases",
        ]),
#        ("sujets avancés", [                        # 08
#            "context managers",
#            "méthodes statiques et de classe",
#            "décorateurs",
#            "espaces de nommage",
#            "protocole d'accès aux attributs",
#            "générateurs",
#            "métaclasses",
#        ]),
    ],
}


PLAN_EXTRAS = {
    'header': "plan des suppléments",
    'outline': [
        ("numpy", [                          # 01
            "dimension 1",
            "dimension supérieures",
            "algèbre linéaire",
            "structured arrays",
        ]),
        "pandas (in english)",               # 02
        None,
        "notebooks",                         # 03
        "tests - bonnes pratiques",          # 04
        ("génération de documentation", [    # 05
            "outils",
            "readthedocs.io",
        ]),
        "packaging",                         # 06
        "vscode",                            # 07
    ],
}

def span(text, bold=False, strike=False):
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


def section_plan(data, title, subtitle, level):
    """
    one specific section, and possibly one specific subsection
    """
    result = ""
    result += plan_style
    result += f"<h{level} class='plan'>{data['header']}</h{level}>"
    result += "<ul class='plan'>"
    done = True
    for item in data['outline']:
        # ignore sectioning
        if item is None:
            continue
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


def detailed_plan(data, level):
    """
    all sections and subsections
    """
    result = ""
    result += plan_style
    result += f"<h{level} class='plan'>{data['header']}</h{level}>"
    result += "<div class='plan-container'>"
    result += "<div class='plan-part'>"
    result += "<ul class='plan'>"
    for item in data['outline']:
        if item is None:
            result += "</ul>"
            result += "</div>" # class='plan-part'
            result += "<div class='plan-part'>"
            result += "<ul class='plan'>"
            continue
        # are there subsections ?
        if isinstance(item, str):
            pl_title, pl_subtitles = item, []
        else:
            pl_title, pl_subtitles = item
        result += f"<li>{span(pl_title)}"
        if pl_subtitles:
            result += "<ul class='subplan'>"
            for pl_subtitle in pl_subtitles:
                result += f"<li>{span(pl_subtitle)}</li>"
            result += "</ul>"
        # close section
        result +="</li>"
    result += "</ul>"
    result += "</div>" # class='plan-part'
    result += "</div>" # class='plan-container'
    return HTML(result)



def plan(title=None, subtitle=None, *, level=1):
    if title is None:
        return detailed_plan(PLAN, level)
    else:
        return section_plan(PLAN, title, subtitle, level)


def plan_extras(title=None, subtitle=None, level=1):
    if title is None:
        return detailed_plan(PLAN_EXTRAS, level)
    else:
        return section_plan(PLAN_EXTRAS, title, subtitle, level)
