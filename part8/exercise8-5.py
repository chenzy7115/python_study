def describe_city(city, country="China"):
    """显示城市的信息"""
    print(f"{city.title()} is in {country.title()}.")


describe_city("beijing")
describe_city("tokyo", "japan")
describe_city("shanghai")
