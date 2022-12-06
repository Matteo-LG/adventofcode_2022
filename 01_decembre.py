with open('01_decembre.txt') as f:
    lines = [x[:-1] for x in f]

max1,max2,max3 = 0,0,0
tmp = 0
for x in lines:
    if x == '':
        if tmp > max1 : 
            max1,max2,max3 = tmp,max1,max2
        elif tmp > max2:
            max2,max3 = tmp,max2
        elif tmp > max3:
            max3 = tmp
        tmp = 0
    else:
        tmp += int(x)

print(max1)
print(max1+max2+max3)