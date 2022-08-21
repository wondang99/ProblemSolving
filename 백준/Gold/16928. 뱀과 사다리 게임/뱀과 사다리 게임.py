import sys
from collections import deque

N, M = list(map(int,sys.stdin.readline().rstrip("\n").split()))
start = []
arrival = []
visited = [False for _ in range(101)]

for n in range(N+M) :
    e=list(map(int,sys.stdin.readline().rstrip("\n").split()))
    start.append(e[0])
    arrival.append(e[1])
count = 0
flag = 0

route = deque([1])
while flag==0:
    for now in range(len(route)) :
        step = route.popleft()
        for d in range(1,7) :
            #step+=d 바보, step이 계속 쌓임
            nstep=step+d
            if nstep==100 :
                break
            if nstep>100 or visited[nstep]:
                continue
            if nstep in start :
                nstep = arrival[start.index(nstep)]
            route.append(nstep)
            visited[nstep]=True
        if nstep==100 :
            flag=1
            break
    count+=1
        
print(count)