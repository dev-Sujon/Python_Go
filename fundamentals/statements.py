class FactorialCalculator:
    def __init__(self):
        pass
    def calculate_fact(self,num):
        if num==0:
            return 1
        else:
            return num* self.calculate_fact(num - 1)

        ###############################
# Creating an instance of the FactorialCalculator class
n=int(input("Enter number : "))
calc=FactorialCalculator()
# Calling the calculate_factorial method with the desired number
res=calc.calculate_fact(n)
print(f"Factorial of {n} is {res}")
#######################################################################

########################################################################
# 3. Create a class named ‘student’ and inside the class, create a
        # function named ‘fun1’- this method should accept the user defined
        # input and return that value.
##########################################################################
class Student:
    def fun1(self):
        user_input = input("Enter something: ")
        return user_input

    def message(self, input_value):
        print("User input from fun1:", input_value)

# Creating an instance of the Student class
student_instance = Student()
# Calling the fun1 method to get user input
user_input_value = student_instance.fun1()
# Calling the message method to print the user input
student_instance.message(user_input_value)

