row1 = ["0", "0", "0"]
row2 = ["0", "0", "0"]
row3 = ["0", "0", "0"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

pos = input("Input the position you want to put the treasure: ")
rowNum = int(pos[1])
colNum = int(pos[0])

if rowNum <= 0 or rowNum > 3 or colNum <= 0 or colNum > 3:
    print("Enter valid index...")
else:
    map[rowNum - 1][colNum - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")
