pet1 = {
    "animal": "cat",
    "name": "tom",
    "owner": "jerry",
}
pet2 = {
    "animal": "dog",
    "name": "lily",
    "owner": "jack",
}
pet3 = {
    "animal": "pig",
    "name": "lucky",
    "owner": "tom",
}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Name: {pet['name']}")
    print(f"Owner: {pet['owner']}")
