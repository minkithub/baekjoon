num_list = []

while len(num_list) < 9:
    num = int(input())
    num_list.append(int(num))
    
max_num = max(num_list)
print(max_num)
print(num_list.index(max_num) + 1)