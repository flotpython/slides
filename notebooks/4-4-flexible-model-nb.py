# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: "le mod\xE8le est flexible"
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # le modèle est flexible
#
# jusqu'ici on a vu le **modèle usuel**, dans lequel
#
# * une instance possède des attributs de données
# * une classe possède des méthodes
# * une méthode prend un objet comme premier paramètre
#
# dans ce notebook on va voir que ce modèle peut être un peu courbé, c'est-à-dire que:
#
# * une classe peut aussi avoir des attributs de données
# * une méthode peut ne pas prendre un objet en paramètre
# * une méthode peut même prendre plutôt .. une classe en paramètre (un peu plus avancé)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## attributs de classe
#
# dans (l'espace de nom d')une classe, on peut mettre 
#
# * des méthodes (on le savait) 
# * et aussi attributs *normaux* - qui référencent des données
#
# rien de nouveau point de vue syntaxe : 
#
# * on écrit juste la déclaration dans la classe,
# * au même niveau d'imbrication que les méthodes
#
# voyons cela sur un exemple

# %% cell_style="center"
class Student:

    all_students = []   # ici all_students est un attribut
                        # de la classe, et pas des instances

    def __init__(self, name):
        self.name = name
        
        # on peut y faire référence
        # en partant de la classe
        
        Student.all_students.append(self)


# %% cell_style="center"
s = Student('jean')

# on peut faire référence à cet attribut comme ceci
#                                 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 
print(f"after step 1 we have {len(Student.all_students)} students")

# %% cell_style="center"
# est-ce que ceci va fonctionner aussi ?

print(f"after step 1 we have {len(s.all_students)} students")

# %% cell_style="center"
# du coup on peut comme cela agréger des choses relatives
# à tous les objets de la classe

s = Student('pierre')
print(f"after step 2 we have {len(Student.all_students)} students")


# %% [markdown]
# ````{admonition} quiz
# :class: seealso
#     
# notez que dans la définition de `__init__` on aurait pu aussi écrire `self.all_students.append(self)`  
# pourquoi ?
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ## méthodes statiques
#
# une technique utile pour exposer des pseudo-constructeurs

# %%
class Student:

    def __init__(self, name):
        self.name = name

    # on ne peut pas appeler cette méthode
    # avec un objet de type Student,
    # puisque précisément, c'est son propos
    # de construire un objet

    @staticmethod
    def load_from_file(filename):
        with open(filename) as f:
            return Student(f.readline().strip())


# %%
# et on l'appelle comme ceci

s1 = Student.load_from_file('student1.txt')
s2 = Student.load_from_file('student2.txt')

# et si on inspecte leur contenus
s1.name, s2.name


# %% [markdown] slideshow={"slide_type": "slide"} tags=[]
# ## méthodes de classe
#
# sujet avancé, lié au précédent, mais d'utilisation plus rare:

# %% tags=[]
class Student:

    all_instances = []

    # avec cette déclaration, ce n'est pas 
    # l'objet qui est passé en paramètre à 
    # la méthode, mais sa classe !
    
    @classmethod
    def record_instance(cls, instance):
        cls.all_instances.append(instance)
        
    def __init__(self, name):
        self.name = name
        self.record_instance(self)


# %% tags=[]
s1 = Student('jean')

len(s1.all_instances)

# %% tags=[]
s2 = Student('jean')

len(s1.all_instances), len(Student.all_instances)
