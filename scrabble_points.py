"""
SOUMENG CHEA
CS 5001
FALL 2019

I GOT HELP AND CONSULTED WITH PEERS(FORM ANOTHER INSTITUTE) AND CLASSMATES
"""
import random
from wordlist import *

POINTS = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
         "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
         "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
         "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
         "X": 8, "Z": 10}

FREQ_DICT = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3,
                  'H': 2,'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6,
                  'O': 8,'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4,
                  'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, '_': 2}

def bag_of_letters(letters_DT):

    letter = []

    for i in letters_DT:
        value = letters_DT.get(i)
        freq = i * value

        if len(freq) <= 1:
            letter.append(freq)
        else:
            letter = letter + [character for character in freq]
            
    return letter
    
def get_word_value(word, letters_DT): 
    """Return: total – score of a word.
        The total for a word is the sum of the point for letters in the word, multiply by the value.

        word: string – uppercase letters
        letters_Dt: integer

        """
    
    total = 0
    word = word.upper()
    
    for character in word:
        if character not in letters_DT:
            return 0
        else:
            value = letters_DT.get(character)
            total = total + value
            
    return total

def raffle_letters(letters_DT):
    """ Return: random_letter and new_letter

            random_letter: lengths of seven letters that randomly pick by the random function.

            new_letter: the letters from random function from random_letter

            letters_DT: dictionary

    """
    
    if len(letters_DT) <= 7:
        return letters_DT

    else:
        random_letter = random.sample(letters_DT, 7)

        for each in random_letter:
            if each in letters_DT:
                letters_DT.remove(each)

        new_letter = letters_DT

        return random_letter, new_letter

def build_word(lst_letters, word):

    """ Return: get_word_value(word, POINTS)

        w_bank: dictionary

        Para: Prompt user to enter the word from the letter tile. Return False if the word isn't the dictionary.

        return False if the player no longer have any letter tile in hand

        if the player enter a word that is in the dictionary, they earn the point from the combination letter value.
    """
    play_letter = lst_letters

    empty_tile = play_letter.count('_')
    empty_character = 0
    w_bank = get_wordlist()

    if word not in w_bank:
        print('This word is not in our dictionary. You rewared with 0 points. \n')
        return False
    
    for character in word:
        if character not in play_letter:
            empty_character += 1
            
        elif character in play_letter:
            play_letter.remove(character)

    if empty_character <= empty_tile:
        if empty_character >= 1:
            for element in range(enpty_character):
                play_letter.remove('_')

    elif empty_character >= empty_tile:
        return('You used a letter not in your hand.'), False

    if word in w_bank:
        print('Nice! Point:  ', str(get_word_value(word, POINTS)), 'for this word. \n')

    return get_word_value(word, POINTS)

def game_menu():
    """Return: user_input

        Ask user_input to input their choices: D – Draw letters, W – Play word, P – Print user_inout words history
                                                                    Q – Quit.

        upper(): Allow user_input to lowercase then convert the words and letters to uppercase, so it can match the dictionary

        Parameter: None

    """
    user_input = input('D: Draw letters\n'+'W: Play word\n'+
                        'P: Print all your words so far\n'+ 'Q: Quit\n\n'+
                        'Enter your choice below:  \n')
    user_input = user_input.upper()

    return user_input

                       
        
    

