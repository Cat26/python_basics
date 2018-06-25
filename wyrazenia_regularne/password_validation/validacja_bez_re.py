# haslo ma :
# miec 10 znakow
# dwie duze litery od b-z
# dwie male litery od b-z
# znak specjalny
# trzy liczby
# nie moze byc haslem z pliku hasla

password = input("enter your password: ")

if len(password) != 10:
    print("Password should have 10 signs! Try again")

lower =0
for sign in password:
    if sign.islower():
        lower += 1
if lower < 2:
    print("Password have to contain two lowercase letters")

