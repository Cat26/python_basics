'''
ax + by + c =0
'''
a = [1, 0]
b = [1, 0]
c = [1, 0]

for number in a:
    for number in b:
        for number in c:
            res = ('duzo' if c == 0 else 'nie ma') if a == 0 else -c/float(a)

res = ('duzo' if c == 0 else 'nie ma') if a == 0 else -c/float(a)

print res

# x = ((a == 0) and [(c == 0 and ['duzo'] or ['nie ma'])[0]] or [-c/float(a)])[0]
# <warunek> ? wy1 : wyr2
# wyr1 if <warunek> else wyr2
# print x, y
#
# wynik = ""
# if a == 0:
#     if c == 0:
#         wynik = 'duzo'
#     else:
#         wynik = 'nie ma'
# else:
#     wynik = -c/float(a)
#
# print wynik
