import random                                               # random module for words selection

def choose_random_word(words_list):                         #function definition
    """Chooses a random word from the provided list of words."""
    return random.choice(words_list)

def initialize_display(word):
    """Creates a display list with underscores representing each letter in the word."""
    return ['_' for _ in word]

def get_player_guess(guessed_letters):
    """Prompts the player to guess a letter and ensures it's a new guess."""
    while True:
        guess = input("Guess a letter: ").lower()           #  lower function lowercases guessed letters as python is case sensitive
        if len(guess) != 1 or not guess.isalpha():          #  checks all characters in string are alphabetic 
            print("Please enter a single letter/alphabet.")
        elif guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try again.")
        else:
            return guess

def update_display_with_guess(word, display, guess):
    """Updates the display list with the guessed letter in the correct positions."""

    # enumerate() to keep  code cleaner instead of index variable
    # enumerate to loop through the list with an index

    for index, letter in enumerate(word):
        if letter == guess:                                # if guessed letter is present in choosen word
            display[index] = letter                        #display letter at that index 

def display_game_state(display, guessed_letters, incorrect_guesses, max_incorrect_guesses):
    """Displays the current state of the game."""

    #fstring for ease of variable concatenation with string
    print("\n-------HANGMAN GAME-------")
    print(f"\nWord: {' '.join(display)}")                  # display contains word as underscores 

    #sorted creates new sorted list as set items in guessed_letters can't be changed                
    print(f"Guessed letters: {' , '.join(sorted(guessed_letters))}")
    print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}\n")

"""Main game loop."""
def play_game():
    
    words_list = ['technology', 'debug', 'programming', 'artificial', 'pseudo']

    #function call 
    #function call for random word selection from given list
    chosen_word = choose_random_word(words_list)

    #function call for display list with underscores
    display = initialize_display(chosen_word)

    max_incorrect_guesses = 5               # limit of max guesses 
    incorrect_guesses = 0                   #initialization
    #use set as they don't contain duplicate values
    guessed_letters = set()                 # empty set for assigning guess letters  

    while incorrect_guesses < max_incorrect_guesses and '_' in display:

        # function call for game state display
        display_game_state(display, guessed_letters, incorrect_guesses, max_incorrect_guesses)
        # gets guess letter 
        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)           # add guessed letter in set 

        if guess in chosen_word:
            update_display_with_guess(chosen_word, display, guess)
        else:
            incorrect_guesses += 1           # increment incorrect guess limit 
            print(f"Incorrect! The letter '{guess}' is not in the word.")

    if '_' not in display:
        print(f"\nCongratulations! You've guessed the word: {''.join(display)}")
    else:
        print(f"\nGame over! The word was: {chosen_word}")

# Start the game
play_game()
