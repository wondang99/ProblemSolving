import sys
from collections import deque
A, B = list(map(int,sys.stdin.readline().rstrip("\n").split()))
count=0
visited = set()
A_ = deque([A])

while A_ :
    for i in range(len(A_)) :
        num = A_.popleft()
        if B < num :
            continue
        elif num==B :
            print(count+1)
            sys.exit(0)
        if not (num in visited) :
            visited.add(num)
            A_.append(num*2)
            A_.append(num*10+1)
    count+=1
    
print(-1)    