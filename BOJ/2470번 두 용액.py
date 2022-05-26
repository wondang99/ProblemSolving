import sys
def liquid() :
        N = int(sys.stdin.readline().rstrip("\n"))
        num = list(map(int,sys.stdin.readline().rstrip("\n").split()))
        num.sort()
        left ,right = 0, N-1
        result = []
        mix = float('inf') 
        if abs(num[left])==abs(num[right]) :
                return [num[left],num[right]]
        while left!=right :
                if abs(num[left]+num[right]) < mix :
                        mix = abs(num[left]+num[right])
                        result = [num[left],num[right]]
                if num[left]+num[right] > 0 :
                        right-=1
                elif num[left]+num[right] <0 :
                        left+=1
                elif num[left]+num[right]==0 or abs(num[left])==abs(num[right]) :
                        left=right
        return result
answer = liquid()
print(answer[0],answer[1])