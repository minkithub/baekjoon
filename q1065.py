natural = input()

def true_han(num):
    if num >= 10:
        num = str(num)
        list_num = list(map(lambda x: int(x), list(num)))
        dif_list = []
        for i in range(1, len(num)):
            dif = list_num[i] - list_num[i-1]
            dif_list.append(dif)
        return len(set(dif_list))
    else:
        return 1

count = 0
for i in range(1, int(natural) + 1):
    res = true_han(i)
    if res == 1:
        count += 1

print(count)
