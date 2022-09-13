#Number Guessing Game Objectives

   
import random
answer = random.randrange(0,101)
print("Welcome to the number guessing game.\nThe number will always be an integer.\n")
difficulty= input("Choose a difficulty. Type 'easy' or 'hard'\n")
if difficulty == 'easy':
  lives = 10
else:
  lives = 5

def high_low(guess, answer):
  if guess > answer:
    print("Too high\n")
   
  else:
    print("Too low\n")
    
    
guess = int(input("Make a guess:\n"))
while guess != answer:
  high_low(guess, answer)
  lives -= 1
  if lives == 0:
    print("You have ran out of lives, GAME OVER!!!")
    break
  guess = int(input("Make another guess:"))
  

if guess == answer:
  print(f"Well done, you guessed correctly, the answer was {answer}")


