# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version, -language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode, -language_info.file_extension, -language_info.mimetype,
#       -toc
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
#     title: attributs de classe
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# </div>
#
# <style>
# .smaller {font-size: smaller}
# </style>

# %% [markdown] slideshow={"slide_type": ""}
# # attributs de classe
#
# où on voit que le modèle peut être un peu courbé:
#
# * les classes peuvent avoir des attributs de données
# * les méthodes peuvent ne pas prendre un objet en paramètre

# %% [markdown] slideshow={"slide_type": "slide"}
# ## attributs de classe

# %% cell_style="center"
class Student:
    
    all_students = []   # ici all_students est un attribut
                        # de la classe, et pas des instances
    
    def __init__(self, name):
        self.name = name
        Student.all_students.append(self)  # on peut y faire référence 
                                           # en partant de la classe


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
print(f"after step 1 we have {len(Student.all_students)} students")


# %% [markdown]
# <div class="micro-note">
#     
#     notez que dans la définition de `__init__` on aurait pu aussi 
#     écrire `self.all_students.append(self)`   
#     pourquoi ?
#     
# </div>    

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
s1.name, s2.name


# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## méthodes de classe
#
# sujet lié au précédent, mais d'utilisation (beaucoup) plus rare

# %% tags=["level_intermediate"]
class Student(RecordInstances):

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


# %% tags=["level_intermediate"]
s1 = Student('jean')
len(s1.all_instances)

# %% tags=["level_intermediate"]
s2 = Student('jean')
len(s1.all_instances), len(Student.all_instances)
