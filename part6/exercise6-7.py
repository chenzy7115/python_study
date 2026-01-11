person0 = {
    "first_name": "eric",
    "last_name": "matthes",
    "location": "alaska",
    "age": 43,
    "city": "sitka",
}
person1 = {
    "first_name": "ever",
    "last_name": "matthes",
    "location": "alaska",
    "age": 17,
    "city": "sitka",
}
person2 = {
    "first_name": "willie",
    "last_name": "matthes",
    "location": "alaska",
    "age": 57,
    "city": "sitka",
}
people = [person0, person1, person2]
for person in people:
    print(f"Name: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"Location: {person['location'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")
