#making a guesing game
import random
def gameIntro():
    intro = str(input("""   Welcome to random NumGuessr
      Press enter to start
      """))
    if intro == "":
        modeSelector()
    else:
        gameIntro()
def modeSelector():
    print("Random number guessing game")
    print("""Pick between 5 difficulties:
    1- Easy (1-10 with 5 guesses)
    2- Medium (1-30 with 12 guesses)
    3- Hard (1-50 with 15 guesses)
    4- Extreme (1-100 with 20 guesses)
    5- One Guess Wonder (1-100 with 1 guess)
    9- Exit
    """)
    difficultySelector = int(input("Select the difficulty you desire: "))
    if difficultySelector == 1:
        guessingGameEasy()
    elif difficultySelector == 2:
        guessingGameMedium()
    elif difficultySelector == 3:
        guessingGameHard()
    elif difficultySelector == 4:
        guessingGameExtreme()
    elif difficultySelector == 5:
        guessingGameOGW()
    elif difficultySelector == 9:
        print("Thank you for playing!")
        exit()
    else:
        modeSelector()
def guessingGameEasy():
    randomNumber = random.randint(1,10)
    flag = True
    counter = 1
    print("   Easy")
    print("In this difficulty you have 5 tries to guess a number from 1 to 10.")
    print("Good Luck!")
    while flag:
        guess = int(input("Guess a number: "))
        if guess == randomNumber:
            flag = False
            print("CONGRATULATIONS!!! YOU WON!!!")
            playAgain = str(input("Do you want to play again? [yes][no] "))
            if playAgain == "yes":
                modeSelector()
            elif playAgain == "no":
                print("Thank you for playing!")
        elif counter == 5:
            flag = False
            print("YOU LOSE")
            print("The number was", randomNumber)
            playAgain = str(input("Do you want to play again? [yes][no] "))
            if playAgain == "yes":
                modeSelector()
            else:
                print("Thank you for playing!")
        else:
            counter +=1
            print("You have", 6-counter, "tries left")
def guessingGameMedium():
    randomNumber = random.randint(1, 30)
    flag = True
    counter = 1
    print("   Hard")
    print("In this difficulty you have 12 tries to guess a number from 1 to 30.")
    print("Good Luck!")
    while flag:
        guess = int(input("Guess a number: "))
        if guess == randomNumber:
            flag = False
            print("CONGRATULATIONS!!! YOU WON!!!")
            playAgain = str(input("Do you want to play again? [yes][no] "))
            if playAgain == "yes":
                modeSelector()
            elif playAgain == "no":
                print("Thank you for playing!")
        elif counter == 12:
            flag = False
            print("YOU LOSE")
            print("The number was", randomNumber)
            playAgain = str(input("Do you want to play again? [yes][no] "))
            if playAgain == "yes":
                modeSelector()
            elif playAgain == "no":
                print("Thank you for playing!")
        else:
            counter += 1
            print("You have", 13 - counter, "tries left")
def guessingGameHard():
    randomNumber = random.randint(1, 50)
    flag = True
    counter = 1
    print("   Hard")
    print("In this difficulty you have 15 tries to guess a number from 1 to 50.")
    print("Good Luck!")
    while flag:
        guess = int(input("Guess a number: "))
        if guess == randomNumber:
            flag = False
            print("CONGRATULATIONS!!! YOU WON!!!")
            playAgain = str(input("Do you want to play again? [yes][no] "))
            if playAgain == "yes":
                modeSelector()
            else:
                print("Thank you for playing!")
        elif counter == 15:
            flag = False
            print("YOU LOSE")
            print("The number was", randomNumber)
            playAgain = str(input("Do you want to play again? [yes][no] "))
            if playAgain == "yes":
                modeSelector()
            elif playAgain == "no":
                print("Thank you for playing!")
        else:
            counter += 1
            print("You have", 16 - counter, "tries left")
def guessingGameExtreme():
    randomNumber = random.randint(1, 100)
    flag = True
    counter = 1
    print("   Extreme")
    print("In this difficulty you have 20 tries to guess a number from 1 to 100.")
    print("Good Luck!")
    while flag:
        guess = int(input("Guess a number: "))
        if guess == randomNumber:
            flag = False
            print("CONGRATULATIONS!!! YOU WON!!!")
            playAgain = str(input("Do you want to play again? [yes][no] "))
            if playAgain == "yes":
                modeSelector()
            elif playAgain == "no":
                print("Thank you for playing!")
        elif counter == 20:
            flag = False
            print("YOU LOSE")
            print("The number was", randomNumber)
            playAgain = str(input("Do you want to play again? [yes][no] "))
            if playAgain == "yes":
                modeSelector()
            elif playAgain == "no":
                return "Thank you for playing!"
        else:
            counter += 1
            print("You have", 21 - counter, "tries left")
def guessingGameOGW():
    randomNumber = random.randint(1, 100)
    flag = True
    print("   One Guess Wonder")
    print("In this difficulty you have 1 try to guess a number from 1 to 100.")
    print("Good Luck!")
    while flag:
        guess = int(input("Guess a number: "))
        if guess == randomNumber:
            print("YOU WON!!! You should play the lottery.")
        else:
            randNumber = random.randint(1,5)
            if randNumber == 1:
                print("You wish")
                print("The number was", randomNumber)
                print("""

                                """)
                modeSelector()
            elif randNumber == 2:
                print("You're not that guy")
                print("The number was", randomNumber)
                print("""

                                """)
                modeSelector()
            elif randNumber == 3:
                print("He need some milk")
                print("The number was", randomNumber)
                print("""

                                """)
                modeSelector()
            elif randNumber == 4:
                print("HA! GAYYYYY")
                print("The number was", randomNumber)
                print("""
                
                """)
                modeSelector()
            else:
                print("Never gonna give you up...")
                print("The number was", randomNumber)
                print("""

                                """)
                modeSelector()
print(gameIntro())