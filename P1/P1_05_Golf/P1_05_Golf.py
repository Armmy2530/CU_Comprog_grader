sum_par, sum_stork = 0, 0
sum_optimize_stork = 0
for i in range(9):
    par, stork, select = [int(x) for x in input().split()]
    sum_par += par
    sum_stork += stork
    if select:
        sum_optimize_stork += stork if stork < par+2 else par+2
score_plus = 0.8*(1.5*sum_optimize_stork - sum_par)
score_plus = int(score_plus) - (0 if score_plus >= 0 else 1)
print(sum_stork)
print(score_plus)
print(sum_stork - score_plus)