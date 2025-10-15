#########################################################
###Create a base class Animal with a method speak().#####
#########################################################
class Animal:
    def speak(self):
        print("i am a animal")
class Dog(Animal):
    def speak(self):
        print("Woof Woof")
class Cat(Animal):
    def speak(self):
        print("meaw")
def main() -> object:
    dog=Dog()
    dog.speak()
    cat=Cat()
    cat.speak()

if __name__:='__main__':
    main()

