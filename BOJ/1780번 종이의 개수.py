import sys

N = int(sys.stdin.readline())

paper = [list(map(int,sys.stdin.readline().rstrip("\n").split())) for _ in range(N)]
num = {-1:0,0:0,1:0}

def dq (n,y,x) :
    
    count=0
    if n==1:
        num[paper[y][x]]+=1
        return
    
    for j in range(y,y+n) :
        if len(set(paper[j][x:x+n]))!=1 or (j!=y+n-1 and paper[j][x]!=paper[j+1][x]):
            for n_y in range(0,n,n//3) :
                for n_x in range(0,n,n//3) :
                    dq(n//3,y+n_y,x+n_x)
                    count=1
            return
    if not count:
        num[paper[y][x]]+=1
        
dq(N,0,0)
for result in num :
    print(num[result])