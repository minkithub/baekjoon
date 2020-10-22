letter = input()
letter = letter.upper()

letter_all_list = list(letter)
letter_list = list(set(letter_all_list))

count = 0
letter_dict = {}

for i in letter_list:
    for j in letter_all_list:
        if i == j:
            count += 1
    
    letter_dict[i] = count
    count = 0

max_num = max(letter_dict.values())

res_list = [k for k, v in letter_dict.items() if v == max_num]

if len(res_list) > 1:
    print('?')
else:
    print(res_list[0])
