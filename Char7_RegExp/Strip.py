#! /usr/bin/python3
# аналог функции strip(), которая убирает пробелы в начале и
# конце строки, но реализованная с помощью регулярных выражений.

def stripAllReg(text):
    import re
    word = ''
    stripRegex = re.compile(r'^\s|\s$')
    for i in text:
        mo = stripRegex.sub('', i)
        word += mo
    return word


def stripReg(text, char=''):
    import re
    stripRegex = re.compile(r'^(\s)*|(\s)*$')
    mo1 = stripRegex.sub(char, text)
    return mo1

print(stripAllReg('  spa ser '))
print(stripReg('    spa ser   ', 'a'))

