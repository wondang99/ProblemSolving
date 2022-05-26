import sys

N, M = list(map(int,sys.stdin.readline().rstrip("\n").split()))
listen = set()
dtbo = set()

for n in range(N+M) :
    name = sys.stdin.readline().rstrip("\n")
    dtbo.add(name) if name in listen else listen.add(name)
print(len(dtbo))
for name in sorted(list(dtbo)) :
    print(name)