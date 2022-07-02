import sys

N = int(sys.stdin.readline())

box = list(map(int,sys.stdin.readline().rstrip("\n").split()))

dp = [0 for _ in range(N)]

for i in range(N) :
    for j in range(i) :
        if box[j]<box[i] :
            if dp[i] < dp[j] :
                dp[i] = dp[j]
    dp[i]+=1
print(max(dp))