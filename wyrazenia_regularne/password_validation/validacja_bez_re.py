# haslo ma :
# miec 10 znakow
# dwie duze litery od b-z
# dwie male litery od b-z
# znak specjalny
# trzy liczby
# nie moze byc haslem z pliku hasla

class Password:
    def __init__(self, password):
        self.password = password
        

    def length(self):
        answer = True
        if len(password) != 10:
            answer = False
        return answer
    
    def lowercase_letters(self):
        lower = 0
        for sign in password:
            if sign.islower() and sign != 'a':
                lower += 1
        if lower < 2:
            answer = False
        else:
            answer = True
        return answer

    def upper_letters(self):
        upper = 0
        for sign in password:
            if sign.isupper() and sign != 'A':
                upper += 1
        if upper < 2:
            answer = False
        else:
            answer = True
        return answer
    
    def special_caracters(self):
        special = False
        for sign in password:
            if not sign.isalpha() and not sign.isdigit():
                special =True
        return special

    def numbers(self):
        num = 0
        for sign in password:
            if sign.isdigit():
                num += 1
        if num == 3:
            answer = True
        else:
            answer =False
        return answer

    def from_file(self):
        answer = True
        with open('hasla.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if password == line:
                    answer = False
        return answer


    
        
password = input("enter your password: ")

p = Password(password)
print(p.length())
print(p.lowercase_letters())
print(p.upper_letters())
print(p.special_caracters())
print(p.numbers())
print(p.from_file())




