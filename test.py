import time
count=0

def c():
    name = "audio"+str(count)
    print(name)
while True:
    count+=1
    c()
    time.sleep(2)