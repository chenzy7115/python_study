# 使用**形参的函数
# 形参名*toppings中的星号让Python创建一个名为toppings的空元组,并将收到的所有值都封装到这个元组中
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")
