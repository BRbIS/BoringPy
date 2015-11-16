__author__ = 'agorgoma'

import re


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                 # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
)''', re.VERBOSE)

text = 'My number is 415-555-4242, (123)345-7890, 444 333 2222, 111 2222'
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    #print(matches)
    #print(groups)
    #print(groups[0])
    #print(groups[1])
    #print(groups[3])
    #print(groups[5])
    #print(groups[8])
    #print(groups[4])

#print(phoneRegex.findall(text))
print(matches)
print(matches[1])