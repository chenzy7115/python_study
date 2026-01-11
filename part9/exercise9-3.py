class user:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")


user1 = user("John", "Doe", 30, "Male")
user2 = user("Jane", "Smith", 25, "Female")
user3 = user("Bob", "Johnson", 40, "Male")
user4 = user("Alice", "Williams", 35, "Female")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user4.describe_user()
user4.greet_user()
