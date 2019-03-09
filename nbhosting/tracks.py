# pylint: disable=c0111
from nbhosting.courses import (
    Track, Section, Notebook,
    notebooks_by_pattern, track_by_directory,
    DEFAULT_TRACK)

def tracks(coursedir):
    """
    coursedir is a CourseDir object that points
    at the root directory of the filesystem tree
    that holds notebooks

    result is a dictionary trabkname -> Track instance
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
        ]

    extra_section_names = [
        "numpy",
        "pandas",
        "notebooks",
        "tests",
        "doc",
        "packaging",
    ]

    def _track(topdir, section_names):
        sections = [
            Section(coursedir=coursedir,
                    name=section_name,
                    notebooks=notebooks_by_pattern(
                        coursedir,
                        f"{topdir}/{number:02}*.ipynb"))
            for number, section_name in enumerate(section_names, 1)]
        return Track(coursedir, sections)

    return {
        DEFAULT_TRACK: _track("slides", default_section_names),
        'extras': _track("slides-extras", extra_section_names),
        'samples': track_by_directory(
            coursedir,
            notebooks_by_pattern(coursedir, "samples/*.ipynb")),
    }
