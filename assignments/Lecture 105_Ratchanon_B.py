class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")
class Car(Vehicle):
    pass
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

Car1 = Car()
Car1.turnOnAirConditioner()
Pickup1 = Pickup()
Pickup1.turnOnAirConditioner()
Van1 = Van()
Van1.turnOnAirConditioner()
Estatecar1 = Estatecar()
Estatecar1.turnOnAirConditioner()