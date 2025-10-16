# Create class named ‘Modified_Super’ and inherit this class from the Super class.
# a. Inside the Modified_Super class, create a function named ‘fun1’ and pass the
# following message inside the print statement: ‘This is function 1 in the Modified
# Super class.’
# b. Create another user-defined function named ‘fun2’ and pass the message: ‘This is
# the 2nd function from the Modified Super class’ in the print statement.
# c. After that, now create an object for the Modified_Super class and call the fun1().

class Super():
    def __init__(self):
        print("MODIFIED SUPER CLASS")

class Modified_super(Super):
    def fun1(self):
        print("This is function 1 in the Modified Super Class")
    def fun2(self):
        print("THis is the 2nd function from the Modified Super Class")
    def __str__(self):
        print(self.fun1)
        print()
        print(self.fun2)
m=Modified_super()

m.fun1()
m.fun2()
