from getWord import getWordForGame as gWFG

class guessCompare():
    def __init__(self) -> None:
        pass

    def check_user_input(self):
        while True:
            guess = input("Give me an alphabet: ")
            if guess.isdigit():
                print("Given input is NOT an alphabet.")
            elif len(guess) != 1:
                print("Given input is MORE than one alphabet.")
            else:
                return guess
            
word_to_guess = gWFG().returnRandomWord()

print(word_to_guess)

guessCompare().check_user_input()
