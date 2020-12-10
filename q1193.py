X = int(input())

count = 1
hap = 1

if X!=1:
    while hap < X :
        hap = count/2*(count + 1)
        count += 1
        if hap >= X:
            break

    dif = hap - X
    mo = (count-1)-dif
    ja = (1) + dif

    if count%2 == 0:
        print(f'{int(ja)}/{int(mo)}')
    else:
        print(f'{int(mo)}/{int(ja)}')
else:
    print('1/1')
