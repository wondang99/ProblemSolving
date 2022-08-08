import sys
from collections import deque

T = int(sys.stdin.readline().rstrip("\n"))

def AC(function,n) :
    global nums #함수 내부 변경을 통해 밖에서도 변경 적용
    reverse=1
    for f in function :
        if f == "R":
            reverse = 1 if reverse==-1 else -1
            continue
        elif f == "D" :
            if not nums:
                return False
            if reverse==1 :
                nums.popleft()
            else: #reverse==-1
                nums.pop()
    if reverse==-1:
        nums=list(nums)[::-1]
    return True
for _ in range(T) :
    function = sys.stdin.readline().rstrip("\n")
    n = int(sys.stdin.readline().rstrip("\n"))
    nums = deque(sys.stdin.readline().rstrip("\n")[1:-1].split(","))
    if n==0 :
        nums=deque([])
    if AC(function,n) :
        print("["+",".join(list(nums))+"]")
    else :
        print("error")