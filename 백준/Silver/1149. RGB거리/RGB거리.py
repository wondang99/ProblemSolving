import sys

N = int(sys.stdin.readline())

RGB = [ list(map(int,sys.stdin.readline().rstrip("\n").split())) for _ in range(N)]

dp_R= [0 for _ in range(N)]
dp_G= [0 for _ in range(N)]
dp_B= [0 for _ in range(N)]
dp_R[0], dp_G[0], dp_B[0] = RGB[0][0],RGB[0][1],RGB[0][2]

for i in range(1,N) :
    dp_R[i] = min(dp_G[i-1],dp_B[i-1])+RGB[i][0]
    dp_G[i] = min(dp_R[i-1],dp_B[i-1])+RGB[i][1]
    dp_B[i] = min(dp_R[i-1],dp_G[i-1])+RGB[i][2]
print(min(dp_R[N-1],dp_G[N-1],dp_B[N-1]))