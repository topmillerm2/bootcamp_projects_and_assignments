class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health= 100
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Health:{}".format(self.health)
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health+=5
        # print "Health:{}".format(self.health)
        return self
class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health-=10
        return self
    def display_health(self):
        print "Health:{}. I am a Dragon".format(self.health)
    
    

cat = Animal("cat")
cat.walk().walk().walk().run().run().display_health()

animal1 = Dog("Leo")
animal1.walk().walk().walk().run().run().display_health()

animal2 = Dragon("Garfield")
animal2.walk().walk().walk().run().run().display_health()


