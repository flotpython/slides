# pylint: disable=c0111
from nbhosting.courses import (
    Track, Section, Notebook,
    notebooks_by_pattern, track_by_directory)

def tracks(coursedir):
    """
    coursedir is a CourseDir object that points
    at the root directory of the filesystem tree
    that holds notebooks

    result is a list of Track instances
    """

    # in this repo we want to define 3 tracks:
    # (*) one for the plain course in 'slides',
    # (*) another one named 'extras' for the contents in 'slides-extras'
    # (*) last one from 'samples'

    default_section_names = [
        "introduction",
        "types de base",
        "syntaxe & instructions",
        "fonctions",
        "modules & packages",
        "classes & programmation objet",
        "compléments",
        "notions avancées",
        ]

    extra_section_names = [
        "numpy",
        "pandas",
        "notebooks",
        "tests",
        "doc",
        "packaging",
        "vscode",
    ]

    def _track(topdir, section_names, *, name, description):
        sections = [
            Section(coursedir=coursedir,
                    name=section_name,
                    notebooks=notebooks_by_pattern(
                        coursedir,
                        f"{topdir}/{number:02}*.ipynb"))
            for number, section_name in enumerate(section_names, 1)]
        return Track(coursedir, sections, name=name, description=description)

    return [
        _track("slides", default_section_names, name="slides", description="Cours: tronc commun"),
        _track("slides-extras", extra_section_names, name="extras", description="Cours: suppléments"),
        track_by_directory(
            coursedir,
            name="échantillons",
            description="Des exemples de codes plus réalistes",
            notebooks=notebooks_by_pattern(coursedir, "samples/[0-9]*.ipynb")
                     +notebooks_by_pattern(coursedir, "samples/[0-9]*.py")),
        track_by_directory(
            coursedir,
            name="TPs",
            description="TPs",
            notebooks=notebooks_by_pattern(coursedir, "tps/metro/metro.py")
                      + notebooks_by_pattern(coursedir, "tps/redis/README.md")
                      + notebooks_by_pattern(coursedir, "tps/boxes/unicode-boxes.py")),
    ]
