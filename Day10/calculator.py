import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)

    stop = False

    while not stop:

        operationSym = input("Pick and operation ")

        num2 = float(input("What's the next number?: "))

        function = operations[operationSym]

        answer = function(num1, num2)

        print(f"{num1} {operationSym} {num2} = {answer}")

        shouldRun = input(
            f"Type 'y' to continue calculation with {answer}, or type 'n' to start new calculation, or 'exit' to exit calculator: ")
        if shouldRun == "n":
            stop = True
            calculator()
        elif shouldRun == "y":
            num1 = answer
        else:
            return


calculator()
