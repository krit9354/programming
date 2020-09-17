num1 = int(input(">>>"))
process = input(">>>")
num2 = int(input(">>>"))

def add(num1,num2):
    print("=",num1+num2)
def delete(num1,num2):
    print("=",num1-num2)
def multiply(num1,num2):
    print("=",num1*num2)
def divide(num1,num2):
    print("=",num1/num2)

if process=="+":
    add(num1,num2)
elif process=="-":
    delete(num1,num2)
elif process=="*":
    multiply(num1,num2)
elif process=="/":
    divide(num1,num2)