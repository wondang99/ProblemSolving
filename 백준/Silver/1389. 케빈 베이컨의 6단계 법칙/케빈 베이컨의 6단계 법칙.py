import sys
from collections import defaultdict
from collections import deque

N, M = list(map(int,sys.stdin.readline().rstrip("\n").split()))
user = defaultdict(set)
result = [0 for _ in range(N+1)]

for m in range(M) :
    x, y = list(map(int,sys.stdin.readline().rstrip("\n").split()))
    user[x].add(y)
    user[y].add(x)
    
for u in user :
    visited = [ 0 for _ in range(N+1)]
    visited[u] = -1
    dq = deque([u])
    count=1
    while(dq) :
        for _ in range(len(dq)) :
            for i in user[dq.popleft()] :
                if visited[i]!=0 :
                    continue
                visited[i] = count
                dq.append(i)
        count+=1
    result[u] = sum(visited)+1

print(result.index(min(result[1:])))