month = ["January","February","March","April","May","June","July","August","September","October","November","December"]

u1_name , u1_m , u1_d , u1_y = input().split()
u2_name , u2_m , u2_d , u2_y = input().split()

def m_StrToInt(m):
    for i in range(12):
        if m == month[i]:
            return i+1

u1_m = m_StrToInt(u1_m)
u2_m = m_StrToInt(u2_m)

u1_d = int(u1_d[:-1])
u2_d = int(u2_d[:-1])

if(u1_y == u2_y):
    if(u1_m == u2_m):
        if(u1_d == u2_d):
            print(u1_name,u2_name)
        else:
            print(u1_name if u1_d < u2_d else u2_name)
    else:
        print(u1_name if u1_m < u2_m else u2_name)
else:
    print(u1_name if u1_y < u2_y else u2_name)
