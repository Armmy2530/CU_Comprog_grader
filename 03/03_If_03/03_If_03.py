score = [float(x) for x in input().split()]

min_score = score[0]
max_score = score[0]
sum_score = 0
for i in score:
    if(i < min_score):
        min_score = i
    if(i > max_score):
        max_score = i
    sum_score += i

sum_score = sum_score - min_score - max_score
avg_score = round(sum_score / 2 , 2)

print(avg_score)