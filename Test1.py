
def strip(text):
    import re
    stripRegex = re.compile(r'^(\s)*|(\s)*$')
    mo1 = stripRegex.sub('', text)
    return mo1

print(strip(' spa ser '))
print(strip('  spa ser     '))