import random
class Patient(object):
    def __init__(self, id_number, name, allergies):
        self.id_number = id_number
        self.name = name
        self.allergies = allergies
        self.bed_number = random.randint(0,100)
    def display_info(self):
        print self.id_number, self.name, self.allergies, self.bed_number

class Hospital(object):
    def __init__(self):
        self.patients = []
        self.capacity= 100

    def admit(self, patient):
        print "New Patient"
        self.patients.append(patient)
        if len(self.patients)> self.capacity:
            print "Hospital is full"
        else:
            print "Admission Complete"
            for i in range(0, len(self.patients)):
                print str(self.patients[i].name) + " Room:" + str(self.patients[i].bed_number)

    def discharge(self, name):
        for i in range(0, len(self.patients)):
            if str(self.patients[i].name) == name:
                bedToPop = i
        self.patients.pop(bedToPop)
        for i in range(0,len(self.patients)):
            print self.patients[i].name
patient1 = Patient("2323", "Freddy", "peanuts")
patient2 = Patient("232", "William", "water")
patient3 = Patient("2323", "Pat", "pickles")
# patient1.display_info()
 
event1 = Hospital()
event1.admit(patient1)
event1.admit(patient2)
event1.admit(patient3)


event1.discharge("Freddy")

