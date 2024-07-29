# Hangman - Python - Shaun Bolten

import random

words = ("apple" , "orange", "banana", "coconut", "pineapple, grape, watermelon")

#Dictionary of Key
hangmanArt = {0: ("  ",
                  "  ",
                  "  "),
              1: (" o ",
                  "  ",
                  "  "),
              2: (" o ",
                  " | ",
                  "  "), 
              3: (" o ",
                  "/| ",
                  "  "), 
              4: (" o ",
                  "/|\\",
                  "  "), 
              5:(" o ",
                 "/|\\",
                 "/ "), 
              6: (" o ",
                  "/|\\",
                  "/\\")}


#for line in hangmanArt[5]: Testing Output
    #print(line)

def displayHangman(wrongGuesses):
    print("__________")
    for line in hangmanArt[wrongGuesses]:
        print(line)
    print("__________")

def displayHint(hint):
    print(" ".join(hint))

def displayAnswer(answer):
    pass

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrongGuesses = 0
    guessedLetters = set()
    isRunning = True

    while isRunning:
        displayHangman(wrongGuesses)
        displayHint(hint)
        guess = input("Guess a letter: ").lower()
        
        if len(guess) !=1 or not guess.isalpha():
            print("Invalid")
            continue

        if guess in guessedLetters:
            print(f"{guess} is already guessed")
            continue

        guessedLetters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrongGuesses+=1
        
        if "_" not in hint:
            displayHangman(wrongGuesses)
            displayAnswer(answer)
            print("You win!")
            isRunning = False
        elif wrongGuesses >= len(hangmanArt) - 1:
            displayHangman(wrongGuesses)
            displayAnswer(answer)
            print("You Lose!")
            isRunning = False

if __name__ == "__main__":
    main()