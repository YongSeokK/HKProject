## MySQL set
DB_USERNAME = 'root'
DB_HOST = 'localhost'
DB_PORT = '3306'

SECRET_KEY = 'dev'

### 로컬별 수정할 항목 Start ------------------------------------Start
#                                                                 #
#                                                                 #
#                                                                 #
DB_PASSWORD = 'test1234'  # MySQL Password
DB_NAME = 'project_db'  # MySQL Name

## Path - 파이참 프로젝트 가장 상위 폴더 = Main 절대 경로
Root_Path = r'C:\Users\sonmj\G_Project\Code\Pycharm\Main'
#                                                                 #
#                                                                 #
#                                                                 #
### 로컬별 수정할 항목 End ----------------------------------------End


## Folder Path
# Daily DATA관련 init
Daily_Folder_Path = Root_Path + '\\DB_source\\Daily\\'
# csv DATA관련 init
csv_Folder_Path = Root_Path + '\\DB_source\\csv\\'
# 초기 DATA관련 init
Retail_Folder_Path = Root_Path + "\\DB_source\\Init\\retail_json\\"
RecipeData_File_Path = Root_Path + "\\DB_source\\Init\\recipe.json"
WholesaleVolume_File_Path = Root_Path + "\\DB_source\\Init\\220726_농산물거래량.json"
WholesalePrice_File_Path = Root_Path + "\\DB_source\\Init\\220726_농산물가격.json"
# YOLO
Yolo_imgFolder_Path = Root_Path + '\\server\\yolo\\img\\'
pt_Path = Root_Path + '\\server\\yolo\\best.pt'
Food_List = ['.', '닭볶음탕', '된장찌개', '갈치구이', '감자조림', '김밥',
             '김치전', '계란찜', '깻잎장아찌', '메추리알장조림', '떡볶이',
             '떡국', '파전', '미역국', '소불고기', '잡채']
# 제철 음식
Excel_Path = Root_Path + '\\DB_source\\Init\\월별_제철재료_통합.xlsx'
# Shop
Shop_imgFolder_Path = Root_Path + '\\server\\static\\img\\shop\\'


## NAVER API KEY
Client_id = "MiUA1cOwkgZ7FPIPBawa"
Client_secret = "sdSR7YXRu8"

## 참고 DATA
# Source
Whole_List = ['농산물가격', '농산물거래량']

# 변환
Days = ['월', '화', '수', '목', '금', '토', '일']
Tier = ['관리자', '일반 회원', '판매자', '매니저']
Category_Kor = ['식량작물', '특용작물', '채소류', '과일류']
Category_Eng = ['Foodcrop', 'Specialcrop', 'Vegetable', 'Fruit']
Region_Dict = {'서울': 'seoul', '인천': 'incheon', '대전': 'daejeon', '광주': 'gwangju',
               '대구': 'daegu', '울산': 'ulsan', '부산': 'busan', '전체': 'total'}

# 도매 식량작물, 특용작물, 채소류, 과일류
Foodcrop_Dict_W = {'감자': 'potato', '고구마': 'sweet_potato', '콩': 'beans'}
Specialcrop_Dict_W = {'느타리버섯': 'oyster_mushroom', '땅콩': 'peanut', '새송이버섯': 'king_oyster_mushroom', '참깨': 'sesame',
                      '팽이버섯': 'enoki_mushrooms', '호두': 'walnut'}
Vegetable_Dict_W = {'건고추': 'dried_red_pepper', '고추': 'pepper', '깻잎': 'sesame_leaf', '당근': 'carrot', '대파': 'green_onion',
                    '딸기': 'strawberry', '무': 'radish', '미나리': 'parsley', '방울토마토': 'cherry_tomato',
                    '배추': 'napa_cabbage', '상추': 'lettuce', '생강': 'ginger', '수박': 'watermelon', '시금치': 'spinach',
                    '양배추': 'cabbage', '양파': 'onion', '얼갈이배추': 'winter_cabbage', '열무': 'yeol_radish', '오이': 'cucumber',
                    '쪽파': 'chives', '참외': 'korean_melon', '토마토': 'tomato', '파프리카': 'paprika', '피망': 'pimento',
                    '호박': 'pumpkin'}
Fruit_Dict_W = {'감귤': 'citrus', '단감': 'persimmon', '레몬': 'lemon', '망고': 'mango', '바나나': 'banana', '배': 'pear',
                '복숭아': 'peach', '사과': 'apple', '오렌지': 'orange', '체리': 'cherry', '키위': 'kiwi', '파인애플': 'pineapple',
                '포도': 'grape'}

# Radio button check 값을 주기 위한 value 값이 공란인 딕셔러니 생성
Foodcrop_radioDict_W = dict.fromkeys(list(Foodcrop_Dict_W.keys()), '')
Specialcrop_radioDict_W = dict.fromkeys(list(Specialcrop_Dict_W.keys()), '')
Vegetable_radioDict_W = dict.fromkeys(list(Vegetable_Dict_W.keys()), '')
Fruit_radioDict_W = dict.fromkeys(list(Fruit_Dict_W.keys()), '')

Category_List_W = [Foodcrop_Dict_W, Specialcrop_Dict_W, Vegetable_Dict_W, Fruit_Dict_W]
Category_radioList_W = [Foodcrop_radioDict_W, Specialcrop_radioDict_W, Vegetable_radioDict_W, Fruit_radioDict_W]

# 소매 식량작물, 특용작물, 채소류, 과일류
Foodcrop_Dict_R = {'감자': 'potato', '고구마': 'sweet_potato', '녹두': 'green_beans', '쌀': 'rice', '찹쌀': 'glutinous_rice',
                   '콩': 'bean', '팥': 'red_bean'}
Specialcrop_Dict_R = {'느타리버섯': 'oyster_mushroom', '땅콩': 'peanut', '새송이버섯': 'king_oyster_mushroom', '아몬드': 'almond',
                      '애느타리버섯': 'oyster_mushroomA', '참깨': 'sesame', '팽이버섯': 'enoki_mushroom', '호두': 'walnut'}
Vegetable_Dict_R = {'갓': 'leaf_mustard', '건고추(양건)': 'dried_red_pepperS', '건고추(화건)': 'dried_red_pepperD',
                    '고추가루': 'chili_powder', '깐마늘': 'garlic', '깻잎': 'sesame_leaf', '꽈리고추': 'chilli_pepper',
                    '당근': 'carrot', '대추토마토': 'jujube_cherry_tomato', '대파': 'green_onion', '딸기': 'strawberry',
                    '멜론': 'melon', '무': 'radish', '미나리': 'parsley', '방울토마토': 'cherry_tomato', '배추': 'napa_cabbage',
                    '붉은고추': 'red_pepper', '상추(적)': 'lettuceR', '상추(청)': 'lettuceB', '생강': 'ginger', '수박': 'watermelon',
                    '시금치': 'spinach', '애호박': 'squash', '양배추': 'cabbage', '양파': 'onion', '얼갈이배추': 'winter_cabbage',
                    '열무': 'yeol_radish', '오이(가시)': 'cucumberS', '오이(다다기)': 'cucumberD', '오이(취청)': 'cucumberW',
                    '주키니': 'zucchini', '쪽파': 'chives', '참외': 'korean_melon', '청양고추': 'cheongyang_pepper',
                    '토마토': 'tomato', '파프리카': 'paprika', '풋고추': 'pepper', '피망': 'pimento'}
Fruit_Dict_R = {'감귤': 'citrus', '건블루베리': 'dried_blueberries', '건포도': 'raisin', '단감': 'persimmon', '레몬': 'lemon',
                '망고': 'mango', '바나나': 'banana', '배': 'pear', '복숭아': 'peach', '사과': 'apple', '샤인머스켓': 'grapeS',
                '오렌지': 'orange', '참다래': 'kiwi', '체리': 'cherry', '파인애플': 'pineapple', '포도': 'grape', '포도(거봉)': 'grapeG',
                '포도(머루)': 'grapeM'}

# Radio button check 값을 주기 위한 value 값이 공란인 딕셔러니 생성
Foodcrop_radioDict_R = dict.fromkeys(list(Foodcrop_Dict_R.keys()), '')
Specialcrop_radioDict_R = dict.fromkeys(list(Specialcrop_Dict_R.keys()), '')
Vegetable_radioDict_R = dict.fromkeys(list(Vegetable_Dict_R.keys()), '')
Fruit_radioDict_R = dict.fromkeys(list(Fruit_Dict_R.keys()), '')

Category_List_R = [Foodcrop_Dict_R, Specialcrop_Dict_R, Vegetable_Dict_R, Fruit_Dict_R]
Category_radioList_R = [Foodcrop_radioDict_R, Specialcrop_radioDict_R, Vegetable_radioDict_R, Fruit_radioDict_R]

# 소매 딕셔너리 농산물 순서
Produce_Num = {'rice': 0, 'glutinous_rice': 1, 'bean': 2, 'red_bean': 3, 'green_beans': 4, 'sweet_potato': 5,
               'potato': 6, 'napa_cabbage': 0, 'cabbage': 1, 'spinach': 2, 'lettuceR': 3, 'lettuceB': 4,
               'winter_cabbage': 5, 'leaf_mustard': 6, 'watermelon': 7, 'korean_melon': 8, 'cucumberS': 9,
               'cucumberD': 10, 'cucumberW': 11, 'squash': 12, 'zucchini': 13, 'tomato': 14, 'strawberry': 15,
               'radish': 16, 'carrot': 17, 'yeol_radish': 18, 'dried_red_pepperD': 19, 'dried_red_pepperS': 20,
               'pepper': 21, 'chilli_pepper': 22, 'cheongyang_pepper': 23, 'red_pepper': 24, 'onion': 25,
               'green_onion': 26, 'chives': 27, 'ginger': 28, 'chili_powder': 29, 'parsley': 30, 'sesame_leaf': 31,
               'pimento': 32, 'paprika': 33, 'melon': 34, 'garlic': 35, 'cherry_tomato': 36, 'jujube_cherry_tomato': 37,
               'sesame': 0, 'peanut': 1, 'oyster_mushroom': 2, 'oyster_mushroomA': 3, 'enoki_mushroom': 4,
               'king_oyster_mushroom': 5, 'walnut': 6, 'almond': 7, 'apple': 0, 'pear': 1, 'peach': 2, 'grape': 3,
               'grapeG': 4, 'grapeM': 5, 'grapeS': 6, 'citrus': 7, 'persimmon': 8, 'banana': 9, 'kiwi': 10,
               'pineapple': 11, 'orange': 12, 'lemon': 13, 'cherry': 14, 'raisin': 15, 'dried_blueberries': 16,
               'mango': 17}
