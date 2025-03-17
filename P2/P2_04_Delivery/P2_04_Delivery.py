month_30 =  [4,6,9,11]
def leap_year(y):
    y = y - 543
    return (y%400 == 0) or (y%4 == 0 and y%100 != 0) 
def valid_checker(src):
    del_id, type, d, m, y = src.split()
    d = int(d)
    m = int(m)
    y = int(y)
    if(y < 2558):
        print(f"Error: {del_id} {type} {d} {m} {y} --> Invalid year")
    elif(m <= 0 or m > 12):
        print(f"Error: {del_id} {type} {d} {m} {y} --> Invalid month")
    elif(m == 2 and (d<1 or d>(29 if leap_year(y) else 28 ))):
        print(f"Error: {del_id} {type} {d} {m} {y} --> Invalid date")
    elif(d < 1 or  d > (30 if  m in month_30  else 31)):
        print(f"Error: {del_id} {type} {d} {m} {y} --> Invalid date")
    elif(type not in "EQNF"):
        print(f"Error: {del_id} {type} {d} {m} {y} --> Invalid delivery type")
    else:
        return True
    return False
def nextDate(n_d,d,m,y):
    remain_day = d+n_d
    if (m == 2 and ((leap_year(y) and remain_day > 29) or (not(leap_year(y)) and remain_day  > 28))):
        m += 1
        d = remain_day - (29 if leap_year(y) else 28)
    elif (m in month_30 and remain_day > 30):
        m += 1
        d = remain_day-30        
    elif (remain_day > 31):
        m += 1
        d = remain_day-31
    else:
        d = remain_day

    if(m == 13):
        m = 1
        y += 1

    return d,m,y

user = ""
data = []
while True:
    user=input()
    if(user == "END"):
      break
    elif(valid_checker(user)):
      del_id, type, d, m, y = user.split()
      d = int(d)
      m = int(m)
      y = int(y)
      senttime = 0
      if(type == "E"):
          senttime = 1
      elif(type == "Q"):
          senttime = 3
      elif(type == "N"):
          senttime = 7
      else:
          senttime = 14
      ad,am,ay = nextDate(senttime,d,m,y)
      data.append([del_id,ad,am,ay])

data = sorted(data,key=lambda x:(x[3],x[2],x[1],x[0]))
for i in data:
    print(f"{i[0]}: delivered on {i[1]}/{i[2]}/{i[3]}")
