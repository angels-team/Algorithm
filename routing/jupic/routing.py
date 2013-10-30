import sys

readl = lambda:sys.stdin.readline().strip()

INF = 9999999999999

def find1(nodes):
    visited = [False] * len(nodes)
    visited[0] = True
    stack = []
    min = INF
    weight = 1
    
    stack.append(0)

    while(len(stack) > 0):
        curNode = stack[0]
        for nextNode in range(len(nodes)):
            if not visited[nextNode] and nodes[curNode][nextNode] :
                candidate = weight * nodes[curNode][nextNode]
                
                if weight > min : break

                visited[nextNode] = True
                stack.insert(0, nextNode)
                weight = candidate
                curNode = nextNode

def min(num1, num2):
    if num1 < num2 : return num1
    else : return num2

def find(node, weight) :
    visited[node] = True
    
    if node == len(nodes)-1 : 
        result = min(minWeight, weight)
        visited[node] = False
        return result
    
    for nextNode in range(len(nodes)):
        if not visited[nextNode] and nodes[node][nextNode] :
            temp = weight * nodes[node][nextNode]
            visited[nextNode] = True
            result = find(nextNode, temp)

testCases = int(readl())

for _ in range(testCases) :
    nodeCount = map(int, readl().split())

    nodes = [[0] * nodeCount[0] for _ in range(nodeCount[0])]
    for _ in range(nodeCount[1]):
        node = readl().split()
        n1 = int(node[0])
        n2 = int(node[1])
        noise = float(node[2])

        if not nodes[n1][n2] or (nodes[n1][n2] and nodes[n1][n2] > noise) : 
            nodes[n1][n2] = noise
            nodes[n2][n1] = noise
