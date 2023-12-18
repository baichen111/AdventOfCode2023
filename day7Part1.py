from collections import Counter
data = {}
with open("input.txt") as f:
    for line in f:
        hand = line.split()[0]
        bid = int(line.split()[1])
        data[hand] = bid
        

class Hand:
    charRanking = "23456789TJQKA"
    ranking = ["High","One","Two","Three","Full","Four","Five"]
    def __init__(self,handType:tuple) -> None:
        self.hand = handType[0]
        self.Type = handType[1]

    def __lt__(self,other):
        if other.Type == self.Type:
            for s,o in zip(self.hand,other.hand):
                if not o == s:              
                    return Hand.charRanking.index(s) < Hand.charRanking.index(o)
        else:
            return Hand.ranking.index(self.Type) < Hand.ranking.index(other.Type)

def Convert(hand:str):
    counter = Counter(hand)
    vs = sorted(list(counter.values()),reverse=True)
    if len(vs) == 1:
        return (hand,"Five")
    if len(vs) == 2:
        if vs[0] == 4 and vs[1] == 1:
            return (hand,"Four")
        if vs[0] == 3 and vs[1] == 2:
            return (hand,"Full")
    if len(vs) == 3:
        if vs[0] == 3 and vs[1] == 1 and vs[2] == 1:
            return (hand,"Three")
        if vs[0] == 2 and vs[1] == 2 and vs[2] ==1:
            return (hand ,"Two")
    if len(vs) == 4:
        if vs[0] == 2 and vs[1] == 1 and vs[2] == 1 and vs[3] ==1:
            return (hand,"One")
    if len(vs) == 5:
        return (hand , "High")
    
converted = [Convert(k) for k in data.keys()]
objs = [Hand(c) for c in converted]
sorted_objs = sorted(objs)

Sum = 0
for i in range(len(sorted_objs)):
    Sum +=data[sorted_objs[i].hand]*(i+1)

print(Sum)  #part1: 250602641
        