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

while len(left) > 0 and len(right) > 0:
    pairs.append([min(left), min(right)])
    left.remove(min(left))
    right.remove(min(right))

distance = 0

for pair in pairs:
    distance += abs(pair[0] - pair[1])

print(distance)