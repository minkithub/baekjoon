num = int(input())

num2 = list(input())

if len(num2) == num:
    sum_num2 = sum(list(map(lambda x: int(x), num2)))
    print(sum_num2)