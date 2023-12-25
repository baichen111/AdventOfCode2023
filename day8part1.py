from itertools import cycle
data = []
with open("input.txt") as f:
    for line in f:
        data.append(line.strip())
directions = data[0]
maps = data[2:]

ls = [m.split("=") for m in maps]
ls = [[x[0].strip(),x[1].split(",")] for x in ls]
maps = {x[0]:(x[1][0][-3:],x[1][1][1:4]) for x in ls}

#logic body
start = 'AAA'
count = 0
for lr in cycle(directions):
    if start == 'ZZZ':
        break
    if lr == 'L':
        start = maps[start][0]
    elif lr == 'R':
        start = maps[start][1]
    count += 1
print(count) #part1: 18157