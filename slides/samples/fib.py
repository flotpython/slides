def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b

# code pour tester le module
# on execute le module directement
# en ligne de commande
if __name__ == '__main__':
    fib(40)
