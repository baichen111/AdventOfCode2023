data = []
with open("input.txt","r") as f:
    for line in f:
        cnt = 0
        nums = line.strip().split("|")
        winnings = nums[0].split(":")
        win_nums = [int(val) for val in winnings[1].split()]
        
        nums_have = [int(val) for val in nums[1].split()]
        lst = [value for value in win_nums if value in  nums_have]
        data.append(lst)

counter = len(data)*[1]   #[1,1,1,1,1,1 ...]
for i in range(len(counter)):
    win_num = len(data[i]) # how many times to copy
    repeat_num = counter[i] #how may times to repeat
    for r in range(repeat_num):
        for j in range(i+1,i+win_num+1):
            counter[j] += 1

print(sum(counter))  # part2 : 5659035
        
        
        
    



