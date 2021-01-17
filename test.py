import random
round  = []
while len(round) != 10:
    a = random.randint(0,10)
    if a in round:
        pass
    else:
        round.append(a)

print(round)