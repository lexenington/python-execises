# The computer will pick a number between 1 and 100. The purpose of the game is to guess the number the computer picked in as few guesses as possible.
import random

print("Time to play the Guessing Games \n You have five (5) tries only")

# Computer selects a random number
rand_num = random.randint(1, 101)
guess = int(input("Enter a number between 1 and 100: "))
count = 0

while rand_num != guess:
    count += 1
    if guess > rand_num:
        guess = int(input("Too high. Try again "))
    else:
        guess = int(input("Too low. Try again "))

    if count == 5:
        print("You had 5 tries and failed! Better Luck next time")
        break

if int(guess) == rand_num:
    success = f"Congratulations!! You got the right answer after guessing {count} time(s) "
    print(success)
