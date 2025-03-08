keyboard = {
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz',
    '0' : ' ',
    }
def text2keys(text):
    text = text.lower()
    keys = ""
    for i in text:
        for key, value in keyboard.items():
            if i in value:
                keys += key*(value.index(i)+1) + " "
    return keys[:-1]
def keys2text(keys):
    text = ""
    for i in keys.split():
        chars = keyboard[i[0]]
        text += chars[len(i)-1] 
    return text
exec(input().strip())
