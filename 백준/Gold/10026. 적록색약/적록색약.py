import sys
sys.setrecursionlimit(10**7)
N  = int(sys.stdin.readline().rstrip("\n"))

board = []
abboard = []
d = [[1,0],[0,1],[-1,0],[0,-1]]
visited = [[ False for _ in range(N)] for _ in range(N)]
abvisited = [[ False for _ in range(N)] for _ in range(N)]
for n in range(N) :
    line = list(sys.stdin.readline().rstrip("\n"))
    board.append(line)
    abboard.append(line[:])
for n in range(N) :
    for m in range(N) :
        if abboard[n][m]=="R" :
            abboard[n][m]="G"
normal=0
abnormal = 0

def dfs(i,j,flag) :
    if flag == 1 :
        visited[i][j] = True
        for v in d :
            if i+v[0]<0 or i+v[0]>N-1 or j+v[1]<0  or j+v[1]>N-1 or visited[i+v[0]][j+v[1]]:
                continue
            if board[i+v[0]][j+v[1]]==board[i][j] :
                dfs(i+v[0],j+v[1],flag)
    else :
        abvisited[i][j] = True
        for v in d :
            if i+v[0]<0 or i+v[0]>N-1 or j+v[1]<0  or j+v[1]>N-1 or abvisited[i+v[0]][j+v[1]]:
                continue
            if abboard[i+v[0]][j+v[1]]==abboard[i][j] :
                dfs(i+v[0],j+v[1],flag)

for i in range(N) :
    for j in range(N) :
        if not visited[i][j] :
            dfs(i,j,1)
            normal+=1
for i in range(N) :
    for j in range(N) :
        if not abvisited[i][j] :
            dfs(i,j,0)
            abnormal+=1
            
print(normal, abnormal)