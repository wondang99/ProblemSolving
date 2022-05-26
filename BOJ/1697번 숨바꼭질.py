import sys
from collections import deque

N,K= list(map(int,sys.stdin.readline().rstrip("\n").split()))
w = [0 for i in range(100001)]
n= deque([N-1,N+1,2*N])
w[N],w[K] =-1, 1
count=0

while n :
    if N==K :
        break
    count+=1
    for _ in range(len(n)) :
        node = n.popleft()
        if node < 0 or 100000<node or [node]==-1:
            continue
        elif w[node]==0 :
            w[node]=-1
            n.extend([node-1,node+1,2*node])
        elif w[node] == 1 : 
            n=[]
            break
print(count)