import csv
dict = {}
add = ""
mean= ""
print("-----Dictionary-----")
print("1.add word")
print("2.dictionary")

#ฟังชันก์เพิ่มคำศัพท์ลงไปในไฟล์
def addWord():
    add = input("word to add :")
    mean = input("mean of word:")
    with open('word.txt', mode='a',encoding='utf-8') as file:
        employee_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow([add,mean])

#ฟังชันก์ค้นหาความหมายของคำศัพท์
def searchWord():
    sellect = input("word :")
    if sellect in dict.keys():
        print("mean :", dict[sellect])
    else:
        print("errror!.try again")

#เปลี่ยนไฟล์txtเป็นdict
with open("word.txt",mode="r",encoding='utf-8')as cvs_file:
    csv_reader = csv.reader(cvs_file, delimiter=',')
    for row in csv_reader:
        if row != []:
            dict[row[0]] = row[1]
        else:
            pass

mode=input("mode :")
while mode.lower() != "stop":
     if mode == "1":
          addWord()
     elif mode == "2":
          searchWord()
     mode=input("mode :")
