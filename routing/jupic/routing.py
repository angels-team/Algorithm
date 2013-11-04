import sys

readl = lambda:sys.stdin.readline().strip()

INF = 9999999999999

def minRoute(adj, nodes):
    minWeight = [INF for _ in range(nodes)]
    minWeight[0] = 1

    for cv in adj:
        for v in adj[cv]:
            weight = minWeight[cv] * adj[cv][v]
            if minWeight[v] > weight :
                minWeight[v] = weight

    return minWeight[nodes-1]

for _ in range(int(readl())) :
    nodeCount = map(int, readl().split())

    adj = {}
    nodes = set()
    for _ in range(nodeCount[1]):
        node = readl().split()
        n1 = int(node[0])
        n2 = int(node[1])
        noise = float(node[2])
        nodes.add(n1)
        nodes.add(n2)

        if n1 in adj:
            adj[n1][n2] = noise
        else :
            adj[n1] = {n2:noise}
        if n2 in adj:
            adj[n2][n1] = noise
        else :
            adj[n2] = {n1:noise}

    print("%.10f" % minRoute(adj, len(nodes)))
