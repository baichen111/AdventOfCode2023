
times = ''
distance = ''
raw_data = []
with open("input.txt") as f:
    for line in f:
        data = line.strip().split(":")
        raw_data.append(data[1].strip().split())

for t in raw_data[0]:
    times += t

for d in raw_data[1]:
    distance += d

Time = int(times)
Distance = int(distance)

cnt = 0
for hold in range(Time+1):
    speed = hold
    travelDist = speed * (Time - hold)
    if travelDist > Distance:
        cnt += 1
print(cnt) # part2: 46173809









