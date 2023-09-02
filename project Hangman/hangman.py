import random
word_list = ["camel","austria","football"]
chosen_word = random.choice(word_list)
guess = input("Guess a word:").lower()
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")