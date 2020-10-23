a, b = map(int, input().split())

def reverse_str(ward):
    blank = ''
    str_ward = str(ward)
    len_ward = len(str_ward)
    for i in range(len_ward):
        blank = blank + str_ward[len_ward - i - 1]

    return int(blank)

reverse_a = reverse_str(a)
reverse_b = reverse_str(b)

if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)