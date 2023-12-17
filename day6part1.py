raw_data = []
with open('input.txt') as f:
    for line in f:
        data = line.strip().split(":")
        raw_data.append(list(map(int,data[1].strip().split())))
        
times = raw_data[0]
distance = raw_data[1]

ans = 1
for t,d in zip(times,distance):
    cnt = 0
    for hold in range(t+1):
        speed = hold
        travelDis = speed * (t - hold)
        if travelDis > d:
            cnt +=1
    ans *= cnt
print(ans)






