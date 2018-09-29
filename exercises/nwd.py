import functools
def euklidesMod(a, b):
    if a <= b:
        return euklidesMod(b, a)
    elif b == 0:
        return a
    else:
        return euklidesMod(b, a % b)

def euklides2(*args):
    return functools.reduce(euklidesMod, args)

print(euklides2(21, 35, 14, 28, 7))