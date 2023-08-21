from tkinter import *
import random

main = Tk()
main.title("NumGuessr")

def center_window(width, height):
    # Get screen width and height
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()

    # Calculate the x and y coordinates for the window to be centered
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    # Set the window geometry
    main.geometry(f"{width}x{height}+{x}+{y}")

# Set the width and height of the main window
window_width = 400
window_height = 300
center_window(window_width, window_height)

def modeSelector1():
    easyMode=Button(main, text="Easy", fg="#ff8f8f", command=lambda: handle_difficulty("Easy"))
    easyMode.pack()
    mediumMode = Button(main, text="Medium", fg="#ff6b6b", command=lambda: handle_difficulty("Medium"))
    mediumMode.pack()
    hardMode = Button(main, text="Hard", fg="#ff4747", command=lambda: handle_difficulty("Hard"))
    hardMode.pack()
    OGWMode = Button(main, text="One Guess Wonder", fg="#ff0000", command=lambda: handle_difficulty("One Guess Wonder"))
    OGWMode.pack()
    exitMode = Button(main, text="Exit", fg="black", command=exit_mode)
    exitMode.pack()

    # Hide the start button and intro text
    startButton.pack_forget()
    introText.pack_forget()
def handle_difficulty(difficulty):
    # Remove all the buttons from the screen
    for widget in main.winfo_children():
        widget.pack_forget()
    if difficulty == "Easy":
        easyDifficulty()
    elif difficulty == "Medium":
        mediumDifficulty()
    elif difficulty == "Hard":
        hardDifficulty()
    elif difficulty == "One Guess Wonder":
        OGWDifficulty()
    else:
        exit_mode()
def exit_mode():
    exitText = Label(main, text="Thanks for playing!", fg="black")
    exitText.pack()
    exit()
def easyDifficulty():
    def play_again():
        main.destroy()  # Close the current window
        easyDifficulty()  # Restart the game

    randomNumber = random.randint(1, 10)
    flag = True
    counter = 1
    lGuesses = []
    def check_guess():
        nonlocal counter, flag
        guess = int(guess_entry.get())
        if guess == randomNumber:
            flag = False
            result_label.config(text="CONGRATULATIONS!!! YOU WON!!!")
            play_again_button.pack()
        elif guess<randomNumber:
            lGuesses.append(guess)
            result_label.config(text=f"You have {5 - counter} tries left.\nTry to guess higher.\nNumbers guessed {lGuesses}")
        elif guess>randomNumber:
            lGuesses.append(guess)
            result_label.config(text=f"You have {5 - counter} tries left.\nTry to guess lower.\nNumbers guessed {lGuesses}")
        if counter == 5:
            flag = False
            result_label.config(text=f"YOU LOSE\nThe number was {randomNumber}.")
            play_again_button.pack()
        if counter <= 15:
            counter += 1
        #     result_label.config(text=f"You have {6 - counter} tries left")
    instruction_label = Label(main, text="In this difficulty, you have 5 tries to guess a number from 1 to 10.")
    instruction_label.pack()
    guess_label = Label(main, text="Guess a number:")
    guess_label.pack()
    guess_entry = Entry(main)
    guess_entry.pack()
    check_button = Button(main, text="Check", command=check_guess)
    check_button.pack()
    result_label = Label(main, text="")
    result_label.pack()
    # Create play again button (hidden initially)
    play_again_button = Button(main, text="Play Again", command=modeSelector1)
def mediumDifficulty():
    def play_again():
        main.destroy()  # Close the current window
        mediumDifficulty()  # Restart the game

    randomNumber = random.randint(1, 30)
    flag = True
    counter = 1
    lGuesses = []

    def check_guess():
        nonlocal counter, flag
        guess = int(guess_entry.get())

        if guess == randomNumber:
            flag = False
            result_label.config(text="CONGRATULATIONS!!! YOU WON!!!")
            play_again_button.pack()
        elif guess < randomNumber:
            lGuesses.append(guess)
            result_label.config(text=f"You have {12 - counter} tries left.\nTry to guess higher.\nNumbers guessed {lGuesses}")
        elif guess > randomNumber:
            lGuesses.append(guess)
            result_label.config(text=f"You have {12 - counter} tries left.\nTry to guess lower.\nNumbers guessed {lGuesses}")
        if counter == 12:
            flag = False
            result_label.config(text=f"YOU LOSE\nThe number was {randomNumber}")
            play_again_button.pack()
        if counter <= 12:
            counter+=1
        #     result_label.config(text=f"You have {13 - counter} tries left")
    instruction_label = Label(main, text="In this difficulty, you have 12 tries to guess a number from 1 to 30.")
    instruction_label.pack()
    guess_label = Label(main, text="Guess a number:")
    guess_label.pack()
    guess_entry = Entry(main)
    guess_entry.pack()
    check_button = Button(main, text="Check", command=check_guess)
    check_button.pack()
    result_label = Label(main, text="")
    result_label.pack()
    # Create play again button (hidden initially)
    play_again_button = Button(main, text="Play Again", command=modeSelector1)
def hardDifficulty():
    def play_again():
        main.destroy()  # Close the current window
        hardDifficulty()  # Restart the game

    randomNumber = random.randint(1, 50)
    flag = True
    counter = 1
    lGuesses = []

    def check_guess():
        nonlocal counter, flag
        guess = int(guess_entry.get())

        if guess == randomNumber:
            flag = False
            result_label.config(text="CONGRATULATIONS!!! YOU WON!!!")
            play_again_button.pack()
        elif guess<randomNumber:
            lGuesses.append(guess)
            result_label.config(text=f"You have {15 - counter} tries left.\nTry to guess higher.\nNumbers guessed {lGuesses}")
        elif guess>randomNumber:
            lGuesses.append(guess)
            result_label.config(text=f"You have {15 - counter} tries left.\nTry to guess lower.\nNumbers guessed {lGuesses}")
        if counter == 15:
            flag = False
            result_label.config(text=f"YOU LOSE\nThe number was {randomNumber}")
            play_again_button.pack()
        if counter<=15:
            counter += 1
        #     result_label.config(text=f"You have {16 - counter} tries left")
    instruction_label = Label(main, text="In this difficulty, you have 15 tries to guess a number from 1 to 50.")
    instruction_label.pack()
    guess_label = Label(main, text="Guess a number:")
    guess_label.pack()
    guess_entry = Entry(main)
    guess_entry.pack()
    check_button = Button(main, text="Check", command=check_guess)
    check_button.pack()
    result_label = Label(main, text="")
    result_label.pack()
    # Create play again button (hidden initially)
    play_again_button = Button(main, text="Play Again", command=modeSelector1)
def OGWDifficulty():
    def play_again():
        main.destroy()  # Close the current window
        OGWDifficulty()  # Restart the game

    randomNumber = random.randint(1, 100)
    flag = True

    def check_guess():
        nonlocal flag
        guess = int(guess_entry.get())

        if guess == randomNumber:
            flag = False
            result_label.config(text="CONGRATULATIONS!!! YOU WON!!!")
            play_again_button.pack()
        else:
            flag = False
            result_label.config(text=f"YOU LOSE\nThe number was {randomNumber}")
            play_again_button.pack()
    instruction_label = Label(main, text="In this difficulty, you have 1 try to guess a number from 1 to 100.")
    instruction_label.pack()
    guess_label = Label(main, text="Guess a number:")
    guess_label.pack()
    guess_entry = Entry(main)
    guess_entry.pack()
    check_button = Button(main, text="Check", command=check_guess)
    check_button.pack()
    result_label = Label(main, text="")
    result_label.pack()
    # Create play again button (hidden initially)
    play_again_button = Button(main, text="Play Again", command=modeSelector1)
introText = Label(main, text= "Welcome to NumGuessr", fg="#228c22")
introText.pack()
startButton = Button(main, text="Start", fg="#1035ac", command=modeSelector1) #Creates button widget
startButton.pack()
main.mainloop() #This tells Python to continually loop our ppython code (our GUI) and prevent it from closing right away
