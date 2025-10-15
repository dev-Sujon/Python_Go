
# 10. Create a class named ‘Encapsulation’:
# a. Inside the class, first create a constructor. Inside the constructor, initialize
# originalValue variable as 10.
# b. After creating the constructor, define a function named ‘Value’ and this function
# should return the variable that we have initialized in the constructor.
# c. Now create 2nd function named setValue, and pass an argument named
# newValue’. The task of this function will be to replace the value of the
# originalValue variable by the value of the newValue variable.
class Encapsulation:
    def __init__(self,val=10):
        self.val = val
    def value(self):
        return self.val
    def set_value(self,newVal):
        self.val=newVal
        return self.val
one=Encapsulation()
res=one.value()
print(res)
res=one.set_value(15)
print(res)












