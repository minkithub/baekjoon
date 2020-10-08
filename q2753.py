# 윤년이면 1, 아니면 0
# 윤년은 연도가 4의 배수 & !100의 배수 or 400의 배수

year = int(input())

if year%4 == 0 and year%400 == 0:
    print(1)
elif year%4 == 0 and year%100 != 0:
    print(1)
else:
    print(0)