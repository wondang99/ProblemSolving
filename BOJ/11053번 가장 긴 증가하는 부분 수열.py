import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().rstrip("\n").split()))

dp = [1]+[0 for _ in range(N)]

for n in range(1,N) :
    
    for j in range(n) :
        if A[j] < A[n] and dp[j] >= dp[n] :
            dp[n] = dp[j]
    dp[n]+=1
print(max(dp))