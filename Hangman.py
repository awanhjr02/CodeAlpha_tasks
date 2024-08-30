import random                                               # random module for words selection

def choose_random_word(words_list):                         
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

    # enumerate to loop through the list with an index

    for index, letter in enumerate(word):
        if letter == guess:                               
            display[index] = letter                        

def display_game_state(display, guessed_letters, incorrect_guesses, max_incorrect_guesses):
    """Displays the current state of the game."""

     print(f"\nWord: {' '.join(display)}")                 

    #sorted creates new sorted list as set items in guessed_letters can't be changed                
    print(f"Guessed letters: {' , '.join(sorted(guessed_letters))}")
    print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}\n")

"""Main game loop."""
def play_game():
    
    words_list = ['tech', 'debug', 'program', 'artificial', 'pseudo']


    chosen_word = choose_random_word(words_list)

    #function call for display list with underscores
    display = initialize_display(chosen_word)

    max_incorrect_guesses = 5                
    incorrect_guesses = 0                  
    #use set as they don't contain duplicate values
    guessed_letters = set()                 

    while incorrect_guesses < max_incorrect_guesses and '_' in display:
       display_game_state(display, guessed_letters, incorrect_guesses, max_incorrect_guesses)
    
        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)          

        if guess in chosen_word:
            update_display_with_guess(chosen_word, display, guess)
        else:
            incorrect_guesses += 1           
            print(f"Incorrect! The letter '{guess}' is not in the word.")

    if '_' not in display:
        print(f"\nCongratulations! You've guessed the word: {''.join(display)}")
    else:
        print(f"\nGame over! The word was: {chosen_word}")


play_game()
