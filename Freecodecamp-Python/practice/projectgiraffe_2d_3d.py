#2D and 3D lists, grid like data in python with list of lists
#for loop inside a for loop - nested for loop
number_grid = [
    [1,2,2], 
    [4,4,6],
    [7,8,9],
    [0]
]

#print(number_grid[3][0])

for row in number_grid:
    print(row)
    for col in row:
        print(col)