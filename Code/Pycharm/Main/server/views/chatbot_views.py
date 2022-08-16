import json
import os
import re
import urllib.request
from glob import glob

import pymysql
from flask import Blueprint, request, jsonify

from config import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME
from ..define.chat_price import Chatbot_iprice
from ..define.naver_api import Navershop
from ..define.yolo5 import Yolorun

#################### DB 초기 설정 ####################
# DB_USERNAME = 'root'
# DB_HOST = 'localhost'
# DB_PORT = '3306'
# DB_PASSWORD = 'rladydtjr1!'
# DB_NAME = 'projectdb'
# SECRET_KEY = 'dev'
#####################################################

bp = Blueprint('kakao_chatbot', __name__, url_prefix='/kakao_chatbot')


## 웰컴 인사
@bp.route('/welcome', methods=['POST', 'GET'])
def welcome():
    ret = {
        "version": "2.0",
        "template": {
            "outputs": [{
                "simpleText": {
                    "text": """
내일 뭐먹지 챗봇을 이용해주셔서 감사합니다. 
아래의 사용방법 버튼을 클릭하여,
사용법을 숙지하신 후,
서비스를 이용해주시기 바랍니다. 
감사합니다.
                                         """
                }
            }]
        }
    }
    return jsonify(ret)


## 소개
@bp.route('/init', methods=['POST', 'GET'])
def init():
    ret = {
        "version": "2.0",
        "template": {
            "outputs": [{
                "simpleText": {
                    "text": """
    내일 뭐 먹지 사용법이에요.😀

1. 하단의 '레시피 검색' 클릭

    1-1. 이미지로 찾기 ❗모바일 만❗
    👉 '이미지' 클릭
    👉 '이미지 업로드' 클릭
    👉 찾고 싶은 음식 사진 전송
    
    1-2. 텍스트로 찾기
    👉 '텍스트' 클릭
    👉 채팅창에 음식명 입력
    
    1-3. '재료 확인'
    👉 음식의 재료와 가격 출력
    
    1-4. '레시피 보기'
    👉 레시피 링크 접속
    
2. '농수산물 가격 정보'
    👉 찾고 싶은 농수산물 입력
    
맛있게 요리해드세요. 😃 """
                }
            }],
            "quickReplies": [{
                "messageText": "레시피 검색",
                "action": "message",
                "label": "레시피 검색"
            }, {
                "messageText": "농수산물 가격 정보",
                "action": "message",
                "label": "농수산물 가격 정보"
            }]
        }
    }
    return jsonify(ret)


## find_img (레시피 검색 > 이미지)
@bp.route('/find_img', methods=['POST', 'GET'])
def find_img():
    req_json = request.get_json()
    temp = req_json['action']['params']['secureimage']
    temp_json = json.loads(temp)
    img_tmp = temp_json['secureUrls']

    URLList = re.sub('List\\(|\\)', "", img_tmp).split(',')  # URLList은 챗봇에서 사용자가 보낸 사진의 URL주소
    UserInfo = req_json['userRequest']['user']['id']  # UserInfo 는 유저의 아이디값

    dir_path = ("C:\\Users\\hkedu\\HKProject\\Code\\Pycharm\\Main\\server\\static\\upload_img\\")
    print('dir_path: ', glob(dir_path))
    if os.path.exists(dir_path):
        if len(glob(dir_path + '\\*')) != 0:
            for file in glob(dir_path + '\\*'):
                os.remove(file)
    cnt = 1
    for i in URLList:
        urllib.request.urlretrieve(i,
                                   "C:\\Users\\hkedu\\HKProject\\Code\\Pycharm\\Main\\server\\static\\upload_img\\" + str(
                                       UserInfo) + "food" + str(cnt) + ".jpg")
        cnt += 1

    # 위의 코드는 URL주소를 이용하여 로컬피시에 저장
    Folder_List = glob("C:\\Users\\hkedu\\HKProject\\Code\\Pycharm\\Main\\server\\static\\upload_img\\*.jpg")
    print('Folder_List: ', Folder_List)
    #  Folder_List 는 폴더에 저장된 이미지주소를 리스트로 받아옴
    #  ex) ['1.jpg','2.jpg', '3.jpg']

    if len(Folder_List) >= 2:
        ret = {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text": '사진을 1장만 보내 주세요'
                    }
                }],
                "quickReplies": [{
                    "messageText": "이미지 검색",
                    "action": "message",
                    "label": "이미지 다시 보내기"
                }, {
                    "messageText": "레시피 검색",
                    "action": "message",
                    "label": "뒤로 돌아가기"
                }, ]
            }
        }
    else:
        Yolorun_return = Yolorun(Folder_List[0])
        #  Yolorun_return 는 Yolorun 함수를 실행시킨 return값을 받아줌
        if len(Yolorun_return) >= 2:
            ret = {
                "version": "2.0",
                "template": {
                    "outputs": [{
                        "simpleText": {
                            "text": '음식이 1개만 있는 사진을 보내 주세요.'
                        }
                    }],
                    "quickReplies": [{
                        "messageText": "이미지 검색",
                        "action": "message",
                        "label": "이미지 다시 보내기"
                    }, {
                        "messageText": "레시피 검색",
                        "action": "message",
                        "label": "뒤로 돌아가기"
                    }, ]
                }
            }
        elif len(Yolorun_return) == 0:
            ret = {
                "version": "2.0",
                "template": {
                    "outputs": [{
                        "simpleText": {
                            "text": '확인할 수 있는 음식이 없습니다.'
                        }
                    }],
                    "quickReplies": [{
                        "messageText": "이미지 검색",
                        "action": "message",
                        "label": "이미지 다시 보내기"
                    }, {
                        "messageText": "레시피 검색",
                        "action": "message",
                        "label": "뒤로 돌아가기"
                    }, ]
                }
            }
        else:
            db = pymysql.Connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_NAME)
            with db:
                with db.cursor() as cur:
                    sql_table = 'SELECT * FROM food_recipe WHERE dish LIKE "%{}%" ORDER BY views DESC LIMIT 3;'.format(
                        Yolorun_return[0])
                    # SELECT 선택 = food_recipe테이블, WHERE = dish컬럼, LIKE = .format(x[0])과 같은 형태로, DESC = 내림차순, LIMIT = 제한 3개

                    cur.execute(sql_table)
                    # 가상의공간에 sql_table를 실행
                    SQLFOOD_list = list(cur.fetchall())
                    print(SQLFOOD_list)
                    # SQLFOOD_list 는 sql_table을 ()에서 []로 바꿈
                    URL = 'https://www.10000recipe.com/recipe/'
                    yolochat_List = []
                    for cnt in range(len(SQLFOOD_list)):
                        yolochat = {
                            "imageTitle": {
                                "title": SQLFOOD_list[cnt][2],
                            },
                            "title": "간단 소개",
                            "description": SQLFOOD_list[cnt][7],
                            "thumbnail": {
                                "imageUrl": SQLFOOD_list[cnt][12],
                                "width": 800,
                                "height": 800},
                            "itemList": [{
                                "title": "요리 난이도",
                                "description": SQLFOOD_list[cnt][10]
                            }, {
                                "title": "테마",
                                "description": SQLFOOD_list[cnt][6]
                            }, {
                                "title": "요리 양",
                                "description": SQLFOOD_list[cnt][9]
                            }, {
                                "title": "평균 조리시간",
                                "description": SQLFOOD_list[cnt][11]
                            }, {
                                "title": "조회수",
                                "description": SQLFOOD_list[cnt][4]
                            }, ],
                            "itemListAlignment": "right",
                            "buttons": [{
                                "label": "재료 확인",
                                "action": "message",
                                "messageText": "재료 확인하기",
                                "extra": {
                                    "Food_Recipe1": SQLFOOD_list[cnt][13],
                                    "Food_Name1": SQLFOOD_list[cnt][2],
                                    "Serial_Number1": SQLFOOD_list[cnt][1]
                                }
                            }, {
                                "label": "레시피 보기",
                                "action": "webLink",
                                "webLinkUrl": URL + str(SQLFOOD_list[cnt][1])
                            }]
                        }
                        yolochat_List.append(yolochat)
                    cur.close()
            print(Yolorun_return[0])
            # ret은 카톡챗봇의 응답
            ret = {
                "version": "2.0",
                "template": {
                    "outputs": [{
                        "simpleText": {
                            "text": "'" + Yolorun_return[0] + "'" + " 사진으로 레시피를 검색 합니다."
                        }
                    }, {
                        "carousel": {
                            "type": "itemCard",
                            "items": yolochat_List
                        }
                    }],
                    "quickReplies": [{
                        "messageText": "이미지 검색",
                        "action": "message",
                        "label": "이미지 다시 보내기"
                    }, {
                        "messageText": "레시피 검색",
                        "action": "message",
                        "label": "뒤로 돌아가기"
                    }]
                }
            }
            print(ret)
    return jsonify(ret)


## find_ingredients (재료 확인)
@bp.route('/find_ingredients', methods=['POST', 'GET'])
def find_ingredients():
    ret = request.get_json()
    ingredient_txt = ret['action']['clientExtra']['Food_Recipe1']
    ingredient_list = ingredient_txt.split(',')
    tmp = '현재 레시피에 들어가는 재료 입니다. \n 추가로 네이버 쇼핑으로 재료를 구매 하고 싶으면 아래 버튼을 이용해 주세요. \n'
    for cnt, data in enumerate(ingredient_list):
        # print(data)
        ingredients = data.split('_')[0]
        quantity = data.split('_')[1]
        quantity = quantity.strip()
        if len(quantity) != 0:
            quantity = '(' + data.split('_')[1].strip("("")") + ')'
        else:
            quantity = ''
        tmp = tmp + '\n' + ingredients + quantity + '\n'
    rets = {
        "version": "2.0",
        "template": {
            "outputs": [{
                "simpleText": {
                    "text": tmp
                }
            }],
            "quickReplies": [{
                "messageText": "네이버 쇼핑",
                "action": "message",
                "label": "네이버에서 구매하기"
            }, {
                "messageText": "텍스트 검색",
                "action": "message",
                "label": "텍스트 다시 작성하기"
            }, {
                "messageText": "레시피 검색",
                "action": "message",
                "label": "뒤로 돌아가기"
            }, ]
        }
    }
    return jsonify(rets)


## find_txt (레시피 검색 > 텍스트)
@bp.route('/find_txt', methods=['POST', 'GET'])
def find_txt():
    req_json = request.get_json()
    temp = req_json['action']['params']['txtfood']
    db = pymysql.Connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_NAME)
    with db:
        with db.cursor() as cur:
            sql_table2 = 'SELECT * FROM projectdb.food_recipe WHERE dish LIKE "%{}%" ORDER BY views DESC LIMIT 3;'.format(
                temp)
            cur.execute(sql_table2)
            SQLFOOD_list = list(cur.fetchall())

            URL = 'https://www.10000recipe.com/recipe/'

            if len(SQLFOOD_list) == 0:
                ret = {
                    "version": "2.0",
                    "template": {
                        "outputs": [{
                            "simpleText": {
                                "text": '작성하신 텍스트가 올바르지 않습니다. 다시 확인해주시기 바랍니다.'
                            }
                        }],
                        "quickReplies": [{
                            "messageText": "텍스트 검색",
                            "action": "message",
                            "label": "텍스트 다시 작성하기"}, {
                            "messageText": "레시피 검색",
                            "action": "message",
                            "label": "뒤로 돌아가기"
                        }]
                    }
                }
            else:
                textchat_List = []
                for cnt in range(len(SQLFOOD_list)):
                    txtchat = {
                        "imageTitle": {
                            "title": SQLFOOD_list[cnt][2],
                        },
                        "title": "간단 소개",
                        "description": SQLFOOD_list[cnt][7],
                        "thumbnail": {
                            "imageUrl": SQLFOOD_list[cnt][12],
                            "width": 800,
                            "height": 800},
                        "itemList": [{
                            "title": "요리 난이도",
                            "description": SQLFOOD_list[cnt][10]
                        }, {
                            "title": "테마",
                            "description": SQLFOOD_list[cnt][6]
                        }, {
                            "title": "요리 양",
                            "description": SQLFOOD_list[cnt][9]
                        }, {
                            "title": "평균 조리시간",
                            "description": SQLFOOD_list[cnt][11]
                        }, {
                            "title": "조회수",
                            "description": SQLFOOD_list[cnt][4]
                        }, ],
                        "itemListAlignment": "right",
                        "buttons": [{
                            "label": "재료 확인",
                            "action": "message",
                            "messageText": "재료 확인하기",
                            "extra": {
                                "Food_Recipe1": SQLFOOD_list[cnt][13],
                                "Food_Name1": SQLFOOD_list[cnt][2],
                                "Serial_Number1": SQLFOOD_list[cnt][1]
                            }
                        }, {
                            "label": "레시피 보기",
                            "action": "webLink",
                            "webLinkUrl": URL + str(SQLFOOD_list[cnt][1])
                        }],
                        "buttonLayout": "vertical"
                    }
                    textchat_List.append(txtchat)
                cur.close()

                # ret은 카톡챗봇의 응답
                ret = {
                    "version": "2.0",
                    "template": {
                        "outputs": [{
                            "simpleText": {
                                "text": "'" + temp + "'" + " 로 레시피를 검색 합니다."
                            }
                        }, {
                            "carousel": {
                                "type": "itemCard",
                                "items": textchat_List
                            }
                        }],
                        "quickReplies": [{
                            "messageText": "텍스트 검색",
                            "action": "message",
                            "label": "텍스트 다시 작성하기"
                        }, {
                            "messageText": "레시피 검색",
                            "action": "message",
                            "label": "뒤로 돌아가기"
                        }]
                    }
                }
                print(ret)
            return jsonify(ret)


## fnaver_shop (네이버 쇼핑)
@bp.route('/naver_shop', methods=['POST', 'GET'])
def naver_shop():
    req_json = request.get_json()
    temp = req_json['action']['params']['naver_shop']
    dataList = Navershop(temp)

    if len(dataList) == 0:
        ret = {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text": '작성하신 텍스트가 올바르지 않습니다. 다시 확인해주시기 바랍니다.'
                    }
                }],
                "quickReplies": [{
                    "messageText": "네이버 쇼핑",
                    "action": "message",
                    "label": "다른 재료 검색하기"
                }, {
                    "messageText": "레시피 검색",
                    "action": "message",
                    "label": "뒤로 돌아가기"
                }]
            }
        }

    else:
        Result_Lsit = []
        for data in dataList:
            data_dict = {
                "imageTitle": {
                    "title": data['이름'],
                },
                "thumbnail": {
                    "imageUrl": data['이미지'],
                    "width": 800,
                    "height": 800
                },
                "itemList": [{
                    "title": "가격",
                    "description": data['최저가격'] + "원"
                }],
                "itemListAlignment": "left",
                "buttons": [{
                    "action": "webLink",
                    "label": "쇼핑하러 가기",
                    "webLinkUrl": data['url']
                }]
            }

            Result_Lsit.append(data_dict)

        ret = {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "carousel": {
                        "type": "itemCard",
                        "items": Result_Lsit
                    }
                }],
                "quickReplies": [{
                    "messageText": "네이버 쇼핑",
                    "action": "message",
                    "label": "다른 재료 검색하기"
                }, {
                    "messageText": "레시피 검색",
                    "action": "message",
                    "label": "뒤로 돌아가기"
                }]
            }
        }
    return jsonify(ret)


@bp.route('/retail_price', methods=['POST', 'GET'])
def retail_price():
    req_json = request.get_json()
    temp = req_json['action']['params']['retail_price']

    PyFile = Chatbot_iprice(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME)
    Price_Dict = PyFile.Price_Dict()
    Price_List = [price for price in Price_Dict.values()]
    Day_List = [price for price in Price_Dict.keys()]
    NongSan_List = [nogsan for nogsan in Price_List[0].keys()]
    print(Price_List)
    print(Day_List)
    Month = str(Day_List[0])[4:6]
    Day = str(Day_List[0])[6:]
    if temp in NongSan_List:
        day = Price_List[0][temp]
        day_1 = Price_List[1][temp]
        Cprice = round(day) - round(day_1)
        if Cprice > 0:
            Cprice = abs(Cprice)
            Cprice = str(Cprice).split('.')[0]
            print(Cprice)
            info = '원 올랐습니다.'
        else:
            Cprice = abs(Cprice)
            Cprice = str(Cprice).split('.')[0]
            info = '원 내렸습니다.'
        day = str(round(day)).split('.')[0]
        ret = {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text":
                            Month + ' 월 ' + Day + ' 일 ' + temp + '의 평균 가격은 ' + day + '원 이며,\n전날과 비교하여, ' + Cprice + info
                    }
                }],
                "quickReplies": [{
                    "messageText": "이미지 검색",
                    "action": "message",
                    "label": "이미지 검색"
                }, {
                    "messageText": "텍스트 검색",
                    "action": "message",
                    "label": "텍스트 검색"
                }, {
                    "messageText": "농수산물 가격 정보 확인하기",
                    "action": "message",
                    "label": "농수산물 가격 검색"
                }, ]
            }
        }
    else:
        ret = {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text": '해당 작물에 대한 정보가 없습니다.'
                    }
                }],
                "quickReplies": [{
                    "messageText": "이미지 검색",
                    "action": "message",
                    "label": "이미지 검색"
                }, {
                    "messageText": "텍스트 검색",
                    "action": "message",
                    "label": "텍스트 검색"
                }, {
                    "messageText": "농수산물 가격 정보 확인하기",
                    "action": "message",
                    "label": "농수산물 가격 검색"
                }, ]
            }
        }

    return jsonify(ret)
