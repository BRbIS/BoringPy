#! /usr/bin/python3

import re

# check 8 char
ch8Regex = re.compile(r'(.{8})+')
#mo = ch8Regex.search('1234567, 2, 3123456789fgfgfgf, 4, 5, 6, 7, 8')
#print('Phone number found: ' + mo.group())
# check Lower\Upper case
upRegex = re.compile(r'([A-Z])+')
lowRegex = re.compile(r'([a-z])+')
#mo1 = lowRegex.search('pasSword')
#mo2 = lowRegex.search('PAsSWORD')
#print('Phone number found: ' + mo2.group())
# check one or more digits
digRegex = re.compile(r'([0-9])+')
#mo3 = digRegex.search('pasSwor1d')
#print('Phone number found: ' + mo3.group())


text = 'pasS1            '

print(ch8Regex.search(text))

if ch8Regex.search(text) and upRegex.search(text) and lowRegex.search(text) and digRegex.search(text) is not None:
    print('Password strong')
else:
    if ch8Regex.search(text) is None:
        print('Need min 8 characters')
    elif upRegex.search(text) is None:
        print('None upper char')
    elif lowRegex.search(text) is None:
        print('None lower char')
    elif digRegex.search(text) is None:
        print('None digit char')