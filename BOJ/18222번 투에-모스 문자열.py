import sys

k = int(sys.stdin.readline())
count,sign  = 0, 0
x =1
reverse_n = {1:2,2:1}

while x<k :
    count+=1
    x=x*2
cou = count
for c in range(count-1) :
    if x//2<k :
        if cou%2 != 0 :
            sign+=1
        k = x-k+1
    cou-=1  
    x = x//2
if sign%2 != 0 :
    k=reverse_n[k]
print(k-1)