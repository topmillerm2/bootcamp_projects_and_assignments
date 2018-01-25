class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
    def display_all(self):
        print "Price:{}, Maximum Speed:{}, Fuel:{} Mileage:{} Tax:{}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

car1 = Car(33200, "50mph", "Empty", "20mpg")
car2 = Car(3200, "100mph", "Full", "12mpg")
car3 = Car(3300, "50mph", "Empty", "15mpg")
car4 = Car(3320, "80mph", "Full", "10mpg")
car5 = Car(3322, "95mph", "Half-full", "12mpg")
car6 = Car(20500, "120mph", "Empty", "22mpg")


car3.display_all()
