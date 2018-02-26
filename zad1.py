import timeit
start = timeit.default_timer()
p = 1234 ** 5678
c = 12345 ** 67890
d = p + c
e = str(d)
print len(e)
stop = timeit.default_timer()
print stop - start
