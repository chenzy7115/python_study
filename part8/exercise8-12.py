def sandwich(*toppings):
    """Summarize the sandwich we are about to make."""
    print(f"\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


sandwich("pepperoni")
sandwich("mushrooms", "green peppers", "extra cheese")
sandwich("tomato", "lettuce", "onion", "pickle")
sandwich("bacon", "cheese", "mayonnaise")