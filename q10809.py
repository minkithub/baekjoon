letter = input()

letter_list = list(letter)
order_list = []
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letter_str = ''

for i in alpha_list:
    try:
        letter_index = letter_list.index(i)
        order_list.append(letter_index)
        letter_str = letter_str + ' ' + str(letter_index)
    except:
        order_list.append(-1)
        letter_str = letter_str + ' ' + str(-1)

print(letter_str[1:len(letter_str)])