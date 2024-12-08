with open('./day 1/input.txt', 'r') as input:
    locations = input.readlines()

left = []
right = []
pairs = []

for i in locations:
    i = i[:-1]
    locations_split = i.split("   ")
    left.append(locations_split[0])
    right.append(locations_split[1])

while len(left) > 0 and len(right) > 0:
    pairs.append([min(left), min(right)])
    left.remove(min(left))
    right.remove(min(right))

distance = 0

for pair in pairs:
    distance += abs(int(pair[0]) - int(pair[1]))

print(distance)