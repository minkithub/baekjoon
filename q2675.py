num = int(input())
count = 0

while count < num:
    p, q = input().split()

    final_str = ''

    for j in q:
        sub_str = j*int(p)
        final_str = final_str + sub_str

    print(final_str)

    count += 1