#object oriented programming..
class Car:

    def _ _init_ _ (self, make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color =color
        
    def drive(self):
        print("this car is driving..")

    def stop(self):
        print("This car has stopped..")


car_1 = car("chevy","corvette", 2022, "black")

print (car_1.make)
print (car_1.model)
print (car_1.year)
print (car_1.black)