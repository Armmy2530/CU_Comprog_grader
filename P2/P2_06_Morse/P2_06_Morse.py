filename = input()
f = open(filename)

mode = f.readline().strip()
if(mode not in ["T2M","M2T"]):
    print("Invalid code")
    exit()
pattern = f.readline().strip()

pattern_data = {}
i = 0
while i < len(pattern) - 2:
    i  = pattern.find('[',i)
    ie = pattern.find(']',i)
    i2 = pattern.find('[',i+1)
    pattern_data[pattern[i+1:ie]] = pattern[ie+1:i2]
    pattern_data[pattern[ie+1:i2]] = pattern[i+1:ie]
    i = i2

def T2M(text,pattern_data):
    result = ""
    for char in text:
        # print(char)
        if (char in pattern_data.keys()):
            result += pattern_data[char] + " "
        else:
            return "Invalid : " + text
    return result

def M2T(morse,pattern_data):
    result = ""
    morse = morse.split()
    for char in morse:
        if (char in pattern_data.keys()):
            result += pattern_data[char]
        else:
            return "Invalid : " + text
    return result

for text in f:
    text = text.strip()
    if(mode == "T2M"):
        print(T2M(text,pattern_data))
    else:
        print(M2T(text,pattern_data))
