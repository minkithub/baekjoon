first_num = input()
final_num = first_num
count = 0

while(True):
    if len(first_num) != 2:
        first_num = str('0') + first_num
        final_num = first_num
    
    sub1 = int(first_num[0])
    sub2 = int(first_num[1])
    sub_res = str(sub1 + sub2)
    first_num = str(sub2) + str(sub_res[-1])

    if final_num == first_num:
        count += 1
        break
    else:
        count += 1

print(count)
