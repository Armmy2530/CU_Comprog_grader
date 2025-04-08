answer = input()
student= input()
score = 0

if(len(answer) == len(student)):
    for i , data in enumerate(answer):
        score += 1 if data == student[i] else 0
    print(score)
else:
    print("Incomplete answer")
