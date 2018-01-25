import datetime

class Call(object):
    def __init__(self, id, name, number, reason):
        self.id  = id
        self.name = name
        self.number = number
        self.time = datetime.datetime.now()
        self.reason = reason

    def display(self):
        printStr = "ID: " + self.id
        printStr += "\nName: " +self.name
        printStr += "\nNumber: " +self.number
        printStr += "\nTime: " + str(self.time)
        printStr += "\nReason: " +self.reason
        print printStr

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.size = len(self.calls)

    def add(self, call):
        self.calls.append(call)
        self.size = len(self.calls)
        return self
    def remove(self):
        self.calls.pop(0)
        self.size = len(self.calls)
        return self

    def removeNum(self, number):
        for i in range(0,self.size):
            if self.calls[i].number == number:
                callToPop = i
        self.calls.pop(callToPop)
        self.size = len(self.calls)
    def info(self):
        for i in range (0, self.size):
            print self.calls[i].name + " " + self.calls[i].number + " " + str(self.calls[i].time)
        print "Queue Size: " + str(self.size)
        return self
 
now = datetime.datetime.now()
print now
    

call1 = Call("1","Michael","555-456-7890","Bills too high")
call2 = Call("2","Patrick","555-456-7450","Bills too low")
call3 = Call("3","Andy","555-456-1234","IDK")

cen1 = CallCenter()
cen1.add(call1)
cen1.add(call2)
cen1.add(call3)
cen1.info().removeNum("555-456-7450")
cen1.info()