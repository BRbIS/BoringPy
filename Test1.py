__author__ = 'agorgoma'

# merge 2 dicts

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = {'dagger': 1, 'gold coin': 3, 'ruby': 1}

for i in dragonLoot.keys():
    if i not in inv:
        inv[i] = dragonLoot.get(i, 0)
    else:
        inv[i] = inv[i] + dragonLoot.get(i, 0)


print(inv)
print(dragonLoot)