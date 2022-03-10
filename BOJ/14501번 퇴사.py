import sys

N = int(sys.stdin.readline().rstrip("\n"))
counsel = [list(map(int,sys.stdin.readline().rstrip("\n").split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N) :
    
    for j in range(i) :
        if i-j >= counsel[j][0] :
            dp[i] =dp[j] if dp[i]<dp[j] else dp[i]
    if counsel[i][0]+i <=N :
        dp[i]+=counsel[i][1]
print(max(dp))
# DP, 브루트포스