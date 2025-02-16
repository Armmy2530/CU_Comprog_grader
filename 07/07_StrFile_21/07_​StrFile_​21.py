special_char = '"!@#$%^&*()-+?_=,<;>/.\ '
while True:
    user_input = input()
    if(user_input == "end"):
        break
    else:
        ans = ""
        for i in user_input:
            if(i in special_char):
                ans += i
            else:
                char_value = ord(i)
                if(char_value >= 65):
                    if((char_value >= 65 and char_value < 78) or (char_value >= 97 and char_value < 110)):
                        ans += chr(char_value + 13)
                    else:
                        ans += chr(char_value - 13)
                else:
                    ans += i
                
        print(ans)