__author__ = 'agorgoma'


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

#def printTable(table):


# find the longest string in each of the inner list
def longest(list):
    max_long = 0
    for i in list:
        #print(i, len(i))
        if len(i) > max_long:
            max_long = len(i)
        else:
            continue
    return max_long

#print(longest(tableData[0])


colWidths = [0] * len(tableData[0])
print(colWidths)



print(tableData[0][0], tableData[1][0], tableData[2][0])