class Vehicle:

    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels


class Car(Vehicle):

    def __init__(self, color, wheels, speed, cc):
        super().__init__(color, wheels)
        self.speed = speed
        self.cc = cc


class Wagon(Car):

    def __init__(self, color, wheels, speed, cc, load):
        super().__init__(color, wheels, speed, cc)
        self.load = load


class Bycicle(Vehicle):

    def __init__(self, color, wheels, type):
        super().__init__(color, wheels)
        self.type = type


class Motorcycle(Bycicle):

    def __init__(self, color, wheels, type, speed, cc):
        super().__init__(color, wheels, type)
        self.speed = speed
        self.cc = cc


car = Car("Blue", "4", "250 kmh", "250cc")
wagon = Wagon("Black", "4", "200 kmh", "190cc", "10 tons")
bycicle = Bycicle("Red", "2", "Urban")
motorcycle = Motorcycle("Blue", "2", "Sport", "230 kmh", "250cc")

list = [car, wagon, bycicle, motorcycle]


def catalog(wheels):
    print("\nSe han encontrado {} vehículos con {} ruedas:".format(
        len([v for v in list if int(v.wheels) == wheels]), wheels))
    for v in list:
        if int(v.wheels) == wheels:
            print("---------" + type(v).__name__ + "---------")
            print("Color: " + v.color)
            print("Wheels: " + v.wheels)

            if isinstance(v, Car) or isinstance(v, Wagon) or isinstance(v, Motorcycle):
                print("Speed: " + v.speed)
                print("CC: " + v.cc)

            if isinstance(v, Bycicle) or isinstance(v, Motorcycle):
                print("Type: " + v.type)

            if isinstance(v, Wagon):
                print("Load: " + v.load)


catalog(0)
catalog(2)
catalog(4)
