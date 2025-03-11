def is_odd(n):
# คืน (True/False) ว่า n เป็นจานวนคี่หรือไม่
    return n%2 == 1
def has_odds(x):
    for i in x:
        if(i%2 == 1):
            return True
    return False
# คืน (True/False) ว่า x เป็นลิสต์ที่มีข้อมูลบางตัวเป็นจานวนคี่
def all_odds(x):
    for i in x:
        if(i%2 == 0):
            return False
    return True
# คืน (True/False) ว่า x เป็นลิสต์ที่มีข้อมูลทุกตัวเป็นจานวนคี่
def no_odds(x):
    for i in x:
        if(i%2 == 1):
            return False
    return True
# คืน (True/False) ว่า x เป็นลิสต์ที่มีไม่มีข้อมูลที่เป็นจานวนคี่เลย
def get_odds(x):
    ans = []
    for i in x:
        if(i % 2 == 1): ans.append(i)
    return ans
# คืนลิสต์ที่มีจานวนคี่ที่มีเก็บในลิสต์ x (ลาดับก่อนหลังให้เป็นไปตามลาดับเดียวกับใน x)
# เช่น x = [1,2,3,5,0] จะได้ผลคือ [1,3,5]
def zip_odds(a, b):
    a_odds = get_odds(a)
    b_odds = get_odds(b)
    ans = []
    zig_zag = True if len(a_odds) != 0 else False
    while len(a_odds) != 0 or len(b_odds) != 0:
        if(zig_zag):
            ans.append(a_odds[0])
            a_odds.pop(0)
            zig_zag = False if len(b_odds) > 0 else True
        else:
            ans.append(b_odds[0])
            b_odds.pop(0)                        
            zig_zag = True if len(a_odds) > 0 else False
    return ans

exec(input().strip()) # ต้องมีคาสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ

# print(is_odd(31)) # True
# print(has_odds([0,2,3,4,8])) # True
# print(all_odds([1,3,11,17])) # True
# print(no_odds([2,0,4,8])) #True
# print(get_odds([1,20,3,11,2,17]))# [1, 3, 11, 17]
# print(zip_odds([1,3,11,2,17], [1,2,2,2,3,3,3,3,3,3,2,4,97,99]))# [1, 97, 3, 99, 11, 17]
# print(zip_odds([2,4,97,99], [1,3,11,2,17]))# [97, 1, 99, 3, 11, 17]
