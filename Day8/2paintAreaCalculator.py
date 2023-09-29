import math


def paintCalc(height, width, cover):
    area = height * width
    cans = math.ceil(float(area) / cover)
    return cans


test_h = int(input("Height of wall: "))
test_w = int(input("width of wall: "))

coverage = 5
cans = paintCalc(height=test_h, width=test_w, cover=coverage)
print(f"You will need {cans} cans to paint the wall..")
