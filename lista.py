l = ['r','t','r','e',2]

print (l[3:5])
print (l[:])
l.insert(2,'r')
print (l)
print(('r'in l),('a'in l))
l.remove('t')
print(l)
print (l.pop())
#element koncowy wyciaga z listy(wypisuje i usuwa)
print (type(l))

a=[]
b =[1,a]
b[1].append(1)
print( a, b)

x=[]
y=[1, x]
x.append(l)
print(x, y)

x = []
x.append(x)
print(x)
# cykl