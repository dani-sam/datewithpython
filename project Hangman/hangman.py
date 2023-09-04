import random
word_list = ["camel","austria","football"]
chosen_word = random.choice(word_list)
# len_chosenWord = len(chosen_word)
# print(len_chosenWord)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
symbol = '_'
for _ in range(len(chosen_word)):
    display  += '_'
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a word:").lower()
    # check guessed word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    print(display)

    if '_' not in display:
        end_of_game = True
        print('You win')
    