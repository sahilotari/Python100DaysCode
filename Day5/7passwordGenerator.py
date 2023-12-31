import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to Password Generator")
numLetters = int(input("Enter number of letters would you like : "))
numSymbols = int(input("Enter number of symbols you want: "))
numNumbers = int(input("How many numbers would you like: "))

# Easy level
# password = ""
# for char in range(1, numLetters + 1):
#     password += random.choice(letters)

# for char in range(1, numSymbols + 1):
#     password += random.choice(symbols)

# for char in range(1, numNumbers + 1):
#     password += random.choice(numbers)

# print(password)

# Hard level
password = []
for char in range(1, numLetters + 1):
    password += random.choice(letters)

for char in range(1, numSymbols + 1):
    password += random.choice(symbols)

for char in range(1, numNumbers + 1):
    password += random.choice(numbers)

random.shuffle(password)
print(password)

passWd = ""
for char in password:
    passWd += char

print(passWd)
