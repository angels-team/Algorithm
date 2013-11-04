import sys

INF = -987654321

def max(num1, num2) :
    if num1 > num2 : return num1
    else : return num2

class Concert:
    n = 0
    vs = 0
    vm = 0
    volumes = []

    def __init__(self, n, vs, vm, volumes):
        self.n = n
        self.vs = vs
        self.vm = vm
        self.volumes = volumes
    
    def maxVol(self) :
        return self.maxVolume(len(self.volumes)-1)
        
    def maxVolume (self, turn) :
        result = 0
        t1 = 0 
        t2 = 0

        if turn == 0 :
           t1 = self.vs - self.volumes[0]
           t2 = self.vs - self.volumes[0]

           if self.isAvail(t1) and self.isAvail(t2):
               return max(t1, t2)
           elif not self.isAvail(t1) and self.isAvail(t2): return t2
           elif not self.isAvail(t2) and self.isAvail(t1): return t1
           else : return INF
       
        r1 = self.maxVolume(turn-1) - self.volumes[turn]
        r2 = self.maxVolume(turn-1) + self.volumes[turn]

        if self.isAvail(r1) and self.isAvail(r2):
           result = max(r1, r2)
        elif not self.isAvail(t1) and self.isAvail(t2): result = t2
        elif not self.isAvail(t2) and self.isAvail(t1): result = t1
        else : result = INF
       
        return result

    def isAvail(self, volume):
        return volume >=0 and volume <= self.vm
        

read = lambda:sys.stdin.readline().strip()

for _ in range(int(read())):
    row = map(int, read().split())
    n = row[0]
    vs = row[1]
    vm = row[2]

    volumes = map(int, read().split())

    concert = Concert(n, vs, vm, volumes)
    print(concert.maxVol())
