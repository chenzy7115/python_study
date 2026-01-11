class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f"Number of customers served: {self.number_served}")

    def increment_number_served(self, additional_served):
        self.number_served += additional_served
        print(f"Number of customers served: {self.number_served}")


restaurant = Restaurant("The Great Table", "Italian")
restaurant.describe_restaurant()
print(f"Number of customers served: {restaurant.number_served}")
restaurant.number_served = 430
print(f"Number of customers served: {restaurant.number_served}")
restaurant.set_number_served(1257)
restaurant.increment_number_served(239)
