import sys

N = int(sys.stdin.readline().rstrip("\n"))
card = [0]+list(map(int,sys.stdin.readline().rstrip("\n").split()))
dp = [0 for _ in range(N+1)]

for i in range(1,N+1) :
    dp[i] = max(dp[j]+card[i-j] for j in range(0,i+1))
print(max(dp))