import random

random_number = random.randint(1,9)
shots = 5

print(f"Can you guess this number between 1 and 9, you have {shots} shots ")

guess = int(input("What is your guess? "))
while guess != random_number:
  if shots == 0:
    print(f'you are out of shots, the correct answer was {random_number}')
    break
  if guess == random_number:
    print(f"Correct! it took you {shots} shots to crack it")
    break
  if guess < random_number:
    shots -= 1
    guess = int(input(f"to low, you have {shots} shots left, try again: "))
  if guess > random_number:
    shots -= 1
    guess = int(input(f"to high, you have {shots} shots left, try again: "))
if random_number == guess:
  print(f"Correct! it took you {shots} shots to crack it")
