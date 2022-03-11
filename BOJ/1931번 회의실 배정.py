import sys

N = int(sys.stdin.readline())
conference = [tuple(map(int,sys.stdin.readline().rstrip("\n").split())) for _ in range(N)]
conference.sort(key = lambda x : (x[1],x[0]))
end = conference[0][1]
count=1

for c in range(1,N) :
    if end <= conference[c][0] :
        count+=1
        end = conference[c][1]
print(count)