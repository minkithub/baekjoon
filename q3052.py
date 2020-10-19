count = 0
empty = []

while count < 10:
    num = int(input())
    sub = num%42
    empty.append(sub)
    count += 1

final_list = []

for i in empty:
    if i not in final_list:
        final_list.append(i)
    else:
        pass

print(len(final_list))


