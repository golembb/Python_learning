import csv
from datetime import datetime
from matplotlib import pyplot as plt


filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)  # 创建一个与文件相关联的阅读器对象
    header_row = next(reader)  # next方法返回文件中的下一行
    # for index, column_header in enumerate(header_row):   enumerate 获取每个元素的索引及值
    # print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        try:  # 使用测试语句来防止有数据错误
            high = int(row[1])
            low = int(row[3])
            current_date = datetime.strptime(row[0], '%Y-%m-%d')  # 将字符串转换成日期
        except ValueError:
            print(current_date, 'missing date')
        else:
            dates.append(current_date)
            highs.append(high)  # 将索引一处的数据附加到highs末尾
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 5))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)  # 在一张图上可绘制多种数据
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # 接受一个x值系列和两个y值系列
plt.title('Daily high and low temperatures - 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 将x轴标签变斜
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

