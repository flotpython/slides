# pour passer des majuscules aux minuscules, il faut ajouter
# 97-65=32
import string

UPPER_TO_LOWER = ord('a') - ord('A')


def cesar(clear, key, encode=True):
    """
    retourne l'encryption du caractere <clear> par la clé <key>

    le caractère <key> doit être un caractère alphabétique ASCII
    c'est à dire que son ord() est entre ceux de 'a' et 'z' ou
    entre ceux de 'A' et 'Z'
    """

    if clear not in string.ascii_letters:
        return clear

    # le codepoint de la clé
    okey = ord(key)
    # on normalise la clé pour être dans les minuscules
    if key.isupper():
        okey += UPPER_TO_LOWER

    # la variable offset est un entier entre 0 et 25 qui indique
    # de combien on doit décaler; si vous référez qu tout premier
    # exemple, avec une clé qui vaut 'C' offset va valoir 3
    offset = (okey - ord('a') + 1)

    # si on encode, il faut ajouter l'offset,
    # et si on décode, il faut le retrancher
    if not encode:
        offset = -offset

    # ne reste plus qu'à faire le modulo
    # sauf que les bornes ne sont pas les mêmes
    # pour les majuscules ou pour les minuscules
    bottom = ord('A') if clear.isupper() else ord('a')

    return chr(bottom + (ord(clear) - bottom + offset) % 26)