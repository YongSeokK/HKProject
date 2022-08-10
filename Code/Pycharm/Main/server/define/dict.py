import traceback
from datetime import datetime, timedelta

import pymysql
from tqdm import tqdm

#################### DB 초기 설정 ####################
DB_USERNAME = 'root'
DB_HOST = 'localhost'

DB_PASSWORD = 'ghtjddl!4akfl'
DB_NAME = 'projectdb'
SECRET_KEY = 'dev'


#####################################################

class Retail_Dict:
    ### init 설정
    def __init__(self, DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME):
        self.DB_USERNAME = DB_USERNAME
        self.DB_HOST = DB_HOST
        self.DB_PASSWORD = DB_PASSWORD
        self.DB_NAME = DB_NAME

    def Make_Retail_Dict(self):
        ## 초기 딕셔너리 값
        KeyDict = {"Foodcrops": {"T": '''rice_T, riceF_T, glutinous_rice_T, 
                                         bean_T, red_bean_T, green_beans_T, 
                                         sweet_potato_T, potato_T''',
                                 "M": '''rice_M, riceF_M, glutinous_rice_M, 
                                         bean_M, red_bean_M, green_beans_M, 
                                         sweet_potato_M, potato_M'''},

                   "Vegetables": {"T": '''chinese_cabbageF_T, chinese_cabbageW_T, chinese_cabbageS_T, chinese_cabbageH_T,
                                          cabbage_T, spinach_T, lettuceR_T, lettuceB_T, 
                                          korean_cabbage_T, leaf_mustard_T, watermelon_T, korean_melon_T, 
                                          cucumberS_T, cucumberD_T, cucumberW_T, 
                                          squash_T, zucchini_T, tomato_T, strawberry_T, 
                                          radishF_T, radishW_T, radishS_T, radishH_T, 
                                          carrot_T, yeol_radish_T, 
                                          dried_red_pepperD_T, dried_red_pepperS_T, 
                                          pepper_T, chilli_pepper_T, cheongyang_pepper_T, red_pepper_T, 
                                          onion_T, green_onion_T, chives_T, ginger_T, chili_powder_T, 
                                          parsley_T, sesame_leaf_T, pimento_T, paprika_T, 
                                          melon_T, garlic_T, cherry_tomato_T, jujube_cherry_tomato_T''',
                                  "M": '''chinese_cabbageF_M, chinese_cabbageW_M, chinese_cabbageS_M, chinese_cabbageH_M, 
                                          cabbage_M, spinach_M, lettuceR_M, lettuceB_M, 
                                          korean_cabbage_M, leaf_mustard_M, watermelon_M, korean_melon_M, 
                                          cucumberS_M, cucumberD_M, cucumberW_M, 
                                          squash_M, zucchini_M, tomato_M, strawberry_M, 
                                          radishF_M, radishW_M, radishS_M, radishH_M, 
                                          carrot_M, yeol_radish_M, 
                                          dried_red_pepperD_M, dried_red_pepperS_M, 
                                          pepper_M, chilli_pepper_M, cheongyang_pepper_M, red_pepper_M, 
                                          onion_M, green_onion_M, chives_M, ginger_M, chili_powder_M, 
                                          parsley_M, sesame_leaf_M, pimento_M, paprika_M, 
                                          melon_M, garlic_M, cherry_tomato_M, jujube_cherry_tomato_M '''},

                   "Specialcrops": {"T": '''sesame_T, peanut_T, oyster_mushroom_T, oyster_mushroomA_T, 
                                            enoki_mushroom_T, king_oyster_mushroom_T, walnut_T, almond_T''',
                                    "M": '''sesame_M, peanut_M, oyster_mushroom_M, oyster_mushroomA_M, 
                                            enoki_mushroom_M, king_oyster_mushroom_M, walnut_M, almond_M'''},

                   "Fruit": {"T": '''appleF_T, appleT_T, appleR_T, pearS_T, pearW_T, 
                                     peach_T, grapeC_T, grapeG_T, grapeM_T, grapeS_T, 
                                     grapeR_T, citrusR_T, citrusH_T, persimmon_T, banana_T, 
                                     kiwiN_T, kiwiK_T, pineapple_T, orangeU_T, orangeA_T,
                                     lemon_T, cherry_T, raisin_T, dried_blueberries_T, mango_T''',
                             "M": '''appleF_M, appleT_M, appleR_M, pearS_M, pearW_M, 
                                     peach_M, grapeC_M, grapeG_M, grapeM_M, grapeS_M, 
                                     grapeR_M, citrusR_M, citrusH_M, persimmon_M, banana_M, 
                                     kiwiN_M, kiwiK_M, pineapple_M, orangeU_M, orangeA_M, 
                                     lemon_M, cherry_M, raisin_M, dried_blueberries_M, mango_M'''}}
        try:
            ## DB 연결
            db = pymysql.Connect(host=DB_HOST,
                                 user=DB_USERNAME,  # db 계정
                                 password=DB_PASSWORD,  # db 비밀 번호
                                 database=DB_NAME)  # 접속 하고자 하는 db 명

            ## DB 작업
            with db:

                ## 초기 값
                Result = {}
                Table_List = []

                with db.cursor() as cur:

                    # 쿼리문
                    sql_retail_table = 'SHOW TABLES LIKE "%retail%";'
                    cur.execute(sql_retail_table)

                    for table in tqdm(cur.fetchall()):
                        AreaDict = {}
                        area = table[0].split('_')[0]

                        CateDict = {}
                        for category in KeyDict.keys():
                            CateDictTmp = {}

                            MarketDict = {}
                            for keys in KeyDict[category].keys():
                                MarketDictTmp = {}
                                sql_retail_Tdata = 'SELECT date, {} FROM {} ORDER BY date'
                                sql_retail_Tdata = sql_retail_Tdata.format(KeyDict[category][keys], table[0])
                                cur.execute(sql_retail_Tdata)

                                DataDict = {}
                                for data in cur.fetchall():
                                    DataDictTmp = {}
                                    date = data[0]
                                    df_date = datetime.strptime(str(date), '%Y%m%d')

                                    ## 전체는 1년 기준 // 소매는 14일 기준
                                    if table[0] == 'total_retail':
                                        required = (datetime.today() - timedelta(days=365))
                                    else:
                                        required = (datetime.today() - timedelta(days=14))

                                    date_diff = (required - df_date).days

                                    ## 기준일이 되는 날부터 계산
                                    if date_diff < 1:
                                        if category == 'Foodcrops':
                                            price = [data[1], data[3], data[4], data[5], data[6], data[7], data[8]]
                                            price = tuple(price)
                                            DataDictTmp[date] = price
                                            DataDict.update(DataDictTmp)

                                        elif category == 'Vegetables':
                                            chinese_cabbage_tuple = data[1: 5]
                                            radish_tuple = data[20: 24]
                                            try:
                                                chinese_cabbage = sum(data[1: 5]) / (
                                                        len(data[1: 5]) - data[1: 5].count(0))
                                            except:
                                                chinese_cabbage = 0
                                            try:
                                                radish = sum(data[20: 24]) / (len(data[20: 24]) - data[20: 24].count(0))
                                            except:
                                                radish = 0
                                            price = [chinese_cabbage, data[5], data[6], data[7], data[8],
                                                     data[9], data[10], data[11], data[12], data[13],
                                                     data[14], data[15], data[16], data[17], data[18],
                                                     data[19], radish, data[24], data[25], data[26],
                                                     data[27], data[28], data[29], data[30], data[31],
                                                     data[32], data[33], data[34], data[35], data[36],
                                                     data[37], data[38], data[39], data[40], data[41],
                                                     data[42], data[43]]
                                            price = tuple(price)
                                            DataDictTmp[date] = price
                                            DataDict.update(DataDictTmp)

                                        elif category == 'Specialcrops':
                                            price = [data[1], data[2], data[3], data[4], data[5], data[6], data[7],
                                                     data[8]]
                                            price = tuple(price)
                                            DataDictTmp[date] = price
                                            DataDict.update(DataDictTmp)

                                        else:
                                            try:
                                                apple = sum(data[1: 4]) / (len(data[1: 4]) - data[1: 4].count(0))
                                            except:
                                                apple = 0
                                            try:
                                                pear = sum(data[4: 6]) / (len(data[4: 6]) - data[4: 6].count(0))
                                            except:
                                                pear = 0
                                            try:
                                                grape = sum((data[7], data[11])) / (
                                                        len((data[7], data[11])) - (data[7], data[11]).count(0))
                                            except:
                                                grape = 0
                                            try:
                                                citrus = sum(data[12: 14]) / (len(data[12: 14]) - data[12: 14].count(0))
                                            except:
                                                citrus = 0
                                            try:
                                                kiwi = sum(data[16: 18]) / (len(data[16: 18]) - data[16: 18].count(0))
                                            except:
                                                kiwi = 0
                                            try:
                                                orange = sum(data[19: 21]) / (len(data[19: 21]) - data[19: 21].count(0))
                                            except:
                                                orange = 0
                                            price = [apple, pear, data[6], grape, data[8],
                                                     data[9], data[10], citrus, data[14], data[15],
                                                     kiwi, data[18], orange, data[21], data[22],
                                                     data[23], data[24], data[25]]
                                            price = tuple(price)
                                            DataDictTmp[date] = price
                                            DataDict.update(DataDictTmp)

                                    MarketDictTmp[keys] = DataDict
                                    MarketDict.update(MarketDictTmp)

                                CateDictTmp[category] = MarketDict
                                CateDict.update(CateDictTmp)

                            AreaDict[area] = CateDict
                            Result.update(AreaDict)
                    cur.close()
        except Exception as e:
            Result = traceback.format_exc()
        return Result


retail_dict = Retail_Dict(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME)
result_dict = retail_dict.Make_Retail_Dict()
print(result_dict)

'''
식량작물 : 
		rice            # 쌀
		glutinous_rice      # 찹쌀
		bean         # 콩
		red_bean     # 팥
		green_beans      # 녹두
		sweet_potato      # 고구마
		potato          # 감자

채소류 :
		chinese_cabbage      # 배추
		cabbage    # 양배추
		spinach      # 시금치
		lettuceR       # 상추(적)
		lettuceB_T       # 상추(청) 
		korean_cabbage    # 얼갈이배추
		leaf_mustard     # 갓
		watermelon      # 수박 
		korean_melon    # 참외
		cucumberS      # 오이(가시계통)
		cucumberD    # 오이(다다기계통)
		cucumberW      # 오이(취청) 
		squash        # 애호박 
		zucchini    # 주키니
		tomato         # 토마토 
		strawberry      # 딸기
		radish          # 무
		carrot       # 당근
		yeol_radish      # 열무
		dried_red_pepperD    # 건고추(화건)
		dried_red_pepperS    # 건고추(양건) 
		pepper         # 풋고추
		chilli_pepper     # 꽈리고추
		cheongyang_pepper  # 청양고추
		red_pepper   # 붉은고추 
		onion         # 양파
		green_onion     # 대파 
		chives          # 쪽파 
		ginger        # 생강
		chili_powder      # 고추가루
		parsley         # 미나리
		sesame_leaf       # 깻잎 
		pimento       # 피망 
		paprika         # 파프리카 
		melon        # 멜론 
		garlic       # 깐마늘 
		cherry_tomato      # 방울토마토 
		jujube_cherry_tomato    # 대추방울토마토 

특용작물:
	sesame          # 참깨 
	peanut          # 땅콩
	oyster_mushroom       # 느타리버섯
	oyster_mushroomA    # 애느타리버섯 
	enoki_mushroom      # 팽이버섯 
	king_oyster_mushroom  # 새송이버섯 
	walnut          # 호두 
	almond     # 아몬드 

과일류:
	apple          # 사과
	pear         # 배 
	peach         # 복숭아 
	grape          # 포도 
	grapeG         # 포도(거봉) 
	grapeM       # 포도(MBA;머루) 
	grapeS         # 포도(샤인머스켓) 
	citrus         # 감귤 
	persimmon       # 단감 
	banana          # 바나나 
	kiwi          # 참다래 
	pineapple       # 파인애플 
	orange         # 오렌지 
	lemon         # 레몬 
	cherry          # 체리 
	raisin         # 건포도 
	dried_blueberries      # 건블루베리 
	mango         # 망고 
'''
