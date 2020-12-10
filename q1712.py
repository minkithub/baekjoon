A, B, C = map(int, input().split())

profit = C - B

if profit <= 0:
    print(-1)
else:
    bp = A//profit + 1
    print(bp)