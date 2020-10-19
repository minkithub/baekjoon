count = 0
sub = 1

while count < 3:
    num = int(input())
    sub = sub * num
    count += 1

for i in range(0, 10):
    same = 0
    for j in range(len(str(sub))):
        if (i == int(str(sub)[j])):
            same += 1
    print(same)
