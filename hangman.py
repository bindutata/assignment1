# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

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
    
    '''secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    requiredword=''
    for x in secret_word:
      for y in letters_guessed:
        if x==y:
          requiredword+=y
    if requiredword==secret_word:        
      return True
    else:
      return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessedletters=''
    for x in secret_word:
      if x in letters_guessed:
         guessedletters=guessedletters+' '+x
      else:
         guessedletters=guessedletters+' '+'_'
             
    return guessedletters





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    remainingletters=''
    print("available letters to be guessed are :")
    for x in string.ascii_lowercase:
        if x not in letters_guessed:
            remainingletters=remainingletters+x
    return remainingletters

    
    
    

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("hello buddy,welcome to hangman game")
    name=input("please enter your name :")
    print("good luck",name)
    secret_word=choose_word(wordlist)
    print(secret_word)
    print("I am the word with {} letters".format(len(secret_word)))
    warnings=3
    guesses=6
    letters_guessed=[]
    while guesses>0 and  is_word_guessed(secret_word,letters_guessed)==False:
      print("- - - - - - - - - - - - - - - -")
      print("warnings you are left with:",warnings)
      print("guesses you are left with :",guesses)
      print(get_available_letters(letters_guessed))
      letter=input("please guess the letter :")
      if not letter.isalpha() and len(letter)!=1:
        if warnings!=0:
          warnings-=1
          print("this is not a valid letter")
          print(get_guessed_word(secret_word,letters_guessed))
        else:
          guesses-=1
          print("this is not a valid letter.you ran out of warnings.")
          print(get_guessed_word(secret_word,letters_guessed))
      else:
          letter=letter.lower()
          if letter in letters_guessed:
            print("you have already guessed the letter")
            print(get_guessed_word(secret_word,letters_guessed))
            if  warnings!=0:
              warnings-=1
            else:
              guesses-=1
              print("you have already guessed the letter.you ran out of warnings.")
          else:
            letters_guessed.append(letter)
            if letter in secret_word:
              print("you guessed right") 
              print(get_guessed_word(secret_word,letters_guessed)) 
            else:
              if letter in 'aeiou':
                guesses-=2
              else:
                guesses-=1
              print("you guessed wrong")
              print(get_guessed_word(secret_word,letters_guessed))
          if is_word_guessed(secret_word,letters_guessed):
              print('- - - - - - - - - - - - - - - - -')
              print("congrats!you won the game.the word was:",secret_word) 
              score=guesses*len(set(letters_guessed))
              print("your score is:",score)        
          if guesses==0 :
              print('- - - - - - - - - - - - - - - - -')
              print("sorry!you ran out of guesses and loose the game.word was :",secret_word)
        
                 
            




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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_without_spaces=my_word.strip()
    guessedword=''
    if  len(my_word_without_spaces)!=len(other_word) :
        return False
    for i in range(len(my_word_without_spaces)):
     
        if my_word_without_spaces[i]!='_':
            if my_word_without_spaces[i]!=other_word[i]:
              return False
            else:
              guessedword=guessedword+other_word[i]
              print(guessedword)
        else:
            if other_word[i] in guessedword:
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    match=''
    for word in wordlist:
      if match_with_gaps(my_word,word):
        match=match+word
    return match
       



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("hello buddy,welcome to hangman game")
    name=input("please enter your name :")
    print("good luck",name)
    secret_word=choose_word(wordlist)
    print(secret_word)
    print("I am the word with {} letters".format(len(secret_word)))
    warnings=3
    guesses=6
    letters_guessed=[]
    while guesses>0 and  is_word_guessed(secret_word,letters_guessed)==False:
      print("- - - - - - - - - - - - - - - -")
      print("warnings you are left with:",warnings)
      print("guesses you are left with :",guesses)
      print(get_available_letters(letters_guessed))
      letter=input("please guess the letter :")
      if not letter.isalpha() and len(letter)!=1:
        if letter=='*':
          my_word=print(get_guessed_word(secret_word,letters_guessed))
          print(show_possible_matches(my_word))
        else:
          if warnings!=0:
            warnings-=1
            print("this is not a valid letter")
            print(get_guessed_word(secret_word,letters_guessed))
          else:
            guesses-=1
            print("this is not a valid letter.you ran out of warnings.")
            print(get_guessed_word(secret_word,letters_guessed))
      else:
          letter=letter.lower()
          if letter in letters_guessed:
            print("you have already guessed the letter")
            print(get_guessed_word(secret_word,letters_guessed))
            if  warnings!=0:
              warnings-=1
            else:
              guesses-=1
              print("you have already guessed the letter.you ran out of warnings.")
          else:
            letters_guessed.append(letter)
            if letter in secret_word:
              print("you guessed right") 
              print(get_guessed_word(secret_word,letters_guessed)) 
            else:
              if letter in 'aeiou':
                guesses-=2
              else:
                guesses-=1
              print("you guessed wrong")
              print(get_guessed_word(secret_word,letters_guessed))
          if is_word_guessed(secret_word,letters_guessed):
              print('- - - - - - - - - - - - - - - - -')
              print("congrats!you won the game.the word was:",secret_word) 
              score=guesses*len(set(letters_guessed))
              print("your score is:",score)        
          if guesses==0 :
              print('- - - - - - - - - - - - - - - - -')
              print("sorry!you ran out of guesses and loose the game.word was :",secret_word)
        
                 
            







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
