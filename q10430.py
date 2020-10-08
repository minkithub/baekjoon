up_number = input()
down_number = input()

final_number = 0
sub_number = 0

for i in range(3):
    sub_number1 = int(down_number[2-i])
    for j in range(3):
        sub_number2 = int(up_number[2-j])
        sub_number = sub_number + (sub_number1*sub_number2)*(10**(i + j))
    print(int(sub_number/(10**i)))
    final_number = final_number + sub_number
    sub_number = 0
print(final_number)

