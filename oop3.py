class car:
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def start(self):
        print("Starting the engine")


# creating a car object
my_car = car("Corolla", "White", 505)
print(my_car.name)
print(my_car.color)
print(my_car.model)
my_car.start()
