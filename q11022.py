num = int(input())

for i in range(num):
    p, q = map(int, input().split())
    print(f'Case #{i+1}: {p} + {q} = {p+q}')