total=0
id=input("username :")
pw=input("password :")
if id=="krit" and pw=="9354":
    print("-----krit shop-------")
    print("goods       pice(bath)")
    print("1.pen        10")
    print("2.book       20")
    print("3.water      12")
    userselect=input("seclect goods number :")
    while userselect != "exit":
        if userselect=="1":
            total+=10
        elif userselect =="2":
            total+=20
        elif userselect =="3":
            total+=12
        else:
            print("error#/*#+")
        userselect = input("seclect goods number :")
    print("total :",total,"bath")