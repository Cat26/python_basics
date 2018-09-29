def minimum_fixed_payment(b, i, p):
    monthly_interest_rate = i/12.0
    c = 12
    while(c > 0):
        ub = b - p
        b = ub + (monthly_interest_rate * ub)
        #print (b)
        c -=1
    return b

def min_fix_pay(b,i,p):
    while (minimum_fixed_payment(b,i,p)>0):
        p = p+10
    return p

print("minimal fixed payment is:{}".format(min_fix_pay(3926, 0.2, 10)))
