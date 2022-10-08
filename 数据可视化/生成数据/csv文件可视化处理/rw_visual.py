import matplotlib.pyplot as plt
from 数据可视化.生成数据.csv文件可视化处理.random_walk import RandomWalk

while True:
    rw = RandomWalk(num_points=8000)
    rw.fill_walk()
    plt.figure(figsize=(10, 6), facecolor='black', edgecolor='yellow')  # 用于指定图表的宽度、高度、分辨率及背景色
    point_numbers = list(range(rw.num_points))  # 根据次数设置颜色渐变效果
    plt.plot(rw.x_values, rw.y_values, linewidth=1)  # 将随机漫步的图绘制出来
    plt.scatter(0, 0, c='green', s=100)  # 差异化起点和终点
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
    plt.xticks([])  # 隐藏坐标轴
    plt.yticks([])
    plt.show()
    keep_running = input('Make another walk?(y/n): ')
    if keep_running == 'n':
        break





























