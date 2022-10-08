import requests  # 向网站请求信息


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  # 存储API调用的URL
r = requests.get(url)  # 使用requests来执行调用
print('Status code: ', r.status_code)
response_dict = r.json()  # 使用json将这些信息转换为Python字典
print(response_dict.keys())
print('Total repositories: ', response_dict['total_count'])  # 总共包含多少个Python仓库
repo_dicts = response_dict['items']
print('Repositories returned: ', len(repo_dicts))  # 获得了多少个仓库的信息
repo_dict_0 = repo_dicts[0]  # 查看第一个仓库
print('\nKeys:', len(repo_dict_0))
for key in sorted(repo_dict_0.keys()):
    print(key)

print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print('\nName: ', repo_dict['name'])
    print('Owner: ', repo_dict['owner']['login'])  # 先使用owner来访问表示所有者的字典，在使用key来获取所有者的登录名
    print('Stars: ', repo_dict['stargazers_count'])
    print('Repository: ', repo_dict['html_url'])  # 在GitHub上的URL
    print('Created: ', repo_dict['created_at'])
    print('Updated: ', repo_dict['updated_at'])
    print('Description: ', repo_dict['description'])

































