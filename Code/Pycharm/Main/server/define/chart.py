import pandas as pd
import pymysql

from config import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME, csv_FolderPath, Category_Kor, Category_List

# DB 초기 설정
mydb = pymysql.Connect(host=DB_HOST, user=DB_USERNAME,
                       password=DB_PASSWORD, database=DB_NAME)
cursor = mydb.cursor()


def chart_data(category, radio_key):
    button = Category_List[Category_Kor.index(category)][radio_key]
    # 리스트2 [리스트1인덱스 (리스트1의 값 = category)][리스트2의 해당 딕셔너리 키 값 = radio_key]
    sql1 = 'SELECT date, ' + button + ' FROM Wholesale_price ORDER BY date DESC LIMIT 14;'  # 열 선택&열 내림차순 행 제한
    cursor.execute(sql1)
    W_price = list(reversed(cursor.fetchall()))  # 역순 리스트로 변환
    sql2 = 'SELECT ' + button + ' FROM Wholesale_quantity ORDER BY date DESC LIMIT 14;'
    cursor.execute(sql2)
    W_quantity = list(reversed(cursor.fetchall()))
    # print('W_price: ' + W_price)
    # print('W_quantity: ' + W_quantity)
    date = []  # 최근 날짜
    price = []  # 가격
    deal = []  # 거래량
    for i, j in zip(W_price, W_quantity):
        # print(i[0], i[1], j[0])
        date.append(str(i[0])[4:6] + '.' + str(i[0])[6:8])  # 날짜 형식
        price.append(round(i[1], -1))  # 1의 자리에서 반올림
        deal.append(j[0] / 1000)  # 1000kg 순자 단위 조정

    # Prophrt : DB_source 파일의 csv 가져오기
    test_df = pd.read_csv(csv_FolderPath + '20220804_wholesale_' + button + '.csv')
    date_f = []  # 미래 날짜 f=future
    ds_val = test_df['ds'].values.tolist()
    for i in ds_val:
        date_f.append(str(i)[5:7] + '.' + str(i)[8:10])
    yhat = round(test_df['yhat'], -1).values.tolist()  # 중간값 1의 자리에서 반올림
    yhat_l = round(test_df['yhat_lower'], -1).values.tolist()  # 최솟값
    yhat_u = round(test_df['yhat_upper'], -1).values.tolist()  # 최댓값
    # print(date_f)
    # print('평균: '+yhat)
    # print('최소: '+yhat_l)
    # print('최대: '+yhat_u)

    # 18년 1분기 ~ 22년 3분기까지 전부 - 식량작물 감자 평균가격
    price_quarter = []
    wholesale_price_list = {
        'sql_18_1': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20180102 and 20180331;",
        'sql_18_2': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20180402 and 20180630;",
        'sql_18_3': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20180702 and 20180929;",
        'sql_18_4': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20181001 and 20181231;",
        'sql_19_1': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20190102 and 20190330;",
        'sql_19_2': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20190401 and 20190629;",
        'sql_19_3': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20190701 and 20190930;",
        'sql_19_4': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20191001 and 20191231;",
        'sql_20_1': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20200102 and 20200331;",
        'sql_20_2': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20200302 and 20200630;",
        'sql_20_3': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20200701 and 20200929;",
        'sql_20_4': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20201005 and 20201231;",
        'sql_21_1': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20210102 and 20210331;",
        'sql_21_2': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20210401 and 20210630;",
        'sql_21_3': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20210701 and 20210930;",
        'sql_21_4': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20211001 and 20211231;",
        'sql_22_1': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20220103 and 20220331;",
        'sql_22_2': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20220401 and 20220630;",
        'sql_22_3': "SELECT sum(" + button + "), count(" + button + ") FROM wholesale_price WHERE date between 20220701 and 20220730;"
    }

    for i in wholesale_price_list.values():
        cursor.execute(i)
        result = cursor.fetchall()
        # print('---', result[0])
        days = result[0][1]
        total_price = result[0][0]
        price_quarter.append(round((total_price / days), -1))
    # print('price_quarter: ' + price_quarter)

    # 18년 1분기 ~ 22년 3분기까지 전부 - 식량작물 감자 총 판매량
    deal_quarter = []
    wholesale_deal_list = {
        'sql_18_1': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20180102 and 20180331;",
        'sql_18_2': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20180402 and 20180630;",
        'sql_18_3': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20180702 and 20180929;",
        'sql_18_4': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20181001 and 20181231;",
        'sql_19_1': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20190102 and 20190330;",
        'sql_19_2': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20190401 and 20190629;",
        'sql_19_3': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20190701 and 20190930;",
        'sql_19_4': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20191001 and 20191231;",
        'sql_20_1': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20200102 and 20200331;",
        'sql_20_2': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20200302 and 20200630;",
        'sql_20_3': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20200701 and 20200929;",
        'sql_20_4': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20201005 and 20201231;",
        'sql_21_1': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20210102 and 20210331;",
        'sql_21_2': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20210401 and 20210630;",
        'sql_21_3': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20210701 and 20210930;",
        'sql_21_4': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20211001 and 20211231;",
        'sql_22_1': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20220103 and 20220331;",
        'sql_22_2': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20220401 and 20220630;",
        'sql_22_3': "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20220701 and 20220730;"
    }

    for i in wholesale_deal_list.values():
        cursor.execute(i)
        result = cursor.fetchall()
        deal_quarter.append(round(result[0][0] / 1000))
    # print('deal_quarter: ' + deal_quarter)
    print('chart data set ok')
    # List: 날짜, 가격, 거래량, 미래 날짜, 예측 중간, 최소, 최대, 가격 분기, 거래량 분기
    return date, price, deal, date_f, yhat, yhat_l, yhat_u, price_quarter, deal_quarter
