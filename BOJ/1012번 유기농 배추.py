import sys
from collections import deque
T = int(sys.stdin.readline().rstrip("\n"))
dic = [[-1,0],[0,1],[1,0],[0,-1]]

for _ in range(T):
    M, N, K = list(map(int,sys.stdin.readline().rstrip("\n").split()))
    cabbage = [[0 for _ in range(M+2)] for _ in range(N+2)]
    num=0
    #방문 기록을 위해 vistied 리스트 만들었지만 0으로 바꿈으로써 생략 가능
    for c in range(K) : #양배추 밭 생성
        x,y = list(map(int,sys.stdin.readline().rstrip("\n").split()))
        cabbage[y+1][x+1]=1

    def dfs(cab) :
        for d in dic :
            if cabbage[cab[0]+d[0]][cab[1]+d[1]]==1:
                cabbage[cab[0]+d[0]][cab[1]+d[1]]=0
                dfs([cab[0]+d[0],cab[1]+d[1]])

    for x in range(M+1) :
        for y in range(N+1) : #초기 양배추 탐색
            if cabbage[y][x]==1 :
                cabbage[y][x]=0
                dfs([y,x])
                num+=1
    print(num)
