import random

user_score = 0
computer_score = 0
choices = {"r":"rock","p":"paper","s":"scissors"}
victory = {"r":"p", "p":"s", "s":"r"}
while True:
  user_choice = input("Please choose r for rock, p for paper or s for scissors or q to quit the game: ").lower()
  if user_choice == "q":
    break
  if user_choice not in choices :
    continue
  computer_choice = random.choice(list(choices.keys()))
  if computer_choice == user_choice:
    print("It's a tie, try again!")
    continue
  elif user_choice == victory[computer_choice]:
    user_score += 1
    print(f"You won! the computer choice was {choices[computer_choice]}")
  else: 
    computer_score += 1
    print(f"You lost! the computer choice was {choices[computer_choice]}")

print(f"Thanks for playing, your score = {user_score}\n computer score = {computer_score} ")