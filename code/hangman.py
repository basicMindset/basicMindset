from re import M
from getWord import getWordForGame as gWFG
import string

class guessCompare():
    def __init__(self, word) -> None:
        self.word = word
        self.word_letters = set(word)

    def play(self):
        alphabet = set(string.ascii_uppercase)
        used_letters = set()

        lives = 7

        while len(self.word_letters) > 0 and lives > 0:
            #print used letters
            print('You have', lives, ' lives left and you have already used these letters: ', ', '.join(used_letters))

            word_letter = [letter if letter in used_letters else '_' for letter in self.word]
            print('Current word:', ' '.join(word_letter))

            user_input = input("Give me an alphabet: ").upper()
            if user_input in alphabet - used_letters:
                used_letters.add(user_input)
                if user_input in self.word_letters:
                    self.word_letters.remove(user_input)
                else:
                    lives = lives - 1
                    if lives > 0:
                        print('Alphabet is not in the word.')

            elif user_input in used_letters:
                print('Alphabet already used. Choose another one.')
            else: 
                print('Invalid character. Try again')
        if lives == 0:
            print('No more lives left. You lose.')
        else:
            print('You guessed the word correctly:', self.word)
            
module = guessCompare(gWFG().returnRandomWord())
module.play()