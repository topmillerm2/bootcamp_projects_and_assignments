class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Price:{}, Maximum Speed:{}, Total miles:{}".format(self.price, self.max_speed, self.miles)
    def ride(self):
        print "Riding"
        self.miles+=1
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 1
        if(self.miles<0):
            self.miles = 0
        return self

bike1 = Bike("$800","25mph", 100)
bike2 = Bike("$1000", "50mph", 500)
bike3 = Bike("$1500", "100mph", 25)
bike1.ride().ride().ride().reverse()
bike1.displayInfo()

bike2.ride().ride().reverse().reverse()
bike2.displayInfo()

bike3.reverse().reverse().reverse()
bike3.displayInfo()




# book answer:

# class Bike(object):
#     def __init__(self, price, max_speed):
#         self.price = price
#         self.max_speed = max_speed
#         self.miles = 0

#     def displayInfo(self):
#         print 'Price is: $' + str(self.price)
#         print 'Max speed: ' + str(self.max_speed) + 'mph'
#         print 'Total miles: ' + str(self.miles) + ' miles'

#     def drive(self):
#         print 'Driving'
#         self.miles += 10

#     def reverse(self):
#         print 'Reversing'
#         # prevent negative miles
#         if self.miles >= 5:
#             self.miles -= 5

# # create instances and run methods
# bike1 = Bike(99.99, 12)
# bike1.drive()
# bike1.drive()
# bike1.drive()
# bike1.reverse()
# bike1.displayInfo()

# bike2 = Bike(139.99, 20)
# bike2.drive()
# bike2.drive()
# bike2.reverse()
# bike2.reverse()
# bike2.displayInfo()