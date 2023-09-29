def greet():
    print(f"Helllo")
    print(f"How to you do?")
    print("Isn't the weather nice today?")


def greetWithName(name):
    print(f"Helllo {name}")
    print(f"How to you do {name}?")
    print("Isn't the weather nice today?")


greet()
greetWithName("Sahil")

# parameter - variable name passed to function
# argument - actual value of that variable.


def greetWith(name, location):
    print(f"Helllo {name}")
    print(f"How to you do {name}?")
    print(f"Isn't the weather nice today in {location}?")


greetWith("Sahil", "Vaduj")  # positional argument

# keyword argument
greetWith(location="Vaduj", name="Sahil")
