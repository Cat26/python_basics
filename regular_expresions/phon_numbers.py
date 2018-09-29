import re

numbers = ['123 456 789', '(123) 456 789', '123-256-789', '123.456.789', '123456789']

pat = r'\(?\d{3}[\)-\.]?\s?\d{3}[-\s\.]?\d{3}'

for num in numbers:
    m = re.search(pat, num)
    if m:
        print(m.group())