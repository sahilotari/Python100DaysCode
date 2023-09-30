import random
import art
print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

chances = 0
if difficulty == "hard":
    chances = 5
elif difficulty == "easy":
    chances = 10

number = random.randint(1, 100)

while chances > 0:
    print(f"You have {chances} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print("You won !!!")
        break
    elif guess < number:
        print("Too low...\nGuess again")
        chances -= 1
    else:
        print("Too High....\nGuess again")
        chances -= 1

if chances == 0:
    print("You ran out of chances... You lose")
