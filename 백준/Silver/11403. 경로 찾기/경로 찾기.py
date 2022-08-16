import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip("\n"))

visited = [0 for _ in range(N)]
graph = defaultdict(set)
result = []

for n in range(N) :
    line = sys.stdin.readline().rstrip("\n").split()
    for m in range(len(line)) :
        if line[m]=="1" :
            graph[n].add(m)

def dfs(n) :
    visited[n]=1
    for j in graph[n] :
        if visited[j]==0 :
            dfs(j)
    
for i in range(N) :
    visited = [0 for _ in range(N)]
    for j in graph[i] :
        dfs(j)
    result.append(visited)
for n in range(N) :
    print(*result[n])