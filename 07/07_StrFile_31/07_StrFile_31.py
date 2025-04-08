dna = input().strip().upper()
operation_mode = input().strip()

if(operation_mode == 'R'):
    temp_ans = ""
    for i in dna[::-1]:
        match i:
            case 'A':
                temp_ans += 'T'
            case 'T':
                temp_ans += 'A'
            case 'G':
                temp_ans += 'C'
            case 'C':
                temp_ans += 'G'
    print(temp_ans)
elif(operation_mode == 'F'):
#     A T G C
    count = [0,0,0,0]
    error = False
    for i in dna:
        match i:
            case 'A':
                count[0] += 1
            case 'T':
                count[1] += 1
            case 'G':
                count[2] += 1
            case 'C':
                count[3] += 1
            case Default:
                error = True
    print(f"A={count[0]}, T={count[1]}, G={count[2]}, C={count[3]}") if not error else print("Invalid DNA")
else:
    error = False
    for i in dna:
        if(i not in ['A','T','G','C']):
            error = True
            break
    if(not error):  
        match_dna = input().strip()
        matched = 0
        for i in range(len(dna)-1):
            if(dna[i:i+2] == match_dna):
                matched += 1
        print(matched)
    else:
        print("Invalid DNA")