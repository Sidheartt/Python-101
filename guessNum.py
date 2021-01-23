#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random 
from art import logo
print(logo)

a = (random.randint(0,100))


diff=input("Wan it easy or hard ?:")

  
if diff == "easy":
  print("you get 10 Attempts")
  for x in range(0,10):
    guess=int(input("guess a number: "))
    if guess == a:
      print("You Won ")
    elif guess < a:
      print("too low")
    elif guess > a:
      print("Too High")

elif diff == "hard":
  print("you get 5 attempts") 
  for x in range(0,5):
    guess=int(input("guess a number: "))
    if guess == a:
      print("You Won ")
    elif guess < a:
      print("too low")
    elif guess > a:
      print("Too high")





