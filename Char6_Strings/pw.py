#! /usr/bin/python3
__author__ = 'agorgoma'

# pw.py - An insecure password locker program.

import sys, pyperclip


PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' coppied to clipboard.')
    print(pyperclip.paste())
else:
    print('THERE is no account named ' + account)