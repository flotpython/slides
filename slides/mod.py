# comme la variable GLOBALE est définie au niveau le plus haut
# dans le fichier, elle va être accessible comme un attribut
# dans le module mod, c'est à dire mod.GLOBALE

GLOBALE = 100

# pareil ici, la fonction spam nous sera accessible comme mod.spam

def spam(data):
    print(f"dans mod.spam, data={data}")
