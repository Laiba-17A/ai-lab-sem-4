class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)   # call parent constructor
        self.model = model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # call parent constructor
        self.battery_capacity = battery_capacity


# create object
ecar = ElectricCar("Tesla", "Model S", "100 kWh")

# print details
print("Brand:", ecar.brand)
print("Model:", ecar.model)
print("Battery:", ecar.battery_capacity)