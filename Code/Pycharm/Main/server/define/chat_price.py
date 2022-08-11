import traceback

import pymysql
from tqdm import tqdm


class Chatbot_Iprice:
    ### init 설정
    def __init__(self, DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME):
        self.DB_USERNAME = DB_USERNAME
        self.DB_HOST = DB_HOST
        self.DB_PASSWORD = DB_PASSWORD
        self.DB_NAME = DB_NAME

    def Price_Dict(self):
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
                    sql_retail_table = 'SELECT * FROM total_retail ORDER BY date DESC LIMIT 1;'
                    cur.execute(sql_retail_table)

                    for data in tqdm(cur.fetchall()):
                        # print(data)

                        try:
                            rice = sum(data[1: 5]) / (len(data[1: 5]) - data[1: 5].count(0))
                        except:
                            rice = 0
                        try:
                            glutinous_rice = sum(data[5: 7]) / (len(data[5: 7]) - data[5: 7].count(0))
                        except:
                            glutinous_rice = 0
                        try:
                            bean = sum(data[7: 9]) / (len(data[7: 9]) - data[7: 9].count(0))
                        except:
                            bean = 0
                        try:
                            red_bean = sum(data[9: 11]) / (len(data[9: 11]) - data[9: 11].count(0))
                        except:
                            red_bean = 0
                        try:
                            green_beans = sum(data[11: 13]) / (len(data[11: 13]) - data[11: 13].count(0))
                        except:
                            green_beans = 0
                        try:
                            sweet_potato_T = sum(data[13: 15]) / (len(data[13: 15]) - data[13: 15].count(0))
                        except:
                            sweet_potato_T = 0
                        try:
                            potato = sum(data[15: 17]) / (len(data[15: 17]) - data[15: 17].count(0))
                        except:
                            potato = 0
                        try:
                            chinese_cabbage = sum(data[17: 25]) / (len(data[17: 25]) - data[17: 25].count(0))
                        except:
                            chinese_cabbage = 0
                        try:
                            cabbage = sum(data[25: 27]) / (len(data[25: 27]) - data[25: 27].count(0))
                        except:
                            cabbage = 0
                        try:
                            spinach = sum(data[27: 29]) / (len(data[27: 29]) - data[27: 29].count(0))
                        except:
                            spinach = 0
                        try:
                            lettuceR = sum(data[29: 31]) / (len(data[29: 31]) - data[29: 31].count(0))
                        except:
                            lettuceR = 0
                        try:
                            lettuceB = sum(data[31: 33]) / (len(data[31: 33]) - data[31: 33].count(0))
                        except:
                            lettuceB = 0
                        try:
                            korean_cabbage = sum(data[33: 35]) / (len(data[33: 35]) - data[33: 35].count(0))
                        except:
                            korean_cabbage = 0
                        try:
                            leaf_mustard = sum(data[35: 37]) / (len(data[35: 37]) - data[35: 37].count(0))
                        except:
                            leaf_mustard = 0
                        try:
                            watermelon = sum(data[37: 39]) / (len(data[37: 39]) - data[37: 39].count(0))
                        except:
                            watermelon = 0
                        try:
                            korean_melon = sum(data[39: 41]) / (len(data[39: 41]) - data[39: 41].count(0))
                        except:
                            korean_melon = 0
                        try:
                            cucumber = sum(data[41: 47]) / (len(data[41: 47]) - data[41: 47].count(0))
                        except:
                            cucumber = 0
                        try:
                            squash = sum(data[47: 49]) / (len(data[47: 49]) - data[47: 49].count(0))
                        except:
                            squash = 0
                        try:
                            zucchini = sum(data[49: 51]) / (len(data[49: 51]) - data[49: 51].count(0))
                        except:
                            zucchini = 0
                        try:
                            tomato = sum(data[51: 53]) / (len(data[51: 53]) - data[51: 53].count(0))
                        except:
                            tomato = 0
                        try:
                            strawberry = sum(data[53: 55]) / (len(data[53: 55]) - data[53: 55].count(0))
                        except:
                            strawberry = 0
                        try:
                            radish = sum(data[55: 63]) / (len(data[55: 63]) - data[55: 63].count(0))
                        except:
                            radish = 0
                        try:
                            carrot = sum(data[63: 65]) / (len(data[63: 65]) - data[63: 65].count(0))
                        except:
                            carrot = 0
                        try:
                            yeol_radish = sum(data[65: 67]) / (len(data[65: 67]) - data[65: 67].count(0))
                        except:
                            yeol_radish = 0
                        try:
                            dried_red_pepper = sum(data[67: 71]) / (len(data[67: 71]) - data[67: 71].count(0))
                        except:
                            dried_red_pepper = 0
                        try:
                            pepper = sum(data[71: 73]) / (len(data[71: 73]) - data[71: 73].count(0))
                        except:
                            pepper = 0
                        try:
                            chilli_pepper = sum(data[73: 75]) / (len(data[73: 75]) - data[73: 75].count(0))
                        except:
                            chilli_pepper = 0
                        try:
                            cheongyang_pepper = sum(data[75: 77]) / (len(data[75: 77]) - data[75: 77].count(0))
                        except:
                            cheongyang_pepper = 0
                        try:
                            red_pepper = sum(data[77: 79]) / (len(data[77: 79]) - data[77: 79].count(0))
                        except:
                            red_pepper = 0
                        try:
                            onion = sum(data[79: 81]) / (len(data[79: 81]) - data[79: 81].count(0))
                        except:
                            onion = 0
                        try:
                            green_onion = sum(data[81: 83]) / (len(data[81: 83]) - data[81: 83].count(0))
                        except:
                            green_onion = 0
                        try:
                            chives = sum(data[83: 85]) / (len(data[83: 85]) - data[83: 85].count(0))
                        except:
                            chives = 0
                        try:
                            ginger = sum(data[85: 87]) / (len(data[85: 87]) - data[85: 87].count(0))
                        except:
                            ginger = 0
                        try:
                            chili_powder = sum(data[87: 89]) / (len(data[87: 89]) - data[87: 89].count(0))
                        except:
                            chili_powder = 0
                        try:
                            parsley = sum(data[89: 91]) / (len(data[89: 91]) - data[89: 91].count(0))
                        except:
                            parsley = 0
                        try:
                            sesame_leaf = sum(data[91: 93]) / (len(data[91: 93]) - data[91: 93].count(0))
                        except:
                            sesame_leaf = 0
                        try:
                            pimento = sum(data[93: 95]) / (len(data[93: 95]) - data[93: 95].count(0))
                        except:
                            pimento = 0
                        try:
                            paprika = sum(data[95: 97]) / (len(data[95: 97]) - data[95: 97].count(0))
                        except:
                            paprika = 0
                        try:
                            melon = sum(data[97: 99]) / (len(data[97: 99]) - data[97: 99].count(0))
                        except:
                            melon = 0
                        try:
                            garlic = sum(data[99: 101]) / (len(data[99: 101]) - data[99: 101].count(0))
                        except:
                            garlic = 0
                        try:
                            cherry_tomato = sum(data[101: 105]) / (len(data[101: 105]) - data[101: 105].count(0))
                        except:
                            cherry_tomato = 0
                        try:
                            sesame = sum(data[105: 107]) / (len(data[105: 107]) - data[105: 107].count(0))
                        except:
                            sesame = 0
                        try:
                            peanut = sum(data[107: 109]) / (len(data[107: 109]) - data[107: 109].count(0))
                        except:
                            peanut = 0
                        try:
                            oyster_mushroom = sum(data[109: 113]) / (len(data[109: 113]) - data[109: 113].count(0))
                        except:
                            oyster_mushroom = 0
                        try:
                            enoki_mushroom = sum(data[113: 115]) / (len(data[113: 115]) - data[113: 115].count(0))
                        except:
                            enoki_mushroom = 0
                        try:
                            king_oyster_mushroom = sum(data[115: 117]) / (len(data[115: 117]) - data[115: 117].count(0))
                        except:
                            king_oyster_mushroom = 0
                        try:
                            walnut = sum(data[117: 119]) / (len(data[117: 119]) - data[117: 119].count(0))
                        except:
                            walnut = 0
                        try:
                            almond = sum(data[119: 121]) / (len(data[119: 121]) - data[119: 121].count(0))
                        except:
                            almond = 0
                        try:
                            apple = sum(data[121: 127]) / (len(data[121: 127]) - data[121: 127].count(0))
                        except:
                            apple = 0
                        try:
                            pear = sum(data[127: 131]) / (len(data[127: 131]) - data[127: 131].count(0))
                        except:
                            pear = 0
                        try:
                            peach = sum(data[131: 133]) / (len(data[131: 133]) - data[131: 133].count(0))
                        except:
                            peach = 0
                        try:
                            grape = sum((data[133], data[134], data[141], data[142])) / (
                                    len((data[133], data[134], data[141], data[142])) - (
                                data[133], data[134], data[141], data[142]).count(0))
                        except:
                            grape = 0
                        try:
                            grapeG = sum(data[135: 137]) / (len(data[135: 137]) - data[135: 137].count(0))
                        except:
                            grapeG = 0
                        try:
                            grapeM = sum(data[137: 139]) / (len(data[137: 139]) - data[137: 139].count(0))
                        except:
                            grapeM = 0
                        try:
                            grapeS = sum(data[139: 141]) / (len(data[139: 141]) - data[139: 141].count(0))
                        except:
                            grapeS = 0
                        try:
                            citrus = sum(data[143: 147]) / (len(data[143: 147]) - data[143: 147].count(0))
                        except:
                            citrus = 0
                        try:
                            persimmon = sum(data[147: 149]) / (len(data[147: 149]) - data[147: 149].count(0))
                        except:
                            persimmon = 0
                        try:
                            banana = sum(data[149: 151]) / (len(data[149: 151]) - data[149: 151].count(0))
                        except:
                            banana = 0
                        try:
                            kiwi = sum(data[151: 155]) / (len(data[151: 155]) - data[151: 155].count(0))
                        except:
                            kiwi = 0
                        try:
                            pineapple = sum(data[155: 157]) / (len(data[155: 157]) - data[155: 157].count(0))
                        except:
                            pineapple = 0
                        try:
                            orange = sum(data[157: 161]) / (len(data[157: 161]) - data[157: 161].count(0))
                        except:
                            orange = 0
                        try:
                            lemon = sum(data[161: 163]) / (len(data[161: 163]) - data[161: 163].count(0))
                        except:
                            lemon = 0
                        try:
                            cherry = sum(data[163: 165]) / (len(data[163: 165]) - data[163: 165].count(0))
                        except:
                            cherry = 0
                        try:
                            raisin = sum(data[165: 167]) / (len(data[165: 167]) - data[165: 167].count(0))
                        except:
                            raisin = 0
                        try:
                            mackerel = sum(data[171: 177]) / (len(data[171: 177]) - data[171: 177].count(0))
                        except:
                            mackerel = 0
                        try:
                            saury = sum(data[177: 179]) / (len(data[177: 179]) - data[177: 179].count(0))
                        except:
                            saury = 0
                        try:
                            cutlassfish = sum(data[179: 183]) / (len(data[179: 183]) - data[179: 183].count(0))
                        except:
                            cutlassfish = 0
                        try:
                            pollock = sum(data[183: 185]) / (len(data[183: 185]) - data[183: 185].count(0))
                        except:
                            pollock = 0
                        try:
                            squid = sum(data[185: 189]) / (len(data[185: 189]) - data[185: 189].count(0))
                        except:
                            squid = 0
                        try:
                            dried_anchovies = sum(data[189: 191]) / (len(data[189: 191]) - data[189: 191].count(0))
                        except:
                            dried_anchovies = 0
                        try:
                            dried_squid = sum(data[191: 193]) / (len(data[191: 193]) - data[191: 193].count(0))
                        except:
                            dried_squid = 0
                        try:
                            seaweedD = sum(data[193: 195]) / (len(data[193: 195]) - data[193: 195].count(0))
                        except:
                            seaweedD = 0
                        try:
                            seaweedF = sum(data[195: 197]) / (len(data[195: 197]) - data[195: 197].count(0))
                        except:
                            seaweedF = 0
                        try:
                            dried_seaweed = sum(data[197: 199]) / (len(data[197: 199]) - data[197: 199].count(0))
                        except:
                            dried_seaweed = 0
                        try:
                            oyster = sum(data[199: 201]) / (len(data[199: 201]) - data[199: 201].count(0))
                        except:
                            oyster = 0
                        try:
                            yellow_corbina = sum(data[201: 203]) / (len(data[201: 203]) - data[201: 203].count(0))
                        except:
                            yellow_corbina = 0
                        try:
                            salted_shrimp = sum(data[203: 205]) / (len(data[203: 205]) - data[203: 205].count(0))
                        except:
                            salted_shrimp = 0
                        try:
                            anchovy_fih_sauce = sum(data[205: 207]) / (len(data[205: 207]) - data[205: 207].count(0))
                        except:
                            anchovy_fih_sauce = 0
                        try:
                            salt = sum(data[207: 209]) / (len(data[207: 209]) - data[207: 209].count(0))
                        except:
                            salt = 0
                        try:
                            abalone = sum(data[209: 211]) / (len(data[209: 211]) - data[209: 211].count(0))
                        except:
                            abalone = 0
                        try:
                            shrimp = sum(data[211: 213]) / (len(data[211: 213]) - data[211: 213].count(0))
                        except:
                            abalone = 0

                        Result['쌀'] = rice
                        Result['찹쌀'] = glutinous_rice
                        Result['콩'] = bean
                        Result['팥'] = red_bean
                        Result['녹두'] = green_beans
                        Result['고구마'] = sweet_potato_T
                        Result['감자'] = potato
                        Result['배추'] = chinese_cabbage
                        Result['양배추'] = cabbage
                        Result['시금치'] = spinach
                        Result['적상추'] = lettuceR
                        Result['청상추'] = lettuceB
                        Result['얼갈이배추'] = korean_cabbage
                        Result['갓'] = leaf_mustard
                        Result['수박'] = watermelon
                        Result['참외'] = korean_melon
                        Result['오이'] = cucumber
                        Result['애호박'] = squash
                        Result['주키니'] = zucchini
                        Result['토마토'] = tomato
                        Result['딸기'] = strawberry
                        Result['무'] = radish
                        Result['당근'] = carrot
                        Result['열무'] = yeol_radish
                        Result['건고추'] = dried_red_pepper
                        Result['풋고추'] = pepper
                        Result['꽈리고추'] = chilli_pepper
                        Result['청양고추'] = cheongyang_pepper
                        Result['붉은고추'] = red_pepper
                        Result['양파'] = onion
                        Result['대파'] = green_onion
                        Result['쪽파'] = chives
                        Result['생강'] = ginger
                        Result['고추가루'] = chili_powder
                        Result['미나리'] = parsley
                        Result['깻잎'] = sesame_leaf
                        Result['피망'] = pimento
                        Result['파프리카'] = paprika
                        Result['멜론'] = melon
                        Result['마늘'] = garlic
                        Result['방울토마토'] = cherry_tomato
                        Result['참깨'] = sesame
                        Result['땅콩'] = peanut
                        Result['느타리버섯'] = oyster_mushroom
                        Result['팽이버섯'] = enoki_mushroom
                        Result['새송이버섯'] = king_oyster_mushroom
                        Result['호두'] = walnut
                        Result['아몬드'] = almond
                        Result['사과'] = apple
                        Result['배'] = pear
                        Result['복숭아'] = peach
                        Result['포도'] = grape
                        Result['거봉'] = grapeG
                        Result['머루'] = grapeM
                        Result['샤인머스켓'] = grapeS
                        Result['감귤'] = citrus
                        Result['단감'] = persimmon
                        Result['바나나'] = banana
                        Result['키위'] = kiwi
                        Result['파인애플'] = pineapple
                        Result['오렌지'] = orange
                        Result['레몬'] = lemon
                        Result['체리'] = cherry
                        Result['건포도'] = raisin
                        Result['고등어'] = mackerel
                        Result['꽁치'] = saury
                        Result['갈치'] = cutlassfish
                        Result['명태'] = pollock
                        Result['오징어'] = squid
                        Result['멸치'] = dried_anchovies
                        Result['건오징어'] = dried_squid
                        Result['마른김'] = seaweedD
                        Result['구운김'] = seaweedF
                        Result['건미역'] = dried_seaweed
                        Result['굴'] = oyster
                        Result['조기'] = yellow_corbina
                        Result['새우젓'] = salted_shrimp
                        Result['멸치액젓'] = anchovy_fih_sauce
                        Result['소금'] = salt
                        Result['전복'] = abalone
                        Result['흰다리새우'] = shrimp

                    cur.close()

        except Exception as e:
            Result = traceback.format_exc()
        return Result


# retail_dict = Chatbot_Iprice(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME)
# result_dict = retail_dict.Price_Dict()
# print(result_dict)
