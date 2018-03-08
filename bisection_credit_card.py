b = 999999
i = 0.18
epsilon = 0.01
monthly_interest_rate = i/12.0
low = b / 12
high = (b * (1 + monthly_interest_rate) ** 12) / 12.0
p = (low + high) / 2
nb = b
for i in range(1, 13):
    ub = nb - p
    nb = ub + (monthly_interest_rate * ub)


while abs(nb) > epsilon:
    if nb > epsilon:
        low = p
    elif nb < (-epsilon):
        high = p
    p = (low + high) / 2
    nb = b
    for i in range(1, 13):
        ub = nb - p
        nb = ub + (monthly_interest_rate * ub)
print("balance: %d, annual interest rate: %d" %(b, i))
print("minimum fixed payment: %.2f" %p)





