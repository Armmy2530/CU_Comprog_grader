def gradeCharToInt(grade):
    if(grade == "A"):
        return 4
    elif(grade == "B+"):
        return 3.5
    elif(grade == "B"):
        return 3
    elif(grade == "C+"):
        return 2.5
    elif(grade == "C"):
        return 2
    elif(grade == "D+"):
        return 1.5
    elif(grade == "D"):
        return 1
    elif(grade == "F"):
        return 0


def choose(stu1, stu2):
    # stu1 และ stu2 เป็นลิสต์[ ID, GPAX, compprog, cal1, cal2 ]
    # ID เป็นสตริงเก็บเลขประจ ำตัว
    # GPAX เป็น float
    # comprog, cal1, cal2 เป็นสตริงเก็บเกรดของสำมวิชำ (เกรดเป็นแบบไม่มีประจุ A,B,C,D,F)
    # ฟังกช์ ันนี้คนื
    # - ถ้ำไม่ผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ คืนลิสต์ว่ำง
    # - ถ้ำผ่ำนเกณฑ์ข้อ 1 คนเดียว คืนลิสต์ที่เก็บเลขประจ ำตัวของคนที่ผ่ำนเกณฑ์ข้อ 1
    # - ถ้ำผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ คืนลิสต์ที่เก็บเลขประจ ำตัวของนิสติ ที่มีข้อ 2 ที่ดีกว่ำ
    # - ถ้ำผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ และมีข้อ 2 เท่ำกัน คืนลิสต์ที่เก็บเลขประจ ำตัวของนิสติ คนแรก ตำมด้วยของคนที่สอง
    id_1, gpa_1, comprog_1, cal1_1, cal2_1 = stu1
    id_2, gpa_2, comprog_2, cal1_2, cal2_2 = stu2

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
                        return [id_1,id_2]
                    else:
                        if(cal2_1 > cal2_2):
                            return [id_1]
                        else:
                            return [id_2]
                else:
                    if(cal1_1 > cal1_2):
                        return [id_1]
                    else:
                        return [id_2]
            else:
                if(gpa_1 > gpa_2):
                    return [id_1]
                else:
                    return [id_2]
        elif(p1_minReq):
            return [id_1]
        else:
            return [id_2]
    else:
        return []

exec(input()) # DON'T remove this line
