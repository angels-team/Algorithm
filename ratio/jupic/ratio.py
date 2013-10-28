import sys
import math

readl = lambda : sys.stdin.readline().strip()

def minWin(play, win):
    ratio = (win * 100 / play) + 1
    
    if (ratio-1 > 98) : return -1

    top = ratio * play - 100 * win
    bottom = 100 - ratio

    result = int(math.ceil(float(top) / bottom))
    return result

testCases = int(readl())

for _ in range(testCases):
    line = map(int, readl().split())
    play = line[0]
    win = line[1]
        
    result = minWin(play, win)
    print(result)
