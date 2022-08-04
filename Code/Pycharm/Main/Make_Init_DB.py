import json

import pymysql
import requests
from bs4 import BeautifulSoup

from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, RecipeData_FilePath

#################### DB 초기 설정 ####################
db = pymysql.Connect(host=DB_HOST,
                     user=DB_USERNAME,  # db 계정
                     password=DB_PASSWORD,  # db 비밀 번호
                     database=DB_NAME)  # 접속 하고자 하는 db 명
cursor = db.cursor()

Area_Dict = {'광주': 'gwangju', '대구': 'daegu', '대전': 'daejeon', '부산': 'busan',
             '서울': 'seoul', '울산': 'ulsan', '인천': 'incheon', '전체': 'total'}

URL = 'https://www.10000recipe.com/recipe/'
#################### DB 초기 설정 ####################


#################### 만개의 레시피 자료 처리 ####################
with open(RecipeData_FilePath, 'r', encoding='UTF8') as f:
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

for num in Data_Json.keys():
    Row_Dict = Data_Json[num]
    Ingreient_Text = ''
    Imgurl_Text = ''
    Total_URL = requests.get(URL + str(Row_Dict['레시피일련번호']))
    if Total_URL.status_code == 200:
        html = Total_URL.text
        soup = BeautifulSoup(html, 'html.parser')
        Imgurl_Text = soup.find('div', class_='centeredcrop').find('img')['src']

        count = 0
        Ingreient_Text = ''
        tag_li = soup.find('div', class_='ready_ingre3').find_all("li")
        for rcnt, datas in enumerate(tag_li):
            tmp = datas.get_text().replace('\n', '').replace('구매', '').replace(
                '                                                        ', '  ')
            rtext = tmp.split('  ')
            text = ''
            for cnt, txt in enumerate(rtext):
                if cnt == 0:
                    text += txt
                else:
                    text = text + "_" + txt
            if rcnt == 0:
                Ingreient_Text += text
            else:
                Ingreient_Text = Ingreient_Text + "," + text

    # DB 쿼리문
    query = "INSERT INTO food_recipe ({}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(col_Text)
    Result_Text = (
        Row_Dict['레시피일련번호'], Row_Dict['요리명'], Row_Dict['등록자명'], Row_Dict['조회수'], Row_Dict['추천수'], Row_Dict['요리상황별 명'],
        Row_Dict['요리소개'], Ingreient_Text, Row_Dict['요리인분 명'], Row_Dict['요리난이도 명'], Row_Dict['요리시간 명'], Imgurl_Text)
    cursor.execute(query, Result_Text)
    db.commit()
#################### 만개의 레시피 자료 처리 ####################


# #################### 거래량 데이터 ####################
# for file in [WholesaleVolume_FilePath, WholesalePrice_FilePath]:
#     if file == WholesaleVolume_FilePath:
#         table = 'wholesale_quantity'
#         name = '거래량(kg)'
#     else:
#         table = 'wholesale_price'
#         name = '가격(원/kg)'
#
#     with open(file, 'r', encoding='UTF8') as f:
#         Data_Json = json.load(f)
#     cursor.execute("SHOW columns FROM {}".format(table))
#
#     col_Text = ''
#     for cnt, column in enumerate(cursor.fetchall()):
#         if cnt == 0:
#             col_Text += column[0]
#         else:
#             col_Text = col_Text + "," + column[0]
#
#     for num in Data_Json.keys():
#         Row_Dict = Data_Json[num]
#
#         # DB 쿼리문
#         query = """INSERT INTO {} ({}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
#                                                 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                 """.format(table, col_Text)
#         Result_Text = (Row_Dict['date'], Row_Dict['콩_' + name], Row_Dict['고구마_' + name], Row_Dict['감자_' + name],
#                        Row_Dict['배추_' + name], Row_Dict['양배추_' + name], Row_Dict['시금치_' + name], Row_Dict['상추_' + name],
#                        Row_Dict['얼갈이배추_' + name], Row_Dict['수박_' + name], Row_Dict['참외_' + name],
#                        Row_Dict['오이_' + name],
#                        Row_Dict['호박_' + name], Row_Dict['토마토_' + name], Row_Dict['딸기_' + name], Row_Dict['무_' + name],
#                        Row_Dict['당근_' + name], Row_Dict['열무_' + name], Row_Dict['건고추_' + name], Row_Dict['풋고추_' + name],
#                        Row_Dict['양파_' + name], Row_Dict['대파_' + name], Row_Dict['쪽파_' + name], Row_Dict['생강_' + name],
#                        Row_Dict['미나리_' + name], Row_Dict['깻잎_' + name], Row_Dict['피망(단고추)_' + name],
#                        Row_Dict['파프리카_' + name],
#                        Row_Dict['방울토마토_' + name], Row_Dict['참깨_' + name], Row_Dict['땅콩_' + name],
#                        Row_Dict['느타리버섯_' + name],
#                        Row_Dict['새송이_' + name], Row_Dict['팽이버섯_' + name], Row_Dict['호두_' + name],
#                        Row_Dict['사과_' + name],
#                        Row_Dict['배_' + name], Row_Dict['복숭아_' + name], Row_Dict['포도_' + name], Row_Dict['감귤_' + name],
#                        Row_Dict['단감_' + name], Row_Dict['바나나_' + name], Row_Dict['참다래(키위)_' + name],
#                        Row_Dict['파인애플_' + name],
#                        Row_Dict['오렌지_' + name], Row_Dict['레몬_' + name], Row_Dict['체리_' + name], Row_Dict['망고_' + name])
#         cursor.execute(query, Result_Text)
#         db.commit()
# #################### 거래량 데이터 ####################
#
#
# #################### 전체 소매 데이터 ####################
# for file in glob(Retail_FolderPath + '*.json'):
#     Total_List = []
#     day = int(file.split('.')[0].split('\\')[-1].split('_')[0])
#     area = file.split('.')[0].split('\\')[-1].split('_')[1]
#     Total_List.append(day)
#
#     with open(file, 'r', encoding='utf-8') as f:
#         Data_Json = json.load(f)
#     for data_List in Data_Json['Result']:
#         for price in data_List.values():
#             Total_List.append(price[0])
#             Total_List.append(price[1])
#     cursor.execute("SHOW columns FROM {}_retail".format(Area_Dict[area]))
#
#     col_Text = ''
#     for cnt, column in enumerate(cursor.fetchall()):
#         if cnt == 0:
#             col_Text += column[0]
#         else:
#             col_Text = col_Text + "," + column[0]
#
#     # DB 쿼리문
#     query = "INSERT INTO {}_retail ({}) VALUES {}".format(Area_Dict[area], col_Text, tuple(Total_List))
#     cursor.execute(query)
#     db.commit()
# #################### 전체 소매 데이터 ####################
