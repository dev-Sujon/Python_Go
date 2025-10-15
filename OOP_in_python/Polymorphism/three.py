#########################################################################################
# Implement a Vehicle class with methods start_engine and stop_engine. Create subclasses
# Car, Motorcycle, and Bus that override these methods.
#########################################################################################
class Vehicle:
    def start_engine(self):
        return "must implement"

    def stop_engine(self):
        return "must implement"


class Car(Vehicle):
    def start_engine(self):
        return "Car engine is started"

    def stop_engine(self):
        return "Car engine is stopped now"


class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine is started"

    def stop_engine(self):
        return "Motorcycle engine is stopped now"


def main():
    car = Car()
    print(car.start_engine())
    print(car.stop_engine())
    print()
    motorcycle = Motorcycle()
    print(motorcycle.start_engine())
    print(motorcycle.stop_engine())

if __name__ == "__main__":
    main()
