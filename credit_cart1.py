def credit_card(b, r, i):
    monthlyPaymentRate = r/12.0
    monthly_Interest = i/12.0
    s = 12

    while(s>0):
        minimum_payment = b * monthlyPaymentRate
        ub = b - minimum_payment
        interest = monthly_Interest * ub
        b = interest + ub
        s -= 1
        print("%.2f"% b)

credit_card(484, 0.48, 0.2)

