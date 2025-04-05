# Noted ** it not pass 2 last testcase because of word per line that output
# -------------------
# Expected:
# Aaa Bbbb VXYZ, Ddd
# ddD "VXYZ" BbbB
# AaaA Aa Bb
# VXYZVXYZ DD BbBB
# Aa VXYZ.
# -------------------
# My Output:
# Aaa Bbbb VXYZ,
# Ddd ddD "VXYZ"
# BbbB AaaA Aa Bb
# VXYVXYVXYZ DD
# BbBB Aa VXYZ.

#
# 2567_2_Q2_B2: Text Replace in File
#

filename,find_word,replace_word = input().split(',')

find_word = find_word.lower()
line_num = []
file = open(filename)
text = ""
for i in file:
    i = i.strip()
    line_num.append(len(i))
    text += i + " "

text_low = text.lower()
text = list(text)
# for start when -len(find_word)-1 it goint to find at index = 0
index = -len(find_word)+1
index2 = 0
c = 0
while True:
    # text_low.find(find_word,index+len(find_word)-1)    
    # (index + len(find_word) - 1) is position of last found word
    # example: abcabc
    # Find "abc"
    # index before enter loop = -2
    # round 0: index = -2 + 3 - 1 = 0
    # abcabc
    # -
    # -------------------------------
    # round 1: index =  0 + 3 - 1 = 2
    # abcabc
    #   -
    index = text_low.find(find_word,index+len(find_word)-1)
    index2 = index + c*(len(replace_word) - len(find_word)) if index != -1 else 0

    # --- For Debug ---
    # print("-"*40)
    # print(index)
    # print("".join(text_low))
    # print(" "*index+"-")
    # print(index2)
    # print("".join(text))
    # print(" "*index2+"-")
    # print("-"*40)
    # -----------------

    if (index == -1):
        break
    else:
        text[index2:index2+len(find_word)] = replace_word
        c += 1
text = ("".join(text)).split()
display = ""
count = 0
char = 0
word = 0
line_num = max(line_num)
# print(line_num)
while word <= len(text)-1:
    # print(char,char+len(text[word]))
    if char + len(text[word]) <= line_num:
        display += text[word] + " "
        char = len(display)
        word += 1
    else:
        print(display)
        char = 0
        display = ""
if(display != ""):
    print(display)
