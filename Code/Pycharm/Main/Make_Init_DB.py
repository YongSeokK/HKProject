from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, RecipeData_FilePath, WholesaleVolume_FilePath, \
    WholesalePrice_FilePath, Retail_FolderPath
from glob import glob
import json
import pymysql

#################### DB 초기 설정 ####################
print('DB 초기 설정 시작')
db = pymysql.Connect(host=DB_HOST,
                     user=DB_USERNAME,  # db 계정
                     password=DB_PASSWORD,  # db 비밀 번호
                     database=DB_NAME)  # 접속 하고자 하는 db 명
cursor = db.cursor()
#################### DB 초기 설정 ####################


#################### 만개의 레시피 자료 처리 ####################
print('만개의 레시피 자료 처리 시작')
# 불러올 json 파일
with open(RecipeData_FilePath, 'r', encoding='UTF8') as f:
    json_data = json.load(f)

cursor.execute("SHOW columns FROM food_recipe")

colText = ''
for cnt, column in enumerate(cursor.fetchall()):
    if cnt == 0:
        pass
    elif cnt == 1:
        colText += column[0]
    else:
        colText = colText + "," + column[0]
print(colText)

# for 문 사용하여 json 파일 하나씩 넣기
for num in json_data.keys():
    tmp = json_data[num]
    print(tmp)

    # DB 쿼리문
    query = "INSERT INTO food_recipe ({}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(colText)
    data = (tmp['레시피일련번호'], tmp['요리명'], tmp['등록자명'], tmp['조회수'], tmp['추천수'], tmp['요리상황별 명'],
            tmp['요리소개'], tmp['요리재료내용'], tmp['요리인분 명'], tmp['요리난이도 명'], tmp['요리시간 명'])
    cursor.execute(query, data)
    db.commit()
print('만개의 레시피 자료 처리 끝')
#################### 만개의 레시피 자료 처리 ####################


#################### 거래량 데이터 ####################
print('도매 거래량 처리 시작')
# 불러올 json 파일
for file in [WholesaleVolume_FilePath, WholesalePrice_FilePath]:
    if file == WholesaleVolume_FilePath:
        Table = 'wholesale_quantity'
        name = '거래량(kg)'
    else:
        Table = 'wholesale_price'
        name = '가격(원/kg)'

    print(Table)
    print(file + '파일 처리 시작')
    with open(file, 'r', encoding='UTF8') as f:
        json_data = json.load(f)

    cursor.execute("SHOW columns FROM {}".format(Table))

    colText = ''
    for cnt, column in enumerate(cursor.fetchall()):
        if cnt == 0:
            colText += column[0]
        else:
            colText = colText + "," + column[0]
    print(colText)

    # for 문 사용하여 json 파일 하나씩 넣기
    for num in json_data.keys():
        tmp = json_data[num]
        print(tmp)

        # DB 쿼리문
        query = """INSERT INTO {} ({}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """.format(Table, colText)
        data = (
        tmp['date'], tmp['콩_' + name], tmp['고구마_' + name], tmp['감자_' + name], tmp['배추_' + name], tmp['양배추_' + name],
        tmp['시금치_' + name], tmp['상추_' + name], tmp['얼갈이배추_' + name], tmp['수박_' + name], tmp['참외_' + name],
        tmp['오이_' + name],
        tmp['호박_' + name], tmp['토마토_' + name], tmp['딸기_' + name], tmp['무_' + name], tmp['당근_' + name],
        tmp['열무_' + name],
        tmp['건고추_' + name], tmp['풋고추_' + name], tmp['양파_' + name], tmp['대파_' + name], tmp['쪽파_' + name],
        tmp['생강_' + name],
        tmp['미나리_' + name], tmp['깻잎_' + name], tmp['피망(단고추)_' + name], tmp['파프리카_' + name], tmp['방울토마토_' + name],
        tmp['참깨_' + name],
        tmp['땅콩_' + name], tmp['느타리버섯_' + name], tmp['새송이_' + name], tmp['팽이버섯_' + name], tmp['호두_' + name],
        tmp['사과_' + name],
        tmp['배_' + name], tmp['복숭아_' + name], tmp['포도_' + name], tmp['감귤_' + name], tmp['단감_' + name],
        tmp['바나나_' + name],
        tmp['참다래(키위)_' + name], tmp['파인애플_' + name], tmp['오렌지_' + name], tmp['레몬_' + name], tmp['체리_' + name],
        tmp['망고_' + name])
        cursor.execute(query, data)
        db.commit()
print('도매 거래량 처리 끝')
#################### 거래량 데이터 ####################


checkDict = {'광주': 'gwangju', '대구': 'daegu', '대전': 'daejeon', '부산': 'busan',
             '서울': 'seoul', '울산': 'ulsan', '인천': 'incheon', '전체': 'total'}

#################### 전체 소매 데이터 ####################
print('소매 데이터 처리 시작')
for file in glob(Retail_FolderPath + '*.json'):
    TotalList = []
    print('파일 경로 : ' + file)
    day = int(file.split('.')[0].split('\\')[-1].split('_')[0])
    area = file.split('.')[0].split('\\')[-1].split('_')[1]
    TotalList.append(day)
    print(str(day) + " : " + area)

    with open(file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    for datalist in json_data['Result']:
        for price in datalist.values():
            # print(str(price[0]), ",", str(price[1]))
            TotalList.append(price[0])
            TotalList.append(price[1])

    cursor.execute("SHOW columns FROM {}_retail".format(checkDict[area]))

    colText = ''
    for cnt, column in enumerate(cursor.fetchall()):
        if cnt == 0:
            colText += column[0]
        else:
            colText = colText + "," + column[0]
    print(colText)
    print(tuple(TotalList))

    query = "INSERT INTO {}_retail ({}) VALUES {}".format(checkDict[area], colText, tuple(TotalList))
    print(query)
    cursor.execute(query)
    db.commit()
print('소매 데이터 처리 끝')
#################### 전체 소매 데이터 ####################
