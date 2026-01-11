from random import choice

lottery_tickets = (5, 15, 25, 35, 45, 55, 65, 75, 85, 95, "c", "h", "e", "n", "z")

luky_number = []
for i in range(4):
    luky_ticket = choice(lottery_tickets)
    luky_number.append(luky_ticket)

print(f"If your number is：")
for i in luky_number:
    print(f"{i}", end=" ")
    # print(f"if your number is {i}, you will winned!")
print(f"\nYou will winned!")
