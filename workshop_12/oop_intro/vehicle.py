"""Vehicle example showing simple class with behavior and state"""
import time

MAX_SPEED = 210

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, delta = 5):
        new_speed = self.speed + delta

        if MAX_SPEED < new_speed:
            new_speed = MAX_SPEED

        self.speed = new_speed

    def brake(self, delta = 5):
        new_speed = self.speed - delta
        
        if new_speed < 0:
            new_speed = 0

        self.speed = new_speed


    def __str__(self):
        # dunder methods
        return f"{self.year} {self.make} {self.model} (speed: {self.speed})"




my_car = Vehicle("Tesla", "Model 3", 2025)

# print(my_car.make, my_car.model, my_car.year, my_car.speed)
print(my_car)
# my_car.speed += 10
# print(my_car.speed)

for i in range(5):
    my_car.accelerate()
    print(my_car)
    # time.sleep(1)

for i in range(7):
    my_car.brake(12)
    print(my_car)
    # time.sleep(1)


print(my_car)
