import random

def roll():
  return random.randint(1,6)

while True:
  num_of_players = input('Enter the number of players(2 - 4): ')
  if num_of_players.isdigit():
    num_of_players = int(num_of_players)
    if 2 > num_of_players or num_of_players > 4:
      print("Enter a valid number")
    else:
      print("Enjoy the game!")
      break
  else:
    print("Enter a valid value.")

max_score = 30
players_score = [0 for _ in range(num_of_players)]

while max(players_score) < max_score:

  for player in range(num_of_players):
    if max(players_score) >= max_score:
      break
    while True:
      roll_or_not = input(f"Player {player + 1} Do you want to roll (y for yes)?: ")
      if roll_or_not.lower() != "y":
        break
      value = roll()
    
      if value == 1:
        players_score[player] = 0
        print(f"It's a 1! Turn done player {player + 1}!")
        break
      else:
        print("It's a", value)
      players_score[player] += value
      if players_score[player] >= max_score:
        break
      else:
        print(f"Your current score is {players_score[player]} points player {player + 1}")

print(f"The winner is player {players_score.index(max(players_score)) + 1} with a score of {max(players_score)}")

print(f"Final score table:\n {players_score}")