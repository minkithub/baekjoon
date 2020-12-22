def _sosuList(n):
    _sosu = [False, False] + [True]*9998
    for i in range(2, int(n**0.5)+1):
        if _sosu[i] == True:
            for j in range(i+i, n, i):
                _sosu[j] = False
    
    return [n-i for i in range(2, n) if _sosu[i] == True and _sosu[n-i] == True]

T = int(input())

for _ in range(T):
    n = int(input())
    _list = _sosuList(n)
    _half = int(len(_list)/2)

    if len(_list)%2 == 0:
        print(f'{_list[_half]} {_list[_half-1]}')
    else:
        print(f'{_list[_half]} {_list[_half]}')