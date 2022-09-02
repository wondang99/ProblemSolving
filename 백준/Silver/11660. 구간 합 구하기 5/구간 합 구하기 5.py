import sys

N, M = list(map(int,sys.stdin.readline().rstrip("\n").split()))
board = [list(map(int,sys.stdin.readline().rstrip("\n").split())) for _ in range(N)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for n in range(0,N) :
    for m in range(0,N) :
        dp[n+1][m+1]= board[n][m]+dp[n+1][m]+dp[n][m+1]-dp[n][m]
for _ in range(M) :
    result = 0
    x1,y1,x2,y2 = list(map(int,sys.stdin.readline().rstrip("\n").split()))
    result = dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1]
    print(result)