import sys
import heapq

N = int(sys.stdin.readline().rstrip("\n"))
heap = []

for n in range(N) :
    x = int(sys.stdin.readline().rstrip("\n"))
    if x==0 :
        if not heap :
            print(0)
            continue
        print(heapq.heappop(heap)[1])
    else :
        heapq.heappush(heap,(abs(x),x))