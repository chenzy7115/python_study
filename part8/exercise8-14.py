def car_info(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

car = car_info("subaru", "outback", color="blue", tow_package=True)
print(car)