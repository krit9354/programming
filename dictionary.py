dic1 = {"mom":"แม่","dad":"พ่อ","baby":"เด็ก"}
add=""
mean=""
sellect=""
print("1.add word")
print("2.dictionary")
mode=input("mode :")
def f_add():
     add = input("word to add :")
     mean = input("mean of word:")
     dic1[add]=mean
def dic():
     sellect = input("word :")
     if sellect in dic1.keys():
          print("mean :",dic1[sellect])
     else:
          print("errror")
while mode.lower() != "stop":
     if mode == "1":
          f_add()
     elif mode == "2":
          dic()
     mode=input("mode :")