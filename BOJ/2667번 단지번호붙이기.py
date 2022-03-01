import sys

N = int(sys.stdin.readline().rstrip("\n"))

apartment = [[0]+list(map(int,sys.stdin.readline().rstrip("\n")))+[0] for _ in range(N)]
apartment = [[0 for _ in range(N+2)]]+apartment+[[0 for _ in range(N+2)]]
dic= [[-1,0],[0,1],[1,0],[0,-1]]
dong=[]
def dfs(x,y,result) :
    apartment[x][y]=0
    for d in dic :
        if apartment[x+d[0]][y+d[1]]==1 :
            apartment[x+d[0]][y+d[1]]=0
            result=dfs(x+d[0],y+d[1],result)
    return result+1
for x in range(1,N+1) :
    for y in range(1,N+1) :
        if apartment[x][y]!=0 :
            dong.append(dfs(x,y,0))
print(len(dong))
for num in sorted(dong) :
    print(num)