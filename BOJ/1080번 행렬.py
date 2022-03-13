import sys

N, M = list(map(int,sys.stdin.readline().split()))
A , B = [list(map(int,sys.stdin.readline().rstrip("\n"))) for _ in range(N)],[list(map(int,sys.stdin.readline().rstrip("\n"))) for _ in range(N)]
count = [[0 for _ in range(M)] for _ in range(N)]
result = 0

for x in range(M-2) :
    for y in range(N-2) :
        if (count[y][x]%2 == 0 and A[y][x]!=B[y][x]) or (count[y][x]%2!=0 and A[y][x]==B[y][x]) :
            result+=1
            for x_p in range(x,x+3) :
                for y_p in range(y,y+3) :
                     count[y_p][x_p]+=1

for x in range(M) :
    for y in range(N) :
        if (count[y][x]%2 == 0 and A[y][x]!=B[y][x]) or (count[y][x]%2!=0 and A[y][x]==B[y][x]) :
            result = -1
            break
    if result==-1 : break
print(result)
            