from car import Car, ElectricCar


my_beetle = Car("volkswagen", "beetle", 2019)
my_tsla = ElectricCar("tesla", "roadster", 2019)

print(my_beetle.get_descriptive_name())
print(my_tsla.get_descriptive_name())
