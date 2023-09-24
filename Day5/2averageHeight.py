heights = input("Input a list of students heights ").split()

for i in range(0, len(heights)):
    heights[i] = int(heights[i])
print(heights)

sum = 0
cnt = 0
for height in heights:
    sum += height
    cnt += 1
avg_height = round(float(sum) / cnt)
print(avg_height)
