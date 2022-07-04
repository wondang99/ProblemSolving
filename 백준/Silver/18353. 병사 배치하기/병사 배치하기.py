import sys

N = int(sys.stdin.readline())

soldiers = list(map(int,sys.stdin.readline().rstrip("\n").split()))
dp = [0 for _ in range(N)]
for i in range(N) :
    
    for j in range(i) :
        # i 병사를 추가
        if soldiers[j] > soldiers[i] :
            if dp[i] < dp[j] :
                dp[i] = dp[j]
        
        # if 15 11 12 10 , 15 13 11 10인지 15 13 12 10 인지 중요하지 않다.
        # optimal substructure. 이전 subproblem의 optimal이 현재의 optimal을 결정
    dp[i]+=1
print(N-max(dp))
    