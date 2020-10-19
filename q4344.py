num = int(input())
count = 0

while count < num:
    all_list = list(map(int, input().split()))

    student_num = all_list[0]
    sub_score = all_list[1:]

    # 학생들의 평균
    avg_score = sum(sub_score)/student_num

    # 평균을 넘는 학생 filtering
    upper_student = list(filter(lambda x: x > avg_score, sub_score))
    
    # 평균을 넘는 학생 비율
    ratio_student = round(len(upper_student)/student_num * 100, 3)

    print(str('%0.3f' % ratio_student) + '%')

    count += 1