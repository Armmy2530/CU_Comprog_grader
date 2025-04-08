students_data = []
while True:
    user = input()
    if(user == "q"):
        break
    id, grade = user.split()
    students_data.append([id,grade])

upgrade_id = input().split()

for i in range(len(students_data)):
    if students_data[i][0] in upgrade_id:
        if students_data[i][1] == "B":
            students_data[i][1] = "B+"
        elif students_data[i][1] == "B+":
            students_data[i][1] = "A"
        elif students_data[i][1] == "C+":
            students_data[i][1] = "B"
        elif students_data[i][1] == "C":
            students_data[i][1] = "C+"
        elif students_data[i][1] == "D+":
            students_data[i][1] = "C"
        elif students_data[i][1] == "D":
            students_data[i][1] = "D+"
        elif students_data[i][1] == "F":
            students_data[i][1] = "D"
    print(students_data[i][0],students_data[i][1])