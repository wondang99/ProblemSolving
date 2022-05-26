import sys

S = int(sys.stdin.readline())
x = 1
while 2*S >= x*(x+1) :
    x+=1
print(x-1)
