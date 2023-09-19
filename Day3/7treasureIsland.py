print("Welcome to Treasure Island\nYour mission is to find treaure...")

leftOrRight = input("Left or Right? \n")
if leftOrRight == "Right":
    print("Game Over")
else:
    swimOrWait = input("Swim or Wait \n")
    if swimOrWait == "Swim":
        print("Game Over")
    else:
        door = input("Choose Door.. Blue or Yellow or Red \n")
        if door == "Red" or door == "Blue":
            print("Game Over")
        else:
            print("You Win")
