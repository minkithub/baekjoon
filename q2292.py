N = int(input())

if N==1:
    print(1)
else:
    count = 1
    start = 2
    while start <= N:
        start = start + 6*(count-1)
        if start > N:
            break
        else:
            count += 1
    print(count)
