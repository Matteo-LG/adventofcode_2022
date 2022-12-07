with open('data/07_decembre.txt') as f:
    lines = [x[:-1] for x in f]

s = 0
size = {'root_root':0}
parent = {'root_root':'root_root'}
dir_act = 'root_root'

for x in lines:
    if x[:4] == '$ cd':
        if x[5] == '/':
            dir_act = 'root_root'
        elif x[5] == ".":
            dir_act = parent[dir_act]
        else:
            nv = dir_act + ' ' + x[5:]
            if not (nv in size):
                size[nv] = 0
                parent[nv] = dir_act
            dir_act = nv

    elif x[:4] != '$ ls' and x[0] != 'd':
        x = x.split()
        sz = int(x[0])
        size[dir_act] += sz
        mem = dir_act
        while mem != parent[mem]:
            mem = parent[mem]
            size[mem] += sz

for x in size:
    if size[x] <= 100000 :
        s += size[x]

print(s)

val = size['root_root'] - 40000000
poss = sorted(list(size.values()))
for x in poss:
    if x >= val:
        print(x)
        break
