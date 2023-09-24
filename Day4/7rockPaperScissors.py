import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]
myChoice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 3 for Scissors.\n")
)

compChoice = random.randint(0, 2)

print(f"Your choice: \n{choices[myChoice]}\n")
print(f"Computer's choice:\n{choices[compChoice]}")

if myChoice == 0:
    if compChoice == 0:
        print("Tie")
    elif compChoice == 1:
        print("Computer won")
    else:
        print("You won")
elif myChoice == 1:
    if compChoice == 0:
        print("You Won")
    elif compChoice == 1:
        print("Tie")
    else:
        print("Computer Won")
else:
    if compChoice == 0:
        print("Computer Won")
    elif compChoice == 1:
        print("You Won")
    else:
        print("Tie")
