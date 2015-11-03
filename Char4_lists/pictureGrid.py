__author__ = 'agorgoma'


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#print(grid[0][0], grid[1][0], grid[2][0],grid[3][0], grid[4][0], grid[5][0], grid[6][0], grid[7][0], grid[8][0])
#print(grid[0][1], grid[1][1], grid[2][1],grid[3][1], grid[4][1], grid[5][1], grid[6][1], grid[7][1], grid[8][1])
#print(grid[0][2], grid[1][2], grid[2][2],grid[3][2], grid[4][2], grid[5][2], grid[6][2], grid[7][2], grid[8][2])

#a = ''
#for i in range(len(grid)):
#    a +=grid[i][0]

#b = ''
#for y in range(len(grid[0])):
#    print(grid[0][y])

for y in range(len(grid[0])):
    a = ''
    for x in range(len(grid)):
        a +=grid[x][y]
    print(a)


