import sys

N = int(sys.stdin.readline().rstrip("\n"))

line = list(map(int,sys.stdin.readline().rstrip("\n").split()))
dp = [0 for _ in range(N)]

for i in range(N) :
    for j in range(i) :
        if (line[j] < line[i]) and (dp[i]<dp[j]):
            #뒤의 조건이 없으면 무시돼버리는 경우가 생길 수 있음
            dp[i]=dp[j]
    dp[i]+=1
            
print(max(dp))