class car:
    name = "Premio"
    color = "red"

    def start():
        print("Starting the Engine")


print("Name of the car", car.name)
print("Color of the car", car.color)
print(dir(car))
car.start()
