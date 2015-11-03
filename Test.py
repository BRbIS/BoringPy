__author__ = 'agorgoma'

#list to dict

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

dictAddItems = {}
for v in dragonLoot:
    dictAddItems.setdefault(v, 0)
    dictAddItems[v] = dictAddItems[v] + 1
print(dictAddItems)