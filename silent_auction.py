from replit import clear
#HINT: You can call clear() to clear the output in the console.
bids = {}
continue_decision = ""
bidders_remaining = True

while bidders_remaining:
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n$"))
  bids[name] = bid
  continue_decision = input("Are there still bidders left to input? please answer 'yes' or 'no'\n")
  if continue_decision == "yes":
    clear()
  if continue_decision == "no":
    bidders_remaining = False

max_value = max(bids.values())
max_key = max(bids, key=bids.get)

print(f"The winner is {max_key}, with a winning bid of ${max_value}")

