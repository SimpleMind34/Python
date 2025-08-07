import random
import time

OPERATORS = ["+", "-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
  left = random.randint(MIN_OPERAND,MAX_OPERAND)
  right = random.randint(MIN_OPERAND, MAX_OPERAND)
  operator = random.choice(OPERATORS)

  expr = f"{str(left)} {operator} {str(right)}"
  answer = eval(expr)  #evaluates a string as a python expression
  # print(f"{expr} = {answer}")
  return expr, answer

wrong = 0
input("Press anything to start!")
print("------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
   expr, answer = generate_problem()
   while True:
    guess = input(f"problem {i + 1} : {expr} = ")
    if guess == str(answer):
      break
    wrong += 1

end_time = time.time() 
total_time = end_time - start_time   
print("------------------------")
print(f"Nice work you finished in {round(total_time,2)} seconds")