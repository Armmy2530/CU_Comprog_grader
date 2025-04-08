word = input()

word = word.lower()
special_char = '"!@#$%^&*()-+?_=,<;>/.\ '
ans = ""
next_cap = False
for i in word:
    if(next_cap and i not in special_char):
        if ans != "":
            ans += i.capitalize()
        else:
            ans += i
        next_cap = False
    elif(i in special_char):
        next_cap = True    
    else:
        ans += i    
print(ans)