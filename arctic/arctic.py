import sys
import math

readl = lambda : sys.stdin.readline().strip()

baseNumber = 0
distance = []

def init(bases) :
    global distance
    distance = []
    for _ in range(len(bases)):
        distance.append([-1]*len(bases))

    for idx in range(len(bases)) :
        for n in range(idx+1, len(bases)):
            x = bases[n][0] - bases[idx][0]
            y = bases[n][1] - bases[idx][1]
            
            d = x*x + y*y
            distance[idx][n] = d
            distance[n][idx] = d

def decide(d):
    visited = [False] * baseNumber
    visited[0] = True
    queue = []
    queue.append(0)
    seen = 0
    
    while (len(queue) > 0):
        curBase = queue.pop()
        seen = seen + 1
        for nextBase in range(baseNumber):
            if not visited[nextBase] and distance[curBase][nextBase] < (d*d) :
                queue.append(nextBase)
                visited[nextBase] = True

    return seen == baseNumber

def find():
    lo = 0 
    hi = 1416.00
    for _ in range(100) :
        mid = (lo + hi) / 2
        if decide(mid) : hi = mid
        else : lo = mid
    return hi

testCases = int(readl())

for _ in range(testCases):
    baseNumber = int(readl())
    bases = []
    for _ in range(baseNumber):
        bases.append(map(float, readl().split()))

    init(bases)
    result = find()
    print("%.2f" % round(result, 2))
