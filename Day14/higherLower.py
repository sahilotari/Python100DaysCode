import art
import random
from game_data import data
import os


def format_data(account):
    return f'{account["name"]}, a {account["description"]}, from {account["country"]}'


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
shouldRun = True
accountB = random.choice(data)
while shouldRun:

    print(art.logo)

    accountA = accountB
    accountB = random.choice(data)

    while accountA == accountB:
        accountB = random.choice(data)

    print(f"Compare A: {format_data(accountA)}")
    print(art.vs)

    print(f"Against B: {format_data(accountB)}")

    # Ask user for guess
    guess = input("Who has more folloers? Type 'A' or 'B': ").lower()

    # Check if they ot correct
    a_followers = accountA["follower_count"]
    b_followers = accountB["follower_count"]

    isCorrect = check_answer(guess, a_followers, b_followers)

    os.system("clear")

    if isCorrect:
        score += 1
        print(f"You are right!!. Current Score: {score}.")

    else:
        print(f"Sorry, you are wrong!. Final Score: {score}")
        shouldRun = False
