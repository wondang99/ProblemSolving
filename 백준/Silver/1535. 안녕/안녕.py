import sys

N = int(sys.stdin.readline())

loss = list(map(int,sys.stdin.readline().rstrip("\n").split()))
happy = list(map(int,sys.stdin.readline().rstrip("\n").split()))

dp = [[0 for _ in range(100)] for _ in range(N)]
for n in range(N) :
    if n== 0:
        dp[n][loss[n]:]= [happy[n] for _ in range(100-loss[n])]
        continue
    for l in range(100) :
        if l < loss[n] :
            dp[n][l] = dp[n-1][l]
            continue
        else :
            dp[n][l] = max(dp[n-1][l-loss[n]]+happy[n],dp[n-1][l])

print(max(dp[N-1]))