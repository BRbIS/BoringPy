# Найти самое длинное слово в спитке

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice123456789', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


# find the longest string in each of the inner list
# находит только в одном элементе списка
def longest(list):
    max_long = 0
    for i in list:
        #print(i, len(i))
        if len(i) > max_long:
            max_long = len(i)
        else:
            continue
    return max_long


# идет по всем элементам списка и находит самое большое из всех
def biggest(table):
    max_long = 0
    for i in range(len(table)):
        for y in table[i]:
            if len(y) > max_long:
                max_long = len(y)
            else:
                continue
    return max_long

print(longest(tableData[0]))

print(biggest(tableData))