import json
from glob import glob

import pandas as pd
import pymysql
from tqdm import tqdm

from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, \
    Region_Dict, Retail_Folder_Path, RecipeData_File_Path, \
    WholesaleVolume_File_Path, WholesalePrice_File_Path, Excel_Path

#################### DB 초기 설정 ####################
db = pymysql.Connect(host=DB_HOST,
                     user=DB_USERNAME,  # db 계정
                     password=DB_PASSWORD,  # db 비밀 번호
                     database=DB_NAME)  # 접속 하고자 하는 db 명
cursor = db.cursor()
#################### DB 초기 설정 ####################


#################### 제철 음식 자료 처리 ####################
data = pd.read_excel(Excel_Path)
data['Month'] = data['Month'].apply(lambda x: str(x))
data['Month'] = data['Month'].apply(lambda x: '0' + x if len(x) == 1 else x)
sql = 'insert into seasonal_food (Month, Name, Period) values(%s, %s, %s)'
for idx in tqdm(range(len(data)), desc='제철 음식 자료', mininterval=0.05):
    cursor.execute(sql, tuple(data.values[idx][:3]))
db.commit()
#################### 제철 음식 자료 처리 ####################


#################### 만개의 레시피 자료 처리 ####################
with open(RecipeData_File_Path, 'r', encoding='UTF8') as f:
    Data_Json = json.load(f)
cursor.execute("SHOW columns FROM food_recipe")

col_Text = ''
for cnt, column in enumerate(cursor.fetchall()):
    if cnt == 0:
        pass
    elif cnt == 1:
        col_Text += column[0]
    else:
        col_Text = col_Text + "," + column[0]

for num in tqdm(Data_Json.keys(), desc='만개의 레시피 DB INSERT', mininterval=0.05):
    Row_Dict = Data_Json[num]

    # DB 쿼리문
    query = "INSERT INTO food_recipe ({}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(col_Text)
    Result_Text = (
        Row_Dict['일련번호'], Row_Dict['요리명'], Row_Dict['등록자'], Row_Dict['조회수'], Row_Dict['추천수'], Row_Dict['요리상황'],
        Row_Dict['요리소개'], Row_Dict['전체요리재료'], Row_Dict['요리인분'], Row_Dict['난이도'], Row_Dict['시간'], Row_Dict['URL'],
        Row_Dict['요리재료'])
    cursor.execute(query, Result_Text)
    db.commit()
#################### 만개의 레시피 자료 처리 ####################


#################### 거래량 데이터 ####################
for file in [WholesaleVolume_File_Path, WholesalePrice_File_Path]:
    if file == WholesaleVolume_File_Path:
        table = 'wholesale_quantity'
        name = '거래량(kg)'
    else:
        table = 'wholesale_price'
        name = '가격(원/kg)'

    with open(file, 'r', encoding='UTF8') as f:
        Data_Json = json.load(f)
    cursor.execute("SHOW columns FROM {}".format(table))

    col_Text = ''
    for cnt, column in enumerate(cursor.fetchall()):
        if cnt == 0:
            col_Text += column[0]
        else:
            col_Text = col_Text + "," + column[0]

    for num in tqdm(Data_Json.keys(), desc='도매 DB INSERT', mininterval=0.05):
        Row_Dict = Data_Json[num]

        # DB 쿼리문
        query = """INSERT INTO {} ({}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """.format(table, col_Text)
        Result_Text = (Row_Dict['date'], Row_Dict['콩_' + name], Row_Dict['고구마_' + name], Row_Dict['감자_' + name],
                       Row_Dict['배추_' + name], Row_Dict['양배추_' + name], Row_Dict['시금치_' + name], Row_Dict['상추_' + name],
                       Row_Dict['얼갈이배추_' + name], Row_Dict['수박_' + name], Row_Dict['참외_' + name],
                       Row_Dict['오이_' + name],
                       Row_Dict['호박_' + name], Row_Dict['토마토_' + name], Row_Dict['딸기_' + name], Row_Dict['무_' + name],
                       Row_Dict['당근_' + name], Row_Dict['열무_' + name], Row_Dict['건고추_' + name], Row_Dict['풋고추_' + name],
                       Row_Dict['양파_' + name], Row_Dict['대파_' + name], Row_Dict['쪽파_' + name], Row_Dict['생강_' + name],
                       Row_Dict['미나리_' + name], Row_Dict['깻잎_' + name], Row_Dict['피망(단고추)_' + name],
                       Row_Dict['파프리카_' + name],
                       Row_Dict['방울토마토_' + name], Row_Dict['참깨_' + name], Row_Dict['땅콩_' + name],
                       Row_Dict['느타리버섯_' + name],
                       Row_Dict['새송이_' + name], Row_Dict['팽이버섯_' + name], Row_Dict['호두_' + name],
                       Row_Dict['사과_' + name],
                       Row_Dict['배_' + name], Row_Dict['복숭아_' + name], Row_Dict['포도_' + name], Row_Dict['감귤_' + name],
                       Row_Dict['단감_' + name], Row_Dict['바나나_' + name], Row_Dict['참다래(키위)_' + name],
                       Row_Dict['파인애플_' + name],
                       Row_Dict['오렌지_' + name], Row_Dict['레몬_' + name], Row_Dict['체리_' + name], Row_Dict['망고_' + name])
        cursor.execute(query, Result_Text)
        db.commit()
#################### 거래량 데이터 ####################


#################### 전체 소매 데이터 ####################
for file in tqdm(glob(Retail_Folder_Path + '*.json'), desc='소매 DB INSERT', mininterval=0.05):
    Total_List = []
    day = int(file.split('.')[0].split('\\')[-1].split('_')[0])
    area = file.split('.')[0].split('\\')[-1].split('_')[1]
    Total_List.append(day)

    with open(file, 'r', encoding='utf-8') as f:
        Data_Json = json.load(f)
    for data_List in Data_Json['Result']:
        for price in data_List.values():
            Total_List.append(price[0])
            Total_List.append(price[1])
    cursor.execute("SHOW columns FROM {}_retail".format(Region_Dict[area]))

    col_Text = ''
    for cnt, column in enumerate(cursor.fetchall()):
        if cnt == 0:
            col_Text += column[0]
        else:
            col_Text = col_Text + "," + column[0]

    # DB 쿼리문
    query = "INSERT INTO {}_retail ({}) VALUES {}".format(Region_Dict[area], col_Text, tuple(Total_List))
    cursor.execute(query)
    db.commit()
#################### 전체 소매 데이터 ####################

cursor.close()
