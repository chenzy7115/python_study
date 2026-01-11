import random

my_tickets = [5, 15, 25, 24]

# 下面的函数完成了模拟彩票的过程
# 它接受一个可能的彩票列表作为参数
# 然后不断地模拟随机选择彩票，直到有一个与实际彩票匹配的彩票被选中为止
# my_tickets为实际彩票，随机彩票的排量和数字都要和实际彩票相同
def get_winning_tickets():
    """返回一个列表，其中包含彩票中可能出现的数字"""
    winning_tickets = []
    count = 0
    flag = 1

    while flag:
        # possible_ticket = random.choice(possibilities)
        # if possible_ticket not in winning_tickets:
        #     winning_tickets.append(possible_ticket)
        count += 1
        for i in range(4):
            possible_ticket = random.randint(1, 36)
            winning_tickets.append(possible_ticket)

        if winning_tickets == my_tickets:
            flag = 0
        else:
            winning_tickets.clear()

    print(f"It took {count} times to win!")
    return winning_tickets


# 下面的代码模拟了多次彩票的选择过程
winning_tickets = get_winning_tickets()
print(f"\nThe winning tickets are:")
for ticket in winning_tickets:
    print(f"{ticket}", end=" ")  # 打印每个数字，不换行
print("\n")

print(f"Your ticket is:")
for ticket in my_tickets:
    print(f"{ticket}", end=" ")  # 打印每个数字，不换行
