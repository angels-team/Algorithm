import sys

read = lambda:sys.stdin.readline().strip()

boards = []

def max(num1, num2) :
	if num1 > num2 : return num1
	else : return num2
	
def min(num1, num2) :
	if num1 < num2 : return num1
	else : return num2
	
def fence(left, right) :
	global boards
	
	if left == right :
		return boards[left]
	
	mid = (left + right) / 2
	
	leftS = fence(left, mid)
	rightS = fence(mid+1, right)
	
	lo = mid
	hi = mid+1
	
	bothS = 0
	while lo >= left and hi <= right :
		minHeight = boards[lo]
		if minHeight <= board[hi] :
			hi = hi + 1
		else :
			lo = lo - 1
			
		bothS = max(bothS, minHeight * (hi - lo))
	
	result = max(leftS, max(rightS, bothS))
	return result
		
		
		
for _ in range(int(read())):
	boardCount = int(read())
	boards = map(int, read().split());
	
	fence(0, boardCount-1)