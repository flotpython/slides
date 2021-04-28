# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Edit Metadata
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   nbhosting:
#     title: exceptions
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] tags=["raises-exception"]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% slideshow={"slide_type": "slide"}
from plan import plan; plan("compléments", "exceptions") 

# %% [markdown] slideshow={"slide_type": "slide"}
# # exceptions

# %% [markdown]
# * mécanisme pour gérer les situations exceptionnelles

# %% cell_style="center" tags=["raises-exception"]
1 / 0


# %% [markdown] slideshow={"slide_type": "slide"}
# ## l'instruction `try` .. `except`

# %%
# une instruction `try except`
# permet de capturer une exception
def divide(x, y):
    try:
        res  = x / y
    except ZeroDivisionError:
        print('division by zero! ')
    print('continuing... ')


# %% cell_style="split"
divide(8, 3)

# %% cell_style="split"
divide(8, 0)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## l'instruction `raise`

# %% [markdown]
# pour signaler une condition exceptionnelle

# %%
def set_age(person, age):
    if not isinstance(age, int):
        raise ValueError("a person's age must be an integer")
    person['age'] = age


# %% cell_style="center" tags=["raises-exception"]
person = dict()

set_age(person, '10')


# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# ## exception et pile d'exécution

# %% [markdown]
# * en général, le `raise` ne se produit pas dans le même bloc
# * mais peut avoir lieu dans une fonction
# * à n'importe quelle profondeur de la pile

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exception et pile d'exécution

# %% cell_style="center"
# une fonction qui va faire raise
# mais pas tout de suite
def time_bomb(n):
    if n > 0:
        return time_bomb(n-1)
    else:
        raise OverflowError("BOOM")


# %% cell_style="split" slideshow={"slide_type": "slide"} tags=["raises-exception"]
def driver():
    time_bomb(1)
    print("will never pass here")

driver()     


# %% [markdown] cell_style="split"
# ![uncaught](media/except-stack-uncaught.png)

# %% cell_style="split" slideshow={"slide_type": "slide"}
def driver_try():
    try:
        time_bomb(2)
    except Exception as exc:
        print(f"OOPS {type(exc)}, {exc}")
    print("will do this")
    
driver_try()    

# %% [markdown] cell_style="split"
# ![try](media/except-stack-try.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## clause `except`

# %% [markdown] cell_style="center"
# * la clause `raise` doit fournir un objet idoine  
#   ne peut pas par exemple faire `raise 1`
#
# * doit être une instance de `BaseException`  
#   (ou de l'une de ses sous-classes)
#
# * la clause `except` permet de n'attraper  
#   qu'une partie des exceptions possibles
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ![exceptions](media/except-list.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### clause `except`

# %% [markdown]
# #### forme générale
#
# * on peut mettre plusieurs `except` après un `try:`  
#   chacune attrape **une partie** seulement des classes
#
# * la **première** qui convient est la bonne  
#   retour à un régime non exceptionnel
#
# * si **aucune** ne convient:  
#   l'exception se propage dans la pile  
#   c'est comme si on n'avait pas mis le `try:` du tout

# %% [markdown] slideshow={"slide_type": "slide"}
# #### clause `except`

# %% [markdown]
# ```python
# try:
#     bloc
#     de code
# except ExceptionClass:        # les instances de
#                               # ExceptionClass
# except (Class1, .. Classn):   # comme avec isinstance
# except Class as instance:     # donne un nom à l'objet 
#                               # levé par raise
# except:                       # attrape-tout - déconseillé    
# ```    

# %% [markdown] slideshow={"slide_type": "slide"}
# ### attrape-tout ?

# %% [markdown]
# #### capturer **toutes** les exceptions avec `except:` ou `except Exception:` 
#
# * est généralement une mauvaise idée
# * il vaut mieux comprendre ce que l’on capture
# * on risque de rendre silencieuses des exceptions non prévues
# * et d’avoir du mal à trouver les erreurs d’exécution
# * à réserver à une profondeur faible dans la pile
#   * pour éviter notamment une sortie brutale

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le module `traceback`

# %% [markdown]
# * en production
#   * pas d'attrape-tout
# * en développement
#   * ce n'est pas évident de tout envisager du premier coup
#   * forme répandue: attrape-tout avec instrumentation

# %% slideshow={"slide_type": "slide"}
import traceback

try:
    # un gros code; difficile de dire 
    # a priori toutes les exceptions
    # qui peuvent se produire
    pass
except OSError as exc:
    print(f"pour celle-ci je sais quoi faire {exc}")
except KeyboardInterrupt:
    print("pour celle-ci aussi")
except:
    # je suis tout près du main(), je ne veux pas laisser 
    # passer l'exception car ça se terminerait mal
    import traceback
    traceback.print_exc()

# %% slideshow={"slide_type": "slide"}
# la même chose avec le module logging
# en vrai on ne fait jamais print()
import logging

logging.basicConfig(level=logging.INFO)


try:
    # un gros code; difficile de dire 
    # a priori toutes les exceptions
    # qui peuvent se produire
    logging.info("in the code")
    1/ 0
except OSError as exc:
    logging.error(f"pour celle-ci je sais quoi faire {exc}")
except KeyboardInterrupt:
    logging.info("pour celle-ci aussi: bye")
except:
    # je suis tout près du main(), je ne veux pas laisser 
    # passer l'exception car ça se terminerait mal
    logging.exception("exception inattendue")


# %% [markdown] slideshow={"slide_type": "slide"}
# ## `try` .. `else` 

# %% [markdown]
# * avec une instruction `try except`, comment exécuter du code seulement lorsqu’il n’y a pas eu d’exception ?
#   * on utilise une clause `else`
#   * exécutée uniquement s’il n’y a pas eu d’exception
#   * une exception dans la clause `else` n’est pas capturée par les `except` précédents
# * inspiré de `while` .. `else` et `for` .. `else`  

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `try` .. `else` 

# %%
def divide(x,y):
    try:
        res  = x / y
    except ZeroDivisionError:
        print('zero divide !')
    else:
        print('all right, result is', res)
    print('continuing... ')


# %%
divide(8, 3)

# %%
divide(8, 0)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## `except` .. `as`

# %% [markdown]
# * la syntaxe `except Class as instance`
# * va réaliser une affectation de `instance`
# * vers l'objet qu'on a donné à `raise`
# * cette instance peut avoir des arguments stockés dans `instance.args` 

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `except` .. `as`

# %% [markdown]
# * la présence et le type de `inst.args` 
#   * va dépendre de l’exception
#   * ça peut être notamment une chaîne  
#     donnant des explications sur l’exception
#
# * dans tous les cas, cela donne des détails sur l’exception

# %% [markdown] slideshow={"slide_type": "slide"}
# ## instruction `raise`

# %% [markdown]
# **formes possibles**
#
# * `raise instance`  
#   forme usuelle, pour **déclencher**  
#   instance doit être une instance de `BaseException`
#
# * `raise`  
#   forme usuelle pour **propager** depuis un `except`  
#   l'exception originale est intacte
#
# * `raise new_instance from original_exc`  
#   pour **propagation** avec modification

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple de `as name`

# %%
# anticipons un peu: 
# je me définis ma propre classe d'exception
class MyException(Exception):
    def __str__(self):
        return f"<my-exception : {self.args}>"


# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple de `as value`

# %%
try:
    raise MyException('spam', 'eggs')
except MyException as exc:
    # comme on a redéfini __str__
    logging.info(exc) 
    # on peut extraire les données dans l'instance
    x, y = exc.args
    logging.info(f'x = {x}, y = {y}')


# %% [markdown] slideshow={"slide_type": "slide"}
# ## `try` .. `finally`

# %% [markdown]
# **une instruction `try` peut avoir une clause `finally`**
#
# * cette clause est **toujours** exécutée
#   * si il n'y a aucune exception
#   * si il y a une exception attrapée
#   * si il y a une exception non attrapée
#   * et même s'il y a un `return` dans le code !
# * elle sert à faire du nettoyage après l’exécution du bloc try
#   * par exemple fermer un fichier

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `try` .. `finally`

# %%
def finally_trumps_return(n):
    try:
        return n ** 2
    finally:
        logging.info("finally is invicible !")


# %%
finally_trumps_return(10)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple de `try`

# %% cell_style="split"
def divide(x, y):
    try:
        res  = x / y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is', res)
    finally:
        print('finally ..')
    print('continuing...')


# %% cell_style="split"
# pas d'exception
# try -> else 
#   -> finally -> continuing
divide(3, 4) 

# %% cell_style="split"
# une exception traitée
# try -> except 
#   -> finally -> continuing
divide(3, 0) 

# %% slideshow={"slide_type": "slide"} tags=["raises-exception"]
# une exception non traitée
# try -> finally -> BOOM
divide(3, 'a')


# %% [markdown] slideshow={"slide_type": "slide"}
# ## exception personnalisée

# %% [markdown]
# * dans la majorité des cas, on a uniquement besoin
#   * d’un nom d’exception explicite finissant par `Error`
#   * d’un message d’erreur
# * une exception personnalisée doit toujours hériter de `Exception`
#   * par défaut, tous les arguments passés au constructeur  
#     sont mis dans un tuple `args`
#
#   * on peut hériter de n’importe quelle exception  
#     qui hérite de `Exception`

# %% slideshow={"slide_type": "slide"}
class SplitError(Exception):
    pass

x, y = 1, 'a'

try:
    raise SplitError('split error', x, y)
except SplitError as exc:
    print(exc.args)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### conception d’exceptions

# %% [markdown]
# * une exception est une vraie classe  
#   on peut donc surcharger le constructeur  
#   et ajouter des méthodes
#
# * on peut utiliser l'arbre d’héritage pour structurer les exceptions 
#   * une clause `except MyException` capture  
#     les instance de `MyException`  
#     ou de ses sous-classes (cf `isinstance()`)
#
#   * maintenance plus facile

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les exceptions sont très efficaces

# %% [markdown]
# * voici la bonne manière d’ouvrir un fichier

# %%
try:
    with open('fichier-inexistant', 'r') as feed:
        for line in feed:
            print(line)
except OSError as err:
    print(err)
    print(err.args)
    print(err.filename)

# %% [markdown]
# beaucoup plus concis et efficace que de tester si le fichier existe,  
# si ça n’est pas un répertoire, si on a les droits d’écriture, etc.
