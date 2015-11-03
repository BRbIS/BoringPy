__author__ = 'agorgoma'


def list_to_dict(ilist):
    idict = {}
    for v in ilist:
        idict.setdefault(v, 0)
        idict[v] += 1
    return idict


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v,k)
        item_total = item_total + inventory.get(k, 0)
    print("Total number of items " + str(item_total))


def addToInventory(inventory, addedItems):
    addedItems = list_to_dict(addedItems)
    for i in addedItems.keys():
        if i not in inventory:
            inventory[i] = addedItems.get(i, 0)
        else:
            inventory[i] += addedItems.get(i, 0)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)