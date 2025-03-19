filename = "2110100.txt"
# filename = input().strip()
aj_id = input().strip()

file = open(filename)

student=[]
for i in file:
    i = i.strip()
    student.append(i.split(','))

sections = []
female = 0
male = 0
for i in student:
    if i[4] == aj_id:
        if(i[3] not in sections):
            sections.append(i[3])
