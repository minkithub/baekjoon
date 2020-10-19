# M : max
# /M *100

num = int(input())
sub_score = list(map(int, input().split()))
max_score = max(sub_score)
new_score = list(map(lambda x: x/max_score*100, sub_score))
print(sum(new_score)/num)