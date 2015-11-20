#! /usr/bin/python3
# аналог функции strip(), которая убирает пробелы в начале и
# конце строки, но реализованная с помощью регулярных выражений.


import re

text = ' spacer '

stripRegex = re.compile(r'^\s|\s$')
#mo = stripRegex.sub('.', text)
#s = mo.group()
#print(text)
#print(mo)

for i in text:
    if stripRegex.search(i) is True:
        i = stripRegex.sub('.', i)
        print(i)
    else:
        continue

