def no_lowercase(t):
    for i in t:
        if i.islower():
            return False
    return True
def no_uppercase(t): 
    for i in t:
        if i.isupper():
            return False
    return True
def no_number(t):
    for i in t:
        if i.isdigit():
            return False
    return True
def no_symbol(t):
    for i in t:
        if i in "!@#$%^&*()_+[];'\,./{}:|<>?\"":
            return False
    return True
def character_repetition(t):
    for i in range(len(t)-3):
        if(sum([ord(x) for x in t[i:i+4]]) == sum(ord(x)for x in t[i]*4)):
            return True
    return False
def number_sequence(t):
    for i in range(len(t)-3):
        if(t[i:i+4].isdigit()):
            pev_digit = int(t[i])
            flag = True
            if(t[i+1] == "9" and t[i] == "0"):
                pev_digit = 10
            Increasing = (pev_digit < int(t[i+1]))
            for j in t[i+1:i+4]:
                if(Increasing):
                    if(int(j) != pev_digit+1):
                        flag = False
                else:
                    if(int(j) != pev_digit-1):
                        flag = False
                pev_digit = int(j)
            if(flag == True):
                return True
    return False
def letter_sequence(t):
    t = t.lower()
    for i in range(len(t)-3):
        if(not t[i:i+4].isdigit()):
            pev_digit = ord(t[i])
            flag = True
            Increasing = (t[i] < t[i+1])
            for j in t[i+1:i+4]:
                if(Increasing):
                    if(ord(j) != pev_digit+1):
                        flag = False
                else:
                    if(ord(j) != pev_digit-1):
                        flag = False
                pev_digit = ord(j)
            if(flag == True):
                return True
    return False
def keyboard_pattern(t):
    t = t.lower()
    qwerty_pattern = "!@#$%^&*()_+qwertyuiopasdfghjklzxcvbnm"
    for i in range(len(t)-3):
        pev_digit = qwerty_pattern.find(t[i])
        flag = True
        Increasing = (qwerty_pattern.find(t[i]) < qwerty_pattern.find(t[i+1]))
        for j in t[i+1:i+4]:
            if(Increasing):
                if(j != qwerty_pattern[pev_digit+1]):
                    flag = False
                pev_digit += 1
            else:
                if(j != qwerty_pattern[pev_digit-1]):
                    flag = False
                pev_digit -= 1
        if(flag == True):
            return True
    return False
    
#-----------------------------
passw = input().strip()
errors = []
if len(passw) < 8:
 errors.append("Less than 8 characters")
if no_lowercase(passw):
 errors.append("No lowercase letters")
if no_uppercase(passw):
 errors.append("No uppercase letters")
if no_number(passw):
 errors.append("No numbers")
if no_symbol(passw):
 errors.append("No symbols")
if character_repetition(passw):
 errors.append("Character repetition")
if number_sequence(passw):
 errors.append("Number sequence")
if letter_sequence(passw):
 errors.append("Letter sequence")
if keyboard_pattern(passw):
 errors.append("Keyboard pattern")
   
if len(errors) == 0:
    print("OK")
else:
    for i in errors:
        print(i)