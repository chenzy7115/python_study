def get_city_country(city, country, population=""):
    """Return a string like 'Santiago, Chile - population 5000000'."""
    if population:
        city_country = f"{city.title()}, {country.title()} - population {population}"
    else:
        city_country = f"{city.title()}, {country.title()}"
    return city_country