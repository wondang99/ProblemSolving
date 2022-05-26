import sys

n = int(sys.stdin.readline().rstrip("\n"))

wine = [int(sys.stdin.readline().rstrip("\n")) for _ in range(n)]+[0,0]
dp = [ 0 for _ in range(n)]+[0,0]
dp[0], dp[1] = wine[0], wine[0]+wine[1]
dp[2] = max(wine[2]+wine[1],wine[2]+dp[0],dp[1])

for w in range(3,len(wine)):
    dp[w] = max( wine[w]+wine[w-1]+dp[w-3],wine[w]+dp[w-2],dp[w-1] )
print(max(dp))