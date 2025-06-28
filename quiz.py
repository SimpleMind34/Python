import requests
import random
import html


num_of_questions = input("How many questions do you want? ")

url = f"https://opentdb.com/api.php?amount={num_of_questions}&category=9&difficulty=medium&type=multiple"
response = requests.get(url)
data = response.json()
results = data['results']
score = 0
for result in results:
  question = result['question']
  correct = result['correct_answer']
  incorrect = result['incorrect_answers']
  options  = incorrect + [correct]
  random.shuffle(options)
  print(f"{html.unescape(question)}")
  i = 1
  for option in options:
    print(f"{i}. {html.unescape(option)}\n")
    i = i + 1

  answer = int(input("choose an answer (1-4): "))
  chosen_option = options[answer - 1]
  if chosen_option == correct:
    score = score + 1
    print(f"The answer is correct, your score is {score}")
    
  else: print(f"The answer is wrong, the correct answer is {correct}")

print(f"Thanks for playing, your total score = {score}")



  