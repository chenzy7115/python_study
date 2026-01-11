def city_country(name, country):
    """返回城市和国家"""
    return f"{name.title()},{country.title()}"


city = city_country("beijing", "china")
print(city)
city = city_country("tokyo", "japan")
print(city)
city = city_country("shanghai", "china")
print(city)
