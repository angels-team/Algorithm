import sys

def max(num1, num2) :
    if num1 > num2 : return num1
    else : return num2

class Concert:
    n = 0
    vm = 0
    volumes = []
    table = None

    def __init__(self, n, vs, vm, volumes):
        self.n = n
        self.vm = vm
        self.volumes = volumes
        self.volumes.insert(0, vs)
        self.table = [[-1]*(vm+1) for _ in range(n+1)]
    
    def maxVol(self) :
        return self.maxVolume(0, self.volumes[0])
        
    def maxVolume (self,turn, volume) :
        if self.table[turn][volume] > 0:
            return self.table[turn][volume]

        nVol = volume - self.volumes[turn+1]
        pVol = volume + self.volumes[turn+1]

        if turn == self.n - 1:
            if not self.isAvail(nVol) : nVol = -1
            if not self.isAvail(pVol) : pVol = -1

            return max(nVol, pVol)
        else :
            left = -1
            right = -1

            if self.isAvail(nVol) :
                left = self.maxVolume(turn+1, nVol)
                self.table[turn+1][nVol] = left
            if self.isAvail(pVol) :
                right = self.maxVolume(turn+1, pVol)
                self.table[turn+1][pVol] = right

            return max(left, right)

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
