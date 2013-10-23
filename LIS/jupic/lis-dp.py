#lis2.py
import sys

readl = lambda : sys.stdin.readline().strip()

numbers = 0
sequence = []
table = []
def max(num1, num2) :
	if num1 > num2 : return num1
	else : return num2
	
def lis(begin) :
	if table[begin] > -1 : return table[begin]
	
	result = 1
	for i in range(begin+1, numbers) :
		if int(sequence[begin]) < int(sequence[i]) :
			result = max(result, 1 + lis(i))
	
	table[begin] = result
	return result

testCases = int(readl())
for _ in range(testCases) :
	numbers = int(readl())
	sequence = readl().split()
	table = [-1] * numbers

	print(lis(0))
	print(table)