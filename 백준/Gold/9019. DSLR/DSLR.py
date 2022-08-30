import sys
from collections import deque

T = int(sys.stdin.readline().rstrip("\n"))

for _ in range(T) :
    A,B = list(map(int,sys.stdin.readline().rstrip("\n").split()))
    visited = [False for _ in range(10000)]
    DSLR = deque([(A,"")])

    while DSLR :
        node,c = DSLR.popleft()
        if node==B :
            print(c)
            break
        if not visited[node-1] :
            visited[node-1]=True
            DSLR.append(((node*2)%10000,c+"D"))
            S=node-1 if node!=0 else 9999
            DSLR.append((S,c+"S"))
            DSLR.append(((node*10+node//1000)%10000,c+"L"))
            DSLR.append(((node//10+node%10*1000)%10000,c+"R"))