for _ in range(int(input())):
    text = input()
    count = 0
    for i in text:
        if i == ".":
            count += 1
        else:
            text = text[count//2:]
            break
    print(text)
