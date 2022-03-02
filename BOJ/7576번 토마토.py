import sys
from collections import deque

M, N = list(map(int,sys.stdin.readline().rstrip("\n").split()))
tomato = [list(map(int,sys.stdin.readline().rstrip("\n").split())) for _ in range(N)]
dic = [[-1,0],[0,1],[1,0],[0,-1]]
first = []
result = 0

def bfs(tomato_list) :
    global tomato
    dq = deque(tomato_list)
    count=-1
    n= len(tomato_list)
    while dq:
        for _ in range(len(dq)) :
            x = dq.popleft()
            for d in dic :
                x_t = x[0]+d[0]
                y_t = x[1]+d[1]
                if 0<=x_t and x_t<N and 0<=y_t and y_t<M and tomato[x_t][y_t]==0:
                    tomato[x_t][y_t]=1
                    dq.append([x_t,y_t])
        count+=1
    for m in range(M) :
        for n in range(N) :
            if tomato[n][m]==0 :
                count = -1
                return count
    return count

for m in range(M) :
    for n in range(N) :
        if tomato[n][m] == 1:
            first.append([n,m])
print(bfs(first))