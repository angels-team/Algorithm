import sys

readl = lambda : sys.stdin.readline().strip()

EMPTY = -9999999
table = []
sequence = []

def max(num1, num2):
    if num1 > num2 : return num1
    else : return num2

def game(left, right):
    global table, sequence

    if left > right : return 0
    
    if table[left][right] != EMPTY : return table[left][right]

    lsum = sequence[left] - game(left+1, right)
    rsum = sequence[right] - game(left, right-1)
    
    result = max(lsum, rsum)
    if (right - left + 1) >=2 :
        result = max(result, -game(left+2, right))
        result = max(result, -game(left, right-2))
    
    table[left][right] = result
    return result


testCases = int(readl())

for _ in range(testCases) :
    numbers = int(readl())
    sequence = map(int, readl().split())
    
    table = []
    for _ in range(numbers) :
        table.append([EMPTY] * numbers)
    
    result = game(0, numbers-1)
    print(result)
