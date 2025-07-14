class Car:
    def __init__(self, model, color, make, year, size, mileage, top_speed, height):
        self.model = model
        self.color = color
        self.make = make
        self.year = year
        self.size = size
        self.mileage = mileage
        self.top_speed = top_speed
        self.height = height
        self.doors = 4
        self.speed = 0
        self.open_doors = 0

def open_door(self):
    print(f"The door of {self.make} {self.model} is now open.")

def accelerate(self):
    print(f"The car has started accelerating at {self.speed} mph.")

def  steer(self, direction):
    if direction.lower() == "left" or direction.lower() == 'right':
        print(f"The {self.make} {self.model} is turning {direction}.")
    else:
        print(f"{direction}is not a valid direction. Please enter a valid direction.")

my_car = Car("Camaro", "Blue", "Chevrolet", 2016, 20, 10000, 200, 7)

my_car.steer("Left")