class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "ratchanon"
customer1.lastName = "non"
customer1.addCart()

customer2 = Customer()
customer2.name = "name2"
customer2.lastName = "lastname2"
customer2.addCart()

customer3 = Customer()
customer3.name = "name3"
customer3.lastName = "lastname3"
customer3.addCart()

customer4 = Customer()
customer4.name = "name4"
customer4.lastName = "lastname4"
customer4.addCart()