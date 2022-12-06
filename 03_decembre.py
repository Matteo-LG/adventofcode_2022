with open('data/03_decembre.txt') as f:
    lines = [x[:-1] for x in f]


s = 0
for x in lines:
    n = len(x)
    x1 = x[:int(n/2)]
    x2 = x[int(n/2):]
    c = False
    for el in x1:
        for el2 in x2:
            if el == el2:
                num = ord(el)
                if num < 97:
                    num -= 38
                else :
                    num -= 96
                c = True
                break
        if c : break
    s += num
print(s)

s = 0

for k in range(int(len(lines)/3)):
    c = False
    el1 = lines[3*k]
    el2 = lines[3*k+1]
    el3 = lines[3*k+2]
    for x1 in el1:
        for x2 in el2:
            for x3 in el3:
                if x1 == x2 == x3:
                    num = ord(x1)
                    if num < 97:
                        num -= 38
                    else :
                        num -= 96
                    c = True
                    break
            if c : break
        if c : break
    s += num

print(s)

