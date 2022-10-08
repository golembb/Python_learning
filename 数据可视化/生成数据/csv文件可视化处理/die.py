from random import randint


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides  # 也可指定其他的数

    def roll(self):
        return randint(1, self.num_sides)  # 随机返回一个介于1和骰子数之间的值，模拟掷骰子




















