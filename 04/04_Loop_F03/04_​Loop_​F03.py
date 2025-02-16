def grade_mcq(sol, ans):
    score = 0
    if(len(sol) == len(ans)):
        for i , data in enumerate(sol):
            score += 1 if data == ans[i] else 0
        return score
    else:
        return -1        
exec(input())
