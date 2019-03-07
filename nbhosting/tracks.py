# pylint: disable=c0111
from nbhosting.courses import (
    Sections, Section, Notebook,
    notebooks_by_pattern, sections_by_directory,
    DEFAULT_TRACK)

def tracks(coursedir):
    """
    coursedir is a CourseDir object that points
    at the root directory of the filesystem tree
    that holds notebooks
    track is a name that is set by the nbhosting admin,
    by default it is "course" which would mean the full
    course, but you can define alternate tracks among the
    course material

    result should be a Sections object
    """

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
        return Sections(coursedir, sections)

    return {
        DEFAULT_TRACK: _track("slides", default_section_names),
        'extras': _track("slides-extras", extra_section_names),
        'samples': sections_by_directory(
            coursedir,
            notebooks_by_pattern(coursedir, "samples/*.ipynb")),
    }
