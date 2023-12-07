from collections import defaultdict

cnt = defaultdict(int)
ans = 0
with open("input.txt","r") as f:
    for line in f:
        game = line.strip("\n").split(":")
        gameNum = int(game[0].split()[1])
        grabs = game[1].split(";")
        power = 1
        for grab in grabs:
            cubes = grab.split(",")
            for cube in cubes:
                play = cube.strip().split()
                num = int(play[0])
                color = play[1]
                if num > cnt[color]:
                    cnt[color] = num
        val = list(cnt.values())
        for i in val:
            power *=i
        cnt.clear()
        ans += power
print(ans)  #part2 : 70924
