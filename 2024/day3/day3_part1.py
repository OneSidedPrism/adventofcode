import re

with open('./2024/day3/input.txt', 'r') as f:
    memory = f.read()

mul_list = []
mul_total = 0

pattern = r'mul\([1-9][0-9]{0,2}\,[1-9][0-9]{0,2}\)'

for mul in re.findall(pattern, memory):
    mul = mul.strip(r'mul\(\)')
    mul = mul.split(',')
    mul = [int(num) for num in mul]
    mul_list.append(mul)

for pair in mul_list:
    mul_total += pair[0] * pair[1]

print(mul_total)