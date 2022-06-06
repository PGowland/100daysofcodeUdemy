print("There is a fork in the road, would you like to take the left path or the right?")
left_or_right = input().lower()
if left_or_right == "right":
  print("You step off a cliff and die, \n GAME OVER!")
else: print("You take the left path until you arrive at the banks of a river. Do you try to swim across or wait for a boat?")
swim_or_wait = input().lower()
if swim_or_wait == "swim":
  print("The current pulls you under, and you drown to death \n GAME OVER!")
else: print("On the other side of the river are two doors, one red, the other blue, which do you pick?")
red_or_blue = input().lower()
if red_or_blue == "red":
  print("Flames shoot out and burn you to death. \n GAME OVER!")
else:
  print("You have found the treasure. \n YOU WIN!")
  