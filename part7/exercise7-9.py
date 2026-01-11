sandwich_orders = ["tuna", "pastrami", "ham", "pastrami", "roast beef", "pastrami"]
finished_sandwiches = []

print("Sorry, we are out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
