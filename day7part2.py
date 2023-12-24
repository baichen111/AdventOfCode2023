from collections import Counter
data = {}
with open("input.txt") as f:
    for line in f:
        hand = line.split()[0]
        bid = int(line.split()[1])
        data[hand] = bid
        

class Hand:
    charRanking = "J23456789TQKA"
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
    vs = sorted(Counter(hand).items(),key=lambda x:x[1],reverse=True)
    if len(vs) == 1:
        return (hand,"Five")
    if len(vs) == 2:
        if vs[0][1] == 4 and vs[1][1] == 1:  #[('x',4),('y',1)]
            if vs[0][0] == 'J' or vs[1][0] == 'J':
                return (hand,"Five")
            return (hand,"Four")
        if vs[0][1] == 3 and vs[1][1] == 2:  #[('x',3),('y',2)]
            if vs[0][0] == 'J' or vs[1][0] == 'J':
                return (hand,"Five")
            return (hand,"Full")
    if len(vs) == 3:
        if vs[0][1] == 3 and vs[1][1] == 1 and vs[2][1] == 1:  #[('x',3),('y',1),('z',1)]
            if vs[0][0] == 'J' or vs[1][0] == 'J' or vs[2][0] == 'J':
                return (hand,"Four") 
            return (hand,"Three")
        if vs[0][1] == 2 and vs[1][1] == 2 and vs[2][1] ==1:  #[('x',2),('y',2),('z',1)]
            if vs[0][0] == 'J' or vs[1][0] == 'J':
                return (hand,"Four")
            if vs[2][0] == 'J':
                return (hand,"Full")
            return (hand ,"Two")
    if len(vs) == 4:
        if vs[0][1] == 2 and vs[1][1] == 1 and vs[2][1] == 1 and vs[3][1] ==1:   #[('x',2),('y',1),('z',1),('p',1)]
            if vs[0][0] == 'J' or vs[1][0] == 'J' or vs[2][0] == 'J' or vs[3][0] == 'J':
                return (hand,"Three")
            return (hand,"One")
    if len(vs) == 5:
        if vs[0][0] == 'J' or vs[1][0] == 'J' or vs[2][0] == 'J' or vs[3][0] == 'J' or vs[4][0] == 'J':
            return (hand,"One")
        return (hand , "High")
    
converted = [Convert(k) for k in data.keys()]
objs = [Hand(c) for c in converted]
sorted_objs = sorted(objs)

Sum = 0
for i in range(len(sorted_objs)):
    Sum +=data[sorted_objs[i].hand]*(i+1)

print(Sum)  #part2: 251037509
