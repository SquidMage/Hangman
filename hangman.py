#! python3

# hangman.py

import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

# Declaring important variables.
maxAttempts = 0
attemptsLeft = 0
currentGuess = ""
prevGuesses = []
correctWord = ""
hiddenWord = ""
victoryStatus = False

# Getting the possible words.
txtObj = open(r".\words.txt", "r")
words = txtObj.read()
txtObj.close()
wordList = words.split("\n")

# Getting the number of possible attempts.
while True:
    maxAttempts = input("How many incorrect guesses do you want to have? [3-25] ")
    
    try:
        int(maxAttempts)
        if int(maxAttempts) < 3 or int(maxAttempts) > 25:
            print("Choose a number between 3 and 25.")
            continue

        else:
            attemptsLeft = int(maxAttempts)
            break
        
    except ValueError:
        print("You must enter an integer.")
        continue

# Getting and encrypting the word.
correctWord = wordList[random.randint(0,len(wordList))]
#logging.debug(print(correctWord))
hiddenWord = "*" * len(correctWord)
tempList = list(hiddenWord)
print("Selecting and hiding word...\n")

# Taking guesses from the user.
while attemptsLeft > 0:
    if victoryStatus:
        print(hiddenWord)
        break
    print("\nWord: " + hiddenWord)
    print("Incorrect attempts left: " + str(attemptsLeft))
    print("Previous guesses: " + ", ".join(prevGuesses))
    currentGuess = input("Enter a letter: ")

    # Invalid input.
    if len(currentGuess) != 1:
        print("Only enter one letter at a time!")
        continue

    elif not currentGuess.isalpha():
        print("Only enter letters!")

    elif currentGuess in prevGuesses:
        print("You already guessed " + currentGuess + ".")

    # Guess was correct.
    elif currentGuess.lower() in correctWord:
        print(currentGuess + " is correct!")
        for i in range(len(correctWord)):
            if currentGuess == correctWord[i - 1]:
                tempList[i - 1] = currentGuess.lower()
                hiddenWord = "".join(tempList)
                if hiddenWord == correctWord:
                    victoryStatus = True
                    break
                    
    # Guess was incorrect.
    else:
        print(currentGuess.lower() + " is not correct!")
        attemptsLeft = attemptsLeft - 1
        prevGuesses.append(currentGuess.lower())


if victoryStatus:
    print("Congrats, you did it!")

else:
    print("Looks like you're out of attempts, maybe next time.")
    print("The word was " + correctWord + ".")
