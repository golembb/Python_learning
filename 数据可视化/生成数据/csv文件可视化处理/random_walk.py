from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):  # 随机次数
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
        self.get_step()

    def fill_walk(self):
        while len(self.x_values) < self.num_points:  # 不够次数就一直循环
            x_step = self.get_step()  # 最终的移动
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:  # 两个坐标轴的移动都是0的话，继续执行下一次循环
                continue
            next_x = self.x_values[-1] + x_step  # 坐标值最终等于最后一个值加移动的量
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step():
        direction = choice([1, -1])  # 随机决定x轴上的方向
        distance = choice([0, 1, 2, 3, 4])  # 随机决定走多远
        step = direction * distance
        return step


































