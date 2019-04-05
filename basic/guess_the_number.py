import random

def printMenu():
    print("Welcome to Guess-the-number game")
    print("--------------------------------")
    print("1. Start new game")
    print("2. Quit")

def playGame():
    print("Instruction: Guess a number between 1 and 100. Enter '0' to give up.")
    # 1. add the option in the code for the user to give up when the user inputs '0' in the guess
    # 2. give a hint to the user after each guess, by telling the user whether his guess is too small or too big
    numOfGuesses = 0
    secretNumber = random.randint(1, 100)
    won = False
    while not won:
        guess = int(input())
        numOfGuesses += 1
        if guess == secretNumber:
            print("Congratulations!! You've won with {} guesses".format(numOfGuesses))
            won = True
        else:
            print("Wrong guess. Try again!")

while True:
    printMenu()
    choice = int(input())
    if choice == 1:
        playGame()
    elif choice == 2:
        print("Thanks for playing!! Bye bye!!")
        break
    else:
        print("Invalid choice")
    
