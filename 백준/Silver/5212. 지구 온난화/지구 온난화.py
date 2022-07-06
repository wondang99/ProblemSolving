import sys

R, C = list(map(int,sys.stdin.readline().rstrip("\n").split()))

dadohae = [list(sys.stdin.readline().rstrip("\n")) for _ in range(R)]
future = [dadohae[i][:] for i in range(R)]
directions = [[-1,0],[0,1],[1,0],[0,-1]]

# 한 줄 입력시 예외
def disappear() :
    for i in range(R) :
        for j in range(C) :
            count = 0
            if dadohae[i][j] == "." :
                continue
            for d in directions:
                if i+d[0]<0 or i+d[0]>R-1 or j+d[1]<0 or j+d[1]>C-1 or \
                dadohae[i+d[0]][j+d[1]]==".":
                    count+=1
            if count==3 or count==4 :
                future[i][j] = "."
def futureMap() :
    minHeight,minWidth = 11, 11
    maxHeight,maxWidth = 0,0
    for i in range(R) :
        for j in range(C) :
            if future[i][j] == "X" :
                if i< minHeight :
                    minHeight = i
                if maxHeight < i :
                    maxHeight = i
                if j< minWidth :
                    minWidth = j
                if maxWidth < j :
                    maxWidth = j
    return minHeight, minWidth, maxHeight, maxWidth
disappear()
sH,sW,fH,fW=futureMap()
for n in range(sH,fH+1) :
    print("".join(future[n][sW:fW+1]))
