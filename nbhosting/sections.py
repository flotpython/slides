# pylint: disable=c0111
from nbhosting.courses import (
    Sections, Section, Notebook,
    notebooks_by_pattern, sections_by_directory)

def sections(coursedir, track):
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

    # default for track is 'course'
    if track == "course":
        # this for now is just some random selection
        # for testing manual sectioning
        sections = [
            "introduction",
            "types de base",
            "syntaxe & instructions",
            "fonctions",
            "modules & packages",
            "classes & programmation objet",
            ]
        sections = [
            Section(coursedir=coursedir,
                    name=section,
                    notebooks=notebooks_by_pattern(
                        coursedir,
                        f"slides/{number:02}*.ipynb"))
            for number, section in enumerate(sections, 1)]
        return Sections(coursedir, sections)
