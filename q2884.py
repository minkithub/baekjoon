h, m = map(int, input().split())

if h >= 0 and m - 45 >= 0 :
    print(f'{h} {m-45}')
elif h > 0 and m - 45 < 0 :
    print(f'{h-1} {15+m}')
elif h == 0 and m-45 < 0 :
    print(f'23 {15 + m}')