from argparse import ArgumentParser

parser = ArgumentParser()
  # on déclare l'option -v
  # qui aura pour effet de mettre args.verbose à true

parser.add_argument("-v", "--verbose", action='store_true')
  # il faut au moins un argument obligatoire
  # on peut en mettre plusieurs

parser.add_argument("files", nargs='+')
  # args.verbose et args.files sont remplis par parse_args()

args = parser.parse_args()
  # le résultat

print(f"Bonjour !\n"
      f"args: verbose={args.verbose}, files={args.files}")
