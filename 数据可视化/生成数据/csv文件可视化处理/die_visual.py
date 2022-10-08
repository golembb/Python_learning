from 数据可视化.生成数据.csv文件可视化处理.die import Die
import pygal  # 生成矢量图


die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
hist = pygal.Bar()  # 创建一个实例，对结果进行可视化
hist.title = 'Results of rolling one D6 1000 times'
hist.x_labels = [str(x) for x in range(1, die.num_sides+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6', frequencies)  # 将值和标签添加到图表中
hist.render_to_file('die_visual.svg')

















