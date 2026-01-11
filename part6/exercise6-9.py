favorite_places = {
    "alice": ["beijing", "shanghai", "guangzhou"],
    "bob": ["shenzhen", "hangzhou"],
    "carl": ["tianjin", "wuhan"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
