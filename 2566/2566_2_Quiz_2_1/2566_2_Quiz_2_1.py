def hide_vowel(w): # ฟังกช์ นั นี้เขยีนใหแ้ลว้ เรยี กใชไ้ดเ้ลย
    # รับ w เป็นสตริง
    # คืน สตริงที่เหมือน w แต่ตัวอักษรใดใน w ที่เป็นสระจะถูกแทนด้วยเครื่องหมายดอกจัน *
    h = ""
    for c in w:
        if c.lower() in 'aeiou':
            c = '*'
        h += c
    return h
def less_offensive(t, oword):
    # รับ t เป็นสตริง
    # รับ oword เป็นสตริงที่เก็บค าไม่สุภาพหนึ่งค า
    # คืน สตริงใหม่ที่เหมือน t แต่แทนสระในสตริงย่อยของ t ที่เหมือนกับ oword ด้วยเครื่องหมายดอกจัน เชน่
    # less_offensive("ABCDEFabcdef D E F", "def") จะคืน "ABCD*Fabcd*f D E F"k
    return t.replace(oword,hide_vowel(oword))

Owords = input().split()
text = input()

for i in Owords:
    i = i.lower()
    text = less_offensive(text,i)
print(text)
