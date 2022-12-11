import numpy as np

with open('data/08_decembre.txt') as f:
    lines = [x[:-1] for x in f]

#lines = ["30373","25512","65332","33549","35390"]

val = np.array([[0]*len(lines[0]) for n in range(len(lines))])
l = (['' for n in range(len(lines))])
k = -1
s = 0
s += 2*len(lines) + 2*len(lines[0]) - 4

for x in lines:
    k += 1
    maxi = x[0]
    l[0] += x[0]
    l[-1] += x[-1]
    for j in range(1,len(x)-1):
        l[j] += x[j]
        if x[j] > maxi and k not in [0,len(x)-1]:
            maxi = x[j]
            s += 1
            val[k,j] = 1

    maxi = x[len(x)-1]
    for j in range(len(x)-2,0,-1):
        if x[j] > maxi:
            maxi = x[j]
            if val[k,j] == 0 and k not in [0,len(x)-1]:
                val[k,j] = 1
                s += 1

for k in range(len(lines[0])):
    x = l[k]
    maxi = x[0]
    for j in range(1,len(x)-1):
        if x[j] > maxi:
            maxi = x[j]
            if val[j,k] == 0 and k not in [0,len(x)-1]:
                s += 1
                val[j,k] = 1  

    maxi = x[len(x)-1]
    for j in range(len(x)-2,0,-1):
        if x[j] > maxi:
            maxi = x[j]
            if val[j,k] == 0 and k not in [0,len(x)-1]:
                val[j,k] = 1
                s += 1

print(s)

best_sc = 0
case = 0,0

for k in range(1,len(lines)-1):
    row = lines[k]
    for j in range(1,len(lines[0])-1):
        sc = 0
        column = l[j]
        
        maxi, sc_1 = '0', 0
        for i in range(j+1,len(lines[0])):
            if row[j] > row[i]:
                maxi = row[i]
                sc_1 += 1
            else:
                if row[j] <= row[i] : sc_1 += 1
                break
        
        maxi, sc_2 = '0', 0
        for i in range(j-1,-1,-1):
            if row[j] > row[i]:
                maxi = row[i]
                sc_2 += 1
            else:
                if row[j] <= row[i] : sc_2 += 1
                break

        maxi, sc_3 = '0', 0
        for i in range(k+1,len(lines)):
            if row[j] > column[i]:
                maxi = column[i]
                sc_3 += 1
            else:
                if row[j] <= column[i] : sc_3 += 1
                break

        maxi, sc_4 = '0', 0
        for i in range(k-1,-1,-1):
            if row[j] > column[i]:
                maxi = column[i]
                sc_4 += 1
            else:
                if row[j] <= column[i] : sc_4 += 1
                break
        
        sc += sc_1*sc_2*sc_3*sc_4
        if sc > best_sc:
            best_sc = sc
            #print(k,j)
            #print(sc_1,sc_2,sc_3,sc_4)

print(best_sc)
