inputs = []
with open("input.txt","r") as f:
    for line in f:
        inputs.append(line.strip('\n'))

def digits1(text):
    for i in text:
        if i.isdigit():
            first = i
            break
    for j in text[::-1]:
        if j.isdigit():
            last = j
            break
    return int(first+last)

def digits2(text):
    d = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","zero":"0"}
    newStr = ""
    for i in range(len(text)): 
        for numStr in d.keys():
            if text.startswith(numStr,i):
                newStr += d[numStr]
                continue
        else:
            newStr += text[i]
    print("newStr: ",newStr)
    return digits1(newStr)


    

if __name__ == '__main__':
    s1 = 0
    s2 = 0
    for txt in inputs:
        s1 += digits1(txt)
        s2+=digits2(txt)
    print(s1)  # part1 : 55130
    print(s2) #part2: 54985
    
        
