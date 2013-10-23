#lis.py
import sys

readl = lambda : sys.stdin.readline().strip()

testCases = int(readl())

def lis(left, right) :
	leftLen = len(left)
	rightLen = len(right)
	
	result = []
	if leftLen > rightLen :
		result = result + left
	else : result = result + right
	
	if (leftLen > 0) and (rightLen > 0) :
		for i in range(len(left)) :
			if left[i] < right[0] :
				if len(result) < i + rightLen :
					result = left[0:i] + right
					break

		for j in range(len(right)) :
			if left[len(left)-1] < right[j] :
				if len(result) < leftLen + rightLen - j :
					result = left + right[j:rightLen]
				break
			
	return result

for _ in range(testCases) :
	numbers = int(readl())
	sequence = map(int, readl().split())
	
	left=sequence[0:1]
	right=[]

	for i in range(numbers-1) :
		if sequence[i] < sequence[i+1] :
			right.append(sequence[i+1])
		else : 
			left = lis(left, right)
			right = []
	
	print(len(lis(left, right)))
	
	