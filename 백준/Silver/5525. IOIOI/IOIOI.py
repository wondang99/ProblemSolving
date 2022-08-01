import sys

N = int(sys.stdin.readline().rstrip("\n"))
M = int(sys.stdin.readline().rstrip("\n"))
S = sys.stdin.readline().rstrip("\n")

continuity = 0
result = []
count=0

for m in range(M-1) :
    if continuity!=0 and (S[m]!=S[m+1]) :
        continuity+=1
    elif continuity!=0 and (S[m]==S[m+1]) :
        if continuity > 1 :
            result.append(continuity//2)
        continuity=0
    elif continuity==0 and (S[m]!=S[m+1]):
        if S[m]=="I" :
            continuity+=1
if continuity>1 :
    result.append(continuity//2)
for n in result :
    if n >= N :
        count+=(n-N+1)
print(count)