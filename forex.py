from forex_python.converter import CurrencyRates
c = CurrencyRates()
country1=""
country2=""
money=0

def conversion_rate():
    print(c.get_rate(country1, country2))

def conversion_amount():
    print(c.convert(country1, country2, money))

mode = input("mode :")
if mode == "1":
    country1 = input()
    country2 = input()
    conversion_rate()
if mode == "2":
    country1 = input()
    country2 = input()
    money = int(input())
    conversion_amount()