import sys

n = int(sys.stdin.readline().rstrip("\n"))
tile = [ 1 for _ in range(n+1)]
tile[1] = 2

for i in range(2,n) :
    tile[i] = (tile[i-1]+tile[i-2])%10007
print(tile[n-1])