from math import sqrt

_try = int(input())
loop = 0

while loop < _try:
    x, y = map(int, input().split())
    dif = y-x

    N = int(sqrt(dif))

    if N==1:
        print(dif)
    else:
        if dif>N*(N+1):
            print(2*N+1)
        elif dif>N*N:
            print(2*N)
        else:
            print(2*N-1)
    
    loop += 1