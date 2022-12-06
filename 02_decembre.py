with open('data/02_decembre.txt') as f:
    lines = [x[:-1] for x in f]

rules = {"A X":4,"A Y":8,"A Z":3,"B X":1,"B Y":5,"B Z":9,"C X":7,"C Y":2,"C Z":6}
rules_2 = {"A X":3,"A Y":4,"A Z":8,"B X":1,"B Y":5,"B Z":9,"C X":2,"C Y":6,"C Z":7}

score = 0
for x in lines:
    score += rules[x]

print(score)

score = 0
for x in lines:
    score += rules_2[x]

print(score)