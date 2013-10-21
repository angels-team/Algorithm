import sys

readl = lambda:sys.stdin.readline().strip()

criterion = 0
pathCache = []

def init(n) :
    global pathCache
    pathCache = []
    diamond = []
    for i in range(2*n - 1) :
        pathCache.append([-1]*n)
        diamond.append([0]*n)
    return diamond
    

def path(diamond, row, col):
    global pathCache

    if row == (len(diamond)-1) : return diamond[row][col]
    
    result = pathCache[row][col]
    if (result > -1) : return result
    
    if (row < criterion-1) :
        leftCol = col
        rightCol = col + 1
    else :
        leftCol = col - 1
        rightCol = col
    
    left = 0
    right = 0
    if (leftCol > -1) :
        left = path(diamond, row+1, leftCol) + diamond[row][col]
    if (rightCol < criterion):
        right = path(diamond, row+1, rightCol) + diamond[row][col]

    if (left >= right) :
        result = left
    else :
        result = right
    
    pathCache[row][col] = result
    return result;

testCases = int(readl())

for i in range(testCases):
    criterion = int(readl())
    diamond = init(criterion)
    
    for r in range(len(diamond)):
        cols = map(int, readl().split())
        for c in range(len(cols)) :
            diamond[r][c] = cols[c]
    
    result = path(diamond, 0, 0)
    print(result)
