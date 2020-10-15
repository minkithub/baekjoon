num = int(input())

for i in range(num):
    left_num = ' '*(num - i - 1)
    right_num = '*'*(i + 1)
    print(left_num + right_num)