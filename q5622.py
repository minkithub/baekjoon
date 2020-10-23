number = input()
alpha_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

all_time = 0

for i in number.upper():
    for j in alpha_list:
        if i in j:
            sub_time = alpha_list.index(j) + 3
            all_time = all_time + sub_time

print(all_time)
