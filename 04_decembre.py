with open('data/04_decembre.txt') as f:
    lines = [x[:-1] for x in f]

s = 0
s1 = 0
for k in range(len(lines)):
    data = lines[k].split(',')
    d1,d2 = data[0].split('-'),data[1].split('-')
    d1,d2 = list(map(int,d1)),list(map(int,d2))
    if (d1[0] >= d2[0] and d1[1] <= d2[1]) or (d1[0]<=d2[0] and d1[1]>=d2[1]):
        s += 1
    if not(d1[0] > d2[1] or d1[1] < d2[0]) :
        s1 += 1

print(s)
print(s1)
