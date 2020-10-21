# 수열을 만드는 함수
def self_sum(num):
    str_num = str(num)
    list_num = list(str_num)

    list_int_num = sum(list(map(lambda x: int(x), list_num)))

    num = num + list_int_num
    return num

list_self_num = set(range(1, 10001))
not_self_num = set()

for i in range(1, 10001):
    num = self_sum(i)
    not_self_num.add(num)

self_num_set = list_self_num - not_self_num
self_num_set =sorted(self_num_set)

for i in self_num_set:
    print(i)

