import spam

x = 2
def f():
    print(x)

# va imprimer 2
f()


spam.x = 3
# va imprimer 3
spam.f()
