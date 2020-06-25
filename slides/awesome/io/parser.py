# le fichier awesome/io/parser.py
# qu'on peut importer avec
# import awesome.io.parser

# ce module fait un import relatif
# pour importer la classe Token
# du fichier token.py dans le même dossier
from .token import Token

# le code
class Parser:
    pass # blabla

# un test unitaire old-school
if __name__ == '__main__':
    Parser().blabla()
