import sys
from collections import deque

N, M = list(map(int,sys.stdin.readline().rstrip("\n").split()))
miro = [[0 for _ in range(M+2)]]
for _ in range(N) :
    miro.append([0]+list(map(int,list(sys.stdin.readline().rstrip("\n"))))+[0])
miro.append([0 for _ in range(M+2)])

d = [[-1,0],[0,1],[1,0],[0,-1]]
dq = deque([[1,1]])
count=0
while dq:
    
    for route in range(len(dq)) :
        node = dq.popleft()
        if node[0]==N and node[1]==M :
            dq=[]
            break
        #결국 최단경로 이후로 지난다면 이미 최단 경로 X
        for next_d in d :
            if miro[node[0]+next_d[0]][node[1]+next_d[1]]==1 :
                miro[node[0]+next_d[0]][node[1]+next_d[1]]=0
                dq.append([node[0]+next_d[0],node[1]+next_d[1]])
    count+=1
print(count)