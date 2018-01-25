import math
class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name= item_name
        self. weight = weight
        self. brand = brand
        self.cost = cost
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self, decimal):
        self.price += round(self.price * decimal, 2)
        return self
    def ret(self, reason):
        if reason == "defective":
            self.status = "defective"
            price = 0
        if reason == "in a box":
            status = "for sale"
        if reason == "opened":
            status = "used"
            self.price -= self.price * .02
        return self
    def display_info(self):
         print "Price:{}, Item name:{}, Weight:{} Brand:{} Cost:{} Status:{}".format(self.price, self.item_name, self.weight, self.brand, self.cost, self.status)

sweater = Product(50, "RedSweater", "5oz", "H&M", 40, "for sale")
Xbox = Product(500, "Xbox", "20lbs", "Microsoft", 250, "")



sweater.addTax(.0725).ret("defective").sell()
sweater.display_info()
# Xbox.sell().ret("opened").addTax(.075)
# Xbox.display_info()

