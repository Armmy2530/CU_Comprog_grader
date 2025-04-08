def is_mobile_number(phonenum):
    # number เป็นสตริงเก็บหมายเลข (ภายในสตริงมีแต่ตัวเลขแน่ ๆ)
    # คืน True ถ้า number เป็นหมายเลขโทรศัพท์ถา้ไม่เป็น คืน False
    return True if(len(phonenum) == 10 and phonenum[0:2] in ["06","08","09"]) else False

exec(input()) # DON'T remove this line