# class Addition:
#     def __init__(self, value_A, value_B):
#         self.value_1 = value_A
#         self.value_2 = value_B

#     def adding(self):
#         print("Hello World..!!")
    
    
    
#     # add = Addition(value_1= '22', value_2= "33")
#     self.adding()
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.is_running = False

#     def start_engine(self):
#         if not self.is_running:
#             print(f"The {self.year} {self.make} {self.model}'s engine is now running.")
#             self.is_running = True
#         else:
#             print(f"The {self.year} {self.make} {self.model}'s engine is already running.")

#     def stop_engine(self):
#         if self.is_running:
#             print(f"The {self.year} {self.make} {self.model}'s engine is now stopped.")
#             self.is_running = False
#         else:
#             print(f"The {self.year} {self.make} {self.model}'s engine is already stopped.")

# # Creating an instance of the Car class
# my_car = Car(make="Toyota", model="Camry", year=2022)

# # Accessing attributes
# print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")

# # Calling methods
# my_car.start_engine()
# my_car.stop_engine()


def adding(a, b):
    sum = a + b
    return str(sum)


