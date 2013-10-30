import sys

readl = lambda:sys.stdin.readline().strip()

def convert(code, index):
    
    if code[index] == 'x' :
        index = index + 1
        leftTop = convert(code, index)
        
        index = index + len(leftTop)
        rightTop = convert(code, index)

        index = index + len(rightTop)
        leftDown = convert(code, index)

        index = index + len(leftDown)
        rightDown = convert(code, index)
        
        return "x" + leftDown + rightDown + leftTop + rightTop
    else : return code[index]

testCases = int(readl())

for _ in range(testCases):
    code = readl()
    print(convert(code, 0))
