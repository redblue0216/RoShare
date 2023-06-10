# RoShare

![shields_version](/static/shields_version.svg)    ![shields_license](/static/shields_license.svg)    ![shields_author](/static/shields_author.svg)    ![shiedls_python](/static/shields_python.svg)

![roshare_symbol](/static/roshare_symbol.jpeg)


## 介绍
+ RoShare是一个金融数据服务，满足金融量化的各种数据需求，它与市面上的金融数据服务的最大不同是提供进阶版的金融数据，比如基于金融新闻使用NLP技术构建的每日主题热度、基于基础数据使用经典理论构建的各类因子。


## 技术说明
+ RoShare的服务端和客户端都使用Python3.9.13开发，依赖第三方包如下：
	+ pandas
	+ numpy
	+ fastapi


## 安装
+ 使用pip安装
```bash
$ pip install shihua-roshareclient
```
+ 使用wheel安装
```bash
$ pip install roshareclient-0.1.1-py3-none-any.whl
```


## 快速指南
+ 首先，需要注册roshare账号，使用tushare的个人token(roshare只是进阶数据的算法提供方，具体的数据服务还需要自行接入相应的基础数据，目前支持tushare的数据接入)
+ 示例1：获取每日新闻咨询
```python
from roshareclient.client.api import DataAPI

tmp_dict = {}
tmp_dict['src'] = 'eastmoney'
tmp_dict['start_date'] = '2023-06-09+00:00:00' ### url中+号表示空格
tmp_dict['end_date'] = '2023-06-10+00:00:00'
roshareclient = DataAPI(token_key = 7890,
                    token='xxxxxxxxxxxxxxxxxxx',
                    tushare_token='xxxxxxxxxxxxxxxxxxxxxx',
                    timeout=6000)
df = roshareclient.get_tushare_news(params=tmp_dict)
print(df)
```


## 更多文档
+ 想要了解RoShare提供的进阶数据背后的算法设计，想要了解RoShare提供哪些进阶数据，请移步此处了解

## 更新记录
+ 0.1.1------2023/06/10
	+ 推出了新闻主题热度数据 	