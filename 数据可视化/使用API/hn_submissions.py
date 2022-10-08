import pygal
from pygal.style import LightenStyle as LS
import requests
from operator import itemgetter


url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)  # 对于每篇文章都执行一个API调用
    # print(submission_r.status_code)   检查status code,为节省运行时间这里不检查了
    response_dict = submission_r.json()  # 转换为Python字典
    submission_dict = {
        'label': response_dict['title'],
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),  # 到其讨论页面的链接
        'value': response_dict.get('descendants', 0),  # get方法当字典的键存在，返回其值，不存在返回指定的值
    }
    submission_dicts.append(submission_dict)
# 对submiss dicts进行排序，使用模块operator中的函数， 从所在列表的每个字典中提取与comments相关的值
#submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
my_style = LS('#333366')
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_leged=False, truncate_label=15, show_y_guides=False)
chart.title = 'Most-popular article on hacker-news'
chart.add('', submission_dicts)
chart.render_to_file('hn_submissions.svg')



















