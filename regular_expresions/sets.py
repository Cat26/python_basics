import re

text ='hititgjewhitihaisif'
print(re.findall(r'[th]i', text)) # t or h
print(re.findall(r'i[^th]+', text))

text1='My father have Birthday today'
print(re.findall(r'[A-Z][a-z]*', text1))# every word strarted with uppercase

text2 ='Hello -- my friend!'
print(re.findall(r'[^\-! ]+', text2))