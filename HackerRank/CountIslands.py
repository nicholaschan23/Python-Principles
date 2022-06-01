"""
[
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1],
]
"""
def countIslands(matrix, h, w):
    numIslands = 0
    for x in range(0, h):
        for y in range(0, w):
            if (matrix[x][y] == 1):
                numIslands += 1
                matrix[x][y] = -1 # mark found
                countIslandsHelper(matrix, h, w, x, y)
    return numIslands

# clears islands
def countIslandsHelper(matrix, h, w, x, y):
    if (matrix[x][y] == 0 or matrix[x][y] == -1):
        return
        
    # directions
    # right
    if (x + 1 < h and matrix[x + 1][y] == 1):
        matrix[x + 1][y] = -1
        countIslandsHelper(matrix, h, w, x + 1, y)
    
    # left
    if (x - 1 >= 0 and matrix[x - 1][y] == 1):
        matrix[x - 1][y] = -1
        countIslandsHelper(matrix, h, w, x - 1, y)
        
    # down
    if (y - 1 >= 0 and matrix[x][y - 1] == 1):
        matrix[x][y - 1] = -1
        countIslandsHelper(matrix, h, w, x, y - 1)
        
    # up
    if (y + 1 < w and matrix[x][y + 1] == 1):
        matrix[x][y + 1] = -1
        countIslandsHelper(matrix, h, w, x, y + 1)