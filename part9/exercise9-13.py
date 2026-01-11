# from random import randint
class Die:
    """表示一个骰子的类"""

    def __init__(self, sides=6):
        """骰子默认为6面"""
        self.sides = sides

    def roll_die(self):
        """返回一个位于1和骰子面数之间的随机值"""
        import random
        return random.randint(1, self.sides)


die = Die()
for i in range(10):
    print(die.roll_die())
