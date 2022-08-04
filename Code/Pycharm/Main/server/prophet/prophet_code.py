import itertools
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql
from prophet import Prophet
from prophet.diagnostics import cross_validation
from prophet.diagnostics import performance_metrics
from prophet.plot import add_changepoints_to_plot
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error

from parameter import Parameter_Dict

#################### DB 초기 설정 ####################
DB_USERNAME = 'root'
DB_HOST = 'localhost'
DB_PORT = '3306'

DB_PASSWORD = 'test1234'
DB_NAME = 'projectdb'

SECRET_KEY = 'dev'

sql_wholecol = 'SHOW columns FROM wholesale_price'
sql_wholedata = "SELECT * FROM wholesale_price ORDER BY date"

db = pymysql.Connect(host=DB_HOST,
                     user=DB_USERNAME,  # db 계정
                     password=DB_PASSWORD,  # db 비밀 번호
                     database=DB_NAME)  # 접속 하고자 하는 db 명

today = datetime.today().strftime("%Y%m%d")

#################### DB 초기 설정 ####################

# ##### 파라미터 다시 설정 해줘야할 때 사용할 것 ######
# param_grid = {'changepoint_prior_scale': [0.05, 0.1, 0.3, 0.5, 0.7],
#               'seasonality_prior_scale': [0.05, 0.1, 0.3, 0.5, 0.7],}
# # Generate all combinations of parameters
# all_params = [dict(zip(param_grid.keys(), v)) for v in itertools.product(*param_grid.values())]
# ##### 파라미터 다시 설정 해줘야할 때 사용할 것 ######

#################### 데이터 예측 ####################
with db:
    with db.cursor() as cur:
        Result = pd.DataFrame()
        Price_DF = pd.DataFrame()
        col_List = []
        Price_List = []
        cur.execute(sql_wholecol)
        for column in cur.fetchall():
            col_List.append(column[0])
        col_List = tuple(col_List)
        Price_List.append(col_List)

        cur.execute(sql_wholedata)
        for data in cur.fetchall():
            Price_List.append(data)

        Price_DF = pd.DataFrame(Price_List[1:], columns=Price_List[0])
        Price_DF['date'] = Price_DF['date'].astype('str')
        Price_DF['date'] = Price_DF['date'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))

        for cnt, column in enumerate(col_List[1:]):
            print('----------------------' + column + '----------------------')
            rmses = []  # Store the RMSEs for each params here
            Each_DF = Price_DF[['date', column]]
            Each_DF = Each_DF.rename(columns={'date': 'ds', column: 'y'})[['ds', 'y']]

            q1 = Each_DF['y'].quantile(0.25)
            q3 = Each_DF['y'].quantile(0.75)
            iqr = q3 - q1
            condition = Each_DF['y'] > q3 + 1.5 * iqr
            a = Each_DF[condition].index
            Each_DF.drop(a, inplace=True)

            #            ###### 파라미터 다시 설정 해줘야할 때 사용할 것 ######
            #             # Use cross validation to evaluate all parameters
            #             for params in all_params:
            #                 # print(params)
            #                 m = Prophet(**params,
            #                             seasonality_mode='multiplicative',
            #                             yearly_seasonality = True,
            #                             weekly_seasonality = True).fit(Each_DF)  # Fit model with given params
            #                 df_cv = cross_validation(m, initial='730 days', period='180 days',horizon = '365 days')
            #                 df_p = performance_metrics(df_cv)
            #                 rmses.append(df_p['rmse'].values[0])

            #             # Find the best parameters
            #             tuning_results = pd.DataFrame(all_params)
            #             tuning_results['rmse'] = rmses
            #             print(tuning_results)

            #             best_params = all_params[np.argmin(rmses)]
            #             print(best_params)
            #             print('----------------------' + column + '----------------------')
            #            ###### 파라미터 다시 설정 해줘야할 때 사용할 것 ######

            # 각각의 파라미터 설정
            param_grid = Parameter_Dict[column]
            print(param_grid)
            m = Prophet(**param_grid,
                        seasonality_mode='multiplicative',
                        yearly_seasonality=True,
                        weekly_seasonality=True).fit(Each_DF)  # Fit model with given params

            # 모델 학습
            future = m.make_future_dataframe(periods=25)
            forecast = m.predict(future)

            sundayList = forecast.query('ds.dt.dayofweek == 6')
            sundayList
            n_forecast = forecast.drop(sundayList.index)
            n_forecast

            #             ###### Pycharm 실행시 나오지 않음 ######
            #             fig, ax = plt.subplots(figsize=(16,5))
            #             plt.plot(n_forecast['ds'].dt.to_pydatetime(), n_forecast['yhat'], label='forecast', color='blue')
            #             plt.plot(Each_DF['ds'].dt.to_pydatetime(), Each_DF['y'], label='observations ', color='black')
            #             plt.fill_between(n_forecast['ds'].dt.to_pydatetime(), n_forecast['yhat_upper'],
            #                              n_forecast['yhat_lower'], color='skyblue',label='80% confidence interval')
            #             plt.legend()
            #             plt.xlabel('date')
            #             plt.ylabel('price')
            #             plt.show()
            #             ###### Pycharm 실행시 나오지 않음 ######
            filtered_df = n_forecast.query("ds >= {} ".format(today))

            Result_DF = filtered_df[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head(10)
            Result_DF.to_csv(
                'C:\\G_Project\\Code\\Pycharm\\Main\\DB_source\\csv\\' + today + '_' + "wholesale" + '_' + column + '.csv')
