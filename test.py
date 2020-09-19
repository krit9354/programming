import csv


add = input("word to add :")
mean = input("mean of word:")
with open('demo.csv', mode='a',newline="" ,encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([add,mean])