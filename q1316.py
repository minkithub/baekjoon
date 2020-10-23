num = int(input())
count = 0
isGroup = num

while count < num:
    seq_str = input()
    len_seq_str = len(seq_str)

    if len_seq_str > 1:
        for i in range(len_seq_str-1):
            if seq_str[i] != seq_str[i+1]:
                finish_ward = seq_str[i]
                if finish_ward in seq_str[i+1:]:
                    isGroup -= 1
                    break
                    
    count += 1

print(isGroup)