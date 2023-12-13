
raw_data = []
with open("input.txt","r") as f:
    inputs = f.read().split("\n\n")  #split by new empty line
    raw_data.append(inputs[0])
    for input in inputs[1:]:
        raw_data.append(input.split("\n"))

seeds = list(map(int,raw_data[0].split()[1:]))
maps = [m[1:] for m in raw_data[1:]]
maps = [list(map(str.split,mp)) for mp in maps]


output = []
for x in maps:
    k=[]
    for y in x:
         k.append(list(map(int,y)))
    output.append(k)

ans = []
for src in seeds:
    for src_tgt in output:
        for interval in src_tgt:
            src_start = interval[1]
            src_end = src_start + interval[2]
            if src_start <= src <src_end:
                target = interval[0] + src - src_start
                break
            target = src
        src = target    
    ans.append(target)
print(min(ans)) # part1: 174137457















