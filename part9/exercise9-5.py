class user:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts: {self.login_attempts}")


user1 = user("John", "Doe", 30, "Male")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()

