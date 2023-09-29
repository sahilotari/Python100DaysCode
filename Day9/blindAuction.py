import art
import os

print(art.logo)

# os.system("clear")  to clear the screen

auction = {}
should_run = True
while should_run:
    name = input("What is your name?\n")
    price = int(input("What is your Bid Price? $"))
    auction[name] = price

    runAgain = input("Are there any other bidders? 'yes' or 'no'\n")
    if runAgain == "yes":
        os.system("clear")
    else:
        should_run = False
        winnerName = ""
        bidAmt = 0
        for bidder in auction:
            if auction[bidder] > bidAmt:
                winnerName = bidder
                bidAmt = auction[bidder]
        print(f"Winner is {winnerName} with the maximum bid of ${bidAmt}")
