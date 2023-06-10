# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个roshareclient数据服务sdk类，主要功能提供数据接口，主要技术requests,http和partial
"""
模块介绍
-------

这是一个roshareclient数据服务sdk类，主要功能提供数据接口，主要技术requests,http和partial

设计模式：

    无

关键点：    

    （1）requests

主要功能：            

    （1）roshareclient数据接口
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import pandas as pd
import json
from functools import partial
from urllib.request import urlopen,Request
from roshareclient.client.cons import API_DICT



####### roshareclient服务应用用户路由 #########################################
### 设计模式：                                                             ###
###     无                                                                ###
### 关键点：                                                               ###
### （1）requests                                                         ###
### 主要功能：                                                             ###
### （1）roshareclient数据接口                                             ###
############################################################################



###### roshareclient数据接口-PythonSDK ###############################################################
#####################################################################################################



class DataAPI(object):
    '''
    类介绍：

        这是一个客户端数据接口类，主要功能提供python客户端获取各种数据的接口，主要技术partial和__getattr__
    '''

    ### 将token_key，token和默认http_url作为私有属性
    __token_key = ''
    __token = ''
    __tushare_token = ''
    __http_url = '127.0.0.1:8000' ### 暂时用不上，具体数据服务路由信息可在roshareclient.client.cons中获得；后续如果有了固定数据服务地址可在此使用此私有属性固定住,一般url信息保存在cons.py中


    def __init__(self,token_key,token,tushare_token,timeout):
        '''
        属性功能：

            定义一个初始化属性，主要功能提供加载token和请求相关信息

        参数：
            token_key (str): token密钥
            token (str): token字符串
            tushare_token (str): tushare的token字符串
            timeout (int): 超时时间

        返回：
            无
        '''

        self.__token_key = token_key
        self.__token = token
        self.__tushare_token = tushare_token
        self.__timeout = timeout


    def query(self,dataapi,params):
        '''
        方法功能：

            定义一个调用http服务接口获得数据，进行操作的方法，主要功能调用数据服务

        参数：
            dataapi (str): 数据接口名称
            params (dict): 参数数据字典

        返回：
            df (dataframe): 请求获得的数据，数据类型在非正常返回状况下也可以为其他类型
        '''

        ### 参数字典中加入token_key和token,使用http发送get协议的时候不需要考虑参数顺序,此处加入了tushare自己的token
        params['token_key'] = self.__token_key
        params['token'] = self.__token
        params['tushare_token'] = self.__tushare_token
        print(params)
        ### 从cons中收集URL路由，然后转化参数字典为字符串，最后拼接URL
        ### 使用字典装填dataapi,替代if-elif，实现flat-if形式的条件判断
        url_route = API_DICT[dataapi]
        url_params = resolve_dict_for_url_params(tmp_dict=params)
        url = url_route + url_params
        ### 使用urllib发起请求，并获得数据
        df = get_dataframe_from_request(url=url,timeout=self.__timeout)

        return df


    def __getattr__(self,dataapi):
        '''
        方法功能：

            重写一个实例'.'操作符的魔法方法__getattr__，主要功能以'.'方式调用数据服务，主要技术partial

        参数：
            dataadpi (str): 数据服务名称，具体为API_DICT中的键名称

        返回：
            partial (object): 固定了dataapi参数的偏函数对象
        '''

        return partial(self.query,dataapi)



######## 辅助函数 ###############################################################################################
################################################################################################################



### 解析参数字典为URL字符串格式
def resolve_dict_for_url_params(tmp_dict):
    '''
    函数功能：
        定义一个将参数字典解析为符合URL要求的字符串格式

    参数：
        tmp_dict (dict): 参数字典
    
    返回：
        tmp_str (str): URL参数字符串
    '''

    tmp_params_tuple_list = [i for i in zip(tmp_dict.keys(),tmp_dict.values())]
    tmp_params_list  = [str(tmp_tuple[0]) + '=' + str(tmp_tuple[1]) for tmp_tuple in tmp_params_tuple_list]
    tmp_str = ''
    for i,item in enumerate(tmp_params_list):
        if i == 0:
            tmp_join_str = item
        else:
            tmp_join_str = '&' + item
        tmp_str = tmp_str + tmp_join_str

    return tmp_str



### 从请求中获取DataFrame
def get_dataframe_from_request(url,timeout):
    '''
    函数功能：

        定义一个从请求中获取DataFrame的函数

    参数：
        url (str): URL字符串
        timeout (int): 超时时间

    返回：
        df (DataFrame): 请求返回的数据
    '''

    ### 请求request
    request = Request(url=url)
    ### 解析请求
    lines = urlopen(request, timeout = timeout).read()
    js = json.loads(lines.decode('utf-8'))   
    print(type(js))
    ### 如果返回直接为字典的话，直接返回
    if type(js) != list:
        return js
    else:
        ### 转换成dataframe
        df = pd.DataFrame(js)    
        return df ### 此处返回的dataframe在stdout中可能无法全部显示，可以导出在csv中查看或直接内存中操作，jupyter中测试已通过



################################################################################################################## 
##################################################################################################################


