n = int(input())     
v = list() 
for i in range(n):
    data = input().split()
    data[1:] = [float(i) for i in data[1:]]
    v.append(data)
    
c = input().split()
if c[0] == 'show' :
    for i in v:
        i = [str(j) for j in i]
        print(" ".join(i))
elif c[0] == 'max' :
    v_sort = sorted(v,key=lambda x:(-x[int(c[1])],x[0]))
    print(v_sort[0][0],v_sort[0][int(c[1])])
elif c[0] == 'avg' :
    vitamine = [i[int(c[1])] for i in v]
    print( round(sum(vitamine)/len(vitamine), 4) ) 
elif c[0] == 'get' :
    for i in v:
        if (i[0] == c[1]):
            i = [str(j) for j in i]
            print(" ".join(i))
            exit()
    print(c[1],"not found")
elif c[0] == 'sort':
    v_sort = sorted(v,key=lambda x:(x[int(c[1])],x[0]))
    print(" ".join([i[0] for i in v_sort]))
