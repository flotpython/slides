#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser
from itertools import chain


STUDENTS_ROOT = Path("/nbhosting/current/students")
COURSE = "python-initial-cnrs"
SOURCE = Path("~thierry.parmentelat/python-initial-cnrs").expanduser()
def STUDENT_ROOT(student):
    return STUDENTS_ROOT / student / COURSE

def ITER_STUDENTS():
    for student_dir in (STUDENTS_ROOT.glob(f"*.*/{COURSE}")):
        yield student_dir.parent.name



def publish(exo, student, dry_run):
    source = SOURCE / 'raw' / exo
    if not source.exists():
        print(f"WARNING: exo {exo} unknown from {source}")
        return
    dest = STUDENT_ROOT(student) / exo
    if dest.exists():
        print(f"WARNING: student {student} already has exo {exo} in {dest}")
        return
    if dry_run:
        print(f"DRY-RUN: Would copy {source} into {dest}")
        return
    dest.write_text(source.read_text())


def list_exos():
    for exo in sorted(
        chain(
            (SOURCE / 'raw').glob('*.md'),
            (SOURCE / 'raw').glob('*.py'),
        )):
        print(exo)


def main():
    parser = ArgumentParser()
    parser.add_argument("-s", "--student", dest='students', default=[], action='append')
    parser.add_argument("-n", "--dry-run", default=False, action='store_true')
    parser.add_argument("exos", nargs='*',
                        help="with no argument, list available exos")
    args = parser.parse_args()

    if not args.students:
        args.students = list(ITER_STUDENTS())

    if not args.exos:
        list_exos()
        return

    for exo in args.exos:
        # obtained by completion means it may contain an extra path
        exo = Path(exo).name
        for student in args.students:
            publish(exo, student, args.dry_run)


if __name__ == '__main__':
    main()
