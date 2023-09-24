# max or min function

scores = input("Enter scores: ").split()
for i in range(0, len(scores)):
    scores[i] = int(scores[i])

print(scores)

max_score = 0

for score in scores:
    if score > max_score:
        max_score = score
print(f"Highest score in the class is {max_score}")
