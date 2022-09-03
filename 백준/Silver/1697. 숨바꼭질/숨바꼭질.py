import sys
from collections import deque

N, K = list(map(int,sys.stdin.readline().rstrip("\n").split()))

time = 0
visit = {N}
subin = deque([(N,0)])
def bfs() :
    
    while subin :
        t = subin.popleft()
        if t[0]==K :
            return t[1]
        next_s = {t[0]+1, t[0]-1, t[0]*2}
        for n in next_s :
            if n < 0 or n>100000:
                continue
            if not n in visit :
                subin.append((n,t[1]+1))
                visit.add(n)
print(bfs())