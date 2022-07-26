from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT, RecipeData_Path, VolumeData_Path
import json
import pymysql

## DB 초기 설정
db = pymysql.Connect(host=DB_HOST,
                     user=DB_USERNAME,  # db 계정
                     password=DB_PASSWORD,  # db 비밀 번호
                     database=DB_NAME)  # 접속 하고자 하는 db 명
cursor = db.cursor()

### 만개의 레시피 자료 처리
## 불러올 json 파일
with open(RecipeData_Path, 'r', encoding='UTF8') as f:
    json_data = json.load(f)

## for 문 사용하여 json 파일 하나씩 넣기
for num in json_data.keys():
    tmp = json_data[num]

    # DB 넘어가는 데이터 내용
    print(str(tmp['레시피일련번호']) + " : " + tmp['요리명'] + " : " + tmp['등록자명'] + " : "
          + str(tmp['조회수']) + " : " + str(tmp['추천수']) + " : " + tmp['요리상황별 명'] + " : "
          + tmp['요리소개'] + " : " + tmp['요리재료내용'] + " : " + tmp['요리인분 명'] + " : "
          + tmp['요리난이도 명'] + " : " + tmp['요리시간 명'])

    # DB 쿼리문
    query = "INSERT INTO food_recipe (serial, dish, registrant, views, likes, situation, intro, ingredients, servings, level, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (tmp['레시피일련번호'], tmp['요리명'], tmp['등록자명'], tmp['조회수'], tmp['추천수'], tmp['요리상황별 명'], tmp['요리소개'], tmp['요리재료내용'],
            tmp['요리인분 명'], tmp['요리난이도 명'], tmp['요리시간 명'])
    cursor.execute(query, data)
    db.commit()

### 만개의 레시피 자료 처리
### 거래량 데이터
## 불러올 json 파일
with open(VolumeData_Path, 'r', encoding='UTF8') as f:
    json_data = json.load(f)

## for 문 사용하여 json 파일 하나씩 넣기
for num in json_data.keys():
    tmp = json_data[num]

    query = "INSERT INTO wholesale_quantity (date, beans, sweet_potato, potato, chinese_cabbage, cabbage, spinach, lettuce, korean_cabbage, watermelon, korean_melon, cucumber, pumpkin, tomato, strawberry, radish, carrot, yeol_radish, dried_red_pepper, pepper, onion, green_onion, chives, ginger, parsley, sesame_leaf, pimento, paprika, cherry_tomato, sesame, peanut, oyster_mushroom, king_oyster_mushroom, enoki_mushrooms, walnut, apple, pear, peach, grape, citrus, persimmon, banana, kiwi, pineapple, orange, lemon, cherry, mango) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (tmp['date'], tmp['콩_가격(원/kg)'], tmp['고구마_가격(원/kg)'], tmp['감자_가격(원/kg)'],
            tmp['배추_가격(원/kg)'], tmp['양배추_가격(원/kg)'], tmp['시금치_가격(원/kg)'],
            tmp['상추_가격(원/kg)'], tmp['얼갈이배추_가격(원/kg)'], tmp['수박_가격(원/kg)'],
            tmp['참외_가격(원/kg)'], tmp['오이_가격(원/kg)'], tmp['호박_가격(원/kg)'],
            tmp['토마토_가격(원/kg)'], tmp['딸기_가격(원/kg)'], tmp['무_가격(원/kg)'],
            tmp['당근_가격(원/kg)'], tmp['열무_가격(원/kg)'], tmp['건고추_가격(원/kg)'],
            tmp['풋고추_가격(원/kg)'], tmp['양파_가격(원/kg)'], tmp['대파_가격(원/kg)'],
            tmp['쪽파_가격(원/kg)'], tmp['생강_가격(원/kg)'], tmp['미나리_가격(원/kg)'],
            tmp['깻잎_가격(원/kg)'], tmp['피망(단고추)_가격(원/kg)'], tmp['파프리카_가격(원/kg)'],
            tmp['방울토마토_가격(원/kg)'], tmp['참깨_가격(원/kg)'], tmp['땅콩_가격(원/kg)'],
            tmp['느타리버섯_가격(원/kg)'], tmp['새송이_가격(원/kg)'], tmp['팽이버섯_가격(원/kg)'],
            tmp['호두_가격(원/kg)'], tmp['사과_가격(원/kg)'], tmp['배_가격(원/kg)'],
            tmp['복숭아_가격(원/kg)'], tmp['포도_가격(원/kg)'], tmp['감귤_가격(원/kg)'],
            tmp['단감_가격(원/kg)'], tmp['바나나_가격(원/kg)'], tmp['참다래(키위)_가격(원/kg)'],
            tmp['파인애플_가격(원/kg)'], tmp['오렌지_가격(원/kg)'], tmp['레몬_가격(원/kg)'],
            tmp['체리_가격(원/kg)'], tmp['망고_가격(원/kg)'])
    cursor.execute(query, data)
    db.commit()
    print(tmp)

### 거래량 데이터
