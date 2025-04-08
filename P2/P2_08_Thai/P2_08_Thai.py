th_pattern = {
    0:'soon', 
    1:'neung', 
    2:'song', 
    3:'sam', 
    4:'si', 
    5:'ha', 
    6:'hok', 
    7:'chet', 
    8:'paet', 
    9:'kao', 
    10:'sip', 
    11:'et', 
    20:'yi', 
    100:'roi', 
    1000:'pun', 
}
def to_Thai( N ): 
    out = ""
    N_copy = N
    if N >= 1000:  # จัดกำรหลักพัน 
        out += th_pattern[N//1000] + " " + th_pattern[1000]+ " "
        N %= 1000 
    if N >= 100:  # จัดกำรหลักร้อย 
        out += th_pattern[N//100]+ " " + th_pattern[100]+ " "
        N %= 100 
    if N >= 11:
        if (N//10 == 2):
            out += th_pattern[20]+ " "
        elif(N//10 > 2):
            out += th_pattern[N//10]+ " "        
        out += th_pattern[10]+ " "
        N %= 10
    
    if (N == 1):
        out += th_pattern[1] if N_copy == 1 else th_pattern[11]
    elif (N > 0):
        out += th_pattern[N]
    elif (N_copy == 0):
        out += th_pattern[0]
    return out.strip()
exec(input().strip())
# print(to_Thai(1024))
# print(to_Thai(1)) #neung 
#  
# print(to_Thai(10)) #sip 
#  
# print(to_Thai(21)) #yi sip et 
#  
# print(to_Thai(101)) #neung roi et 
#  
# print(to_Thai(8009)) #paet pun kao
