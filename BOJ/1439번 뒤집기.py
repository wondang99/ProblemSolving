import sys

S = list(sys.stdin.readline().rstrip("\n"))
start = S[0]
differ = 0
count = 0

for s in S:
    if s != start and differ == 0:
        differ = 1
    elif s!=start and differ == 1 :
        continue
    elif s==start and differ == 1 :
        differ = 0
        count+=1
if differ==1 :
    count+=1
print(count)