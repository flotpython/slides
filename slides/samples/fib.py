# un module définit souvent des fonctions et classes

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b


# le code qui suit sera exécuté seulement si on le lance
# depuis la ligne de commande, et pas pendant un import

if __name__ == '__main__':
    fib(40)
