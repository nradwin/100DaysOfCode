# import art and words, and random for their selection
import random
import hangman_art
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

# create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # if user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
    # check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # check if wrong
    if guess not in chosen_word:
        # if letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f'{guess} is not in the word. You lose a life.')
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # convert list to string
    print(f"{' '.join(display)}")

    # check user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])