import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    n = int(sys.stdin.readline())
    sticker = [ list(map(int,sys.stdin.readline().rstrip("\n").split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0], dp[1][0] = sticker[0][0],sticker[1][0]
    result = 0
    for i in range(1,n) :
        dp[0][i] = max(dp[0][i-1], dp[1][i-1]+sticker[0][i])
        dp[1][i] = max(dp[1][i-1], dp[0][i-1]+sticker[1][i])
    print(max(max(dp[0]),max(dp[1])))