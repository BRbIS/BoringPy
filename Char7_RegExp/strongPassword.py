#! /usr/bin/python3

import re

# TODO 8 char
ch8Regex = re.compile(r'\d{8}')
#mo = ch8Regex.search('1234567, 2, 3123456789fgfgfgf, 4, 5, 6, 7, 8')
#print('Phone number found: ' + mo.group())
# TODO Lower\Upper case
upRegex = re.compile(r'([A-Z])+')
lowRegex = re.compile(r'([a-z])+')
#mo1 = lowRegex.search('pasSword')
#mo2 = lowRegex.search('PAsSWORD')
#print('Phone number found: ' + mo2.group())
# TODO one or more digits
digRegex = re.compile(r'([0-9])+')
#mo3 = digRegex.search('pasSwor1d')
#print('Phone number found: ' + mo3.group())
# TODO all in one
strongPassRegex = re.compile(r'(\d{8})+|([A-Z]+)+|([a-z]+)+|([0-9]+)+')
mo4 = strongPassRegex.search('password')
print('Phone number found: ' + mo4.group())