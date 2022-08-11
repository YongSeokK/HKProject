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
DB_NAME = 'projectdb'  # MySQL Name

## Path - 파이참 프로젝트 가장 상위 폴더 = Main 절대 경로
Root_Path = 'C:\\Users\\sonmj\\G_Project\\Code\\Pycharm\\Main'
#                                                                 #
#                                                                 #
#                                                                 #
### 로컬별 수정할 항목 End ----------------------------------------End


## Daily DATA관련 init
Daily_FolderPath = Root_Path + '\\DB_source\\Daily\\'

## csv DATA관련 init
csv_FolderPath = Root_Path + '\\DB_source\\csv\\'

## 초기 DATA관련 init
Retail_FolderPath = Root_Path + "\\DB_source\\Init\\retail_json\\"
RecipeData_FilePath = Root_Path + "\\DB_source\\Init\\recipe.json"
WholesaleVolume_FilePath = Root_Path + "\\DB_source\\Init\\220726_농산물거래량.json"
WholesalePrice_FilePath = Root_Path + "\\DB_source\\Init\\220726_농산물가격.json"

## 참고 DATA
# Source
Area_Dict = {'광주': 'gwangju', '대구': 'daegu', '대전': 'daejeon', '부산': 'busan',
             '서울': 'seoul', '울산': 'ulsan', '인천': 'incheon', '전체': 'total'}
Whole_List = ['농산물가격', '농산물거래량']

# 식량작물, 특용작물, 채소류, 과일류
Foodcrop_Dict = {'감자': 'potato', '고구마': 'sweet_potato', '콩': 'beans'}
Cashcrop_Dict = {'느타리버섯': 'oyster_mushroom', '땅콩': 'peanut', '새송이버섯': 'king_oyster_mushroom', '참깨': 'sesame',
                '팽이버섯': 'enoki_mushrooms', '호두': 'walnut'}
Vegetable_Dict = {'건고추': 'dried_red_pepper', '고추': 'pepper', '깻잎': 'sesame_leaf', '당근': 'carrot', '대파': 'green_onion',
                 '무': 'radish', '미나리': 'parsley', '배추': 'chinese_cabbage', '상추': 'lettuce', '생강': 'ginger',
                 '시금치': 'spinach', '양배추': 'cabbage', '양파': 'onion', '얼갈이배추': 'korean_cabbage', '열무': 'yeol_radish',
                 '오이': 'cucumber', '쪽파': 'chives', '피망': 'pimento', '파프리카': 'paprika', '호박': 'pumpkin'}
Fruit_Dict = {'감귤': 'citrus', '단감': 'persimmon', '딸기': 'strawberry', '레몬': 'lemon', '망고': 'mango', '바나나': 'banana',
             '방울토마토': 'cherry_tomato', '배': 'pear', '복숭아': 'peach', '사과': 'apple', '수박': 'watermelon', '오렌지': 'orange',
             '참외': 'korean_melon', '체리': 'cherry', '키위': 'kiwi', '토마토': 'tomato', '파인애플': 'pineapple', '포도': 'grape'}

# Radio button check 값을 주기 위한 value 값이 공란인 딕셔러니 생성
Foodcrop_Dict2 = dict.fromkeys(list(Foodcrop_Dict.keys()), '')
Cashcrop_Dict2 = dict.fromkeys(list(Cashcrop_Dict.keys()), '')
Vegetable_Dict2 = dict.fromkeys(list(Vegetable_Dict.keys()), '')
Fruit_Dict2 = dict.fromkeys(list(Fruit_Dict.keys()), '')

Category_Kor = ['식량작물', '특용작물', '채소류', '과일류']
Category_List = [Foodcrop_Dict, Cashcrop_Dict, Vegetable_Dict, Fruit_Dict]
Category_List2 = [Foodcrop_Dict2, Cashcrop_Dict2, Vegetable_Dict2, Fruit_Dict2]
