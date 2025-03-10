def first_fit(L, e): # นำ e ใส่รำยกำรย่อยใน L ด้วยวิธี first fit
    for i in L:
        if sum(i)+e<=100:
            i.append(e)
            return
    L.append([e])
def best_fit(L, e): # นำ e ใส่รำยกำรย่อยใน L ด้วยวิธี best fit
    sum_list = [[i,sum(x)+e] for i,x in enumerate(L)]
    sum_list = sorted(sum_list,key=lambda x:x[1],reverse=True)
    for i in sum_list:
        if(i[1] <= 100):
            L[i[0]].append(e)
            return
    L.append([e])
def partition_FF(D): # คืนลิสต์ของลิสต์ที่ได้จำกกำรแบ่งข้อมูลใน D ด้วย first fit
    data = [[D[0]]]
    D = D[1:]
    while len(D) != 0:
        for i in D:
            first_fit(data,i)
            D.remove(i)
            break
    return data
def partition_BF(D): # คืนลิสต์ของลิสต์ที่ได้จำกกำรแบ่งข้อมูลใน D ด้วย best fit
    data = [[D[0]]]
    D = D[1:]
    while len(D) != 0:
        for i in D:
            best_fit(data,i)
            D.remove(i)
            break
    return data

exec(input().strip()) # ต้องมีคำสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ
