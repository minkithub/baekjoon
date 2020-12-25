a, b, c = map(int, input().split())

while a*b*c != 0:

    _list = [a, b, c]

    if a == max(_list):
        if a**2 == b**2 + c**2:
            print("right")
        else:
            print("wrong")
    elif b == max(_list):
        if b**2 == a**2 + c**2:
            print("right")
        else:
            print("wrong")
    else:
        if c**2 == a**2 + b**2:
            print("right")
        else:
            print("wrong")
    
    a, b, c = map(int, input().split())
