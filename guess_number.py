#Python Number Guessing Game

import random

print("Python Number Guessing Game")
print("Choose Difficulty level: ")
print("1. Easy   (1-50)")
print("2. Medium (1-100)")
print("3. Hard   (1-500)")

choice = input("Enter difficulty level: ")

if choice == "1":
    lowest_num, highest_num = 1, 50
    print("Easy Level")
elif choice == "2":
    lowest_num, highest_num = 1, 100
    print("Medium Level")
elif choice == "3":
    lowest_num, highest_num = 1, 500
    print("Hard Level")
else:
    print("Invalid choice!! Defaulting to medium level")
    lowest_num, highest_num = 1, 100

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT!! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")