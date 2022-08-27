import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
N,M = list(map(int,sys.stdin.readline().rstrip("\n").split()))
graph = defaultdict(list)
visited = [False for _ in range(N+1)]
count = 0

for _ in range(M) :
    u,v = list(map(int,sys.stdin.readline().rstrip("\n").split()))
    graph[u].append(v)
    graph[v].append(u)
def dfs(i) :
    visited[i] = True
    for g in graph[i] :
        if not visited[g] :
            dfs(g)

for i in range(1,N+1) :
    if not visited[i] :
        dfs(i)
        count+=1
print(count)