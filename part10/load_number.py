import json

filename = "number_writer.json"

try:
    with open(filename) as f:
        numbers = json.load(f)
except FileNotFoundError:
    numbers = input("What numbers do you want to write? ")
    with open(filename, "w") as f:
        json.dump(numbers, f)
        print(f"We'll remember your numbers when you come back, {numbers}!")
else:
    print(f"Your numbers are {numbers}!")
