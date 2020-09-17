#โปรแกรมคำนวณภาษี
total_price = int(input(">>>"))
def vat(price):
    total = price+(price*7/100)
    return  total

print(vat(total_price))
