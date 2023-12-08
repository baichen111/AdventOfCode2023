data = []
with open("input.txt","r") as f:
    for line in f:  
        data.append(line.strip())
        
def find_entire_number(data,surrounding,r,c):  # find the entire number and the index position for each digit of that number
    pos = []  # to record each digit's position
    pos.append((r,c))
    left = c - 1
    right = c + 1
    num = surrounding
    while data[r][left].isdigit() and left >=0:
        pos.append((r,left))
        num += data[r][left]
        left -= 1
        if left < 0:
            break
    num = num[::-1]
    while data[r][right].isdigit() and right <= len(data[0])-1:
        pos.append((r,right))
        num += data[r][right]
        right += 1
        if right >  len(data[0])-1:
            break
    pos.sort(key=lambda x:x[1])
    return num,tuple(pos)
   
num_pos = set() 
for row,line in enumerate(data):
    for col,char in enumerate(line):
        if not char == "." and not char.isdigit():
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    r = row + i
                    c = col + j
                    surrouding = data[r][c]
                    if  surrouding != char and surrouding != ".":
                        #find entire number with its positions and add them to a set
                        num_pos.add(find_entire_number(data,surrouding,r,c))
nums = [num[0] for num in num_pos]
ans = sum(list(map(int,nums)))   
print(ans)     #part 1: 526404  
