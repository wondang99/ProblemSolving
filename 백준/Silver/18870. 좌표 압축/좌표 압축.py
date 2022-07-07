import sys

N = int(sys.stdin.readline().rstrip("\n"))

xList = list(map(int,sys.stdin.readline().rstrip("\n").split()))

xList = [i for i in enumerate(xList)]
xList.sort( key = lambda x: (x[1]))
result = [0 for _ in range(N)]
continuity = 0
count = 0
for i in range(1,N) :
    if xList[i-1][1]==xList[i][1] :
        continuity+=1
        if i==(N-1) :
            for j in range(1,continuity+1) :
                result[xList[i-j][0]]=count
            result[xList[i][0]]=count
    else :
        for j in range(1,continuity+1) :
            result[xList[i-j][0]]=count
        count+=1
        continuity = 0
        result[xList[i][0]]=count
print(*result)