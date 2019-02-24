free1 = "module-global"

# le bidule qui a besoin d'une callback
def run(f):
    f()

def make_closure(x):
    def f():
        print(free1, x)
    return f

callbacks = [ make_closure(i) for i in range(2) ]

for callback in callbacks:
    run(callback)
