import sys

T = int(sys.stdin.readline().rstrip("\n"))

for _ in range(T) :
    N = int(sys.stdin.readline().rstrip("\n"))
    dp = [(1,0),(0,1)]
    for n in range(2,N+1) :
        dp.append((dp[n-1][0]+dp[n-2][0],dp[n-1][1]+dp[n-2][1]))
    print(*dp[N])