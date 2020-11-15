# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: bonnes pratiques de test
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# </div>

# %% [markdown]
# # bonnes pratiques de test

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un mot sur l'instruction `assert`

# %%
import traceback
x = 10

try: 
    assert x < 0
except Exception:
    traceback.print_exc()

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un mot sur `assert`

# %% [markdown]
# `assert expression` est équivalent à
#
# ```
# if __debug__: 
#     if not expression: raise AssertionError 
# ```
#
# * `__debug__` est `True` par défaut  
#   et `False` si l’interpréteur est lancé avec l’option `–O`
#
# * on ne peut pas modifier à la main la variable `__debug__`
# * avec l’option `–O`, tous les `assert` sont enlevés lors de la compilation

# %% [markdown] slideshow={"slide_type": "slide"}
# # catégories de test

# %% [markdown] slideshow={"slide_type": ""}
# * on trouve souvent dans la littérature des distinctions comme
#   * test unitaires
#   * test d'intégration
#   * tests système, etc...
#   * (non-régression)
# * peuvent faire du sens au niveau d'un projet

# %% [markdown] slideshow={"slide_type": "slide"}
# ## catégorisation - suite

# %% [markdown] slideshow={"slide_type": ""}
# * mais pas sûr que ces distinctions soient pertinentes/utiles
#   * pour comparer deux projets
#
# * exemple
#   * un test système pour une librairie d'algèbre linéaire
#   * peut être plus simple à mettre en place
#   * qu'un test unitaire pour un système de téléphonie

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pourquoi automatiser les tests ?

# %% [markdown] slideshow={"slide_type": ""}
# * nécessité de tester au moins une fois
# * un tout petit changement peut tout casser
# * il faut donc **tout tester à chaque changement**
# * de ce point de vue tous les tests sont de **non-régression**
#   * sauf la première fois
#   * lorsqu'on teste le test

# %% [markdown] slideshow={"slide_type": "slide"}
# ## catégories de test - pratique

# %% [markdown] slideshow={"slide_type": ""}
# * il faut que les scénarii de test soient reproductibles
#   * nécessaire de contrôler entièrement l'environnement
# * il reste une catégorisation objective
#   * selon la complexité de l'environnement de test

# %% [markdown] slideshow={"slide_type": "slide"}
# ## aujourd'hui

# %% [markdown] slideshow={"slide_type": ""}
# * grâce à des outils comme
#   * docker - pour la gestion des environnements
#   * et l'intégration continue (webhooks gitlab/github)
#   * (présentation séparée)
# * il est à la portée d'un *simple individu* de 
#   * mettre en place des tests **systématiques** très complets 
#   * tant que tous les composants tiennent dans une VM
# * et même, au prix d'un effort un peu supérieur
#   * d'orchestrer plusieurs VMs
#   * sur un cloud comme amazon ou autre

# %% [markdown] slideshow={"slide_type": "slide"}
# ### écrire les tests en même temps que le code

# %% [markdown] slideshow={"slide_type": ""}
# * c'est pourquoi il est entendu que
# * on écrit les tests en même temps que le code
#   * que ce soit pour du code from scratch
#   * ou des corrections de bug
# * nécessaire mais généralement pas suffisant
#   * intégration/système
# * trouver le bon compromis

# %% [markdown] slideshow={"slide_type": "slide"}
# # librairies de test

# %% [markdown] slideshow={"slide_type": "slide"}
# * les frameworks de test les plus cités
#   * `unittest` - dans la librairie standard
#   * `pytest` - à installer avec `pip`
#   * (`nose` - à installer avec `pip` - pas présenté)
# * la tendance est en faveur de `pytest`
# * signalons en outre `doctest` (voir partie sur la doc)
#   * beaucoup moins puissant
#   * mais avantage de grouper code et test

# %% [markdown] slideshow={"slide_type": "slide"}
# # `unittest`

# %% [markdown] slideshow={"slide_type": ""}
# fait partie de la librairie standard; contient:
#
# * une interface orientée objet
#   * pour l'écriture des tests
# * une fonctionnalité *runner*
#   * exécution et présentation des résultats
# * et une fonctionnalité *discover*
#   * recherche de tous les test-cases
#   * e.g. dans tout un package ou module

# %% [markdown] slideshow={"slide_type": "slide"}
# ## un exemple

# %%
# !cat library/pgcd.py

# %% slideshow={"slide_type": "slide"}
# !cat tests/test_pgcd_unittest.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ## à noter
#
# * ces tests sont simplistes (⇔ à ceux en doctest)
#   * mais on faire beaucoup plus !
# * les vérifications sont faites à partir de **méthodes**
#   * de la classe `TestCase` - ici `assertEqual`
# * notamment on peut vérifier qu'un appel lève une exception 
#   * avec `assertRaises` et similaires
# * ou que deux valeurs sont presques égales (précision flottants)
#   * avec `AssertAlmostEqual`
# * ou qu'un string matche une expression régulière
#   * avec `assertRegex`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## comment sont découverts les tests
#
# * la convention de nommer les objets en `test_*`:
#   * le module s'appelle `test_pgcd.py`
#   * la méthode s'appelle `test_upper` 
#   * c'est important pour les fonctions de découverte
# * la classe hérite de `TestCase` 
#   * c'est pourquoi son nom importe peu
#   * (les noms de classes sont `EnChasseMixte`)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## quoi en faire
#
# * point d'entrée `python3 -m unittest`
# * on peut lui passer un module, une classe ou une méthode
#   * ou une liste de .. évidemment
# * ou le laisser trouver tous les tests dans un module
#   * fonction `discover`

# %% slideshow={"slide_type": "slide"}
# si on lui passe une méthode précise, seul ce test case est lancé
# !python3 -m unittest tests.test_pgcd_unittest.TestPgcd.test_upper

# %% slideshow={"slide_type": "slide"}
# si on lui précise le module, les deux tests sont lancés
# !python3 -m unittest tests.test_pgcd_unittest

# %% slideshow={"slide_type": "slide"}
# idem avec l'option -v 
# !python3 -m unittest -v tests.test_pgcd_unittest

# %% slideshow={"slide_type": "slide"}
# en fait dans le répertoire tests/ 
# il y a plus de testcases que cela
# !ls tests

# %% slideshow={"slide_type": "slide"}
# on lance la découverte sur tout le package...
# du coup il va trouver les autres versions du même test
# que nous allons voir tout de suite
# !python3 -m unittest discover -v tests

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fixtures
#
# * c'est quoi une fixture ?
# * le code pour mettre le système dans un état initial connu
#   * assez rustique dans `unittest`
# * on veut pouvoir définir simplement
#   * une façon d'initialiser/nettoyer (setup/teardown)
# * à l'entrée et la sortie de **tout le scénario**
#   * `setUpClass/tearDownClass`
# * et aussi à l'entrée et la sortie de **chaque test**
#   * `setUp`/`tearDown`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `setUp`/`tearDown`

# %%
# !cat tests/test_pgcd_unittest_fix1.py

# %% slideshow={"slide_type": "slide"}
# !python3 -m unittest tests.test_pgcd_unittest_fix1

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `setUpClass` et `teardownClass`

# %%
# !cat tests/test_pgcd_unittest_fix2.py

# %% slideshow={"slide_type": "slide"}
# !python3 -m unittest tests.test_pgcd_unittest_fix2

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `unittest` - autres traits
#
# * on peut aussi définir `setUpModule`/`tearDownModule` 
#   * au niveau du module..
# * avec les décorateurs `skip` `skipIf` `skipUnless`
#   * on peut passer des tests en fonction de l'environnement
#   * typiquement de l'operating system
#   * ou de la version python ...
#   * on peut aussi passer un test pendant le run avec [`skipTest()`](https://docs.python.org/3.5/library/unittest.html#unittest.TestCase.skipTest)
# * avec la notion de [`subTest`](https://docs.python.org/3.5/library/unittest.html#unittest.TestCase.subTest)
#   * on peut éviter que la première assertion 
#   * ne cause la fin de toute la méthode

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `unittest` - épilogue
#
# * bref, c'est très complet
# * mais un tout petit peu compliqué
# * par exemple
#   * le niveau 'classe' peut être jugé superflu
#   * dans notre exemple, avec un layout tout bête
#   * un test = niveau 4 !
#
# `tests.test_pgcd_unittest.TestPgcd.test_lower`

# %% [markdown] slideshow={"slide_type": "slide"}
# # `pytest`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `pytest` - introduction
#
# * philosophie générale
#   * "no boilerplate, no required api" 
# * supporte *aussi* les tests écrits en `unittest`
# * format de sortie le plus lisible
#   * notamment pour les tests qui ne passent pas
#   * entre autres une raison de son succès
# * [la documentation sur readthedocs](http://doc.pytest.org/en/latest/assert.html)
#   * système de plugins disponible  

# %% [markdown]
# ## installation
#
# ```
# pip3 install pytest
# ```
#
# * expose une commande `py.test` (⇔ `python3 -m pytest`)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## lancement des tests / discovery 

# %%
# tout simplement
# !py.test tests

# %% slideshow={"slide_type": "slide"}
# ou seulement sur un module, une classe, un testcase
# !py.test -v tests/test_pgcd_pytest.py

# %%
# !py.test -v tests/test_pgcd_pytest.py::test_upper

# %% [markdown] slideshow={"slide_type": "slide"}
# # exemple simpliste

# %%
# un test dans sa forme la plus simple
# !cat tests/test_pgcd_pytest.py

# %% slideshow={"slide_type": "slide"}
# !py.test tests/test_pgcd_pytest.py

# %% slideshow={"slide_type": "slide"}
# et bien sûr toujours le mode bavard
# !py.test -v tests/test_pgcd_pytest.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ## attendre une exception

# %%
# pour spécifier qu'une expression doit retourner une exception
# !cat tests/test_pgcd_pytest_raise.py

# %% slideshow={"slide_type": "slide"}
# !py.test tests/test_pgcd_pytest_raise.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ## presque égal

# %% slideshow={}
## almost-equal
# pas trouvé de méthode native pytest pour cela
# numpy a des outils pour le faire

# %%
import numpy as np
x1 = np.array([1e10, 1e-7])
x2 = np.array([1.000001e10, 1e-8])
np.isclose(x1, x2)

# %%
x3 = 1.00001 * x1
assert all(np.isclose(x1, x3))

# %%
# PS: apparemment cela est maintenant dans pytest 3.0
# voir https://stackoverflow.com/questions/8560131/pytest-assert-almost-equal

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fixtures

# %% [markdown] slideshow={"slide_type": "slide"}
# * mêmes possibilités que les autres frameworks
# * aussi disponibles avec 
#   * les tests dans des classes
#   * ou directement dans le module

# %% slideshow={"slide_type": "slide"}
# !cat tests/test_pgcd_pytest_class.py

# %% slideshow={"slide_type": "slide"}
# pareil que pour nose, en mettant -s on supprime la capture
# !py.test -s tests/test_pgcd_pytest_class.py

# %% slideshow={"slide_type": "slide"}
# un exemple de sortie avec un test qui ne passe pas
# !cat tests/test_pgcd_pytest_broken.py

# %% slideshow={"slide_type": "slide"}
# pareil que pour nose, en mettant -s on supprime la capture
# !py.test -s tests/test_pgcd_pytest_broken.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ### fixtures - suite

# %% [markdown] slideshow={"slide_type": "slide"}
# * toute une ménagerie d'exemples [sur le site pytest](http://doc.pytest.org/en/latest/example/index.html)
#   * [commencer par notamment cette page sur les fixtures](http://doc.pytest.org/en/latest/fixture.html#fixtures)
#   * qui explique bien ...
# * les bases de l'exemple du projet minisim
#   * pour une fixture qui définit des variables globales
#   * [implémentée ici](https://gitlab.com/parmentelat/minisim2/blob/master/tests/conftest.py)
# * notez bien le fichier 'spécial' `conftest.py` qui est chargé automatiquement

# %% [markdown] slideshow={"slide_type": "slide"}
# # pratiques courantes

# %% [markdown] slideshow={"slide_type": "slide"}
# * on place généralement les tests 
#   * dans un directory `tests/`
#   * directement à la racine
#   * ou dans le package principal
#   * mais ce n'est pas une obligation
# * les tests unitaires sont groupés par module source, e.g.
#   * `minisim/zone.py`
#   * `tests/test_zone.py`
# * pour des tests de plus grande portée 
#   * il n'y a pas spécialement d'usage 
#   * le principal c'est de s'y retouver

# %% [markdown] slideshow={"slide_type": "slide"}
# # exercice

# %% [markdown] slideshow={"slide_type": "slide"}
# * s'entraîner a lancer `py.test`
#   * sur un test précis
#   * sur tout un module de test
#
# * aller voir aussi les pipelines sur gitlab 
#   * comment `py.test` est connecté à gitlab-ci
#   * où voir les résultats des tests
#   
# * peut-on améliorer les tests de minisim ?
#   * https://gitlab.com/parmentelat/minisim2
#   * fixtures ou pas fixtures ...

# %% [markdown] slideshow={"slide_type": "slide"}
# # Fin

# %% [markdown] slideshow={"slide_type": "slide"}
# # `nose`
#
# > nose extends unittest to make testing easier
#
# > "no boilerplate, some api"

# %% [markdown] slideshow={"slide_type": "-"}
# ## installation
#
# * sans surprise:
#
# ```
# pip3 install nose
# ```
#
# * expose la commande `nosetests` ($\Longleftrightarrow$ `python3 -m nose`)

# %% slideshow={"slide_type": "slide"}
# !cat tests/test_pgcd_nose.py

# %% slideshow={"slide_type": "slide"}
# lancer tous les tests dans un module
# !nosetests tests/test_pgcd_nose.py

# %% slideshow={"slide_type": "slide"}
# idem en mode bavard
# !nosetests -v tests/test_pgcd_nose.py

# %% [markdown] slideshow={"slide_type": "slide"}
# * On peut tout aussi bien faire des classes tout de même aussi
#   * toujours utile pour les fixtures
#   * mais aussi disponible à base de décorateurs
#   * gamme complète disponible
# * **ATTENTION** par défaut les outputs sont capturés
#   * utiliser `-s` pour éviter la capture
# * et toujours `-v`/`--verbose` pour le mode bavard

# %% slideshow={"slide_type": "slide"}
# des fixtures en utilisant une classe
# !cat tests/test_pgcd_nose_class.py

# %% slideshow={"slide_type": "slide"}
# avec une classe
# !nosetests -v -s tests/test_pgcd_nose_class.py

# %% slideshow={"slide_type": "slide"}
# des fixtures en utilisant un decorateur
# !cat tests/test_pgcd_nose_deco.py

# %% slideshow={"slide_type": "slide"}
# on peut désigner un nom de fichier ou un module python
# !nosetests -v -s tests.test_pgcd_nose_deco

# %% [markdown] slideshow={"slide_type": "slide"}
# ## langage d'assertions

# %% [markdown]
# ### sous-tests
#
# ```
# def test_evens():
#     for i in range(0, 5):
#         yield check_even, i, i*3
#
# def check_even(n, nn):
#     assert n % 2 == 0 or nn % 2 == 0
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## discovery

# %%
# l'interface est la plus simple possible
# !nosetests -s tests

# %% [markdown] slideshow={"slide_type": "slide"}
# ## à noter
#
# * `nosetests` a trouvé les tests que nous avons écrit pour `nose`
#   * **et** ceux écrits en unittest !
# * dans l'environnement du cours j'ai beaucoup de bazar
#   * j'ai dû préciser `python3 -m unittest tests` 
#   * sans préciser `testing` j'obtenais un gros crash
#   * alors que `nosetests` tout court fonctionne correctement
# * voir aussi [la doc complète sur readthedocs](http://nose.readthedocs.io/en/latest/testing.html)
# * on peut exécuter les tests `doctest` depuis `nose`
# * un système de plugins

# %% [markdown] slideshow={"slide_type": "slide"}
# ### pour aller plus loin

# %% [markdown]
# * http://sametmax.com/un-gros-guide-bien-gras-sur-les-tests-unitaires-en-python-partie-1/
