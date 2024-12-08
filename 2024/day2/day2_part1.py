with open('./2024/day2/input.txt', 'r') as f:
    reports = f.read().splitlines()

safe_reports = 0

for report in reports:
    report = [int(report) for report in report.split()]
    if sorted(report) == report or sorted(report, reverse=True) == report:
        delta = [j-i for i, j in zip(report[:-1], report[1:])]
        if all(x in (-3,-2,-1,1,2,3) for x in delta):
            safe_reports += 1

print(safe_reports)