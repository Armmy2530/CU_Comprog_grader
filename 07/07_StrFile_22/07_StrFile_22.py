word1 = input().lower()
word2 = input().lower()

word_1_sum = 0
for i in word1:
    if(i != " "):
        word_1_sum += ord(i)
word_2_sum = 0
for i in word2:
    if(i != " "):
        word_2_sum += ord(i)
    
print("YES" if word_1_sum == word_2_sum else "NO")