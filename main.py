rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player_number = int(input("Type 0 for rock, 1 for paper, and 2 for scissors \n"))
computer_number = random.randint(0,2)

result_list = [rock, paper, scissors] 
print(result_list[player_number] + "\n computer chose: \n" + result_list[computer_number])

if computer_number - player_number == 0:
  print("The match ended in a tie.")
elif computer_number - player_number == 1 or computer_number - player_number == -2:
  print("You have lost the match.")
else:
  print("You have won the match!.")

 
  

 