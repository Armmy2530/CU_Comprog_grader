def index_of(grades, ID):
    for i, data in enumerate(grades):
        if(data[0] == ID):
            return i
    return -1

def upgrade(grades, IDs):
    for i, data in enumerate(grades):
        if data[0] in IDs:
            if grades[i][1] == "B":
                grades[i][1] = "B+"
            elif grades[i][1] == "B+":
                grades[i][1] = "A"
            elif grades[i][1] == "C+":
                grades[i][1] = "B"
            elif grades[i][1] == "C":
                grades[i][1] = "C+"
            elif grades[i][1] == "D+":
                grades[i][1] = "C"
            elif grades[i][1] == "D":
                grades[i][1] = "D+"
            elif grades[i][1] == "F":
                grades[i][1] = "D"
    grades.sort(key=lambda x: x[0])

# DON'T remove the following three lines
exec(input())
exec(input())
exec(input())