
from roshareclient.client.api import DataAPI



### 使用字典设置除了token_key、token和tushare_token外，额外的参数
### get_tushare_stock_basic
# tmp_dict = {}
# tmp_dict['exchange'] = ''
# tmp_dict['list_status'] = 'L'
# tmp_dict['fields'] = 'ts_code,symbol,name,area,industry,list_date'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYyNDAzMjMuNjMwODc5NCwidXNlciI6InRlc3QifQ.MGd7GVAQ48opAPq-k1hG7EYbC-honEFenPNJTPz25BA',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_stock_basic(params=tmp_dict)
# print(df)
### get_tushare_stock_company
# tmp_dict = {}
# tmp_dict['exchange'] = ''
# tmp_dict['fields'] = 'ts_code,chairman,manager,secretary,reg_capital,setup_date,province'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYyNDAzMjMuNjMwODc5NCwidXNlciI6InRlc3QifQ.MGd7GVAQ48opAPq-k1hG7EYbC-honEFenPNJTPz25BA',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_stock_company(params=tmp_dict)
# print(df)
### get_tushare_daily
# tmp_dict = {}
# tmp_dict['ts_code'] = '000001.SZ'
# tmp_dict['start_date'] = '20230601'
# tmp_dict['end_date'] = '20230605'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYyNDAzMjMuNjMwODc5NCwidXNlciI6InRlc3QifQ.MGd7GVAQ48opAPq-k1hG7EYbC-honEFenPNJTPz25BA',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_daily(params=tmp_dict)
# print(df)
### get_tushare_weekly
# tmp_dict = {}
# tmp_dict['ts_code'] = '000001.SZ'
# tmp_dict['start_date'] = '20230601'
# tmp_dict['end_date'] = '20230605'
# tmp_dict['fields'] = 'ts_code,trade_date,open,high,low,close,vol,amount'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYyNDAzMjMuNjMwODc5NCwidXNlciI6InRlc3QifQ.MGd7GVAQ48opAPq-k1hG7EYbC-honEFenPNJTPz25BA',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_weekly(params=tmp_dict)
# print(df)
### get_tushare_monthly
# tmp_dict = {}
# tmp_dict['ts_code'] = '000001.SZ'
# tmp_dict['start_date'] = '20230101'
# tmp_dict['end_date'] = '20230605'
# tmp_dict['fields'] = 'ts_code,trade_date,open,high,low,close,vol,amount'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYyNDAzMjMuNjMwODc5NCwidXNlciI6InRlc3QifQ.MGd7GVAQ48opAPq-k1hG7EYbC-honEFenPNJTPz25BA',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_monthly(params=tmp_dict)
# print(df)
### get_tushare_daily_basic
# tmp_dict = {}
# tmp_dict['ts_code'] = ''
# tmp_dict['trade_date'] = '20230601'
# tmp_dict['fields'] = 'ts_code,trade_date,turnover_rate,volume_ratio,pe,pb'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYyNDAzMjMuNjMwODc5NCwidXNlciI6InRlc3QifQ.MGd7GVAQ48opAPq-k1hG7EYbC-honEFenPNJTPz25BA',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_daily_basic(params=tmp_dict)
# print(df)
### get_tushare_income
# tmp_dict = {}
# tmp_dict['ts_code'] = '600000.SH'
# tmp_dict['start_date'] = '20230101'
# tmp_dict['end_date'] = '20230605'
# tmp_dict['fields'] = 'ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,diluted_eps'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYzMjQ5NDUuODkxOTEzNywidXNlciI6InRlc3QifQ.XElnwVRsMrT9LLJCUNVuRu00WDoTNNm0_X5bTKmoy2A',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_income(params=tmp_dict)
# print(df)
### get_tushare_balancesheet
# tmp_dict = {}
# tmp_dict['ts_code'] = '600000.SH'
# tmp_dict['start_date'] = '20230101'
# tmp_dict['end_date'] = '20230605'
# tmp_dict['fields'] = 'ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,cap_rese'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYzMjQ5NDUuODkxOTEzNywidXNlciI6InRlc3QifQ.XElnwVRsMrT9LLJCUNVuRu00WDoTNNm0_X5bTKmoy2A',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_balancesheet(params=tmp_dict)
# print(df)
### get_tushare_cashflow
# tmp_dict = {}
# tmp_dict['ts_code'] = '600000.SH'
# tmp_dict['start_date'] = '20230101'
# tmp_dict['end_date'] = '20230605'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYzMjQ5NDUuODkxOTEzNywidXNlciI6InRlc3QifQ.XElnwVRsMrT9LLJCUNVuRu00WDoTNNm0_X5bTKmoy2A',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_cashflow(params=tmp_dict)
# print(df)
### get_tushare_forecast
# tmp_dict = {}
# tmp_dict['ann_date'] = '20230131'
# tmp_dict['fields'] = 'ts_code,ann_date,end_date,type,p_change_min,p_change_max,net_profit_min'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYzMjQ5NDUuODkxOTEzNywidXNlciI6InRlc3QifQ.XElnwVRsMrT9LLJCUNVuRu00WDoTNNm0_X5bTKmoy2A',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_forecast(params=tmp_dict)
# print(df)
### get_tushare_express
# tmp_dict = {}
# tmp_dict['ts_code'] = '600000.SH'
# tmp_dict['start_date'] = '20230101'
# tmp_dict['end_date'] = '20230605'
# tmp_dict['fields'] = 'ts_code,ann_date,end_date,revenue,operate_profit,total_profit,n_income,total_assets'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYzMjQ5NDUuODkxOTEzNywidXNlciI6InRlc3QifQ.XElnwVRsMrT9LLJCUNVuRu00WDoTNNm0_X5bTKmoy2A',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_express(params=tmp_dict)
# print(df)
### get_tushare_fina_indicator
# tmp_dict = {}
# tmp_dict['ts_code'] = '600000.SH'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYzMjQ5NDUuODkxOTEzNywidXNlciI6InRlc3QifQ.XElnwVRsMrT9LLJCUNVuRu00WDoTNNm0_X5bTKmoy2A',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_fina_indicator(params=tmp_dict)
# print(df)
### get_tushare_index_daily
# tmp_dict = {}
# tmp_dict['ts_code'] = '399300.SZ'
# tmp_dict['start_date'] = '20230101'
# tmp_dict['end_date'] = '20230605'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYzMjQ5NDUuODkxOTEzNywidXNlciI6InRlc3QifQ.XElnwVRsMrT9LLJCUNVuRu00WDoTNNm0_X5bTKmoy2A',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_index_daily(params=tmp_dict)
# print(df)
### get_tushare_index_weekly
# tmp_dict = {}
# tmp_dict['ts_code'] = '399300.SZ'
# tmp_dict['start_date'] = '20230101'
# tmp_dict['end_date'] = '20230605'
# tmp_dict['fields'] = 'ts_code,trade_date,open,high,low,close,vol,amount'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYzMjQ5NDUuODkxOTEzNywidXNlciI6InRlc3QifQ.XElnwVRsMrT9LLJCUNVuRu00WDoTNNm0_X5bTKmoy2A',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_index_weekly(params=tmp_dict)
# print(df)
### get_tushare_index_monthly
# tmp_dict = {}
# tmp_dict['ts_code'] = '399300.SZ'
# tmp_dict['start_date'] = '20230101'
# tmp_dict['end_date'] = '20230605'
# tmp_dict['fields'] = 'ts_code,trade_date,open,high,low,close,vol,amount'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYzMjQ5NDUuODkxOTEzNywidXNlciI6InRlc3QifQ.XElnwVRsMrT9LLJCUNVuRu00WDoTNNm0_X5bTKmoy2A',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_index_monthly(params=tmp_dict)
# print(df)
### get_tushare_index_dailybasic
# tmp_dict = {}
# tmp_dict['trade_date'] = '20230601'
# tmp_dict['fields'] = 'ts_code,trade_date,turnover_rate,pe'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYzMjQ5NDUuODkxOTEzNywidXNlciI6InRlc3QifQ.XElnwVRsMrT9LLJCUNVuRu00WDoTNNm0_X5bTKmoy2A',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_index_dailybasic(params=tmp_dict)
# print(df)
### get_tushare_index_classify
# tmp_dict = {}
# tmp_dict['level'] = 'L1'
# tmp_dict['src'] = 'SW2021'
# roshareclient = DataAPI(token_key = 7890,
#                     token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYzMjQ5NDUuODkxOTEzNywidXNlciI6InRlc3QifQ.XElnwVRsMrT9LLJCUNVuRu00WDoTNNm0_X5bTKmoy2A',
#                     tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
#                     timeout=6000)
# df = roshareclient.get_tushare_index_classify(params=tmp_dict)
# print(df)
### get_tushare_news
tmp_dict = {}
tmp_dict['src'] = 'eastmoney'
tmp_dict['start_date'] = '2023-06-09+00:00:00' ### url中+号表示空格
tmp_dict['end_date'] = '2023-06-10+00:00:00'
roshareclient = DataAPI(token_key = 7890,
                    token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODY0OTYzMDIuMTE5MjAyNiwidXNlciI6InRlc3QifQ.wZE19w5MLM6FNn78vLTg3PPc-M8Blm-M1mwTLR0xpuw',
                    tushare_token='cd77d46c73f80cb42c4c1cadd52cd81daa9c40f7a137c809de96b90a',
                    timeout=6000)
df = roshareclient.get_tushare_news(params=tmp_dict)
print(df)
