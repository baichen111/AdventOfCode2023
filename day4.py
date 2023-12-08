points = 0
with open("input.txt","r") as f:
    for line in f:
        cnt = 0
        nums = line.strip().split("|")
        winnings = nums[0].split(":")
        win_nums = winnings[1].split()
        win_nums = [int(val) for val in win_nums]
        
        nums_have = [int(val) for val in nums[1].split()]
        
        lst = [value for value in win_nums if value in  nums_have]
        print("len lst: ",len(lst))
        if not len(lst) == 0:
            cnt = 2**(len(lst)-1) 
        points += cnt
print(points) #part1: 24160