N = int(input())
_list = list(map(int, input().split()))

count = 0
divide_list = [2, 3, 5, 7]
sub = []

for i in divide_list:
    sub.append(1)

for i in divide_list:
    res = list(map(lambda x: x%i, _list))
    for k in range(len(res)):
        q = sub[k]*res[k]
        sub[k] = q

j = len(sub) - sub.count(0)
    
for i in divide_list:
    if i in _list:
        count += 1

if 1 in _list:
    count -= 1

print(count + j)
