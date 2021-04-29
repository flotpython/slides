# -*- coding: utf-8 -*-
# ---
# jupyter:
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
#   notebookname: packaging & software distribution
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# </div>

# %% slideshow={"slide_type": "slide"}

from plan import plan_extras; plan_extras("packaging")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *packaging* (software distribution)

# %% [markdown]
# ### portée
# on regroupe ici les outils pour
#
# * **packager** un composant logiciel
# * **exposer** différentes versions à une infrastructure
# * **installer** à partir de l'infrastructure
# * **installer** un module localement à partir des sources
# * **gérer** les dépendances entre composants
# * **maintenir** plusieurs combinaisons de composants 

# %% [markdown] slideshow={"slide_type": "slide"}
# ## publics
#
# * *sysadmins*: installation d'outils en tant que `root` pour les utilisateurs
#   * typiquement la dernière version 
# * **et aussi** *devels*:
#   * installation locale à un utilisateur
#   * possiblement besoin de plusieurs versions différentes d'un même module

# %% [markdown] slideshow={"slide_type": "slide"}
# ## quels challenges ?
#
# * gestion des dépendances
# * et des contraintes en termes de version
# * sous forme de sources ou de binaires
# * installation globale système ou locale utilisateur
# * plusieurs environnement pour un même utilisateur

# %% [markdown] slideshow={"slide_type": "slide"}
# ## avertissement / vocabulaire
#
# * on parle systématiquement de **packages**
# * qui **ne sont pas** des packages au sens du langage (package/module)
# * même s'il arrive que cela coïncide

# %% [markdown] slideshow={"slide_type": "slide"}
# # outils concernés
#
# * `pip` 
#   * installer un package
# * `setuptools`
#   * créer un package
# * `virtualenv` / (`docker`)

# %% [markdown] slideshow={"slide_type": "slide"}
# # un peu d'histoire
#
# * ~~2000 - `distutils` (python 1.6)~~
# * 2003 - [`pypi`](`https://pypi.python.org/pypi)
# * 2005 - `setuptools` - inclut ~~`easy_install`~~
# * 2007 - `virtualenv`
# * 2008 - `pip`

# %% [markdown]
# ## outils obsolètes à éviter
#
# * `distutils` : utiliser `setuptools`
# * `easy_install` : utiliser `pip`

# %% [markdown] slideshow={"slide_type": "slide"}
# dans le cas de python en tous cas:
#
# * un sujet vécu comme un mal nécessaire 
# * plusieurs itérations pas toujours très concertées
# * résultat : pas l'aspect le plus clair dans l'écosystème python !

# %% [markdown]
# ## autres langages
#
# * perl : cpan 
# * ruby : gems
# * ...

# %% [markdown] slideshow={"slide_type": "slide"}
# # survol
#
# le workflow, typiquement pour un package 'python-only' :
#
# * développeur : une fois pour toutes
#   * écrit `setup.py`
# * développeur : à chaque nouvelle version
#   * met à jour changelog (et version.py)
#   * `./setup.py sdist upload -r pypi`
#   * qui crée une distribution source
#   * l'uploade sur [https://pypi.python.org/pypi](https://pypi.python.org/pypi)
# * utilisateur : `sudo pip install [-u] nbautoeval`
#   * va chercher package sur pypi
#   * l'installe localement
#   * tout en installant les dépendances
#   * l'option `-u/--upgrade` autorise une mise à jour 

# %% [markdown] slideshow={"slide_type": "slide"}
# * choisir un nom unique dans `pypi` - e.g. `nbautoeval`
# * arborescence minimale
#
# ```
# nbautoeval/ (pour git)
#     nbautoeval/ (pour python)
#         __init__.py 
#         version.py
#     setup.py
# ```    

# %% [markdown] slideshow={"slide_type": "slide"}
# # `pip`

# %% [markdown]
# * `pip` fait partie de la distribution standard (depuis 2.7.9 et 3.4)
# * permet de chercher et installer les librairies tierces
# * notamment depuis [https://pypi.python.org/pypi](https://pypi.python.org/pypi)
# * prend en charge les dépendances et versions
# * [documentation](https://pip.pypa.io/en/stable/)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## avertissement
#
# * si vous avez plusieurs version de `python`
# * vous avez aussi plusieurs versions de `pip`
# * par exemple, utiliser `pip3` si vous invoquez `python3` 
# * ou encore `python3 -m pip`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## recherche
#
# ```
# $ pip3 search pssh
# apssh (0.5.6)    - Asynchroneous Parallel ssh
#   INSTALLED: 0.5.6 (latest)
# pssh (2.3.1)     - Parallel version of OpenSSH and related tools
# vlcpssh (0.1.5)  - Integrate paramiko into ssh
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### état des lieux

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ```
# $ pip list
# Package            Version
# ------------------ ----------
# aiohttp            3.5.4
# appnope            0.1.0
# astroid            2.2.0
# ...
# ```

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ```
# $ pip3 freeze
# aiohttp==3.5.4
# appnope==0.1.0
# astroid==2.2.0
# ...
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## installation globale
#
# * `pip3 install pssh`
# * **MAIS**
# * ceci demande les droits administrateur !
# * `sudo pip3 install pssh`
# * pas très commode..

# %% [markdown] slideshow={"slide_type": "slide"}
# ## installation privée : `--user`
#
# (Voir aussi `virtualenv`)
#
# ```
# $ pip3 list --user
# ```
#
# ```
# $ pip3 install --user pssh
# ...
# Successfully installed pssh-2.3.1
# ```
#
# ```
# $ pip3 list --user
# Package Version
# ------- -------
# pssh    2.3.1
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## gestion des versions
#
# * on peut obtenir plus de détails sur un package
# * en allant [sur le site `https://pypi.python.org/pypi`](https://pypi.python.org/pypi)
# * par exemple pour [`nbautoeval`](https://pypi.python.org/pypi?%3Aaction=pkg_edit&name=nbautoeval)
#
# ```
# $ pip install SomePackage            # latest version
# $ pip install SomePackage==1.0.4     # specific version
# $ pip install 'SomePackage>=1.0.4'     # minimum version
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## dépendances : photocopie et installation
#
# * développeur
# ```
# pip3 freeze > requirements.txt
# ```
#
# * utilisateur
# ```
# pip3 install -r requirements.txt
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## binaire ou pas binaire
#
# * historiquement limité 
#   * aux installations à partir du source
#   * pas gênant pour le code python
#   * mais lent et contraignant pour les dépendances en C
# * ce **n'est plus le cas**
#   * on peut produire des packages binaires grâce aux *wheels*
#   * souvent disponible pour windows et mac

# %% [markdown]
# ## autres sources: mode devel
#
# * le défaut est d'aller chercher sur pypi
#
# * avec l'option `install -e` on peut utiliser une source locale (en mode devel)
# ```
# pip3 install -e ~parmentelat/git/nbautoeval
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## autres sources: mode devel
#
# * ou bien se fabriquer un pseudo repository pypi local
# * à partir d'un `.tar.gz` produit par `setup.py sdist` (voir +bas)
#
# ```
# cd ~parmentelat/git/nbautoeval
# setup.py sdist
# mkdir -p ~/my-pseudo-pypi/nbautoeval
# cp dist/nbautoeval-0.1.3.tar.gz
# ```
#
# ```
# pip3 install nbautoeval --find-link file:///users/parmentelat/my-pseudo-pypi/
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## mettre à jour `pip`
#
# ```
# sudo pip3 install -U pip setuptools
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## divers
#
# * désinstaller `pip3 uninstall package`
# * lister les fichiers `pip3 show package`
#   * un package installé
# * vérifier `pip3 check package`

# %% [markdown] slideshow={"slide_type": "slide"}
# # `setuptools`
#
# * la librairie qui permet d'écrire `setup.py`
# * [documentation](http://setuptools.readthedocs.io/en/latest/setuptools.html#installing-setuptools)
# * de très nombreuses fonctionnalités
# * présentation limitée à un survol

# %% [markdown] slideshow={"slide_type": "slide"}
# ## objectifs
#
# * permettre de décrire dans un fichier `setup.py`
#   * sous forme **déclarative**
# * les attributs (nom, version)
# * le contenu (code python, ou autres)
# * qui permettent de fabriquer un package

# %% [markdown]
# ### et par extension
#
# * permet de générer une grosse partie du workflow
# * relatif aux build et test

# %% [markdown]
# ## installation
#
# * pas par défaut dans la librairie standard
#   * qui contient d'ailleurs toujours `distutils`
# * lacune souvent comblée par le fournisseur
#   * distrib linux, anaconda, ...
# * en cas de besoin seulement
#
# ```
# pip3 install setuptools
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple de `setup.py`
#
# * [dans la documentation](http://setuptools.readthedocs.io/en/latest/setuptools.html#installing-setuptools); à noter:
# * `packages=find_packages()`
# * `install_requires=['docutils>=0.3']`
#   * utiliser un nom connu de `pypi`
#   * [détails ici](http://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-dependencies)
# * `package_data={ ... }`
# * `scripts=['say_hello.py']`
#   * commandes à installer dans le PATH
# * voir [liste complète ici](http://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords)
#
# * https://gitlab.com/gansanay/dummysim/blob/master/setup.py

# %% [markdown]
# ## les (sous-)commandes
#
# * `setup.py` est destiné à être lancé directement
# * avec une sous-commande (détails + bas)
# * sous linux/macos: `chmod +x setup.py`
#   * pour pouvoir faire directement `setup.py sdist`
# * sous windows: `python3 setup.py sdist`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les sous-commandes usuelles
#
# * nous voyons le setup pypi un peu plus loin
# * imaginons pour l'instant que c'est ok
#
# *** 
# dans les cas usuels on utilise principalement
#
# * `setup.py register` : une bonne fois pour toutes
#   * crée le package correspondant dans pypi
#   * permet par exemple de vérifier l'unicité du nom
# * `setup.py sdist`  : permet de fabriquer localement une distribution 'source'
# * `setup.py upload` : pour pousser le résultat sur pypi
#   * nécessite un setup initial pour l'authentification

# %% [markdown] slideshow={"slide_type": "slide"}
# ## sous-commandes utiles
#
# * `setup.py build` : prépare distribution dans `./build` 
#   * et n'est pas packagé 
#   
# pas forcément utile, mais:
#
# * `setup.py test` : lancer les tests
# * `setup.py build_sphinx` : fabriquer la documentation
#   * peuvent requérir des mot-clés supplémentaires
#   * double emploi avec readthedocs et CI
#
# et aussi, plus mineur
#
# * `setup.py rotate`: fait le ménage sur pypi
# * `setup.py build_ext`: pour fabriquer des librairies C/C++

# %% [markdown] slideshow={"slide_type": "slide"}
# ## bonnes pratiques / versioning
#
# * écrire un **CHANGELOG** [(exemple)](https://raw.githubusercontent.com/parmentelat/apssh/master/CHANGELOG.md)
# * et définir une **version** accessible en python [(exemple)](https://github.com/parmentelat/apssh/blob/master/apssh/version.py)
# * sachant que la version peut être [(dérivée du changelog)](https://github.com/parmentelat/apssh/blob/master/update_version_from_changelog)
# * et ensuite utilisée à son tour [dans `setup.py`](https://github.com/parmentelat/apssh/blob/master/setup.py#L6)
#
# * pas forcément très élégant, mais ça fait le job
# * encore plus abscons
#   * une [recette make](https://github.com/parmentelat/apssh/blob/master/Makefile)
#   * pour vérifier qu'il ne reste pas de code non commité
#   * et poser un tag dans git en même temps qu'on pousse

# %% [markdown] slideshow={"slide_type": "slide"}
# ## enfin
#
# * les numéros de version sont gratuits
# * il ne faut pas hésiter à releaser souvent
# * et **ne jamais** recycler un numéro de version

# %% [markdown] slideshow={"slide_type": "slide"}
# ## piège fréquent
#
# * n'oubliez pas que `setup.py`
# * est appelé à être exécuté sur votre machine
# * **ET AUSSI** sur la machine qui installe le package

# %% [markdown] slideshow={"slide_type": "slide"}
# ## autres mot-clés
#
# ### `package_data` 
#
# * ce mot clé permet de décrire
# * des ressources non-python (données, texte, ...)
# * [voir détails ici](http://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation)

# %% [markdown] slideshow={"slide_type": "-"}
# ### `scripts` *vs `entry_points`
#
# * il existe une méthode plus moderne 
#   * pour décrire `scripts`
# * plus complexe aussi
# * [voir ici](http://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation)

# %% [markdown] slideshow={"slide_type": "slide"}
# # setup pypi

# %% [markdown]
# ## plateformes de production et de test
#
# * en sus de [la plateforme de production](https://pypi.python.org/pypi)
# * il y a [une plateforme de test `testpypi.python.org`](https://testpypi.python.org/pypi)
# * très utile pour mettre au point
#
# ## les deux requèrent de s'enregistrer

# %% [markdown] slideshow={"slide_type": "slide"}
# ## configurer votre `.pypirc`
#
# * une fois que vous avez vos identifiants
# * créez un fichier `.pypirc` dans votre homedir
#
# ```
# [distutils]
# index-servers =
#     pypi
#     testpypi
#
# [pypi]
# repository: https://pypi.python.org/pypi
# username: parmentelat
# password: <...>
#
# [testpypi]
# repository: https://testpypi.python.org/pypi
# username: parmentelat
# password: <...>
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## usage
#
# * dès lors vous pourrez utiliser le site de prod 
#   * avec e.g. `setup.py register` et `setup.py upload`
# * et le site de test
#   * en ajoutant l'option `-r testpypi`
#   * exemple `./setup.py sdist upload -r testpypi`  

# %% [markdown] slideshow={"slide_type": "slide"}
# # `virtualenv`

# %% [markdown] slideshow={"slide_type": "-"}
# ## *vs* `pip --user`
#
# * premier niveau d'isolation / user
# * mais un peu limité 
#   * pas de `pip --user uninstall`
#   * `pip --user install -U` fragile
#   * bref, pas très robuste
# * et surtout, autres besoins
#   * plusieurs `requirements.txt` 
#   * sont potentiellement contradictoires
#   * exemple simple: django-1.9 et django-1.10

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fonction de virtualenv
#
# * permet de définir **plusieurs** espaces
#   * d'installation de librairies
# * pour **un seul** utilisateur
# * dans lesquels on utilise `pip` nativement
# * et permet de passer facilement de l'un à l'autre
# * [la documentation](https://virtualenv.pypa.io/en/stable/)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## installation
#
#
# ```
# pip3 install virtualenv
# ```
#
# * possiblement avec `sudo` sur linux/mac
# * ou bien `pip3 install --user virtualenv`
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## utilisation
#
# * assez rustique
# * une commande pour créer un virtualenv dans un directory
# ```
# virtualenv ./foobar
# ```
#
# * une commande pour *entrer* dans cet espace
#   * linux/mac
# ```
# source ./foobar/bin/activate
# ```
#
# * une commande pour en *sortir*
#
# ```
# deactivate
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## utilisation `virtualenv`
#
# * attention avec `PYTHONPATH`
#   * je recommande de **ne pas** définir PYTHONPATH autant que possible
# * par défaut, une fois dans le virtualenv
#   * on **continue de voir** les packages installés dans le contexte global
# * on peut créer un virtualenv 'vierge' avec
#   * `virtualenv --no-site-packages`

# %% [markdown] slideshow={"slide_type": "slide"}
# # exercice
#
# * installer `virtualenv`
# * installer `virtualenvwrapper(-win)`
# * créer un environnement virtuel vierge `dummysim`
# * créer/vérifier le fichier `requirements.txt`
# * installer les dépendances avec `pip`
# * faire tourner avec succès les tests unitaires
