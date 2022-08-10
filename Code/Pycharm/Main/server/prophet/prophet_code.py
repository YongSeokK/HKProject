import itertools
import os
import traceback
from datetime import datetime

import numpy as np
import pandas as pd
import pymysql
from prophet import Prophet
from prophet.diagnostics import cross_validation
from prophet.diagnostics import performance_metrics
from tqdm import tqdm


#####################################################

class MyProphet:
    ### init 설정
    def __init__(self, DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME, Root_Path, W_Parameter_Dict, R_Parameter_Dict):
        self.DB_USERNAME = DB_USERNAME
        self.DB_HOST = DB_HOST
        self.DB_PASSWORD = DB_PASSWORD
        self.DB_NAME = DB_NAME
        self.Root_Path = Root_Path
        self.Retail_Path = self.Root_Path + '\\DB_source\\csv\\retail\\'
        self.Wholesale_Path = self.Root_Path + '\\DB_source\\csv\\wholesale\\'
        self.W_Parameter_Dict = W_Parameter_Dict
        self.R_Parameter_Dict = R_Parameter_Dict

    ### 도매 데이터 처리
    def Wholesale(self):

        try:
            ## 폴더 내에 파일 있으면 제거
            if os.path.exists(self.Wholesale_Path):
                for file in os.scandir(self.Wholesale_Path):
                    os.remove(file.path)
            else:
                os.mkdir(self.Wholesale_Path)

            ## DB 연결
            db = pymysql.Connect(host=self.DB_HOST,
                                 user=self.DB_USERNAME,  # db 계정
                                 password=self.DB_PASSWORD,  # db 비밀 번호
                                 database=self.DB_NAME)  # 접속 하고자 하는 db 명

            today = datetime.today().strftime("%Y%m%d")

            ## DB 작업
            with db:
                with db.cursor() as cur:

                    # 쿼리문
                    sql_wholecol = 'SHOW columns FROM wholesale_price'
                    sql_wholedata = "SELECT * FROM wholesale_price ORDER BY date"

                    # 각 결과물을 저장할 초기 설정
                    Result = pd.DataFrame()
                    Price_DF = pd.DataFrame()
                    col_List = []
                    Price_List = []

                    # 쿼리문 실행 (컬럼 찾기)
                    cur.execute(sql_wholecol)
                    for column in cur.fetchall():
                        col_List.append(column[0])
                    col_List = tuple(col_List)
                    Price_List.append(col_List)

                    # 퀴리문 실행 (데이터 찾기)
                    cur.execute(sql_wholedata)
                    for data in cur.fetchall():
                        Price_List.append(data)

                    # 데이터 프레임 제작
                    Price_DF = pd.DataFrame(Price_List[1:], columns=Price_List[0])

                    # 날짜를 형식에 맞게 변환
                    Price_DF['date'] = Price_DF['date'].astype('str')
                    Price_DF['date'] = Price_DF['date'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))

                    # 각 농산물 별로 ds, y 데이터 프레임 제작
                    with tqdm(total=len(col_List[1:]), desc='도매 Prophet 예측') as pbar:
                        for cnt, column in enumerate(col_List[1:]):
                            # print('----------------------' + column + '----------------------')
                            rmses = []  # Store the RMSEs for each params here
                            Each_DF = Price_DF[['date', column]]
                            Each_DF = Each_DF.rename(columns={'date': 'ds', column: 'y'})[['ds', 'y']]

                            # 이상치 값 제거
                            q1 = Each_DF['y'].quantile(0.25)
                            q3 = Each_DF['y'].quantile(0.75)
                            iqr = q3 - q1
                            condition = Each_DF['y'] > q3 + 1.5 * iqr
                            a = Each_DF[condition].index
                            Each_DF.drop(a, inplace=True)

                            # 각각의 파라미터 설정
                            param_grid = self.W_Parameter_Dict[column]
                            # print(param_grid)
                            m = Prophet(**param_grid,
                                        seasonality_mode='multiplicative',
                                        yearly_seasonality=True,
                                        weekly_seasonality=True).fit(Each_DF)  # Fit model with given params

                            # 모델 학습
                            future = m.make_future_dataframe(periods=25)
                            forecast = m.predict(future)

                            sundayList = forecast.query('ds.dt.dayofweek == 6')
                            n_forecast = forecast.drop(sundayList.index)

                            # 오늘 날짜를 기준으로 같거나 큰 날짜만 출력
                            filtered_df = n_forecast.query("ds >= {} ".format(today))

                            # 필요 값 추출
                            Result_DF = filtered_df[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head(10)

                            # csv 파일로 저장
                            Result_DF.to_csv(self.Wholesale_Path + today + '_' + "wholesale" + '_' + column + '.csv')
                            pbar.update(1)
            message = 'Wholesale Finish'
            cur.close()
        except Exception as e:
            message = traceback.format_exc()
        return message

    ### 소매 데이터 처리
    def Retail(self):
        ## 데이터 전처리에 필요한 초기 값들
        chinese_cabbage_T = 'chinese_cabbageF_T, chinese_cabbageW_T, chinese_cabbageS_T, chinese_cabbageH_T'
        chinese_cabbage_M = 'chinese_cabbageF_M, chinese_cabbageW_M, chinese_cabbageS_M, chinese_cabbageH_M'
        radish_T = 'radishF_T, radishW_T, radishS_T, radishH_T'
        radish_M = 'radishF_M, radishW_M, radishS_M, radishH_M'
        apple_T = 'appleF_T, appleT_T, appleR_T'
        apple_M = 'appleF_M, appleT_M, appleR_M'
        pear_T = 'pearS_T, pearW_T'
        pear_M = 'pearS_M, pearW_M'
        grape_T = 'grapeC_T, grapeR_T'
        grape_M = 'grapeC_M, grapeR_M'
        citrus_T = 'citrusR_T, citrusH_T'
        citrus_M = 'citrusR_M, citrusH_M'
        kiwi_T = 'kiwiN_T, kiwiK_T'
        kiwi_M = 'kiwiN_M, kiwiK_M'
        orange_T = 'orangeU_T, orangeA_T'
        orange_M = 'orangeU_M, orangeA_M'

        banList = ['riceF_T', 'riceF_M',
                   'chinese_cabbageF_T', 'chinese_cabbageW_T', 'chinese_cabbageS_T', 'chinese_cabbageH_T',
                   'chinese_cabbageF_M', 'chinese_cabbageW_M', 'chinese_cabbageS_M', 'chinese_cabbageH_M',
                   'radishF_T', 'radishW_T', 'radishS_T', 'radishH_T',
                   'radishF_M', 'radishW_M', 'radishS_M', 'radishH_M',
                   'appleF_T', 'appleT_T', 'appleR_T', 'appleF_M', 'appleT_M', 'appleR_M',
                   'pearS_T', 'pearW_T', 'pearS_M', 'pearW_M',
                   'grapeC_T', 'grapeR_T', 'grapeC_M', 'grapeR_M',
                   'citrusR_T', 'citrusH_T', 'citrusR_M', 'citrusH_M',
                   'kiwiN_T', 'kiwiK_T', 'kiwiN_M', 'kiwiK_M',
                   'orangeU_T', 'orangeA_T', 'orangeU_M', 'orangeA_M']

        ## 차후 데이터 프레임에 쌓을 리스트 생성
        chinese_cabbage_T_data_List = [];
        chinese_cabbage_M_data_List = []
        radish_T_data_List = [];
        radish_M_data_List = []
        apple_T_data_List = [];
        apple_M_data_List = []
        pear_T_data_List = [];
        pear_M_data_List = []
        grape_T_data_List = [];
        grape_M_data_List = []
        citrus_T_data_List = [];
        citrus_M_data_List = []
        kiwi_T_data_List = [];
        kiwi_M_data_List = []
        orange_T_data_List = [];
        orange_M_data_List = []

        try:
            ## 폴더 내에 파일 있으면 제거
            if os.path.exists(self.Retail_Path):
                for file in os.scandir(self.Retail_Path):
                    os.remove(file.path)
            else:
                os.mkdir(self.Retail_Path)

            ## DB 연결
            db = pymysql.Connect(host=self.DB_HOST,
                                 user=self.DB_USERNAME,  # db 계정
                                 password=self.DB_PASSWORD,  # db 비밀 번호
                                 database=self.DB_NAME)  # 접속 하고자 하는 db 명

            today = datetime.today().strftime("%Y%m%d")

            ## DB 작업
            with db:
                with db.cursor() as cur:

                    # 쿼리문
                    sql_retailcol = 'SHOW columns FROM total_retail'
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"

                    # 각 결과물을 저장할 초기 설정
                    col_Text = ''
                    col_List = []
                    Price_List = []
                    Result = pd.DataFrame()
                    Price_DF = pd.DataFrame()

                    # 쿼리문 실행(조건에 맞는 컬럼 찾기)
                    cur.execute(sql_retailcol)
                    for column in cur.fetchall():

                        # 조건에 맞는 데이터 추출
                        if column[0] == 'date':
                            col_List.append(column[0])
                            col_Text = col_Text + column[0]
                        else:
                            if column[0] in banList:
                                pass
                            else:
                                # 'mackerelL_T' 이후는 수산물 이므로 break 실행
                                if column[0] != 'mackerelL_T':
                                    col_List.append(column[0])
                                    col_Text = col_Text + "," + column[0]
                                else:
                                    break

                    ## banList 에 있는 데이터 전처리 각 각 특징에 맞게 작업 해야 하므로 각 각 예외처리 진행
                    # 배추(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(chinese_cabbage_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            chinese_cabbage = sum(data[0: 4]) / (len(data[0: 4]) - data[0: 4].count(0))
                        except:
                            chinese_cabbage = 0
                        chinese_cabbage_T_data_List.append(chinese_cabbage)
                    # 배추(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(chinese_cabbage_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            chinese_cabbage = sum(data[0: 4]) / (len(data[0: 4]) - data[0: 4].count(0))
                        except:
                            chinese_cabbage = 0
                        chinese_cabbage_M_data_List.append(chinese_cabbage)

                    # 무(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(radish_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            radish = sum(data[0: 4]) / (len(data[0: 4]) - data[0: 4].count(0))
                        except:
                            radish = 0
                        radish_T_data_List.append(radish)
                    # 무(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(radish_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            radish = sum(data[0: 4]) / (len(data[0: 4]) - data[0: 4].count(0))
                        except:
                            radish = 0
                        radish_M_data_List.append(radish)

                    # 사과(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(apple_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            apple = sum(data[0: 3]) / (len(data[0: 3]) - data[0: 3].count(0))
                        except:
                            apple = 0
                        apple_T_data_List.append(apple)
                    # 사과(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(apple_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            apple = sum(data[0: 3]) / (len(data[0: 3]) - data[0: 3].count(0))
                        except:
                            apple = 0
                        apple_M_data_List.append(apple)

                    # 배(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(pear_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            pear = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            pear = 0
                        pear_T_data_List.append(pear)
                    # 배(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(pear_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            pear = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            pear = 0
                        pear_M_data_List.append(pear)

                    # 포도(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(grape_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            grape = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            grape = 0
                        grape_T_data_List.append(grape)
                    # 포도(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(grape_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            grape = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            grape = 0
                        grape_M_data_List.append(grape)

                    # 귤(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(citrus_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            citrus = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            citrus = 0
                        citrus_T_data_List.append(citrus)
                    # 귤(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(citrus_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            citrus = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            citrus = 0
                        citrus_M_data_List.append(citrus)

                    # 키워(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(kiwi_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            kiwi = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            kiwi = 0
                        kiwi_T_data_List.append(kiwi)
                    # 키워(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(kiwi_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            kiwi = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            kiwi = 0
                        kiwi_M_data_List.append(kiwi)

                    # 오렌지(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(orange_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            orange = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            orange = 0
                        orange_T_data_List.append(orange)
                    # 오렌지(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(orange_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            orange = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            orange = 0
                        orange_M_data_List.append(orange)

                    col_List = tuple(col_List)
                    Price_List.append(col_List)

                    # 퀴리문 실행 (조건에 맞는 데이터 찾기)
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = sql_retaildata.format(col_Text)
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        Price_List.append(data)

                    # 데이터 프레임 제작
                    Price_DF = pd.DataFrame(Price_List[1:], columns=Price_List[0])

                    # 쿼리문으로 실행한 데이터와 위에서 예외 처리한 데이터 병합합
                    Price_DF = Price_DF.assign(chinese_cabbage_T=chinese_cabbage_T_data_List,  # 배추(시장)
                                               chinese_cabbage_M=chinese_cabbage_M_data_List,  # 배추(마트)
                                               radish_T=radish_T_data_List,  # 무(시장)
                                               radish_M=radish_M_data_List,  # 무(마트)
                                               apple_T=apple_T_data_List,  # 사과(시장)
                                               apple_M=apple_M_data_List,  # 사과(마트)
                                               pear_T=pear_T_data_List,  # 배(시장)
                                               pear_M=pear_M_data_List,  # 배(마트)
                                               grape_T=grape_T_data_List,  # 포도(시장)
                                               grape_M=grape_M_data_List,  # 포도(마트)
                                               citrus_T=citrus_T_data_List,  # 귤(시장)
                                               citrus_M=citrus_M_data_List,  # 귤(마트)
                                               kiwi_T=kiwi_T_data_List,  # 키위(시장)
                                               kiwi_M=kiwi_M_data_List,  # 키위(마트)
                                               orange_T=orange_T_data_List,  # 오렌지(시장)
                                               orange_M=orange_M_data_List)  # 오렌지(마트)
                    # 날짜를 형식에 맞게 변환
                    Price_DF['date'] = Price_DF['date'].astype('str')
                    Price_DF['date'] = Price_DF['date'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))

                    # 데이터 프레임 컬럼명 리스트 제작
                    Price_col_List = [col for col in Price_DF.columns]

                    # 각 농산물 별로 ds, y 데이터 프레임 제작
                    with tqdm(total=len(Price_col_List[1:]), desc='소매 Prophet 예측') as pbar:
                        for cnt, column in enumerate(Price_col_List[1:]):
                            # print('----------------------' + column + '----------------------')
                            rmses = []  # Store the RMSEs for each params here
                            Each_DF = Price_DF[['date', column]]
                            Each_DF = Each_DF.rename(columns={'date': 'ds', column: 'y'})[['ds', 'y']]

                            # 이상치 값 제거
                            q1 = Each_DF['y'].quantile(0.25)
                            q3 = Each_DF['y'].quantile(0.75)
                            iqr = q3 - q1
                            condition = Each_DF['y'] > q3 + 1.5 * iqr
                            a = Each_DF[condition].index
                            Each_DF.drop(a, inplace=True)

                            # 각각의 파라미터 설정
                            param_grid = self.R_Parameter_Dict[column]
                            # print(param_grid)
                            m = Prophet(**param_grid,
                                        seasonality_mode='multiplicative',
                                        yearly_seasonality=True,
                                        weekly_seasonality=True).fit(Each_DF)  # Fit model with given params

                            # 모델 학습
                            future = m.make_future_dataframe(periods=15)
                            forecast = m.predict(future)

                            sundayList = forecast.query('ds.dt.dayofweek == 6')
                            n_forecast = forecast.drop(sundayList.index)
                            satdayList = forecast.query('ds.dt.dayofweek == 5')
                            n_forecast = forecast.drop(satdayList.index)

                            # 오늘 날짜를 기준으로 같거나 큰 날짜만 출력
                            filtered_df = n_forecast.query("ds >= {} ".format(today))

                            # 필요 값 추출
                            Result_DF = filtered_df[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head(10)

                            # csv 파일로 저장
                            Result_DF.to_csv(self.Retail_Path + today + '_' + "retail" + '_' + column + '.csv')
                            pbar.update(1)
            message = 'Retail Finish'
            cur.close()
        except Exception as e:
            message = traceback.format_exc()
        return message

    ### 도매 데이터 파라미터 찾기
    def Wholesale_Param(self):
        Result_params_Dict = []
        ##### 파라미터 다시 설정 해줘야할 때 사용할 것 ######
        param_grid = {'changepoint_prior_scale': [0.05, 0.1, 0.3, 0.5, 0.7],
                      'seasonality_prior_scale': [0.05, 0.1, 0.3, 0.5, 0.7], }
        # Generate all combinations of parameters
        all_params = [dict(zip(param_grid.keys(), v)) for v in itertools.product(*param_grid.values())]
        ##### 파라미터 다시 설정 해줘야할 때 사용할 것 ######

        try:
            ## DB 연결
            db = pymysql.Connect(host=self.DB_HOST,
                                 user=self.DB_USERNAME,  # db 계정
                                 password=self.DB_PASSWORD,  # db 비밀 번호
                                 database=self.DB_NAME)  # 접속 하고자 하는 db 명

            today = datetime.today().strftime("%Y%m%d")

            ## DB 작업
            with db:
                with db.cursor() as cur:

                    # 쿼리문
                    sql_wholecol = 'SHOW columns FROM wholesale_price'
                    sql_wholedata = "SELECT * FROM wholesale_price ORDER BY date"

                    # 각 결과물을 저장할 초기 설정
                    Result = pd.DataFrame()
                    Price_DF = pd.DataFrame()
                    col_List = []
                    Price_List = []

                    # 쿼리문 실행 (컬럼 찾기)
                    cur.execute(sql_wholecol)
                    for column in cur.fetchall():
                        col_List.append(column[0])
                    col_List = tuple(col_List)
                    Price_List.append(col_List)

                    # 퀴리문 실행 (데이터 찾기)
                    cur.execute(sql_wholedata)
                    for data in cur.fetchall():
                        Price_List.append(data)

                    # 데이터 프레임 제작
                    Price_DF = pd.DataFrame(Price_List[1:], columns=Price_List[0])

                    # 날짜를 형식에 맞게 변환
                    Price_DF['date'] = Price_DF['date'].astype('str')
                    Price_DF['date'] = Price_DF['date'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))

                    # 각 농산물 별로 ds, y 데이터 프레임 제작
                    for cnt, column in enumerate(col_List[1:]):
                        Result = {}
                        # print('----------------------' + column + '----------------------')
                        rmses = []  # Store the RMSEs for each params here
                        Each_DF = Price_DF[['date', column]]
                        Each_DF = Each_DF.rename(columns={'date': 'ds', column: 'y'})[['ds', 'y']]

                        # 이상치 값 제거
                        q1 = Each_DF['y'].quantile(0.25)
                        q3 = Each_DF['y'].quantile(0.75)
                        iqr = q3 - q1
                        condition = Each_DF['y'] > q3 + 1.5 * iqr
                        a = Each_DF[condition].index
                        Each_DF.drop(a, inplace=True)

                        ###### 파라미터 다시 설정 해줘야할 때 사용할 것 ######
                        # Use cross validation to evaluate all parameters
                        for params in all_params:
                            # print(params)
                            m = Prophet(**params,
                                        seasonality_mode='multiplicative',
                                        yearly_seasonality=True,
                                        weekly_seasonality=True).fit(Each_DF)  # Fit model with given params
                            df_cv = cross_validation(m, initial='730 days', period='180 days', horizon='365 days')
                            df_p = performance_metrics(df_cv)
                            rmses.append(df_p['rmse'].values[0])

                        # Find the best parameters
                        tuning_results = pd.DataFrame(all_params)
                        tuning_results['rmse'] = rmses

                        best_params = all_params[np.argmin(rmses)]
                        Result[data] = best_params
                        Result_params_Dict.append(Result)

                        # print('----------------------' + column + '----------------------')
                        ###### 파라미터 다시 설정 해줘야할 때 사용할 것 ######
            message = Result_params_Dict
            cur.close()
        except Exception as e:
            message = traceback.format_exc()
        return message

    ### 소매 데이터 파라미터 찾기
    def Retail_Param(self):
        Result_params_Dict = []
        ##### 파라미터 다시 설정 해줘야할 때 사용할 것 ######
        param_grid = {'changepoint_prior_scale': [0.05, 0.1, 0.3, 0.5, 0.7],
                      'seasonality_prior_scale': [0.05, 0.1, 0.3, 0.5, 0.7], }
        # Generate all combinations of parameters
        all_params = [dict(zip(param_grid.keys(), v)) for v in itertools.product(*param_grid.values())]
        ##### 파라미터 다시 설정 해줘야할 때 사용할 것 ######

        ## 데이터 전처리에 필요한 초기 값들
        chinese_cabbage_T = 'chinese_cabbageF_T, chinese_cabbageW_T, chinese_cabbageS_T, chinese_cabbageH_T'
        chinese_cabbage_M = 'chinese_cabbageF_M, chinese_cabbageW_M, chinese_cabbageS_M, chinese_cabbageH_M'
        radish_T = 'radishF_T, radishW_T, radishS_T, radishH_T'
        radish_M = 'radishF_M, radishW_M, radishS_M, radishH_M'
        apple_T = 'appleF_T, appleT_T, appleR_T'
        apple_M = 'appleF_M, appleT_M, appleR_M'
        pear_T = 'pearS_T, pearW_T'
        pear_M = 'pearS_M, pearW_M'
        grape_T = 'grapeC_T, grapeR_T'
        grape_M = 'grapeC_M, grapeR_M'
        citrus_T = 'citrusR_T, citrusH_T'
        citrus_M = 'citrusR_M, citrusH_M'
        kiwi_T = 'kiwiN_T, kiwiK_T'
        kiwi_M = 'kiwiN_M, kiwiK_M'
        orange_T = 'orangeU_T, orangeA_T'
        orange_M = 'orangeU_M, orangeA_M'

        banList = ['riceF_T', 'riceF_M',
                   'chinese_cabbageF_T', 'chinese_cabbageW_T', 'chinese_cabbageS_T', 'chinese_cabbageH_T',
                   'chinese_cabbageF_M', 'chinese_cabbageW_M', 'chinese_cabbageS_M', 'chinese_cabbageH_M',
                   'radishF_T', 'radishW_T', 'radishS_T', 'radishH_T',
                   'radishF_M', 'radishW_M', 'radishS_M', 'radishH_M',
                   'appleF_T', 'appleT_T', 'appleR_T', 'appleF_M', 'appleT_M', 'appleR_M',
                   'pearS_T', 'pearW_T', 'pearS_M', 'pearW_M',
                   'grapeC_T', 'grapeR_T', 'grapeC_M', 'grapeR_M',
                   'citrusR_T', 'citrusH_T', 'citrusR_M', 'citrusH_M',
                   'kiwiN_T', 'kiwiK_T', 'kiwiN_M', 'kiwiK_M',
                   'orangeU_T', 'orangeA_T', 'orangeU_M', 'orangeA_M']

        ## 차후 데이터 프레임에 쌓을 리스트 생성
        chinese_cabbage_T_data_List = [];
        chinese_cabbage_M_data_List = []
        radish_T_data_List = [];
        radish_M_data_List = []
        apple_T_data_List = [];
        apple_M_data_List = []
        pear_T_data_List = [];
        pear_M_data_List = []
        grape_T_data_List = [];
        grape_M_data_List = []
        citrus_T_data_List = [];
        citrus_M_data_List = []
        kiwi_T_data_List = [];
        kiwi_M_data_List = []
        orange_T_data_List = [];
        orange_M_data_List = []

        try:
            ## DB 연결
            db = pymysql.Connect(host=self.DB_HOST,
                                 user=self.DB_USERNAME,  # db 계정
                                 password=self.DB_PASSWORD,  # db 비밀 번호
                                 database=self.DB_NAME)  # 접속 하고자 하는 db 명

            today = datetime.today().strftime("%Y%m%d")

            ## DB 작업
            with db:
                with db.cursor() as cur:

                    # 쿼리문
                    sql_retailcol = 'SHOW columns FROM total_retail'
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"

                    # 각 결과물을 저장할 초기 설정
                    col_Text = ''
                    col_List = []
                    Price_List = []
                    Result = pd.DataFrame()
                    Price_DF = pd.DataFrame()

                    # 쿼리문 실행(조건에 맞는 컬럼 찾기)
                    cur.execute(sql_retailcol)
                    for column in cur.fetchall():

                        # 조건에 맞는 데이터 추출
                        if column[0] == 'date':
                            col_List.append(column[0])
                            col_Text = col_Text + column[0]
                        else:
                            if column[0] in banList:
                                pass
                            else:
                                # 'mackerelL_T' 이후는 수산물 이므로 break 실행
                                if column[0] != 'mackerelL_T':
                                    col_List.append(column[0])
                                    col_Text = col_Text + "," + column[0]
                                else:
                                    break

                    ## banList 에 있는 데이터 전처리 각 각 특징에 맞게 작업 해야 하므로 각 각 예외처리 진행
                    # 배추(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(chinese_cabbage_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            chinese_cabbage = sum(data[0: 4]) / (len(data[0: 4]) - data[0: 4].count(0))
                        except:
                            chinese_cabbage = 0
                        chinese_cabbage_T_data_List.append(chinese_cabbage)
                    # 배추(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(chinese_cabbage_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            chinese_cabbage = sum(data[0: 4]) / (len(data[0: 4]) - data[0: 4].count(0))
                        except:
                            chinese_cabbage = 0
                        chinese_cabbage_M_data_List.append(chinese_cabbage)

                    # 무(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(radish_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            radish = sum(data[0: 4]) / (len(data[0: 4]) - data[0: 4].count(0))
                        except:
                            radish = 0
                        radish_T_data_List.append(radish)
                    # 무(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(radish_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            radish = sum(data[0: 4]) / (len(data[0: 4]) - data[0: 4].count(0))
                        except:
                            radish = 0
                        radish_M_data_List.append(radish)

                    # 사과(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(apple_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            apple = sum(data[0: 3]) / (len(data[0: 3]) - data[0: 3].count(0))
                        except:
                            apple = 0
                        apple_T_data_List.append(apple)
                    # 사과(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(apple_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            apple = sum(data[0: 3]) / (len(data[0: 3]) - data[0: 3].count(0))
                        except:
                            apple = 0
                        apple_M_data_List.append(apple)

                    # 배(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(pear_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            pear = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            pear = 0
                        pear_T_data_List.append(pear)
                    # 배(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(pear_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            pear = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            pear = 0
                        pear_M_data_List.append(pear)

                    # 포도(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(grape_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            grape = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            grape = 0
                        grape_T_data_List.append(grape)
                    # 포도(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(grape_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            grape = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            grape = 0
                        grape_M_data_List.append(grape)

                    # 귤(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(citrus_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            citrus = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            citrus = 0
                        citrus_T_data_List.append(citrus)
                    # 귤(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(citrus_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            citrus = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            citrus = 0
                        citrus_M_data_List.append(citrus)

                    # 키워(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(kiwi_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            kiwi = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            kiwi = 0
                        kiwi_T_data_List.append(kiwi)
                    # 키워(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(kiwi_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            kiwi = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            kiwi = 0
                        kiwi_M_data_List.append(kiwi)

                    # 오렌지(시장) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(orange_T))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            orange = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            orange = 0
                        orange_T_data_List.append(orange)
                    # 오렌지(마트) 전처리 작업
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = (sql_retaildata.format(orange_M))
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        try:
                            orange = sum(data[0: 2]) / (len(data[0: 2]) - data[0: 2].count(0))
                        except:
                            orange = 0
                        orange_M_data_List.append(orange)

                    col_List = tuple(col_List)
                    Price_List.append(col_List)

                    # 퀴리문 실행 (조건에 맞는 데이터 찾기)
                    sql_retaildata = "SELECT {} FROM total_retail ORDER BY date"
                    sql_retaildata = sql_retaildata.format(col_Text)
                    cur.execute(sql_retaildata)
                    for data in cur.fetchall():
                        Price_List.append(data)

                    # 데이터 프레임 제작
                    Price_DF = pd.DataFrame(Price_List[1:], columns=Price_List[0])

                    # 쿼리문으로 실행한 데이터와 위에서 예외 처리한 데이터 병합합
                    Price_DF = Price_DF.assign(chinese_cabbage_T=chinese_cabbage_T_data_List,  # 배추(시장)
                                               chinese_cabbage_M=chinese_cabbage_M_data_List,  # 배추(마트)
                                               radish_T=radish_T_data_List,  # 무(시장)
                                               radish_M=radish_M_data_List,  # 무(마트)
                                               apple_T=apple_T_data_List,  # 사과(시장)
                                               apple_M=apple_M_data_List,  # 사과(마트)
                                               pear_T=pear_T_data_List,  # 배(시장)
                                               pear_M=pear_M_data_List,  # 배(마트)
                                               grape_T=grape_T_data_List,  # 포도(시장)
                                               grape_M=grape_M_data_List,  # 포도(마트)
                                               citrus_T=citrus_T_data_List,  # 귤(시장)
                                               citrus_M=citrus_M_data_List,  # 귤(마트)
                                               kiwi_T=kiwi_T_data_List,  # 키위(시장)
                                               kiwi_M=kiwi_M_data_List,  # 키위(마트)
                                               orange_T=orange_T_data_List,  # 오렌지(시장)
                                               orange_M=orange_M_data_List)  # 오렌지(마트)
                    # 날짜를 형식에 맞게 변환
                    Price_DF['date'] = Price_DF['date'].astype('str')
                    Price_DF['date'] = Price_DF['date'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))

                    # 데이터 프레임 컬럼명 리스트 제작
                    Price_col_List = [col for col in Price_DF.columns]

                    # 각 농산물 별로 ds, y 데이터 프레임 제작
                    for cnt, column in enumerate(Price_col_List[1:]):
                        Result = {}
                        # print('----------------------' + column + '----------------------')
                        rmses = []  # Store the RMSEs for each params here
                        Each_DF = Price_DF[['date', column]]
                        Each_DF = Each_DF.rename(columns={'date': 'ds', column: 'y'})[['ds', 'y']]

                        # 이상치 값 제거
                        q1 = Each_DF['y'].quantile(0.25)
                        q3 = Each_DF['y'].quantile(0.75)
                        iqr = q3 - q1
                        condition = Each_DF['y'] > q3 + 1.5 * iqr
                        a = Each_DF[condition].index
                        Each_DF.drop(a, inplace=True)

                        ###### 파라미터 다시 설정 해줘야할 때 사용할 것 ######
                        # Use cross validation to evaluate all parameters
                        for params in all_params:
                            # print(params)
                            m = Prophet(**params,
                                        seasonality_mode='multiplicative',
                                        yearly_seasonality=True,
                                        weekly_seasonality=True).fit(Each_DF)  # Fit model with given params
                            df_cv = cross_validation(m, initial='730 days', period='180 days', horizon='365 days')
                            df_p = performance_metrics(df_cv)
                            rmses.append(df_p['rmse'].values[0])

                        # Find the best parameters
                        tuning_results = pd.DataFrame(all_params)
                        tuning_results['rmse'] = rmses

                        best_params = all_params[np.argmin(rmses)]
                        Result[data] = best_params
                        Result_params_Dict.append(Result)
                        # print('----------------------' + column + '----------------------')
                        ###### 파라미터 다시 설정 해줘야할 때 사용할 것 ######
            message = Result_params_Dict
            cur.close()
        except Exception as e:
            message = traceback.format_exc()
        return message
