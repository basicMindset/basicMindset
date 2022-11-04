from getWord import getWordForGame as gWFG
import string

class guessCompare():
    def __init__(self, word) -> None:
        self.word = word
        self.word_letters = set(word)

    def check_user_input(self):
        alphabet = set(string.ascii_uppercase)
        used_letters = set()

        while len(self.word_letters) > 0:
            #print used letters
            print('Already used letters: ', ', '.join(used_letters))

            word_letter = [letter if letter in used_letters else '-' for letter in self.word]
            print(word_letter)

            user_input = input("\nGive me an alphabet: ").upper()
            if user_input in alphabet - used_letters:
                used_letters.add(user_input)
                if user_input in self.word_letters:
                    self.word_letters.remove(user_input)
            elif user_input in used_letters:
                print('Alphabet already used. Choose another one.')
            else: 
                print('Invalid character. Try again')
            
word = gWFG().returnRandomWord()
module = guessCompare(word)
module.check_user_input()