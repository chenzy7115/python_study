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


class admin(user):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin1 = admin("John", "Doe", 30, "Male")
admin1.describe_user()
admin1.show_privileges()
