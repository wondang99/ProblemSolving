import sys

N= int(sys.stdin.readline())

QT = [list(sys.stdin.readline().rstrip("\n")) for _ in range(N)]

def divide(n,y,x) :
    f = QT[y][x] 
    flag = 0
    # 다른 게 존재한다면 divide
    for i in range(n) :
        for j in range(n) :
            if flag :
                return f
            if QT[y+i][x+j]!=f :
                if n==2 :
                    return "("+QT[y][x]+QT[y][x+1]+QT[y+1][x]+QT[y+1][x+1]+")"
                f = divide(n//2,y,x)
                f+=divide(n//2,y,x+n//2)
                f+=divide(n//2,y+n//2,x)
                f+=divide(n//2,y+n//2,x+n//2)
                f="("+f+")"
                flag = 1
    # 통과했다는 건 모두 같다는 것 이거나 divide가 모두 조사됐을 때
    # flag 하지 않는다면 찾고 난 뒤에도 무의미하게 반복문을 계속한다.
    #분할을 하지 않는 경우에는 괄호를 사용하지 않음
    return f
print(divide(N,0,0))