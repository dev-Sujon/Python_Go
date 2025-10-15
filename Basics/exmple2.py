##parametarised constructor
# default constructor
# ##



class Student:
    def __init__(self,name,Id):
        self.name = name  #instance variable
        self.id = Id

s1 = Student("Ios",15)
s2 = Student("Olf",11)
print(s1.name)
print(s1.name,s1.id)
print(s2.name,s2.id)
print(s1)
s1.name = "Ilhum"
s1.id=17
print(s1.name,s1.id)
print(s1)

##print("s1",s1)
#print("s2",s2)
# ##

class Car:
    def __init__(self,brand,code):
        self.name = brand
        self.serial=code

    def details(self):
        print(self.name,self.serial)
        ##depends on student object

volvo = Car("volvo",1233)
volvo.details()
rangeRover = Car("Range_Rover","1548B")
rangeRover.details()

class pen():
    ##class attributes
    att = "This is soo beauty"
    print("Masanovafaukauka")
    def __init__(self,ink,material):
        self.color=ink
        self.type=material

    def display(self):
        print(self.color,self.type)



