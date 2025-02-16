q = list() 
n = int(input())
q_number = 0
haveCall = False 
avg_qtime = []
for k in range(n):
     c = input().split() 
     if c[0] == 'reset':
         q_number = int(c[1])
     elif c[0] == 'new':
         q.append([q_number,int(c[1])])
         print(f"ticket {q_number}")
         q_number += 1
     elif c[0] == 'next':
         if(haveCall == True ):
             q.pop(0)
         else:
             haveCall = True 
         print(f"call {q[0][0]}")
     elif c[0] == 'order':
         cur_no, q_time = q.pop(0)
         haveCall = False 
         print(f"qtime {cur_no} {int(c[1]) - q_time}")
         avg_qtime.append(int(c[1]) - q_time)
     elif c[0] == 'avg_qtime':
         print("avg_qtime", round(sum(avg_qtime)/len(avg_qtime),4) )