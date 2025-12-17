
#inheritence

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.make} {self.model}")
# # mycar=Car("Toyota","Camry",2020)
# # mycar.display_info()


# class electric_car(Car):
#     def __init__(self,make,model,year,battery):
#         self.battery=battery
#         super().__init__(make,model,year)
#     def display_info(self):
#         super().display_info()
#         print(f"Battery: {self.battery}")
# mycar2=electric_car("Tesla","Model S",2022,"100 kWh vali")
# mycar2.display_info()


# #encsplusulation
class Car:
    def __init__(self, make,model, year):
        self.make = make
        self.__model = model
        self.year = year
    def get_model(self):
        return self.__model

    def display_info(self):
        print(f"{self.year} {self.make}")
mycar=Car("Toyota","Camry",2020)
mycar.display_info()
print(mycar.get_model())


#polimorphism

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.make} {self.model}")
#     def fuel_type(self):
#         print("Petrol Car")
# mycar=Car("Toyota","Camry",2020)
# mycar.display_info()
# mycar.fuel_type()

# class electric_car(Car):
#     def __init__(self,make,model,year,battery):
#         self.battery=battery
#         super().__init__(make,model,year)
#     def display_info(self):
#         super().display_info()
#         print(f"Battery: {self.battery}")
#     def fuel_type(self):
#         print("Electric Car")
# mycar2=electric_car("Tesla","Model S",2022,"100 kWh vali")
# mycar2.display_info()
# mycar2.fuel_type()


# setter and getter

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.__model = model   # private
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.make} {self.__model}")

#     # getter
#     def get_model(self):
#         return self.__model

#     # setter
#     def set_model(self, new_model):
#         if isinstance(new_model, str) and len(new_model) > 0:
#             self.__model = new_model
#         else:
#             print("Invalid model!")

# mycar = Car("Toyota", "Camry", 2020)
# mycar.display_info()

# print(mycar.get_model())   # safe access

# mycar.set_model("Corolla") # safe update
# mycar.display_info()
# mycar.set_model("")        # invalid update
