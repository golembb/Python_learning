import matplotlib.pyplot as plt


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# s表示点的尺寸，edgecolors设计点的轮廓色(默认就是none)，c为点颜色，范围为0~1，cmap为颜色映射（需要将坐标赋予c）
plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Reds, edgecolors='none', s=40)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)  # major意思为不用显示所有坐标轴标签
plt.axis([0, 1100, 0, 1100000])  # 设置每个坐标轴的取值范围
plt.savefig('squares_plot.png', bbox_inches='tight')  # 将图表保存到本地，第一个实参为文件名，第二个为是否将图表空白区域裁剪掉























