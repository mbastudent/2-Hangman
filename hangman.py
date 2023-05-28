#!/usr/bin/env python
# coding: utf-8

# In[9]:


"""
Contains sets of English words from svnweb.freebsd.org/csrg/share/dict/. This is up to date with revision 61569 of their words list.

There are four sets in this package:

english_words_set: A set of English words containing both upper- and lower-case letters; with punctuation.
english_words_lower_set: A set of English words containing lower-case letters; with punctuation.
english_words_alpha_set: A set of English words containing both upper- and lower-case letters; with no punctuation.
english_words_lower_alpha_set: A set of English words containing lower-case letters; with no punctuation.
where the lower set is the same as the english_words_set with all upper-case letters converted to lower-case letters, and where the alpha set is the same as the english_words_set with all apostrophes (') removed. The lower_alpha set intuitively has both of the rules from the lower set and the alpha set applied.

You can use use these like you would any Python set:

>>> from english_words import english_words_set
>>> 'ghost' in english_words_set

"""
import random
from english_words import english_words_lower_alpha_set



# returns a random word from the list of all words
def random_word(words):
    upper = len(words)
    random_number = random.randint(1, upper)
    return words[random_number-1]
    

def is_letter(guess_letter):
    if len(guess_letter) != 1 or not guess_letter.isalpha():
        print("You can guess only one letter!")
        return False
    else:
        return True

    
def is_already_guessed(guess_letter, used_letters):
    if guess_letter in used_letters:
        print("You've already guessed letter '",guess_letter,"', haven't you? Please pick another letter.")
        return False
    else:
        return True

    
def next_guess(used_letters):
    validity = False
    while not validity:
        guess_letter = input("Enter your letter: ").lower()
        validity = is_letter(guess_letter) and is_already_guessed(guess_letter, used_letters)
    used_letters.append(guess_letter)
    return guess_letter


def check_guess(letter, the_word, right_letters, wrong_letters, partial_word):
    hit = False
        
    for index in range(len(the_word)):
        if the_word[index] == letter:
            hit = True
            partial_word[index] = letter
            
    if hit:
        right_letters.append(letter)
    else:
        wrong_letters.append(letter)
            
    return "".join(partial_word)


def play():
    #list of (already guessed, right and wrong) letters
    used_letters = []
    right_letters = []
    wrong_letters = []
    
    #from list of all the words in the dictionary pick random word to be guessed
    words_full_list = list(english_words_lower_alpha_set)
    the_word = random_word(words_full_list)    
    print("You're guessing a", len(the_word), "letter word. Good luck!")
    
    partial_word = []
    while len(partial_word) < len(the_word):
        partial_word.append('_')
   

    count = 1
    while count <= 6:
        print("******************************\n")
        letter = next_guess(used_letters)
        
        check_word_for_success = "".join(partial_word)
        display_word = check_guess(letter, the_word, right_letters, wrong_letters, partial_word)
        print("\nWord: ", display_word)
        print("Correct letters: [",",".join(right_letters),"]; Used incorrect letters: [",",".join(wrong_letters),"]\n")
        
        if display_word == the_word:
            print("*** You won in ", count, "attempts! The word was ",the_word.upper()," ***")
            return True
        
        if display_word == check_word_for_success:
            count += 1

        # simple drawing simulation
        if count >= 2 and count<7:
            print("  0  ")
        elif count==7:
            print("  X  ")
        if count == 3:
            print("  |  ")
        elif count == 4:
            print(" \|  ")
        elif count >= 5:
            print(" \|/ ")
        if count == 6:
            print(" /   ")
        elif count >= 7:
            print(" / \ ")
            
        if 7-count > 0:
            print("\nYou have ",7 - count," attempts left.")
    
    print("*** You lost! The word was ",the_word.upper()," ***")
    return False
    
    
play()


# In[ ]:




