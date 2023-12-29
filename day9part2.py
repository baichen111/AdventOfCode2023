datas = []
with open('input.txt') as f:
    for line in f:
        datas.append(list(map(int,line.strip().split())))    
        

def diffZero(data:list): #[0, 3, 6, 9, 12, 15]
    result = [data]
    while not all(list(map(lambda x:x==0,data))):        
        data = [data[i] - data[i-1] for i in range(1,len(data))]
        result.append(data)
    return result

ans = 0
for data in datas:
    results = list(reversed(diffZero(data)))
    c = 0
    for i in range(1,len(results)):
        diff = results[i][0] - results[i-1][0]
        results[i][0] = diff
        c = diff   
    ans += c
print(ans)  # part2:1022
