with open('data/06_decembre.txt') as f:
    lines = [x[:-1] for x in f]

for x in lines:
    c = 0
    for k in range(len(x)-3):
        y = x[k:k+4]
        z = x[k:k+14]
        if len(set(y)) == 4 and not(c):
            print(k+4)
            c = 1
        if len(set(z)) == 14:
            print(k+14)
            break