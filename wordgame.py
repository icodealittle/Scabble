import wordlist
from scrabble_points import *

POINTS = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
         "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
         "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
         "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
         "X": 8, "Z": 10}

FREQ_DICT = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3,
                  'H': 2,'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6,
                  'O': 8,'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4,
                  'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, '_': 2}

def main():
     print('Welcome! Are you ready to play? Lets play! \n')

     reference = bag_of_letters(FREQ_DICT)
     letters_tile = []
     use_w = []
     history_w = ''
     previous = ''
     scores = 0

     while True:
          user_input = game_menu() #Calling the function from scrabble_points to start the game

          #Winning score is the player manage to make a word out of all the letter tiles
          if len(reference) == 0 and len(letters_tile) == 0:
               print('Congratulations! You have used all of the letters!',
                  'You received a total of', scores, 'points! Goodbye!')
               break
              
          if user_input == 'D':

               #Print out 7 random letters from the dictionary
               if len(reference) <= 7:
                    print(reference)

               else:
                    if previous == 'W':
                         for letter in letters_tile:
                              reference.append(letter)
                              
                   #Call funtion from scrabble_points for 7 random letters – raffle_letters()           
                    (game_lst, new_reference) = raffle_letters(reference)
                    print('Your letters are:', game_lst, '\n')
                    letters_tile = game_lst
                    reference = new_reference
                    
               previous = 'D'

          elif user_input == 'W':
               previous = 'W'

               #Ask user to draw new tile when they are run out of letter tile
               if len(letters_tile) == 0:
                    print('You do not have any letters in play, please draw new tiles!')
                    continue

               print('\nYour letters are:', str(letters_tile))
               print('You have a total of', len(reference), 'letters left')
               player_word = input('What word would you like to play?\n')
               player_word = player_word.upper()

               #No re-use words form the previous round
               while player_word in use_w:
                    print('You have already used that word! Please choose a',
                      'different word!\n')
                    #Ask player to enter a word from the random select letter tiles 
                    player_word = input('What word would you like to play?\n')
                    player_word = player_word.upper()

               inspect = build_word(letters_tile, player_word)

               #If the user enter 
               if inspect != False:
                    game_history = "".join([player_word, '  recieved  ', str(inspect), '  points!  '])

                    use_w.append(player_word)
                    history_w = history_w + game_history + '\n'
                    scores = scores + inspect
           #Print a list of word history that the player already used         
          elif user_input == 'P':
               print('\nYour total scores of:  ', str(scores), 'points')
               print(history_w)
          #When the player enter "Q", the game end
          elif user_input == 'Q':
               print('Awee :( Why you do need to leave so soon?!?! You earned', scores, 'points! See you soon!')
               break
          else:
               print('Sorry, this is not correct input. Please choose again!\n')

main()
