food_system={"rice":15,"pock":30,"bacon":20,"apple":10}
food_list =[]

for x in food_system.keys():
    print(x,'=',food_system[x])
while True:
    menu = input("food :")
    if menu.lower() == "exit":
        break
    else:
        food_list.append([menu.lower(),food_system[menu.lower()]])

def ShowBill():
    total=0
    print("-----My Bill-----")
    for i in range(len(food_list)):
        print(food_list[i][0],'=',food_list[i][1])
        total+=int(food_list[i][1])
    print("total :",total,"Bath")

ShowBill()