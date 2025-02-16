phonenum = input()

if(len(phonenum) == 10 and phonenum[0:2] in ["06","08","09"]):
    print("Mobile number")
else:
    print("Not a mobile number")