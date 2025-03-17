def charCount(src):
    data ={}
    for i in src:
        if(i in "abcdefghijklmnopqrstuvwxyz"):
            if (i in data.keys()):
                data[i] += 1
            else:
                data[i] = 1
    return data
def anagram_method(text):
    text_count = charCount(text.lower())
    print(text)
    

text1 = input().strip()
text2 = input().strip()

print(charCount(text1.lower()))
print(charCount(text2.lower()))
