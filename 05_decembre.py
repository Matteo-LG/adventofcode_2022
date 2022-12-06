import numpy as np
import copy

with open('data/05_decembre.txt') as f:
    lines = [x[:-1] for x in f]

piles = [[] for i in range(9)]
s = ''
s1 = ''
for k in range(7,-1,-1):
    data = lines[k]
    for j in range(9):
        if data[4*j+1] != ' ':
            piles[j].append(data[4*j+1])

piles2 = copy.deepcopy(piles)

for k in range(10,len(lines)):
    move = lines[k]
    move = move.replace('move ','').replace('from ','').replace('to ','').split(' ')
    n,p1,p2 = map(int,move)
    for j in range(n):
        piles[p2-1].append(piles[p1-1].pop())
    piles2[p2-1] += piles2[p1-1][-n:]
    piles2[p1-1] = piles2[p1-1][:-n]

for p in piles:
    s += p[-1]
for p in piles2:
    s1 += p[-1]

print(s)
print(s1)