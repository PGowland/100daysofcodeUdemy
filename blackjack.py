############### Blackjack Project #####################



############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
cards = {
  'A': 11,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  '10': 10,
  'J': 10,
  'Q': 10,
  'K': 10,
}
player_hand = [random.choice(list(cards.keys())), random.choice(list(cards.keys())) ]
dealer_hand = [random.choice(list(cards.keys())), random.choice(list(cards.keys())) ]
player_score = cards[player_hand[0]] + cards[player_hand[1]]
dealer_score = cards[dealer_hand[0]] + cards[dealer_hand[1]]
player_ace_count = 0
dealer_ace_count = 0

if 'A' in player_hand:
  player_ace_count += 1
if 'A' in dealer_hand:
  dealer_ace_count += 1


print(player_hand)
print(dealer_hand[0] + " _?")


def stick_or_twist(hand):
  new_card = random.choice(list(cards.keys()))
  hand.append(new_card)
  print(hand)
  
  
    
while player_score  <= 21:
  hit_me = input("Would you like another card? Please enter 'y' or 'n'\n")
  if hit_me == 'y':
    stick_or_twist(player_hand)
    player_score += cards[player_hand[len(player_hand)-1]]
    if player_hand[len(player_hand)-1] == 'A':
      player_ace_count += 1
    if player_score > 21 and player_ace_count > 0:
      player_score -= 10
      player_ace_count -= 1
    
  else:
    break

print(dealer_hand)


  
while dealer_score < player_score and player_score <= 21 and dealer_score <= 21:
  stick_or_twist(dealer_hand)
  dealer_score += cards[dealer_hand[len(dealer_hand)-1]]
  if dealer_hand[len(dealer_hand)-1] == 'A':
      dealer_ace_count += 1
  if dealer_score > 21 and dealer_ace_count > 0:
      dealer_score -= 10
      dealer_ace_count -= 1
  
 



    
print(f"\nThe player's hand is {player_hand} and the dealer's hand is {dealer_hand}\nTHIS MEANS:")

if player_score > 21:
  print("You Lose due to bust!")
elif player_score <= dealer_score >21:
  print("You Win due to dealer bust")
elif player_score > dealer_score:
  print("You Win, due to higher score")
else:
  print("You lose, due to lower or equal score")
  
  


