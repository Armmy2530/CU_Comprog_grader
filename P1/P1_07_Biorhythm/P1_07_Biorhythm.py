import math

bd, bm, by, d, m, y = [int(e) for e in input().split()]

def day_of_year(d, m, y):
    # d, m, y เป็นจ ำนวนเต็มเก็บเลขวัน เลขเดือน และเลขปี พ.ศ. ตำมล ำดับ
    # คืน เลขวันที่ของปี ของวันเดือนปีที่ได้รับ
    if(m > 11):
        d = d - 4
    elif(m > 9):
        d = d - 3
    elif(m > 6):
        d = d - 2
    elif(m > 4):
        d = d - 1
        
    y = y - 543
    leap_year = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    return (d + ((m-1) * 31) + ((-2 if leap_year else -3) if m > 2 else 0 ))

def leap_year(y):
    y = y - 543
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

n_day = ((366 if leap_year(by) else 365) - day_of_year(bd, bm, by)) + (y - by - 1) * 365 + day_of_year(d, m, y)
print(f"{n_day} {math.sin((2 * math.pi * n_day)/(23)):.2f} {math.sin((2 * math.pi * n_day)/(28)):.2f} {math.sin((2 * math.pi * n_day)/(33)):.2f}")