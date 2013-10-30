import sys

readl = lambda:sys.stdin.readline().strip()

points = []
distance = []

def init():
    global distance, points
    distance = []
    p = len(points)
    for _ in range(p):
        distance.append([-1] * p)

def getDistance(p1, p2):
    if distance[p1][p2] != -1 : return distance[p1][p2]
    
    x = points[p1][0] - points[p2][0]
    y = points[p1][1] - points[p2][1]

    d = (x*x) + (y*y)
    distance[p1][p2] = d
    distance[p2][p1] = d
    return d

def isAvaliable(power) :
    pCount = len(points)
    
    if getDistance(0, pCount-1) <= power : return "YES"

    visited = [False] * pCount
    visited[0] = True
    queue = []
    queue.append(0)

    while (len(queue) > 0):
        curPoint = queue.pop()
        for nextPoint in range(pCount):
            if not visited[nextPoint] and getDistance(curPoint, nextPoint) <= power :
                if getDistance(nextPoint, pCount-1) <= power : return "YES"
                else :
                    queue.append(nextPoint)
                    visited[nextPoint] = True
    return "NO"

testCases = int(readl())

for _ in range(testCases):
    power = int(readl())
    points = []
    points.append(map(int, readl().split()))
    end = map(int, readl().split())
    for _ in range(int(readl())):
        points.append(map(int, readl().split()))
    points.append(end)
    init()
    print(isAvaliable(power*power))
