cities = {
    "santiago": {
        "country": "chile",
        "population": 6_310_000,
        "fact": "Santiago is the largest city in Chile.",
    },
    "talkeetna": {
        "country": "alaska",
        "population": 876,
        "fact": "Talkeetna is alaska's only regional capital.",
    },
    "kathmandu": {
        "country": "nepal",
        "population": 975_453,
        "fact": "Kathmandu is the largest city in Nepal.",
    },
}
for city, city_info in cities.items():
    country = city_info["country"].title()
    population = city_info["population"]
    fact = city_info["fact"]
    print(f"{city.title()}:")
    print(f"\tCountry: {country}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")
