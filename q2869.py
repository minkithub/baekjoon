A, B, V = map(int, input().split())

up = A-B

day = (V-A)//up

if (V-A)%up == 0:
    print(day + 1)
else:
    print(day + 2)