import sys

T = int(sys.stdin.readline())

case = [int(sys.stdin.readline()) for _ in range(T)]
dp = [ 0 for _ in range(1000001)]
m = 4
for t in range(T) :
    if case[t]==1 or case[t]==2 or case[t]==3:
        if case[t]==3 :
            print(4)
        else :
            print(case[t])
        continue
    if dp[case[t]]!=0 :
        print(dp[case[t]])
        continue
    dp[1], dp[2], dp[3] = 1,2,4
    for i in range(m,case[t]+1) :
        dp[i]= (dp[i-1]+dp[i-2]+dp[i-3])%1000000009
    if m<case[t] :
        m = case[t]
    print(dp[case[t]])