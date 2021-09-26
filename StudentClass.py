class Student:
    def __init__(self,roll,name):
        self.roll=roll
        self.age="16"
        self.name=name
    
    def printdetails(self):
        print("student name "+self.name)
        print("student age "+self.age)
        print("student roll no. "+self.roll)

S1 = Student("28","Simar")
S1.printdetails()

S2 = Student("41","Zoyaa")
S2.printdetails()