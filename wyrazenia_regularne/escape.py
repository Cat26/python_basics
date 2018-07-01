import re

text ='Two tickets cost 23zl an 5gr!'
text2 ='How dare you, You are so selfish'
# print(re.findall(r'\d+', text)) # one digit
# print(re.findall(r'\D+', text)) #one no digit
# print(re.sub(r'[wc]o\s', 'kurczak!', text)) #space
# print(re.findall(r'\w+', text)) #alphanumeric

# print(re.findall(r'cost', text))
# print(re.findall(r'^cost', text)) # on the begining of the string
# print(re.findall(r'!$', text)) # end of the string

print(re.findall(r'\bare\b', text2))