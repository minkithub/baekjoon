num = int(input())
count = 0

while count < num:
    answer = input()

    score_list = []
    total_score = 0

    for i in answer:
        if i == 'O':
            score_list.append(i)
            sub_score = len(score_list)
            total_score = total_score + sub_score
        else:
            sub_score = 0
            score_list = []
            pass

    print(total_score)

    count += 1