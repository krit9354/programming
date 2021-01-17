import random

a = [
    ["a chemical used to kill pests","pesticide"],
    ["a small animal or an insect that causes damage to food or crops,or otherwise human being","pest"],
    ["a liveing creature","organism"],
    ["a general class of animals that includes rat , mice, ansd squirrels","rodent"],
    ["to prevent something from succeeding or from happening in the way that was planned","interfere with"],
    ["to remove or get rid of","eliminate"],
    ["to eat in small bites","nibble"],
    ["small,low brushes","brush"],
    ["a weed killer","herbicide"],
    ["unpleasant","harsh"],
    ["easily infuenced or harmed by something","susceptible to"],
    ["not harmed or affected by something", "resistant"],
    ["to change something", "modify"],
    ["ability", "potential "],
    ["harmfully", "adversely"],
    ["the state of depending on someone or something ", "reliance"],
    ["describes a substance which causes cancer", "carcinogenic"],
    ["making something less pure or making it poisonous", "contamination"],
    ["to control something", "regulate"],
    ["a lot of disagreement or argument about something", "controversy"]
    ]

point = 0
d = 10

round  = []
while len(round) != d:
    c = random.randint(0,d-1)
    if c not in round:
        round.append(c)

for i in round:
    print(a[i][0])
    b = input(">>>")
    if b == a[i][1]:
        print("correct")
        point += 1
    else:
        print("wrong the correct is :"+a[i][1])
print("your score :",point)




