data = []
with open("input.txt") as f:
    for line in f:
        data.append(line.strip())

def find_S():
    for i,line in enumerate(data):
        for j,pipe in enumerate(line):
            if pipe == "S":
                return i,j
            
def isValid_neighbor(cur_pipe:str, offset:list, n_row:int , n_col:int):  #check if the neighbor is a valid pipe
    if cur_pipe == "":
        if offset[0] == 1:
            if data[n_row][n_col] == "|" or data[n_row][n_col] == "L" or data[n_row][n_col] == "J" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        elif offset[0] == -1:
            if data[n_row][n_col] == "|" or data[n_row][n_col] == "F" or data[n_row][n_col] == "7" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        elif offset[1] == 1:
            if data[n_row][n_col] == "-" or data[n_row][n_col] == "J" or data[n_row][n_col] == "7" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        elif offset[1] == -1:
            if data[n_row][n_col] == "-" or data[n_row][n_col] == "F" or data[n_row][n_col] == "L" or data[n_row][n_col] == "S":
                return True
            else:
                return False
                
    elif cur_pipe == "|":
        if offset[0] == 1:
            if data[n_row][n_col] == "L" or data[n_row][n_col] == "J" or  data[n_row][n_col] == "|"or data[n_row][n_col] == "S":
                return True
            else:
                return False
        elif offset[0] == -1:
            if data[n_row][n_col] == "F" or data[n_row][n_col] == "7" or  data[n_row][n_col] == "|" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        else:
            return False
    elif cur_pipe == "-":
        if offset[1] == 1:
            if data[n_row][n_col] == "J" or data[n_row][n_col] == "7" or data[n_row][n_col] == "-" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        elif offset[1] == -1:
            if data[n_row][n_col] == "L" or data[n_row][n_col] == "F" or data[n_row][n_col] == "-" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        else:
            return False
    elif cur_pipe == "L":
        if offset[1] == 1:
            if data[n_row][n_col] == "J" or data[n_row][n_col] == "7" or data[n_row][n_col] == "-" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        elif offset[0] == -1:
            if data[n_row][n_col] == "|" or data[n_row][n_col] == "F" or data[n_row][n_col] == "7" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        else:
            return False
    elif cur_pipe == "J":
        if offset[1] == -1:
            if data[n_row][n_col] == "-" or data[n_row][n_col] == "F" or data[n_row][n_col] == "L" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        elif offset[0] == -1:
            if data[n_row][n_col] == "|" or data[n_row][n_col] == "F" or data[n_row][n_col] == "7" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        else:
            return False
    elif cur_pipe == "7":
        if offset[1] == -1:
            if data[n_row][n_col] == "-" or data[n_row][n_col] == "F" or data[n_row][n_col] == "L" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        elif offset[0] == 1:
            if data[n_row][n_col] == "|" or data[n_row][n_col] == "L" or data[n_row][n_col] == "J" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        else:
            return False
    elif cur_pipe == "F":
        if offset[1] == 1:
            if data[n_row][n_col] == "-" or data[n_row][n_col] == "J" or data[n_row][n_col] == "7" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        elif offset[0] == 1:
            if  data[n_row][n_col] == "|" or data[n_row][n_col] == "L" or data[n_row][n_col] == "J" or data[n_row][n_col] == "S":
                return True
            else:
                return False
        else:
            return False
    else:
        return False
                     
offsets = [[0,1],[1,0],[0,-1],[-1,0]]
start_row,start_col = find_S()
prev_visited = ()
cur_pipe = ""
count = 0
while cur_pipe != "S":
    for offset in offsets:
        neighbor_row = offset[0] + start_row
        neighbor_col = offset[1] + start_col
        if prev_visited == (neighbor_row,neighbor_col):
            continue
        if (neighbor_row > len(data) - 1 or neighbor_row < 0) or (neighbor_col > len(data[0]) -1 or neighbor_col < 0):
            continue
        
        if isValid_neighbor(cur_pipe,offset,neighbor_row,neighbor_col):
            cur_pipe = data[neighbor_row][neighbor_col]
            prev_visited = (start_row,start_col)
            start_row = neighbor_row
            start_col = neighbor_col
            count += 1
            break
        else:
            continue

print(count/2)    #part1: 6968   
            
            
            
            
        









