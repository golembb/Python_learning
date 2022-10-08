import requests  # 向网站请求信息
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)
response_dict = r.json()
print('Total repositories: ', response_dict['total_count'])
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],  # value存储星数，label存储项目描述
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],  # 将每个条形用作网站的链接
    }
    plot_dicts.append(plot_dict)
my_style = LS('#333366', base_style=LCS)  # 定义一种样式
my_config = pygal.Config()  # 可定制图表外观的属性
my_config.x_label_rotation = 45  # 让标签旋转45度
my_config.show_legend = False  # 让图例隐藏
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18  # y轴上的刻度
my_config.truncate_label = 15  # 将项目名缩短到15个字符
my_config.show_y_guides = False  # 隐藏图表中的y轴水平线
my_config.width = 1000  # 自定义宽度
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')














