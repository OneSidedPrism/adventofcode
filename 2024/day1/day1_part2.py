with open('./2024/day1/input.txt', 'r') as f:
    locations = f.readlines()

left = []
right = []
pairs = []

for i in locations:
    i = i[:-1]
    locations_split = i.split("   ")
    left.append(int(locations_split[0]))
    right.append(int(locations_split[1]))

similarity_score = 0

for left_number in left:
    count = 0
    for right_number in right:
        if left_number == right_number:
            count += 1
    similarity_score += left_number * count

print(similarity_score)