import random
from hangman_words import word_list
from hangman_arts import logo, stages

print(logo)
print("\nWelcome to Hangman!")

# Choose random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
hint_used = False
end_of_game = False

print(f"\nThe word has {word_length} letters.")
print(f"You have {lives} lives.")
print("Type 'hint' to reveal one letter (costs 1 life).\n")

# Create blank display
display = ["_"] * word_length
print(" ".join(display))

while not end_of_game:

    guess = input("\nGuess a letter: ").lower()

    # -------- HINT SYSTEM --------
    if guess == "hint":
        if hint_used:
            print("You already used your hint!")
        else:
            hint_used = True
            lives -= 1
            print("Hint used! You lost 1 life.")

            hidden_indexes = [i for i in range(len(display)) if display[i] == "_"]

            if hidden_indexes:
                reveal_index = random.choice(hidden_indexes)
                display[reveal_index] = chosen_word[reveal_index]

        print(" ".join(display))
        print(stages[lives])

        if lives == 0:
            end_of_game = True

        continue
    # --------------------------------

    # Prevent repeated correct guess
    if guess in display:
        print(f"You've already guessed '{guess}'")
        continue

    # Correct guess
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

    print(" ".join(display))
    print(stages[lives])

    # Win check
    if "_" not in display:
        end_of_game = True
        print("\n🎉 You win!")

    # Lose check
    if lives == 0:
        end_of_game = True

# Final result
if lives == 0:
    print(f"\n💀 You ran out of lives.")
    print(f"The word was: {chosen_word}")