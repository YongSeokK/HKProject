import math
import traceback
from datetime import datetime
from glob import glob

import pandas as pd
import pymysql
from dateutil.relativedelta import relativedelta


class Chartdata_W:

    ### init 설정
    def __init__(self, DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME,
                 csv_Folder_Path, Category_Kor, Category_List_W, category, key_produce):
        self.DB_USERNAME = DB_USERNAME
        self.DB_HOST = DB_HOST
        self.DB_PASSWORD = DB_PASSWORD
        self.DB_NAME = DB_NAME
        self.csv_Folder_Path = csv_Folder_Path
        self.Category_Kor = Category_Kor
        self.Category_List_W = Category_List_W
        self.category = category
        self.key_produce = key_produce
        self.button = self.Category_List_W[self.Category_Kor.index(self.category)][self.key_produce]
        # 농산물 = 리스트2 [리스트1인덱스 (리스트1의 값 = category)][리스트2의 해당 딕셔너리 키 값 = key_produce]

    ## chart 구성 요소 자릿 수 계산
    def a_cipher_math(self, num):
        try:
            x = '100000'
            multiplier = len(str(int(num)))
            re_num = int(x[0:multiplier])
            return re_num

        except Exception as e:
            message = traceback.format_exc()
            return message

    def a_cipher_round(self, num):
        try:
            multiplier = len(str(int(num))) - 1
            return multiplier

        except Exception as e:
            message = traceback.format_exc()
            return message

    # chart
    def chart1(self):
        try:
            db = pymysql.Connect(host=self.DB_HOST,
                                 user=self.DB_USERNAME,  # db 계정
                                 password=self.DB_PASSWORD,  # db 비밀 번호
                                 database=self.DB_NAME)  # 접속 하고자 하는 db 명
            ## DB 작업
            with db:
                with db.cursor() as cur:
                    sql1 = 'SELECT date, ' + self.button + ' FROM Wholesale_price ORDER BY date DESC LIMIT 14;'  # 열 선택 & 열 내림차순 행 제한
                    cur.execute(sql1)
                    W_price = list(reversed(cur.fetchall()))  # 역순 리스트로 변환
                    sql2 = 'SELECT ' + self.button + ' FROM Wholesale_quantity ORDER BY date DESC LIMIT 14;'
                    cur.execute(sql2)
                    W_quantity = list(reversed(cur.fetchall()))

                    date = []  # 최근 날짜, 가격, 거래량
                    price = []
                    deal = []
                    for i, j in zip(W_price, W_quantity):
                        date.append(str(i[0])[4:6] + '.' + str(i[0])[6:8])  # 날짜 형식
                        price.append(int(round(i[1], -1)))  # 1의 자리에서 반올림
                        deal.append(round(j[0] / 1000, 2))  # 1000kg 순자 단위 조정

                    max_price = math.ceil(max(price) / 100) * 100
                    stepSize_price = round(max_price / 5, -2)  # 10의 자리에서 반올림
                    if stepSize_price >= 500:
                        stepSize_price = (stepSize_price // 500) * 500
                        if stepSize_price * 7 < max_price:
                            stepSize_price = round(max_price / 5, -2)

                    # 정리 필요
                    max_deal = math.ceil(max(deal))
                    if max(deal) < 10:
                        pass
                    elif max(deal) < 1:
                        max_deal = round(max_deal, 1)
                    else:
                        x = self.a_cipher_math(max(deal))
                        max_deal = math.ceil(max(deal) / x) * x
                    if max(deal) < 1:
                        stepSize_deal = 0.2
                    else:
                        stepSize_deal = math.ceil(max_deal / 5)

            # chart1: 날짜, 가격, 거래량, 최소 가격, 최대 가격, 가격 크기, 최소 거래량, 최대 거래량, 거래량 크기
            chart1 = {'date': date, 'price': price, 'deal': deal,
                      'max_price': max_price, 'stepSize_price': stepSize_price,
                      'max_deal': max_deal, 'stepSize_deal': stepSize_deal}
            return chart1

        except Exception as e:
            message = traceback.format_exc()
            return message

    def chart2(self):
        try:
            # Prophrt : DB_source 파일의 csv 가져오기
            filename = glob(self.csv_Folder_Path + 'wholesale\\' + '*_wholesale_' + self.button + '.csv')[0]
            test_df = pd.read_csv(filename)
            date_f = []  # 예측 날짜 f=future
            ds_val = test_df['ds'].values.tolist()
            for i in ds_val:
                date_f.append(str(i)[5:7] + '.' + str(i)[8:10])
            yhat = round(test_df['yhat'], -1).values.tolist()  # 중간값 1의 자리에서 반올림
            yhat_l = round(test_df['yhat_lower'], -1).values.tolist()  # 최솟값
            yhat_u = round(test_df['yhat_upper'], -1).values.tolist()  # 최댓값

            max_yhat = round(max(yhat_u), -2)
            stepSize_yhat = round(max_yhat / 5, -2)
            if stepSize_yhat >= 500:
                stepSize_yhat = (stepSize_yhat // 500) * 500
                if stepSize_yhat * 7 < max_yhat:
                    stepSize_yhat = round(max_yhat / 5, -2)

            # chart2: 예측 날짜, 예측 평균 가격, 최소 평균 예측값, 최대 평균 예측값, 예측 최솟값, 예측 최댓값, 예측 크기
            chart2 = {'date_f': date_f, 'yhat': yhat, 'yhat_l': yhat_l, 'yhat_u': yhat_u,
                      'max_yhat': max_yhat, 'stepSize_yhat': stepSize_yhat}
            return chart2

        except Exception as e:
            message = traceback.format_exc()
            return message

    def chart3(self):
        try:
            db = pymysql.Connect(host=self.DB_HOST,
                                 user=self.DB_USERNAME,  # db 계정
                                 password=self.DB_PASSWORD,  # db 비밀 번호
                                 database=self.DB_NAME)  # 접속 하고자 하는 db 명
            # DB 작업
            with db:
                with db.cursor() as cur:
                    # 분기 계산
                    quarter = {'1Q': ['01', '03'], '2Q': ['04', '06'],
                               '3Q': ['07', '09'], '4Q': ['10', '12']}
                    now = datetime.now()

                    sql_end = "SELECT date FROM wholesale_quantity WHERE date " + "ORDER BY date DESC LIMIT 1;"
                    cur.execute(sql_end)
                    end_db = cur.fetchall()
                    end_date = end_db[0][0]

                    quarter_list = []
                    for minus in range(4, -1, -1):
                        calculation = now - relativedelta(years=minus)
                        year = calculation.strftime("%Y")
                        q_y = []
                        for i, j in quarter.items():
                            q = []
                            sql_first = "SELECT date FROM wholesale_quantity WHERE date LIKE '" + year + j[
                                0] + "%' LIMIT 1;"
                            cur.execute(sql_first)
                            first_db = cur.fetchall()
                            q.append(first_db[0][0])
                            if int(year) == now.year and (int(str(end_date)[:6]) - int(year + j[1])) < 0:
                                sql_last = "SELECT date FROM wholesale_quantity WHERE date= '" + str(end_date) + "';"
                                cur.execute(sql_last)
                                last_db = cur.fetchall()
                                q.append(last_db[0][0])
                                q_y.append(q)
                                break

                            sql_last = "SELECT date FROM wholesale_quantity WHERE date LIKE '" + \
                                       year + j[1] + "%' ORDER BY date DESC LIMIT 1;"
                            cur.execute(sql_last)
                            last_db = cur.fetchall()
                            q.append(last_db[0][0])
                            q_y.append(q)
                        quarter_list.append(q_y)

                    # sql query문 생성
                    wholesale_price_list = []
                    wholesale_deal_list = []
                    for year in quarter_list:
                        for q in year:
                            # print(aa)
                            sql_price = "SELECT sum(" + self.button + "), count(" + self.button + \
                                        ") FROM wholesale_price WHERE date between " + \
                                        str(q[0]) + " and " + str(q[1]) + ";"
                            sql_deal = "SELECT sum(" + self.button + ") FROM wholesale_quantity WHERE date between " + \
                                       str(q[0]) + " and " + str(q[1]) + ";"
                            wholesale_price_list.append(sql_price)
                            wholesale_deal_list.append(sql_deal)

                    # 18년 1분기 ~ 22년 3분기까지 전부 - 식량작물 감자 평균가격
                    price_quarter = []
                    for i in wholesale_price_list:
                        cur.execute(i)
                        result = cur.fetchall()
                        days = result[0][1]
                        total_price = result[0][0]
                        price_quarter.append(round((total_price / days), -1))

                    # 18년 1분기 ~ 22년 3분기까지 전부 - 식량작물 감자 총 판매량
                    deal_quarter = []
                    for i in wholesale_deal_list:
                        cur.execute(i)
                        result = cur.fetchall()
                        deal_quarter.append(round(result[0][0] / 1000))

            # chart3
            max_price_quarter = math.ceil(max(price_quarter) / 1000) * 1000
            stepSize_price_quarter = round(max_price_quarter / 5, -2)
            if stepSize_price_quarter >= 500:
                stepSize_price_quarter = (stepSize_price_quarter // 500) * 500
                if stepSize_price_quarter * 8 < max_price_quarter:
                    stepSize_price_quarter = stepSize_price_quarter * 2

            max_deal_quarter = math.ceil(max(deal_quarter) / 1000) * 1000
            result_deal_quarter = self.a_cipher_round(max_deal_quarter)
            if result_deal_quarter < 2:
                stepSize_deal_quarter = round(max_deal_quarter / 5, 0)
            elif result_deal_quarter < 3:
                stepSize_deal_quarter = round(max_deal_quarter / 5, -1)
            elif result_deal_quarter < 4:
                stepSize_deal_quarter = round(max_deal_quarter / 5, -2)
            elif result_deal_quarter < 5:
                stepSize_deal_quarter = round(max_deal_quarter / 5, -3)
            else:
                stepSize_deal_quarter = round(max_deal_quarter / 5, -4)

            # chart3: 분기별 가격, 분기별 거래량, 최소 가격, 최대 가격, 가격 크기, 최소 거래량, 최대 거래량, 거래량 크기
            chart3 = {'price_quarter': price_quarter, 'deal_quarter': deal_quarter,
                      'max_price_quarter': max_price_quarter,
                      'stepSize_price_quarter': stepSize_price_quarter,
                      'max_deal_quarter': max_deal_quarter,
                      'stepSize_deal_quarter': stepSize_deal_quarter}
            return chart3

        except Exception as e:
            message = traceback.format_exc()
            return message

    def Wholesale(self):
        try:
            chart1 = self.chart1()
            chart2 = self.chart2()
            chart3 = self.chart3()
            chart = {'1': chart1, '2': chart2, '3': chart3}
            print('chart data set ok')
            return chart

        except Exception as e:
            message = traceback.format_exc()
            return message


class Chartdata_R:

    ### init 설정
    def __init__(self, result_dict, csv_Folder_Path, Category_Kor, Category_Eng,
                 Region_Dict, Category_List_R, Produce_Num,
                 region, category, key_produce):
        # 소매가격 딕셔너리, csv 폴더경로, 분류 한국어, 분류 영어,
        # 지역 딕셔너리, 농산물 딕셔너리, 소매가격 딕셔너리 농산물 순서,
        # 지역, 분류, 선택 농산물
        self.result_dict = result_dict
        self.csv_Folder_Path = csv_Folder_Path
        self.Category_Kor = Category_Kor
        self.Category_Eng = Category_Eng
        self.Region_Dict = Region_Dict
        self.Category_List_R = Category_List_R
        self.Produce_Num = Produce_Num
        self.region = region
        self.category = category
        self.key_produce = key_produce

        self.category_index = self.Category_Kor.index(self.category)  # 한글로 입력된 분류 카테고리 순서 인덱스로 추출
        self.category_D = self.Category_List_R[self.category_index]  # 선택 농산물 분류 딕셔너리 불러오기
        self.button = self.category_D[self.key_produce]  # 한글로 입력된 농산물 영어로 번역
        self.produce_index = Produce_Num[self.button]  # 소매 딕셔너리에서 농산물 순서 넘버 딕셔너리에서 불러오기
        self.region_Eng = Region_Dict[region]  # 한글로 입력된 지역, 지역 딕셔너리에서 영어로 번역
        self.category_E = self.Category_Eng[self.category_index]  # 선택 분류 영어로 불러오기

    def ready(self):
        try:
            # chart1,2
            date = []  # 날짜
            result_t = []  # 선택 지역 시장 가격
            result_t_total = []  # 전체 지역 시장 가격
            result_m = []  # 선택 지역 마트 가격
            result_m_total = []  # 전체 지역 마트 가격

            # 소매 딕셔너리에서 지역, 분류, 시장&마트 순차적으로 키 입력하여 날짜 키 값 불러오기
            # list(result_dict[region_Eng][category_E]['T'].keys())

            # 시장 data
            for i in list(self.result_dict[self.region_Eng][self.category_E]['T'].keys())[-10:]:
                date.append(str(i)[4:6] + '.' + str(i)[6:8])
                result_t.append(
                    round(int(self.result_dict[self.region_Eng][self.category_E]['T'][i][self.produce_index]), -1))
            for i in list(self.result_dict['total'][self.category_E]['T'].keys())[-10:]:
                result_t_total.append(
                    round(int(self.result_dict['total'][self.category_E]['T'][i][self.produce_index]), -1))

            # 마트 data
            for i in list(self.result_dict[self.region_Eng][self.category_E]['M'].keys())[-10:]:
                result_m.append(
                    round(int(self.result_dict[self.region_Eng][self.category_E]['M'][i][self.produce_index]), -1))
            for i in list(self.result_dict['total'][self.category_E]['M'].keys())[-10:]:
                result_m_total.append(
                    round(int(self.result_dict['total'][self.category_E]['M'][i][self.produce_index]), -1))
            # print(date)
            # print('T_', '시장 지역: ', result_t, ', 시장 전체: ', result_t_total)
            # print('M_', '마트 지역:', result_m, ', 마트 전체: ', result_m_total)
            return date, result_t, result_t_total, result_m, result_m_total

        except Exception as e:
            message = traceback.format_exc()
            return message

    def chart(self):
        try:
            date, result_t, result_t_total, result_m, result_m_total = self.ready()

            # Prophrt : DB_source 파일의 csv 가져오기
            filePath = glob(self.csv_Folder_Path + 'retail\\' + '*_retail_' + self.button + '*.csv')

            # 파일 이름 확인 용도 5줄 주석 처리 가능
            # filename = []
            # for i in filePath:
            #     re = i.split('retail\\')[1]
            #     filename.append(re)
            # print('csv file: ', filename)

            test_df_T = pd.read_csv(filePath[1])  # 시장 csv
            test_df_M = pd.read_csv(filePath[0])  # 마트 csv
            ds_val = test_df_T['ds'].values.tolist()
            for i in ds_val[0:5]:
                date.append(str(i)[5:7] + '.' + str(i)[8:10])
            yhat_T = list(
                map(int, [i if i > 10 else 0 for i in round(test_df_T['yhat']).values.tolist()[0:5]]))  # 중간값 반올림
            yhat_l_T = list(
                map(int, [i if i > 10 else 0 for i in round(test_df_T['yhat_lower']).values.tolist()[0:5]]))  # 최솟값
            yhat_u_T = list(
                map(int, [i if i > 10 else 0 for i in round(test_df_T['yhat_upper']).values.tolist()[0:5]]))  # 최댓값

            cnt_0 = 0
            for data in yhat_T:
                if data == 0:
                    cnt_0 += 1
            if cnt_0 >= 3:
                yhat_u_T = [0] * len(yhat_u_T)

            yhat_M = list(
                map(int, [i if i > 10 else 0 for i in round(test_df_M['yhat']).values.tolist()[0:5]]))  # 중간값 반올림
            yhat_l_M = list(
                map(int, [i if i > 10 else 0 for i in round(test_df_M['yhat_lower']).values.tolist()[0:5]]))  # 최솟값
            yhat_u_M = list(
                map(int, [i if i > 10 else 0 for i in round(test_df_M['yhat_upper']).values.tolist()[0:5]]))  # 최댓값
            cnt_0 = 0
            for data in yhat_M:
                if data == 0:
                    cnt_0 += 1
            if cnt_0 >= 3:
                yhat_u_M = [0] * len(yhat_u_M)

            result_t_total.extend(yhat_T)  # 전체 지역 과거 값에 예측값 합치기
            result_m_total.extend(yhat_M)  # 전체 지역 과거 값에 예측값 합치기
            # print('차트 날짜: ', date)
            # print('----------')
            # print('시장 평균: ', yhat_T)
            # print('시장 전체 값: ', result_t_total)
            # print('시장 예측 최소: ', yhat_l_T)
            # print('시장 예측 최대: ', yhat_u_T)
            # print('----------')
            # print('마트 평균: ', yhat_M)
            # print('마트 전체 값: ', result_m_total)
            # print('마트 예측 최소: ', yhat_l_M)
            # print('마트 예측 최대: ', yhat_u_M)

            # chart1: <시장> 날짜, 선택 지역 과거값, 전체 지역 과거+예측 평균값, 예측 최솟값, 예측 최댓값
            chart1 = {'date': date,
                      'result_t': result_t, 'result_t_total': result_t_total, 'yhat_l_T': yhat_l_T,
                      'yhat_u_T': yhat_u_T}
            # chart2: <마트> 선택 지역 과거값, 전체 지역 과거+예측 평균값, 예측 최솟값, 예측 최댓값
            chart2 = {'result_m': result_m, 'result_m_total': result_m_total, 'yhat_l_M': yhat_l_M,
                      'yhat_u_M': yhat_u_M}
            return chart1, chart2

        except Exception as e:
            message = traceback.format_exc()
            return message

    def chart3(self):
        try:
            # chart3
            month_List = []
            now = datetime.now()  # 오늘 날짜
            shops = ['T', 'M']
            price_T, price_M = [], []
            result = [price_T, price_M]
            for minus in range(11, -1, -1):  # 11개월 전부터 이번 달까지
                calculation = now - relativedelta(months=minus)
                y_m = calculation.strftime("%y%m")
                month_List.append((y_m[0:2] + '.' + y_m[2:]))
                for i, shop in enumerate(shops):
                    date_List = list(self.result_dict['total'][self.category_E][shop].keys())
                    month_key_List = [date for date in date_List if str(y_m) in str(date)]
                    cnt = 0
                    price_sum = 0
                    for j in month_key_List:
                        produce_price = self.result_dict['total'][self.category_E][shop][j][self.produce_index]
                        if produce_price == 0:
                            pass
                        else:
                            price_sum = price_sum + produce_price
                            cnt += 1
                    if produce_price == 0:
                        result[i].append(0)
                    else:
                        # print(price_sum, cnt)
                        result[i].append(int(price_sum / cnt))
            # print('월: ', month_List)
            # print('월 평균값(t,m): ', result)

            # # chart1
            # min_chart1 = [min(result_t), min(result_t_total), min(yhat_l_T)]
            # max_chart1 = [max(result_t), max(result_t_total), max(yhat_u_T)]
            # min_price = math.floor(min(min_chart1) / 100) * 100
            # max_price = math.ceil(max(max_chart1) / 100) * 100
            # # max_price = round(max(max_chart1), -2)
            # stepSize_chart1 = round(max_price / 50, -2)
            # if stepSize_chart1 >= 500:
            #     stepSize_chart1 = (stepSize_chart1 // 500) * 500
            #     if stepSize_chart1 * 7 < max_price:
            #         stepSize_chart1 = round(max_price / 50, -2)
            # # print(stepSize_chart1)
            # min_x1 = min_price // stepSize_chart1
            # max_x1 = (max_price // stepSize_chart1) + 1
            # print('-----')
            # print(min_price,max_price,stepSize_chart1)
            # print('-----')
            #
            # # chart2
            # min_chart2 = [min(result_m), min(result_m_total), min(yhat_l_M)]
            # max_chart2 = [max(result_m), max(result_m_total), max(yhat_u_M)]
            # max_price = round(max(max_chart2), -2)
            # stepSize_chart2 = round(max_price / 5, -2)
            # if stepSize_chart2 >= 500:
            #     stepSize_chart2 = (stepSize_chart2 // 500) * 500
            #     if stepSize_chart2 * 7 < max_price:
            #         stepSize_chart2 = round(max_price / 5, -2)
            # # print(stepSize_chart2)
            #
            # # chart3
            # min_chart3 = [min(month_price_T), min(month_price_M)]
            # max_chart3 = [max(month_price_T), max(month_price_M)]
            # max_price = round(max(max_chart3), -2)
            # stepSize_chart3 = round(max_price / 5, -2)
            # if stepSize_chart3 >= 500:
            #     stepSize_chart3 = (stepSize_chart3 // 500) * 500
            #     if stepSize_chart3 * 7 < max_price:
            #         stepSize_chart3 = round(max_price / 5, -2)
            # # print(stepSize_chart3)

            # chart3
            chart3 = {'month_List': month_List, 'month_price_T': price_T, 'month_price_M': price_M}
            return chart3

        except Exception as e:
            message = traceback.format_exc()
            return message

    def Retail(self):
        try:
            chart1, chart2 = self.chart()
            chart3 = self.chart3()
            chart = {'1': chart1, '2': chart2, '3': chart3}
            print('chart data set ok')
            return chart

        except Exception as e:
            message = traceback.format_exc()
            return message
