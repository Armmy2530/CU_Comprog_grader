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
    else
        return True
    return False
        
user = ""
data = []
while True:
  user=input()
  if(user == "END"):
      break
  elif(valid_checker(user)):
      pass
