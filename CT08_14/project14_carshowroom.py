class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def start_engine(self):
        print(f"The engine of the {self.brand} {self.model} is starting...")
    def show_details(self):
        print(f"This car is a {self.brand} {self.model}, it costs ${self.price}.")
car1 = Car("BMW", "Z4", 500000)
car2 = Car("Toyota", "Corolla", 180000)
car3 = Car("Kia", "Cerato", 165000)

#car1.start_engine()

showroom = []
showroom.append(car1)
showroom.append(car2)
showroom.append(car3)
for car in showroom:
    car.show_details()