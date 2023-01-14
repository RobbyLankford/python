# Problem Set 2, hangman.py
# Name: Robert Lankford
# Collaborators: N/A
# Time spent: N/A

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"



def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    guessed = []
    for letter in set(secret_word):
      guessed.append(letter in letters_guessed)
    
    return sum(guessed) == len(guessed)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed = []
    for letter in secret_word:
        if letter in letters_guessed:
            guessed.append(letter)
        else:
            guessed.append("_")
    
    return ' '.join(guessed).strip()



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = []
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            letters.append(letter)
    
    return ''.join(letters).strip()



def print_losing_message(secret_word):
    print("------------")
    print(f"Sorry, you ran out of guesses. The word was: {secret_word}")



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
       
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    while guesses_remaining > 0:
        ## Message printed at the start of each round
        print("------------")
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        word_guessed = get_guessed_word(secret_word, letters_guessed)
        
        ## Get guess from user
        guess = input("Please guess a letter: ")
        
        ## A valid guess is a single alphabetical character
        if not str.isalpha(guess):
            ### If the user is out of warnings, they lose a guess
            if warnings_remaining == 0:
                guesses_remaining -= 1
                
                if guesses_remaining == 0:
                    print_losing_message(secret_word)
                    break
                
                else:
                    print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {word_guessed}")
                    continue
            
            else: 
                warnings_remaining -= 1
                
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {word_guessed}")
                continue
        else:
            guess = str.lower(guess)
        
        ## User cannot guess a letter that they have already guessed
        if guess in letters_guessed:
            ### If the user is out of warnings, they lose a guess
            if warnings_remaining == 0:
                guesses_remaining -= 1
                
                if guesses_remaining == 0:
                    print_losing_message(secret_word)
                    break
                
                else:
                    print(f"Opps! You've already guessed that letter. You have no warnings left so you lose one guess {word_guessed}")
                    continue
            
            else:
                warnings_remaining -= 1
                
                print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left: {word_guessed}")
                continue
        
        letters_guessed.append(guess)
        
        word_guessed = get_guessed_word(secret_word, letters_guessed)
        
        ## Incorrect vowels lose two guesses, incorrect consonants lose one guess
        if guess not in secret_word:
            print(f"Oops! That letter is not in my word: {word_guessed}")
            
            if guess in ['a', 'e', 'i', 'o', 'u']:
                guesses_remaining -= 2
            
            else:
                guesses_remaining -= 1
        
        else:
            print(f"Good guess: {word_guessed}")
        
        ## Check if user has won
        if is_word_guessed(secret_word, letters_guessed):
            score = guesses_remaining * len(set(secret_word))
            
            print("------------")
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {score}")
            break
        
        ## Check if user has lost
        if guesses_remaining <= 0:
            print_losing_message(secret_word)
            break



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.strip().replace(" ", "")
    
    #> Check Lengths
    if len(my_word) != len(other_word):
        return False
    
    #> Check Characters
    guessed = []
    for char in my_word:
        if char != "_" and char not in guessed:
            guessed.append(char)
    
    for i in range(len(my_word)):
        if my_word[i] == "_":
            if other_word[i] in guessed:
                return False
            
            else:
                continue
        
        if my_word[i] != other_word[i]:
            return False
        
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    my_word = my_word.strip().replace(" ", "")
    
    #> Check if a possible match
    possible_matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)
    
    #> Print possible matches
    if len(possible_matches) == 0:
        print("No matches found")
    
    else:
        for match in possible_matches:
            print(match, end = " ")
        
        print()
    
    return None



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
       
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    while guesses_remaining > 0:
        ## Message printed at the start of each round
        print("------------")
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        word_guessed = get_guessed_word(secret_word, letters_guessed)
        
        ## Get guess from user
        guess = input("Please guess a letter: ")
        
        ## A valid guess is a single alphabetical character
        if guess == "*":
            show_possible_matches(word_guessed)
            continue
        
        elif not str.isalpha(guess):
            ### If the user is out of warnings, they lose a guess
            if warnings_remaining == 0:
                guesses_remaining -= 1
                
                if guesses_remaining == 0:
                    print_losing_message(secret_word)
                    break
                
                else:
                    print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {word_guessed}")
                    continue
            
            else: 
                warnings_remaining -= 1
                
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {word_guessed}")
                continue
        
        else:
            guess = str.lower(guess)
        
        ## User cannot guess a letter that they have already guessed
        if guess in letters_guessed:
            ### If the user is out of warnings, they lose a guess
            if warnings_remaining == 0:
                guesses_remaining -= 1
                
                if guesses_remaining == 0:
                    print_losing_message(secret_word)
                    break
                
                else:
                    print(f"Opps! You've already guessed that letter. You have no warnings left so you lose one guess {word_guessed}")
                    continue
            
            else:
                warnings_remaining -= 1
                
                print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left: {word_guessed}")
                continue
        
        letters_guessed.append(guess)
        word_guessed = get_guessed_word(secret_word, letters_guessed)
        
        ## Incorrect vowels lose two guesses, incorrect consonants lose one guess
        if guess not in secret_word:
            print(f"Oops! That letter is not in my word: {word_guessed}")
            
            if guess in ['a', 'e', 'i', 'o', 'u']:
                guesses_remaining -= 2
            
            else:
                guesses_remaining -= 1
        
        else:
            print(f"Good guess: {word_guessed}")
        
        ## Check if user has won
        if is_word_guessed(secret_word, letters_guessed):
            score = guesses_remaining * len(set(secret_word))
            
            print("------------")
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {score}")
            break
        
        ## Check if user has lost
        if guesses_remaining <= 0:
            print_losing_message(secret_word)
            break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
