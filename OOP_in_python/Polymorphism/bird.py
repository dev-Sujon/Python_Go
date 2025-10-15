#############################################################################################
# Create a Bird class with a method make_sound. Create subclasses Sparrow, Parrot, and Ostrich
# with their own make_sound implementations.
##############################################################################################
class Bird:
    def make_sound(self):
        return "Every bird has sound."
class Sparrow(Bird):
    def make_sound(self):
        return "Sparrow makes chirping sound"
class Parrot(Bird):
    def make_sound(self):
        return "Parrot makes squawking sound"
class Ostrich(Bird):
    def make_sound(self):
        return "Ostrich makes booming sound"
def main():
    sparrow=Sparrow()
    parrot=Parrot()
    ostrich=Ostrich()
    print(sparrow.make_sound())
    print()
    print(parrot.make_sound())
    print()
    print(ostrich.make_sound())
if __name__:='__main__':
    main()
