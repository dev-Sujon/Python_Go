class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


voglu = Dog("Voglu", 4)
p =voglu.description()
print(p)
p = voglu.speak("ghew ghoo")
print(p)

