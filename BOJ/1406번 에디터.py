import sys
from collections import deque

front, back =list(sys.stdin.readline().rstrip("\n")),[]
M = int(sys.stdin.readline().rstrip("\n"))
for _ in range(M) :
    command = list(sys.stdin.readline().rstrip("\n").split())
    if command[0] == "L" and front:
            back.append(front.pop())
    elif command[0] == "D" and back:
            front.append(back.pop())
    elif command[0] == "B" and front:
        front.pop()
    elif command[0] == "P" :
        front.append(command[1])
#O(N)에서 어떻게 더 줄일 수 있을까
#처음에는 너무 쉽게 생각. 실제로는 링크드 리스트. 두 개의 리스트 이용
print("".join(front+back[::-1]))
    