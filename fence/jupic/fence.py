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
	
	height = min(boards[lo], boards[hi])
	square = max(max(leftS, rightS), height*2)

	while lo > left or hi < right :
		if (hi < right) and (lo == left or height < boards[hi+1]) :
			hi = hi + 1
			height = min(height, boards[hi])
		else :
			lo = lo - 1
			height = min(height, boards[lo])
			
		square = max(square, height * (hi - lo + 1))
		
	return square
		
		
		
for _ in range(int(read())):
	boardCount = int(read())
	boards = map(int, read().split());
	
	print(fence(0, boardCount-1))
