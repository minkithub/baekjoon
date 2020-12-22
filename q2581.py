M = int(input())
N = int(input())

_list = list(range(M, N+1))

for i in range(M, N+1):
    for j in range(2, i):
        if i%j==0:
            _list.remove(i)
            break

if 1 in _list:
    _list.remove(1)

if len(_list)!=0:
    print(sum(_list))
    print(min(_list))
else:
    print(-1)