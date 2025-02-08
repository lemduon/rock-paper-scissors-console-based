import random

choices = [
  "rock",
  "paper",
  "scissor",
]

while True:
  com_choice = random.choice(choices)
  choice = input("Choose between rock, paper, scissor (q to quit): ").lower()
  if choice == 'q':
    break
  elif com_choice == 'rock' and choice == 'scissor':
    print(f"Computer's choice: {com_choice}")
    print("Computer wins!")
  elif com_choice == 'rock' and choice == 'paper':
    print(f"Computer's choice: {com_choice}")
    print("You win!")
  elif com_choice == 'paper' and choice == 'scissor':
    print(f"Computer's choice: {com_choice}")
    print("You win!")
  elif com_choice == 'paper' and choice == 'rock':
    print(f"Computer's choice: {com_choice}")
    print('Computer wins!')
  elif com_choice == 'scissor' and choice == 'rock':
    print(f"Computer's choice: {com_choice}")
    print('You win!')
  elif com_choice == 'scissor' and choice == 'paper':
    print(f"Computer's choice: {com_choice}")
    print('Computer wins!')
  elif com_choice == choice:
    print(f"Computer's choice: {com_choice}")
    print("Stalemate!")
  else:
    print("Invalid Response!")
