import sys

N = int(sys.stdin.readline().rstrip("\n"))
counsel = [list(map(int,sys.stdin.readline().rstrip("\n").split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1,-1,-1) :
    if counsel[i][0]+i <=N :
        dp[i] = counsel[i][1]
    for j in range(N-1,i,-1) :
        if counsel[i][0]+i<=j :
            dp[i] =max(dp[i],counsel[i][1]+dp[j])
        else :
            dp[i] =max(dp[i],dp[j])
print(dp[0])
#역순으로 생각.