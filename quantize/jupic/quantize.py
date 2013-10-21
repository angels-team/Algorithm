import sys

INF = 999999999
numbers = 0
sequence = []

partSum = [0] * 101
squareSum = [0] * 101

table = []
for i in range(101):
    table.append([-1] * 11)

readl = lambda:sys.stdin.readline().strip()

def init() :
    global table
    global partSum
    global squareSum

    for row in table :
        for i in range(len(row)) :
            row[i] = -1

    partSum[0] = sequence[0]
    squareSum[0] = sequence[0] * sequence[0]
    for i in range(1, numbers):
        partSum[i] = partSum[i-1] + sequence[i]
        squareSum[i] = squareSum[i-1] + sequence[i] * sequence[i]
    
def quantize(index, parts) :
    global table

    if (index == numbers) : return 0
    if (parts == 0) : return INF

    result = table[index][parts]
    if result != -1 : return result

    result = INF
    length = 1
    while((index + length) <= numbers) :
        temp = error(index, index+length-1)+quantize(index + length, parts-1)
        if (temp < result) : result = temp
        length = length + 1

    table[index][parts] = result
    return result

def error(begin, end) :
    sum = partSum[end]
    sqSum = squareSum[end]
    if begin > 0 :
        sum = sum - partSum[begin-1]
        sqSum = sqSum - squareSum[begin-1]

    m = int(round(float(sum) / (end - begin + 1)))
    result = sqSum - 2*m*sum + m*m*(end-begin+1)
    return result

testCases = int(readl())

for c in range(testCases):
    inputs = map(int, readl().split())
    numbers = inputs[0]
    parts = inputs[1]

    sequence = map(int, readl().split())
    sequence.sort()

    init()
    #print(error(0,2))
    result = quantize(0, parts)
    print(result)
