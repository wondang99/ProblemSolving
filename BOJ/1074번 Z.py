import sys

N,r,c = list(map(int,sys.stdin.readline().rstrip("\n").split()))
z_direction = [[0,0],[0,1],[1,0],[1,1]]

def z(k,y,x,num) :
    n=2**k
    count = num
    if k==1 :
        for ny,nx in z_direction :
            if y+ny == r and x+nx == c :
                count+=1
                return count
            count+=1
    #y,x의 사분면 판별
    if y<=r<y+n//2 and x+n//2<=c<x+n :
        count=z(k-1,y,x+n//2,num+n*n//4)
    elif y<=r<y++n//2 and x<=c<x++n//2 :
        count=z(k-1,y,x,num)
    elif y+n//2<=r<y+n and x<=c<x+n//2 :
        count=z(k-1,y+n//2,x,num+2*n*n//4)
    elif y+n//2<=r<y+n and x+n//2<=c<x+n :
        count=z(k-1,y+n//2,x+n//2,num+3*n*n//4)
    return count
    
print(z(N,0,0,0)-1)