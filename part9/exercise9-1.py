class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


restaurant = Restaurant("The Great Table", "Italian")

print(f"Restaurant name: {restaurant.restaurant_name}")
print(f"Cuisine type: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()
