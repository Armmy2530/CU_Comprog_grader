def gradeCharToInt(grade):
    if(grade == "A"):
        return 4
    elif(grade == "B"):
        return 3
    elif(grade == "C"):
        return 2
    elif(grade == "D"):
        return 1
    elif(grade == "F"):
        return 0

id_1, gpa_1, comprog_1, cal1_1, cal2_1 = input().split()
id_2, gpa_2, comprog_2, cal1_2, cal2_2 = input().split()

gpa_1, gpa_2 = float(gpa_1), float(gpa_2)
comprog_1, comprog_2 = gradeCharToInt(comprog_1), gradeCharToInt(comprog_2)
cal1_1, cal1_2 = gradeCharToInt(cal1_1), gradeCharToInt(cal1_2) 
cal2_1, cal2_2 = gradeCharToInt(cal2_1), gradeCharToInt(cal2_2) 

p1_minReq = True if(comprog_1 == 4 and cal1_1 >= 2 and cal2_1 >= 2) else False
p2_minReq = True if(comprog_2 == 4 and cal1_2 >= 2 and cal2_2 >= 2) else False

if(p1_minReq or p2_minReq):
    if(p1_minReq and p2_minReq):
        if(gpa_1 == gpa_2):
            if(cal1_1 == cal1_2):
                if(cal2_2 == cal2_1):
                    print("Both")
                else:
                    if(cal2_1 > cal2_2):
                        print(id_1)
                    else:
                        print(id_2)
            else:
                if(cal1_1 > cal1_2):
                    print(id_1)
                else:
                    print(id_2)
        else:
            if(gpa_1 > gpa_2):
                print(id_1)
            else:
                print(id_2)
    elif(p1_minReq):
        print(id_1)
    else:
        print(id_2)
else:
    print("None")