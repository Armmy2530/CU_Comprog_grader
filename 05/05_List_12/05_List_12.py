x = [
["Robert"   ,  "Dick"   ],
["William"  ,  "Bill"   ],
["James"    ,  "Jim"    ],
["John"     ,  "Jack"   ],
["Margaret" ,  "Peggy"  ],
["Edward"   ,  "Ed" ],
["Sarah"    ,  "Sally"  ],
["Andrew"   ,  "Andy"   ],
["Anthony"  ,  "Tony"   ],
["Deborah"  ,  "Debbie" ],
]

num = int(input())
NotFound = False

for i in range(num):
    user = input()
    NotFound = False
    for j in range(len(x)):
        if(x[j][0] == user):
            print(x[j][1])
            NotFound = False
            break
        elif(x[j][1] == user):
            print(x[j][0])
            NotFound = False
            break
        else:
            NotFound = True
    if NotFound == True:
        print("Not found") 