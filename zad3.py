#4. Dla dwóch wektorów v1 i v2, o takiej samej liczbie elementów napisać
#wyrażenie, którego wynikiem będzie lista v1 + v2 (suma wektorów)

v1 = [1, 2, 3]
v2 = [3, 4, 5]
lista =[v1[i] + v2[i] for i in range(len(v1))]

print(lista)



