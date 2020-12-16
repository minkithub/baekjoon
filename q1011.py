_try = int(input())
loop = 0

while loop < _try:
    x, y = map(int, input().split())
    # 최초 앞뒤로 한칸씩 이동
    start = x+1
    final = y-1

    count = 2

    move_list = [0, 1, 2]
    desty_list = list(map(lambda x: x+start, move_list))

    if x-y == 1:
        print(1)
    elif x-y == 2:
        print(2)
    else:
        if final in desty_list:
            print(3)
        else:
            count = 3
            while final not in desty_list:
                k = max(desty_list) - start
                start = start + k
                move_list = [k-1, k, k+1]
                desty_list = list(map(lambda x: x+start, move_list))
    
                if min(desty_list) >= final:
                    count+=1
                    break
                else:
                    count+=1
            
            print(count)

    loop += 1