sandwich_orders = ["tuna", "pastrami", "ham", "pastrami", "roast beef", "pastrami"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
