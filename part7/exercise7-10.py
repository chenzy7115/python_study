places_polled = []
while True:
    place = input("\nIf you could visit one place in the world, where would you go? ")
    places_polled.append(place)
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() != "yes":
        break
print("\n--- Results ---")
for place in places_polled:
    print(place)
