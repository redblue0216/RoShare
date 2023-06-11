# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个客户端参数管理脚本，主要用于存储相应参数
"""
模块介绍
-------

这是一个客户端参数管理脚本，主要用于存储相应参数

    功能：             

        （1）客户端参数管理

类说明
------

"""



####### 载入程序包 ###########################################################
############################################################################






####### 客户端参数管理 ############################################################
### 功能：                                                                    ###
### （1）客户端参数管理                                                         ###
################################################################################



####### 客户端参数管理 ####################################################################################
#########################################################################################################



### 添加新接口三步走：
### 1.添加OPERATOR
### 2.添加基础路由
### 3.加入到API字典



### 基础组件参数管理，为所有数据服务接口的基础
REQUEST_PROTOCOL = {'http':'http'}
REQUEST_HOST = {'local':'127.0.0.1','aliyun':'139.196.234.152'}
REQUEST_PORT = {'default':'11911'}
DATAAPI = {'tushare':'tushare'}
OPERATOR = {'get_tushare_stock_basic':'get_tushare_stock_basic',
            'get_tushare_stock_company':'get_tushare_stock_company',
            'get_tushare_daily':'get_tushare_daily',
            'get_tushare_weekly':'get_tushare_weekly',
            'get_tushare_monthly':'get_tushare_monthly',
            'get_tushare_daily_basic':'get_tushare_daily_basic',
            'get_tushare_income':'get_tushare_income',
            'get_tushare_balancesheet':'get_tushare_balancesheet',
            'get_tushare_cashflow':'get_tushare_cashflow',
            'get_tushare_forecast':'get_tushare_forecast',
            'get_tushare_express':'get_tushare_express',
            'get_tushare_fina_indicator':'get_tushare_fina_indicator',
            'get_tushare_index_daily':'get_tushare_index_daily',
            'get_tushare_index_weekly':'get_tushare_index_weekly',
            'get_tushare_index_monthly':'get_tushare_index_monthly',
            'get_tushare_index_dailybasic':'get_tushare_index_dailybasic',
            'get_tushare_index_classify':'get_tushare_index_classify',
            'get_tushare_news':'get_tushare_news'
            }



### 具体接口路由管理，由基础组件拼接而成
### 沪深股票--基础数据--股票列表
GET_TUSHARE_STOCK_BASIC = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_stock_basic'] + \
                                '?'
### 沪深股票--基础数据--上市公司基本信息
GET_TUSHARE_STOCK_COMPANY = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_stock_company'] + \
                                '?'
### 沪深股票--行情数据--日线行情
GET_TUSHARE_DAILY = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_daily'] + \
                                '?'
### 沪深股票--行情数据--周线行情
GET_TUSHARE_WEEKLY = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_weekly'] + \
                                '?'
### 沪深股票--行情数据--月线行情
GET_TUSHARE_MONTHLY = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_monthly'] + \
                                '?'
### 沪深股票--行情数据--每日指标
GET_TUSHARE_DAILY_BASIC = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_daily_basic'] + \
                                '?'
### 沪深股票--财务数据--利润表
GET_TUSHARE_INCOME = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_income'] + \
                                '?'
### 沪深股票--财务数据--资产负债表
GET_TUSHARE_BALANCESHEET = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_balancesheet'] + \
                                '?'
### 沪深股票--财务数据--现金流量表
GET_TUSHARE_CASHFLOW = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_cashflow'] + \
                                '?'
### 沪深股票--财务数据--业绩预告
GET_TUSHARE_FORECAST = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_forecast'] + \
                                '?'  
### 沪深股票--财务数据--业绩快报
GET_TUSHARE_EXPRESS = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_express'] + \
                                '?'     
### 沪深股票--财务数据--财务指标数据
GET_TUSHARE_FINA_INDICATOR = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_fina_indicator'] + \
                                '?'        
### 沪深股票--指数数据--指数日线行情
GET_TUSHARE_INDEX_DAILY = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_index_daily'] + \
                                '?'    
### 沪深股票--指数数据--指数周线行情
GET_TUSHARE_INDEX_WEEKLY = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_index_weekly'] + \
                                '?' 
### 沪深股票--指数数据--指数月线行情
GET_TUSHARE_INDEX_MONTHLY = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_index_monthly'] + \
                                '?'     
### 沪深股票--指数数据--大盘指数每日指标
GET_TUSHARE_INDEX_DAILYBASIC = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_index_dailybasic'] + \
                                '?'      
### 沪深股票--指数数据--申万行业分类
GET_TUSHARE_INDEX_CLASSIFY = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_index_classify'] + \
                                '?' 
### 另类数据--新闻快讯
GET_TUSHARE_NEWS = REQUEST_PROTOCOL['http'] + \
                                '://' + REQUEST_HOST['aliyun'] + \
                                ':' + REQUEST_PORT['default'] + \
                                '/' + DATAAPI['tushare'] + \
                                '/' + OPERATOR['get_tushare_news'] + \
                                '?'                                                               



### 具体接口路由汇集管理,用于api脚本实现if-elif的flat条件判断功能，避免大量条件语句，提高代码可读性
API_DICT = {}
### 将具体路由加载进api字典中，统一管理
API_DICT['get_tushare_stock_basic'] = GET_TUSHARE_STOCK_BASIC
API_DICT['get_tushare_stock_company'] = GET_TUSHARE_STOCK_COMPANY
API_DICT['get_tushare_daily'] = GET_TUSHARE_DAILY
API_DICT['get_tushare_weekly'] = GET_TUSHARE_WEEKLY
API_DICT['get_tushare_monthly'] = GET_TUSHARE_MONTHLY
API_DICT['get_tushare_daily_basic'] = GET_TUSHARE_DAILY_BASIC
API_DICT['get_tushare_income'] = GET_TUSHARE_INCOME
API_DICT['get_tushare_balancesheet'] = GET_TUSHARE_BALANCESHEET
API_DICT['get_tushare_cashflow'] = GET_TUSHARE_CASHFLOW
API_DICT['get_tushare_forecast'] = GET_TUSHARE_FORECAST
API_DICT['get_tushare_express'] = GET_TUSHARE_EXPRESS
API_DICT['get_tushare_fina_indicator'] = GET_TUSHARE_FINA_INDICATOR
API_DICT['get_tushare_index_daily'] = GET_TUSHARE_INDEX_DAILY
API_DICT['get_tushare_index_weekly'] = GET_TUSHARE_INDEX_WEEKLY
API_DICT['get_tushare_index_monthly'] = GET_TUSHARE_INDEX_MONTHLY
API_DICT['get_tushare_index_dailybasic'] = GET_TUSHARE_INDEX_DAILYBASIC
API_DICT['get_tushare_index_classify'] = GET_TUSHARE_INDEX_CLASSIFY
API_DICT['get_tushare_news'] = GET_TUSHARE_NEWS



##############################################################################################
##############################################################################################


