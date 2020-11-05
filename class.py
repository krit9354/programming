class customer:
    name = ""
    age = ""
    def show(self):
        print("your name are",self.name)
        print("your are", self.age,"year old")

customer1 = customer()
customer1.name="krit"
customer1.age=17
customer2= customer()
customer2.name="ball"
customer2.age=15
customer1.show()
customer2.show()