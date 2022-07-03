import sys

N = int(sys.stdin.readline())

board = [list(map(int,sys.stdin.readline().rstrip("\n").split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
 

def searchPath(y,x) :
    if N<=y or N<=x :
        return 0
    
    n = board[y][x]
    if y==N-1 and x==N-1:
        return 1
    if n==0 :
        return 0
    if dp[y][x]!=0 :
        return dp[y][x]
    dp[y][x] = searchPath(y+n,x)+searchPath(y,x+n)
    
    return dp[y][x]
print(searchPath(0,0))