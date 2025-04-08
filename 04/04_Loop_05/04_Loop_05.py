# ChatGPT Edition
focus_word = input()
sentence = input()

# Define characters that can act as word boundaries
boundary_chars = {" ", "'", '"', "(", ")", ",", ".", "\n"}

found_word = 0
current_word = []

for char in sentence:
    if char in boundary_chars:
        # Check if the accumulated word matches the focus word
        if "".join(current_word) == focus_word:
            found_word += 1
        current_word = []  # Reset for the next word
    else:
        current_word.append(char)

# Handle the last word in the sentence
if "".join(current_word) == focus_word:
    found_word += 1

print(found_word)