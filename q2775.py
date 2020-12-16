_try = int(input())
loop = 0

while loop < _try:
    k = int(input())
    n = int(input())

    _list = list(range(1, n+1)) #0층
    empty = []

    for i in range(k):
        for j in range(n):
            empty.append(sum(_list[:j+1]))
        _list = empty[i*n : (i+1)*n]

    print(_list[-1])
    loop += 1

