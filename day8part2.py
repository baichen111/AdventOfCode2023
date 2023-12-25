from itertools import cycle
import math
data = []
with open("input.txt") as f:
    for line in f:
        data.append(line.strip())
directions = data[0]
maps = data[2:]

ls = [m.split("=") for m in maps]
ls = [[x[0].strip(),x[1].split(",")] for x in ls]
maps = {x[0]:(x[1][0][-3:],x[1][1][1:4]) for x in ls}
starts = [k for k in list(maps.keys()) if k.endswith("A")]  # all starting element ends with "A"

def counter(start):
    count = 0
    for lr in cycle(directions):
        if start[2] == 'Z':
            break
        if lr == 'L':
            start = maps[start][0]
        elif lr == 'R':
            start = maps[start][1]
        count += 1
    return count

steps = [counter(start) for start in starts]

#LCM
print(math.lcm(*steps)) #part2: 14299763833181
