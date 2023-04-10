class product:
    def __init__(self, item, quantity, price):
        self.item = item
        self.quantity = quantity
        self.price = price
    def print_product(self):
        print("{0}\t\t{1}\t\t\t{2}\t\t\t{3} ".format(self.item,self.quantity,self.price,self.quantity*self.price))
num = int(input("how many items u purchased ? "))
a = []
for x in range(num):
    item = str(input("Enter Item name = "))
    quan = int(input("Enter Quantity = "))
    price = int(input("Enter Price = "))
    item1 = product(item, quan, price)
    #item1.print_product()
    a.append(item1)
print("item\tquantity\tprice\tTotal")
total = 0
for i in a:
    i.print_product()
    total = (i.quantity*i.price) + total
print("total amount u purchased=",total)
"""item2 = product("Mariegold", 1, 20)
item3 = product("Goodday", 6, 30)"""

#item2.print_product()
#item3.print_product()