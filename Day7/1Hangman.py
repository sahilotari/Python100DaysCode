import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = ["ardvark", "baboon", "camel"]

# 1. Randomly choose word
word = random.choice(word_list)

# Set lives equal to 6
lives = 6


# make display list
display = []

for letter in word:
    display += "_"
print(display)


end_of_game = False

# 2 ask the user to guess char
while not end_of_game:
    guess = input("Guess the letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")

    # check if letter is present
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = word[i]

    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Loose!")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(stages[lives])
