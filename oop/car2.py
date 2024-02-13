class Car:
    def __init__(self, make, model,year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print("This car is driving")

    def stop(self):
        print("this car has stopped")

    car_1 = Car("make","model","year")
    car_1= input(f"enter the make: {self.make}")