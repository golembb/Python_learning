import matplotlib.pyplot as plt  


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)  # 根据数字绘制图案，linewith决定线条粗细
plt.title("Square Numbers", fontsize=24)  # 标题
plt.xlabel('value', fontsize=14)  # 横纵坐标的标签
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)  # 刻度的大小, axis意思为影响两个轴
plt.show()  # 打开matplotlib查看绘制的图形


















