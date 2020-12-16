_try = int(input())
roop = 0

while roop < _try:
    H, W, N = map(int, input().split())

    if H*W != N:
        Y = N//H + 1
        X = N%H

        if X == 0:
            X = H
            Y = Y-1

        if len(str(Y)) == 1:
            res = str(X) + '0' + str(Y)
            print(res)
        else:
            res = str(X) + str(Y)
            print(res)
    
    else:
        if len(str(W)) == 1:
            res = str(H) + '0' + str(W)
            print(res)
        else:
            res = str(H) + str(W)
            print(res)
    
    roop += 1