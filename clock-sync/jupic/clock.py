#clock sync
import sys

INF = 9999
SWITCHES = 10
CLOCKS_NUMS = 16

clockSwitchs = [
[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1],
[1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0],
[1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1],
[0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0]
]

def isTwelveOclock(clocks) :
	for clock in clocks :
		if clock != 12 : 
			return 0
	return 1

def click(clocks, switch) :
	for clock in range(CLOCKS_NUMS) :
		if (clockSwitchs[switch][clock] == 1) :
			clocks[clock] = clocks[clock] + 3
			if (clocks[clock] == 15) : clocks[clock] = 3
	
def search(clocks, switch) :
	if (switch == SWITCHES) :
		if (isTwelveOclock(clocks)) :
			return 0 
		else : 
			return INF;
	
	result = INF
	for count in range(4) :
		temp = count + search(clocks, switch + 1)
		if (result > temp) : result = temp
		click(clocks, switch)
	
	return result

inputl = lambda : sys.stdin.readline().strip()
	
testCases = int(inputl())

for case in range(testCases) :
	inputs = inputl().split()
	clocks = []
	for i in inputs :
		clocks.append(int(i))
		
	result = search(clocks, 0)
	if result == INF : result = -1
	print(result)