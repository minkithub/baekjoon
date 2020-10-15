n, x = map(int, input().split())
n_list = list(map(int, input().split()))

empty = ''

for i in n_list:
    if (i < x):
        empty = empty + ' ' + str(i)
    else:
        pass

print(empty[1:])
