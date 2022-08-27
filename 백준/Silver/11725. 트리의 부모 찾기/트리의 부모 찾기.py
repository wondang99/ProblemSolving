import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline().rstrip("\n"))
graph = defaultdict(list)
parent_node = [0 for _ in range(N+1)]
visited = [ False for _ in range(N+1)]

for _ in range(N-1) :
    x,y = list(map(int,sys.stdin.readline().rstrip("\n").split()))
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(i) :
    visited[i] = True
    for node in graph[i] :
        if not visited[node] :
            parent_node[node] = i
            dfs(node)
dfs(1)
for n in range(2,N+1) :
    print(parent_node[n])