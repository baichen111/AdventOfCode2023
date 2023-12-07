req = {'red':12,'green':13,'blue':14}
score = 0
with open("input.txt","r") as f:
    for line in f:
        game = line.strip("\n").split(":")
        gameNum = int(game[0].split()[1])
        grabs = game[1].split(";")
        flag = True
        for grab in grabs:
            cubes = grab.split(",")
            for cube in cubes:
                play = cube.strip().split()
                num = int(play[0])
                color = play[1]
                if req[color] < num:
                    flag = False
                
        if flag :
            score += gameNum
print(score) #part1 : 2771