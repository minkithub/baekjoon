x, y, w, h = map(int, input().split())

_list = [x, y, h-y, w-x]

print(min(_list))