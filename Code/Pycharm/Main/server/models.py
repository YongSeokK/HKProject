from datetime import datetime

from server import db


## 회원 Data
class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    userid = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False)
    nickname = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False)
    userpw = db.Column(db.String(120, 'utf8mb4_unicode_ci'), nullable=False)
    name = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False)
    email = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False)
    phone = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False)
    grade = db.Column(db.Integer(), nullable=False)
    start = db.Column(db.DateTime, default=datetime.utcnow())


## 만개의 레시피
class Food_recipe(db.Model):
    no = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)  # 갯수 카운트
    serial = db.Column(db.Integer, nullable=False)  # 일련번호
    dish = db.Column(db.String(50, 'utf8mb4_unicode_ci'), nullable=False)  # 요리명
    registrant = db.Column(db.String(50, 'utf8mb4_unicode_ci'), nullable=False)  # 등록자
    views = db.Column(db.Integer, nullable=False)  # 조회수
    likes = db.Column(db.Integer, nullable=False)  # 추천수
    situation = db.Column(db.String(10, 'utf8mb4_unicode_ci'), nullable=False)  # 요리상황
    intro = db.Column(db.String(2000, 'utf8mb4_unicode_ci'), nullable=False)  # 요리소개
    total_ingredients = db.Column(db.String(1000, 'utf8mb4_unicode_ci'), nullable=False)  # 전체요리재료
    servings = db.Column(db.String(10, 'utf8mb4_unicode_ci'), nullable=False)  # 요리인분
    level = db.Column(db.String(10, 'utf8mb4_unicode_ci'), nullable=False)  # 난이도
    time = db.Column(db.String(10, 'utf8mb4_unicode_ci'), nullable=False)  # 시간
    url = db.Column(db.String(1000, 'utf8mb4_unicode_ci'), nullable=False)  # URL
    ingredients = db.Column(db.String(1000, 'utf8mb4_unicode_ci'), nullable=False)  # 요리재료(_ 로 구분)


## 전체 도매(거래량)
class Wholesale_quantity(db.Model):
    date = db.Column(db.Integer, primary_key=True, nullable=False)  # 일자
    beans = db.Column(db.Float, nullable=False)  # 콩
    sweet_potato = db.Column(db.Float, nullable=False)  # 고구마
    potato = db.Column(db.Float, nullable=False)  # 감자
    napa_cabbage = db.Column(db.Float, nullable=False)  # 배추
    cabbage = db.Column(db.Float, nullable=False)  # 양배추
    spinach = db.Column(db.Float, nullable=False)  # 시금치
    lettuce = db.Column(db.Float, nullable=False)  # 상추
    winter_cabbage = db.Column(db.Float, nullable=False)  # 얼갈이 배추
    watermelon = db.Column(db.Float, nullable=False)  # 수박
    korean_melon = db.Column(db.Float, nullable=False)  # 참외
    cucumber = db.Column(db.Float, nullable=False)  # 오이
    pumpkin = db.Column(db.Float, nullable=False)  # 호박
    tomato = db.Column(db.Float, nullable=False)  # 토마토
    strawberry = db.Column(db.Float, nullable=False)  # 딸기
    radish = db.Column(db.Float, nullable=False)  # 무
    carrot = db.Column(db.Float, nullable=False)  # 당근
    yeol_radish = db.Column(db.Float, nullable=False)  # 열무
    dried_red_pepper = db.Column(db.Float, nullable=False)  # 건고추
    pepper = db.Column(db.Float, nullable=False)  # 고추
    onion = db.Column(db.Float, nullable=False)  # 양파
    green_onion = db.Column(db.Float, nullable=False)  # 대파
    chives = db.Column(db.Float, nullable=False)  # 쪽파
    ginger = db.Column(db.Float, nullable=False)  # 생강
    parsley = db.Column(db.Float, nullable=False)  # 미나리
    sesame_leaf = db.Column(db.Float, nullable=False)  # 깻잎
    pimento = db.Column(db.Float, nullable=False)  # 피망
    paprika = db.Column(db.Float, nullable=False)  # 파프리카
    cherry_tomato = db.Column(db.Float, nullable=False)  # 방울토마토
    sesame = db.Column(db.Float, nullable=False)  # 참깨
    peanut = db.Column(db.Float, nullable=False)  # 땅콩
    oyster_mushroom = db.Column(db.Float, nullable=False)  # 느타리버섯
    king_oyster_mushroom = db.Column(db.Float, nullable=False)  # 새송이 버섯
    enoki_mushrooms = db.Column(db.Float, nullable=False)  # 팽이버섯
    walnut = db.Column(db.Float, nullable=False)  # 호두
    apple = db.Column(db.Float, nullable=False)  # 사과
    pear = db.Column(db.Float, nullable=False)  # 배
    peach = db.Column(db.Float, nullable=False)  # 복숭아
    grape = db.Column(db.Float, nullable=False)  # 포도
    citrus = db.Column(db.Float, nullable=False)  # 감귤
    persimmon = db.Column(db.Float, nullable=False)  # 단감
    banana = db.Column(db.Float, nullable=False)  # 바나나
    kiwi = db.Column(db.Float, nullable=False)  # 키위
    pineapple = db.Column(db.Float, nullable=False)  # 파인애플
    orange = db.Column(db.Float, nullable=False)  # 오렌지
    lemon = db.Column(db.Float, nullable=False)  # 레몬
    cherry = db.Column(db.Float, nullable=False)  # 체리
    mango = db.Column(db.Float, nullable=False)  # 망고


## 전체 도매(가격)
class Wholesale_price(db.Model):
    date = db.Column(db.Integer, primary_key=True, nullable=False)  # 일자
    beans = db.Column(db.Float, nullable=False)  # 콩
    sweet_potato = db.Column(db.Float, nullable=False)  # 고구마
    potato = db.Column(db.Float, nullable=False)  # 감자
    napa_cabbage = db.Column(db.Float, nullable=False)  # 배추
    cabbage = db.Column(db.Float, nullable=False)  # 양배추
    spinach = db.Column(db.Float, nullable=False)  # 시금치
    lettuce = db.Column(db.Float, nullable=False)  # 상추
    winter_cabbage = db.Column(db.Float, nullable=False)  # 얼갈이 배추
    watermelon = db.Column(db.Float, nullable=False)  # 수박
    korean_melon = db.Column(db.Float, nullable=False)  # 참외
    cucumber = db.Column(db.Float, nullable=False)  # 오이
    pumpkin = db.Column(db.Float, nullable=False)  # 호박
    tomato = db.Column(db.Float, nullable=False)  # 토마토
    strawberry = db.Column(db.Float, nullable=False)  # 딸기
    radish = db.Column(db.Float, nullable=False)  # 무
    carrot = db.Column(db.Float, nullable=False)  # 당근
    yeol_radish = db.Column(db.Float, nullable=False)  # 열무
    dried_red_pepper = db.Column(db.Float, nullable=False)  # 건고추
    pepper = db.Column(db.Float, nullable=False)  # 고추
    onion = db.Column(db.Float, nullable=False)  # 양파
    green_onion = db.Column(db.Float, nullable=False)  # 대파
    chives = db.Column(db.Float, nullable=False)  # 쪽파
    ginger = db.Column(db.Float, nullable=False)  # 생강
    parsley = db.Column(db.Float, nullable=False)  # 미나리
    sesame_leaf = db.Column(db.Float, nullable=False)  # 깻잎
    pimento = db.Column(db.Float, nullable=False)  # 피망
    paprika = db.Column(db.Float, nullable=False)  # 파프리카
    cherry_tomato = db.Column(db.Float, nullable=False)  # 방울토마토
    sesame = db.Column(db.Float, nullable=False)  # 참깨
    peanut = db.Column(db.Float, nullable=False)  # 땅콩
    oyster_mushroom = db.Column(db.Float, nullable=False)  # 느타리버섯
    king_oyster_mushroom = db.Column(db.Float, nullable=False)  # 새송이 버섯
    enoki_mushrooms = db.Column(db.Float, nullable=False)  # 팽이버섯
    walnut = db.Column(db.Float, nullable=False)  # 호두
    apple = db.Column(db.Float, nullable=False)  # 사과
    pear = db.Column(db.Float, nullable=False)  # 배
    peach = db.Column(db.Float, nullable=False)  # 복숭아
    grape = db.Column(db.Float, nullable=False)  # 포도
    citrus = db.Column(db.Float, nullable=False)  # 감귤
    persimmon = db.Column(db.Float, nullable=False)  # 단감
    banana = db.Column(db.Float, nullable=False)  # 바나나
    kiwi = db.Column(db.Float, nullable=False)  # 키위
    pineapple = db.Column(db.Float, nullable=False)  # 파인애플
    orange = db.Column(db.Float, nullable=False)  # 오렌지
    lemon = db.Column(db.Float, nullable=False)  # 레몬
    cherry = db.Column(db.Float, nullable=False)  # 체리
    mango = db.Column(db.Float, nullable=False)  # 망고


## 전체 소매
class Total_retail(db.Model):
    date = db.Column(db.Integer, primary_key=True, nullable=False)  # 일자

    # 식량작물
    rice_T = db.Column(db.Float, nullable=False)  # 쌀 시장
    rice_M = db.Column(db.Float, nullable=False)  # 쌀 대형마트
    riceF_T = db.Column(db.Float, nullable=False)  # 햇쌀 시장
    riceF_M = db.Column(db.Float, nullable=False)  # 햇쌀 대형마트
    glutinous_rice_T = db.Column(db.Float, nullable=False)  # 찹쌀 시장
    glutinous_rice_M = db.Column(db.Float, nullable=False)  # 찹쌀 대형마트
    bean_T = db.Column(db.Float, nullable=False)  # 콩 시장
    bean_M = db.Column(db.Float, nullable=False)  # 콩 대형마트
    red_bean_T = db.Column(db.Float, nullable=False)  # 팥 시장
    red_bean_M = db.Column(db.Float, nullable=False)  # 팥 대형마트
    green_beans_T = db.Column(db.Float, nullable=False)  # 녹두 시장
    green_beans_M = db.Column(db.Float, nullable=False)  # 녹두 대형마트
    sweet_potato_T = db.Column(db.Float, nullable=False)  # 고구마 시장
    sweet_potato_M = db.Column(db.Float, nullable=False)  # 고구마 대형마트
    potato_T = db.Column(db.Float, nullable=False)  # 감자 시장
    potato_M = db.Column(db.Float, nullable=False)  # 감자 대형마트

    # 채소류
    napa_cabbageF_T = db.Column(db.Float, nullable=False)  # 배추(가을) 시장
    napa_cabbageF_M = db.Column(db.Float, nullable=False)  # 배추(가을) 대형마트
    napa_cabbageW_T = db.Column(db.Float, nullable=False)  # 배추(월동) 시장
    napa_cabbageW_M = db.Column(db.Float, nullable=False)  # 배추(월동) 대형마트
    napa_cabbageS_T = db.Column(db.Float, nullable=False)  # 배추(봄) 시장
    napa_cabbageS_M = db.Column(db.Float, nullable=False)  # 배추(봄) 대형마트
    napa_cabbageH_T = db.Column(db.Float, nullable=False)  # 배추(고랭지) 시장
    napa_cabbageH_M = db.Column(db.Float, nullable=False)  # 배추(고랭지) 대형마트
    cabbage_T = db.Column(db.Float, nullable=False)  # 양배추 시장
    cabbage_M = db.Column(db.Float, nullable=False)  # 양배추 대형마트
    spinach_T = db.Column(db.Float, nullable=False)  # 시금치 시장
    spinach_M = db.Column(db.Float, nullable=False)  # 시금치 대형마트
    lettuceR_T = db.Column(db.Float, nullable=False)  # 상추(적) 시장
    lettuceR_M = db.Column(db.Float, nullable=False)  # 상추(적) 대형마트
    lettuceB_T = db.Column(db.Float, nullable=False)  # 상추(청) 시장
    lettuceB_M = db.Column(db.Float, nullable=False)  # 상추(청) 대형마트
    winter_cabbage_T = db.Column(db.Float, nullable=False)  # 얼갈이배추 시장
    winter_cabbage_M = db.Column(db.Float, nullable=False)  # 얼갈이배추 대형마트
    leaf_mustard_T = db.Column(db.Float, nullable=False)  # 갓 시장
    leaf_mustard_M = db.Column(db.Float, nullable=False)  # 갓 대형마트
    watermelon_T = db.Column(db.Float, nullable=False)  # 수박 시장
    watermelon_M = db.Column(db.Float, nullable=False)  # 수박 대형마트
    korean_melon_T = db.Column(db.Float, nullable=False)  # 참외 시장
    korean_melon_M = db.Column(db.Float, nullable=False)  # 참외 대형마트
    cucumberS_T = db.Column(db.Float, nullable=False)  # 오이(가시계통) 시장
    cucumberS_M = db.Column(db.Float, nullable=False)  # 오이(가시계통) 대형마트
    cucumberD_T = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 시장
    cucumberD_M = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 대형마트
    cucumberW_T = db.Column(db.Float, nullable=False)  # 오이(취청) 시장
    cucumberW_M = db.Column(db.Float, nullable=False)  # 오이(취청) 대형마트
    squash_T = db.Column(db.Float, nullable=False)  # 애호박 시장
    squash_M = db.Column(db.Float, nullable=False)  # 애호박 대형마트
    zucchini_T = db.Column(db.Float, nullable=False)  # 주키니 시장
    zucchini_M = db.Column(db.Float, nullable=False)  # 주키니 대형마트
    tomato_T = db.Column(db.Float, nullable=False)  # 토마토 시장
    tomato_M = db.Column(db.Float, nullable=False)  # 토마토 대형마트
    strawberry_T = db.Column(db.Float, nullable=False)  # 딸기 시장
    strawberry_M = db.Column(db.Float, nullable=False)  # 딸기 대형마트
    radishF_T = db.Column(db.Float, nullable=False)  # 무(가을) 시장
    radishF_M = db.Column(db.Float, nullable=False)  # 무(가을) 대형마트
    radishW_T = db.Column(db.Float, nullable=False)  # 무(월동) 시장
    radishW_M = db.Column(db.Float, nullable=False)  # 무(월동) 대형마트
    radishS_T = db.Column(db.Float, nullable=False)  # 무(봄) 시장
    radishS_M = db.Column(db.Float, nullable=False)  # 무(봄) 대형마트
    radishH_T = db.Column(db.Float, nullable=False)  # 무(고랭지) 시장
    radishH_M = db.Column(db.Float, nullable=False)  # 무(고랭지) 대형마트
    carrot_T = db.Column(db.Float, nullable=False)  # 당근 시장
    carrot_M = db.Column(db.Float, nullable=False)  # 당근 대형마트
    yeol_radish_T = db.Column(db.Float, nullable=False)  # 열무 시장
    yeol_radish_M = db.Column(db.Float, nullable=False)  # 열무 대형마트
    dried_red_pepperD_T = db.Column(db.Float, nullable=False)  # 건고추(화건) 시장
    dried_red_pepperD_M = db.Column(db.Float, nullable=False)  # 건고추(화건) 대형마트
    dried_red_pepperS_T = db.Column(db.Float, nullable=False)  # 건고추(양건) 시장
    dried_red_pepperS_M = db.Column(db.Float, nullable=False)  # 건고추(양양건) 대형마트
    pepper_T = db.Column(db.Float, nullable=False)  # 풋고추 시장
    pepper_M = db.Column(db.Float, nullable=False)  # 풋고추 대형마트
    chilli_pepper_T = db.Column(db.Float, nullable=False)  # 꽈리고추 시장
    chilli_pepper_M = db.Column(db.Float, nullable=False)  # 꽈리고추 대형마트
    cheongyang_pepper_T = db.Column(db.Float, nullable=False)  # 청양고추 시장
    cheongyang_pepper_M = db.Column(db.Float, nullable=False)  # 청양고추 대형마트
    red_pepper_T = db.Column(db.Float, nullable=False)  # 붉은고추 시장
    red_pepper_M = db.Column(db.Float, nullable=False)  # 붉은고추 대형마트
    onion_T = db.Column(db.Float, nullable=False)  # 양파 시장
    onion_M = db.Column(db.Float, nullable=False)  # 양파 대형마트
    green_onion_T = db.Column(db.Float, nullable=False)  # 대파 시장
    green_onion_M = db.Column(db.Float, nullable=False)  # 대파 대형마트
    chives_T = db.Column(db.Float, nullable=False)  # 쪽파 시장
    chives_M = db.Column(db.Float, nullable=False)  # 쪽파 대형마트
    ginger_T = db.Column(db.Float, nullable=False)  # 생강 시장
    ginger_M = db.Column(db.Float, nullable=False)  # 생강 대형마트
    chili_powder_T = db.Column(db.Float, nullable=False)  # 고추가루 시장
    chili_powder_M = db.Column(db.Float, nullable=False)  # 고추가루 대형마트
    parsley_T = db.Column(db.Float, nullable=False)  # 미나리 시장
    parsley_M = db.Column(db.Float, nullable=False)  # 미나리 대형마트
    sesame_leaf_T = db.Column(db.Float, nullable=False)  # 깻잎 시장
    sesame_leaf_M = db.Column(db.Float, nullable=False)  # 깻잎 대형마트
    pimento_T = db.Column(db.Float, nullable=False)  # 피망 시장
    pimento_M = db.Column(db.Float, nullable=False)  # 피망 대형마트
    paprika_T = db.Column(db.Float, nullable=False)  # 파프리카 시장
    paprika_M = db.Column(db.Float, nullable=False)  # 파프리카 대형마트
    melon_T = db.Column(db.Float, nullable=False)  # 멜론 시장
    melon_M = db.Column(db.Float, nullable=False)  # 멜론 대형마트
    garlic_T = db.Column(db.Float, nullable=False)  # 깐마늘 시장
    garlic_M = db.Column(db.Float, nullable=False)  # 깐마늘 대형마트
    cherry_tomato_T = db.Column(db.Float, nullable=False)  # 방울토마토 시장
    cherry_tomato_M = db.Column(db.Float, nullable=False)  # 방울토마토 대형마트
    jujube_cherry_tomato_T = db.Column(db.Float, nullable=False)  # 대추방울토마토 시장
    jujube_cherry_tomato_M = db.Column(db.Float, nullable=False)  # 대추방울토마토 대형마트

    # 특용작물
    sesame_T = db.Column(db.Float, nullable=False)  # 참깨 시장
    sesame_M = db.Column(db.Float, nullable=False)  # 참깨 대형마트
    peanut_T = db.Column(db.Float, nullable=False)  # 땅콩 시장
    peanut_M = db.Column(db.Float, nullable=False)  # 땅콩 대형마트
    oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 느타리버섯 시장
    oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 느타리버섯 대형마트
    oyster_mushroomA_T = db.Column(db.Float, nullable=False)  # 애느타리버섯 시장
    oyster_mushroomA_M = db.Column(db.Float, nullable=False)  # 애느타리버섯 대형마트
    enoki_mushroom_T = db.Column(db.Float, nullable=False)  # 팽이버섯 시장
    enoki_mushroom_M = db.Column(db.Float, nullable=False)  # 팽이버섯 대형마트
    king_oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 새송이버섯 시장
    king_oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 새송이버섯 대형마트
    walnut_T = db.Column(db.Float, nullable=False)  # 호두 시장
    walnut_M = db.Column(db.Float, nullable=False)  # 호두 대형마트
    almond_T = db.Column(db.Float, nullable=False)  # 아몬드 시장
    almond_M = db.Column(db.Float, nullable=False)  # 아몬드 대형마트

    # 과일류
    appleF_T = db.Column(db.Float, nullable=False)  # 사과(후지) 시장
    appleF_M = db.Column(db.Float, nullable=False)  # 사과(후지) 대형마트
    appleT_T = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 시장
    appleT_M = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 대형마트
    appleR_T = db.Column(db.Float, nullable=False)  # 사과(홍로) 시장
    appleR_M = db.Column(db.Float, nullable=False)  # 사과(홍로) 대마트
    pearS_T = db.Column(db.Float, nullable=False)  # 배(신고) 시장
    pearS_M = db.Column(db.Float, nullable=False)  # 배(신고) 대형마트
    pearW_T = db.Column(db.Float, nullable=False)  # 배(원황) 시장
    pearW_M = db.Column(db.Float, nullable=False)  # 배(원황) 대형마트
    peach_T = db.Column(db.Float, nullable=False)  # 복숭아 시장
    peach_M = db.Column(db.Float, nullable=False)  # 복숭아 대형마트
    grapeC_T = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 시장
    grapeC_M = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 대형마트
    grapeG_T = db.Column(db.Float, nullable=False)  # 포도(거봉) 시장
    grapeG_M = db.Column(db.Float, nullable=False)  # 포도(거봉) 대형마트
    grapeM_T = db.Column(db.Float, nullable=False)  # 포도(MBA) 시장
    grapeM_M = db.Column(db.Float, nullable=False)  # 포도(MBA) 대형마트
    grapeS_T = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 시장
    grapeS_M = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 대형마트
    grapeR_T = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 시장
    grapeR_M = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 대형마트
    citrusR_T = db.Column(db.Float, nullable=False)  # 감귤(노지) 시장
    citrusR_M = db.Column(db.Float, nullable=False)  # 감귤(노지) 대형마트
    citrusH_T = db.Column(db.Float, nullable=False)  # 감귤(시설) 시장
    citrusH_M = db.Column(db.Float, nullable=False)  # 감귤(시설) 대형마트
    persimmon_T = db.Column(db.Float, nullable=False)  # 단감 시장
    persimmon_M = db.Column(db.Float, nullable=False)  # 단감 대형마트
    banana_T = db.Column(db.Float, nullable=False)  # 바나나 시장
    banana_M = db.Column(db.Float, nullable=False)  # 바나나 대형마트
    kiwiN_T = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 시장
    kiwiN_M = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 대형마트
    kiwiK_T = db.Column(db.Float, nullable=False)  # 참다래(국산) 시장
    kiwiK_M = db.Column(db.Float, nullable=False)  # 참다래(국산) 대형마트
    pineapple_T = db.Column(db.Float, nullable=False)  # 파인애플 시장
    pineapple_M = db.Column(db.Float, nullable=False)  # 파인애플 대형마트
    orangeU_T = db.Column(db.Float, nullable=False)  # 오렌지(미국) 시장
    orangeU_M = db.Column(db.Float, nullable=False)  # 오렌지(미국) 대형마트
    orangeA_T = db.Column(db.Float, nullable=False)  # 오렌지(호주) 시장
    orangeA_M = db.Column(db.Float, nullable=False)  # 오렌지(호주) 대형마트
    lemon_T = db.Column(db.Float, nullable=False)  # 레몬 시장
    lemon_M = db.Column(db.Float, nullable=False)  # 레몬 대형마트
    cherry_T = db.Column(db.Float, nullable=False)  # 체리 시장
    cherry_M = db.Column(db.Float, nullable=False)  # 체리 대형마트
    raisin_T = db.Column(db.Float, nullable=False)  # 건포도 시장
    raisin_M = db.Column(db.Float, nullable=False)  # 건포도 대형마트
    dried_blueberries_T = db.Column(db.Float, nullable=False)  # 건블루베리 시장
    dried_blueberries_M = db.Column(db.Float, nullable=False)  # 건블루베리 대형마트
    mango_T = db.Column(db.Float, nullable=False)  # 망고 시장
    mango_M = db.Column(db.Float, nullable=False)  # 망고 대형마트

    # 수산물
    mackerelL_T = db.Column(db.Float, nullable=False)  # 고등어(생물) 시장
    mackerelL_M = db.Column(db.Float, nullable=False)  # 고등어(생물) 대형마트
    mackerelF_T = db.Column(db.Float, nullable=False)  # 고등어(냉동) 시장
    mackerelF_M = db.Column(db.Float, nullable=False)  # 고등어(냉동) 대형마트
    mackerelS_T = db.Column(db.Float, nullable=False)  # 고등어(염장) 시장
    mackerelS_M = db.Column(db.Float, nullable=False)  # 고등어(염장) 대형마트
    saury_T = db.Column(db.Float, nullable=False)  # 꽁치 시장
    saury_M = db.Column(db.Float, nullable=False)  # 꽁치 대형마트
    cutlassfishL_T = db.Column(db.Float, nullable=False)  # 갈치(생물) 시장
    cutlassfishL_M = db.Column(db.Float, nullable=False)  # 갈치(생물) 대형마트
    cutlassfishF_T = db.Column(db.Float, nullable=False)  # 갈치(냉동) 시장
    cutlassfishF_M = db.Column(db.Float, nullable=False)  # 갈치(냉동) 대형마트
    pollock_T = db.Column(db.Float, nullable=False)  # 명태 시장
    pollock_M = db.Column(db.Float, nullable=False)  # 명태 대형마트
    squidL_T = db.Column(db.Float, nullable=False)  # 물오징어(생선) 시장
    squidL_M = db.Column(db.Float, nullable=False)  # 물오징어(생선) 대형마트
    squidF_T = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 시장
    squidF_M = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 대형마트
    dried_anchovies_T = db.Column(db.Float, nullable=False)  # 건멸치 시장
    dried_anchovies_M = db.Column(db.Float, nullable=False)  # 건멸치 대형마트
    dried_squid_T = db.Column(db.Float, nullable=False)  # 건오징어 시장
    dried_squid_M = db.Column(db.Float, nullable=False)  # 건오징어 대형마트
    seaweedD_T = db.Column(db.Float, nullable=False)  # 김(마른김) 시장
    seaweedD_M = db.Column(db.Float, nullable=False)  # 김(마른김) 대형마트
    seaweedF_T = db.Column(db.Float, nullable=False)  # 김(구운김) 시장
    seaweedF_M = db.Column(db.Float, nullable=False)  # 김(구운김) 대형마트
    dried_seaweed_T = db.Column(db.Float, nullable=False)  # 건미역 시장
    dried_seaweed_M = db.Column(db.Float, nullable=False)  # 건미역 대형마트
    oyster_T = db.Column(db.Float, nullable=False)  # 굴 시장
    oyster_M = db.Column(db.Float, nullable=False)  # 굴 대형마트
    yellow_corbina_T = db.Column(db.Float, nullable=False)  # 수입조기 시장
    yellow_corbina_M = db.Column(db.Float, nullable=False)  # 수입조기 대형마트
    salted_shrimp_T = db.Column(db.Float, nullable=False)  # 새우젓 시장
    salted_shrimp_M = db.Column(db.Float, nullable=False)  # 새우젓 대형마트
    anchovy_fish_sauce_T = db.Column(db.Float, nullable=False)  # 멸치액젓 시장
    anchovy_fish_sauce_M = db.Column(db.Float, nullable=False)  # 멸치액젓 대형마트
    salt_T = db.Column(db.Float, nullable=False)  # 굵은소금 시장
    salt_M = db.Column(db.Float, nullable=False)  # 굵은소금 대형마트
    abalone_T = db.Column(db.Float, nullable=False)  # 전복 시장
    abalone_M = db.Column(db.Float, nullable=False)  # 전복 대형마트
    shrimp_T = db.Column(db.Float, nullable=False)  # 흰다리새우 시장
    shrimp_M = db.Column(db.Float, nullable=False)  # 흰다리새우 대형마트


## 서울 소매
class Seoul_retail(db.Model):
    date = db.Column(db.Integer, primary_key=True, nullable=False)  # 일자

    # 식량작물
    rice_T = db.Column(db.Float, nullable=False)  # 쌀 시장
    rice_M = db.Column(db.Float, nullable=False)  # 쌀 대형마트
    riceF_T = db.Column(db.Float, nullable=False)  # 햇쌀 시장
    riceF_M = db.Column(db.Float, nullable=False)  # 햇쌀 대형마트
    glutinous_rice_T = db.Column(db.Float, nullable=False)  # 찹쌀 시장
    glutinous_rice_M = db.Column(db.Float, nullable=False)  # 찹쌀 대형마트
    bean_T = db.Column(db.Float, nullable=False)  # 콩 시장
    bean_M = db.Column(db.Float, nullable=False)  # 콩 대형마트
    red_bean_T = db.Column(db.Float, nullable=False)  # 팥 시장
    red_bean_M = db.Column(db.Float, nullable=False)  # 팥 대형마트
    green_beans_T = db.Column(db.Float, nullable=False)  # 녹두 시장
    green_beans_M = db.Column(db.Float, nullable=False)  # 녹두 대형마트
    sweet_potato_T = db.Column(db.Float, nullable=False)  # 고구마 시장
    sweet_potato_M = db.Column(db.Float, nullable=False)  # 고구마 대형마트
    potato_T = db.Column(db.Float, nullable=False)  # 감자 시장
    potato_M = db.Column(db.Float, nullable=False)  # 감자 대형마트

    # 채소류
    napa_cabbageF_T = db.Column(db.Float, nullable=False)  # 배추(가을) 시장
    napa_cabbageF_M = db.Column(db.Float, nullable=False)  # 배추(가을) 대형마트
    napa_cabbageW_T = db.Column(db.Float, nullable=False)  # 배추(월동) 시장
    napa_cabbageW_M = db.Column(db.Float, nullable=False)  # 배추(월동) 대형마트
    napa_cabbageS_T = db.Column(db.Float, nullable=False)  # 배추(봄) 시장
    napa_cabbageS_M = db.Column(db.Float, nullable=False)  # 배추(봄) 대형마트
    napa_cabbageH_T = db.Column(db.Float, nullable=False)  # 배추(고랭지) 시장
    napa_cabbageH_M = db.Column(db.Float, nullable=False)  # 배추(고랭지) 대형마트
    cabbage_T = db.Column(db.Float, nullable=False)  # 양배추 시장
    cabbage_M = db.Column(db.Float, nullable=False)  # 양배추 대형마트
    spinach_T = db.Column(db.Float, nullable=False)  # 시금치 시장
    spinach_M = db.Column(db.Float, nullable=False)  # 시금치 대형마트
    lettuceR_T = db.Column(db.Float, nullable=False)  # 상추(적) 시장
    lettuceR_M = db.Column(db.Float, nullable=False)  # 상추(적) 대형마트
    lettuceB_T = db.Column(db.Float, nullable=False)  # 상추(청) 시장
    lettuceB_M = db.Column(db.Float, nullable=False)  # 상추(청) 대형마트
    winter_cabbage_T = db.Column(db.Float, nullable=False)  # 얼갈이배추 시장
    winter_cabbage_M = db.Column(db.Float, nullable=False)  # 얼갈이배추 대형마트
    leaf_mustard_T = db.Column(db.Float, nullable=False)  # 갓 시장
    leaf_mustard_M = db.Column(db.Float, nullable=False)  # 갓 대형마트
    watermelon_T = db.Column(db.Float, nullable=False)  # 수박 시장
    watermelon_M = db.Column(db.Float, nullable=False)  # 수박 대형마트
    korean_melon_T = db.Column(db.Float, nullable=False)  # 참외 시장
    korean_melon_M = db.Column(db.Float, nullable=False)  # 참외 대형마트
    cucumberS_T = db.Column(db.Float, nullable=False)  # 오이(가시계통) 시장
    cucumberS_M = db.Column(db.Float, nullable=False)  # 오이(가시계통) 대형마트
    cucumberD_T = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 시장
    cucumberD_M = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 대형마트
    cucumberW_T = db.Column(db.Float, nullable=False)  # 오이(취청) 시장
    cucumberW_M = db.Column(db.Float, nullable=False)  # 오이(취청) 대형마트
    squash_T = db.Column(db.Float, nullable=False)  # 애호박 시장
    squash_M = db.Column(db.Float, nullable=False)  # 애호박 대형마트
    zucchini_T = db.Column(db.Float, nullable=False)  # 주키니 시장
    zucchini_M = db.Column(db.Float, nullable=False)  # 주키니 대형마트
    tomato_T = db.Column(db.Float, nullable=False)  # 토마토 시장
    tomato_M = db.Column(db.Float, nullable=False)  # 토마토 대형마트
    strawberry_T = db.Column(db.Float, nullable=False)  # 딸기 시장
    strawberry_M = db.Column(db.Float, nullable=False)  # 딸기 대형마트
    radishF_T = db.Column(db.Float, nullable=False)  # 무(가을) 시장
    radishF_M = db.Column(db.Float, nullable=False)  # 무(가을) 대형마트
    radishW_T = db.Column(db.Float, nullable=False)  # 무(월동) 시장
    radishW_M = db.Column(db.Float, nullable=False)  # 무(월동) 대형마트
    radishS_T = db.Column(db.Float, nullable=False)  # 무(봄) 시장
    radishS_M = db.Column(db.Float, nullable=False)  # 무(봄) 대형마트
    radishH_T = db.Column(db.Float, nullable=False)  # 무(고랭지) 시장
    radishH_M = db.Column(db.Float, nullable=False)  # 무(고랭지) 대형마트
    carrot_T = db.Column(db.Float, nullable=False)  # 당근 시장
    carrot_M = db.Column(db.Float, nullable=False)  # 당근 대형마트
    yeol_radish_T = db.Column(db.Float, nullable=False)  # 열무 시장
    yeol_radish_M = db.Column(db.Float, nullable=False)  # 열무 대형마트
    dried_red_pepperD_T = db.Column(db.Float, nullable=False)  # 건고추(화건) 시장
    dried_red_pepperD_M = db.Column(db.Float, nullable=False)  # 건고추(화건) 대형마트
    dried_red_pepperS_T = db.Column(db.Float, nullable=False)  # 건고추(양건) 시장
    dried_red_pepperS_M = db.Column(db.Float, nullable=False)  # 건고추(양양건) 대형마트
    pepper_T = db.Column(db.Float, nullable=False)  # 풋고추 시장
    pepper_M = db.Column(db.Float, nullable=False)  # 풋고추 대형마트
    chilli_pepper_T = db.Column(db.Float, nullable=False)  # 꽈리고추 시장
    chilli_pepper_M = db.Column(db.Float, nullable=False)  # 꽈리고추 대형마트
    cheongyang_pepper_T = db.Column(db.Float, nullable=False)  # 청양고추 시장
    cheongyang_pepper_M = db.Column(db.Float, nullable=False)  # 청양고추 대형마트
    red_pepper_T = db.Column(db.Float, nullable=False)  # 붉은고추 시장
    red_pepper_M = db.Column(db.Float, nullable=False)  # 붉은고추 대형마트
    onion_T = db.Column(db.Float, nullable=False)  # 양파 시장
    onion_M = db.Column(db.Float, nullable=False)  # 양파 대형마트
    green_onion_T = db.Column(db.Float, nullable=False)  # 대파 시장
    green_onion_M = db.Column(db.Float, nullable=False)  # 대파 대형마트
    chives_T = db.Column(db.Float, nullable=False)  # 쪽파 시장
    chives_M = db.Column(db.Float, nullable=False)  # 쪽파 대형마트
    ginger_T = db.Column(db.Float, nullable=False)  # 생강 시장
    ginger_M = db.Column(db.Float, nullable=False)  # 생강 대형마트
    chili_powder_T = db.Column(db.Float, nullable=False)  # 고추가루 시장
    chili_powder_M = db.Column(db.Float, nullable=False)  # 고추가루 대형마트
    parsley_T = db.Column(db.Float, nullable=False)  # 미나리 시장
    parsley_M = db.Column(db.Float, nullable=False)  # 미나리 대형마트
    sesame_leaf_T = db.Column(db.Float, nullable=False)  # 깻잎 시장
    sesame_leaf_M = db.Column(db.Float, nullable=False)  # 깻잎 대형마트
    pimento_T = db.Column(db.Float, nullable=False)  # 피망 시장
    pimento_M = db.Column(db.Float, nullable=False)  # 피망 대형마트
    paprika_T = db.Column(db.Float, nullable=False)  # 파프리카 시장
    paprika_M = db.Column(db.Float, nullable=False)  # 파프리카 대형마트
    melon_T = db.Column(db.Float, nullable=False)  # 멜론 시장
    melon_M = db.Column(db.Float, nullable=False)  # 멜론 대형마트
    garlic_T = db.Column(db.Float, nullable=False)  # 깐마늘 시장
    garlic_M = db.Column(db.Float, nullable=False)  # 깐마늘 대형마트
    cherry_tomato_T = db.Column(db.Float, nullable=False)  # 방울토마토 시장
    cherry_tomato_M = db.Column(db.Float, nullable=False)  # 방울토마토 대형마트
    jujube_cherry_tomato_T = db.Column(db.Float, nullable=False)  # 대추방울토마토 시장
    jujube_cherry_tomato_M = db.Column(db.Float, nullable=False)  # 대추방울토마토 대형마트

    # 특용작물
    sesame_T = db.Column(db.Float, nullable=False)  # 참깨 시장
    sesame_M = db.Column(db.Float, nullable=False)  # 참깨 대형마트
    peanut_T = db.Column(db.Float, nullable=False)  # 땅콩 시장
    peanut_M = db.Column(db.Float, nullable=False)  # 땅콩 대형마트
    oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 느타리버섯 시장
    oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 느타리버섯 대형마트
    oyster_mushroomA_T = db.Column(db.Float, nullable=False)  # 애느타리버섯 시장
    oyster_mushroomA_M = db.Column(db.Float, nullable=False)  # 애느타리버섯 대형마트
    enoki_mushroom_T = db.Column(db.Float, nullable=False)  # 팽이버섯 시장
    enoki_mushroom_M = db.Column(db.Float, nullable=False)  # 팽이버섯 대형마트
    king_oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 새송이버섯 시장
    king_oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 새송이버섯 대형마트
    walnut_T = db.Column(db.Float, nullable=False)  # 호두 시장
    walnut_M = db.Column(db.Float, nullable=False)  # 호두 대형마트
    almond_T = db.Column(db.Float, nullable=False)  # 아몬드 시장
    almond_M = db.Column(db.Float, nullable=False)  # 아몬드 대형마트

    # 과일류
    appleF_T = db.Column(db.Float, nullable=False)  # 사과(후지) 시장
    appleF_M = db.Column(db.Float, nullable=False)  # 사과(후지) 대형마트
    appleT_T = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 시장
    appleT_M = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 대형마트
    appleR_T = db.Column(db.Float, nullable=False)  # 사과(홍로) 시장
    appleR_M = db.Column(db.Float, nullable=False)  # 사과(홍로) 대마트
    pearS_T = db.Column(db.Float, nullable=False)  # 배(신고) 시장
    pearS_M = db.Column(db.Float, nullable=False)  # 배(신고) 대형마트
    pearW_T = db.Column(db.Float, nullable=False)  # 배(원황) 시장
    pearW_M = db.Column(db.Float, nullable=False)  # 배(원황) 대형마트
    peach_T = db.Column(db.Float, nullable=False)  # 복숭아 시장
    peach_M = db.Column(db.Float, nullable=False)  # 복숭아 대형마트
    grapeC_T = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 시장
    grapeC_M = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 대형마트
    grapeG_T = db.Column(db.Float, nullable=False)  # 포도(거봉) 시장
    grapeG_M = db.Column(db.Float, nullable=False)  # 포도(거봉) 대형마트
    grapeM_T = db.Column(db.Float, nullable=False)  # 포도(MBA) 시장
    grapeM_M = db.Column(db.Float, nullable=False)  # 포도(MBA) 대형마트
    grapeS_T = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 시장
    grapeS_M = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 대형마트
    grapeR_T = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 시장
    grapeR_M = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 대형마트
    citrusR_T = db.Column(db.Float, nullable=False)  # 감귤(노지) 시장
    citrusR_M = db.Column(db.Float, nullable=False)  # 감귤(노지) 대형마트
    citrusH_T = db.Column(db.Float, nullable=False)  # 감귤(시설) 시장
    citrusH_M = db.Column(db.Float, nullable=False)  # 감귤(시설) 대형마트
    persimmon_T = db.Column(db.Float, nullable=False)  # 단감 시장
    persimmon_M = db.Column(db.Float, nullable=False)  # 단감 대형마트
    banana_T = db.Column(db.Float, nullable=False)  # 바나나 시장
    banana_M = db.Column(db.Float, nullable=False)  # 바나나 대형마트
    kiwiN_T = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 시장
    kiwiN_M = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 대형마트
    kiwiK_T = db.Column(db.Float, nullable=False)  # 참다래(국산) 시장
    kiwiK_M = db.Column(db.Float, nullable=False)  # 참다래(국산) 대형마트
    pineapple_T = db.Column(db.Float, nullable=False)  # 파인애플 시장
    pineapple_M = db.Column(db.Float, nullable=False)  # 파인애플 대형마트
    orangeU_T = db.Column(db.Float, nullable=False)  # 오렌지(미국) 시장
    orangeU_M = db.Column(db.Float, nullable=False)  # 오렌지(미국) 대형마트
    orangeA_T = db.Column(db.Float, nullable=False)  # 오렌지(호주) 시장
    orangeA_M = db.Column(db.Float, nullable=False)  # 오렌지(호주) 대형마트
    lemon_T = db.Column(db.Float, nullable=False)  # 레몬 시장
    lemon_M = db.Column(db.Float, nullable=False)  # 레몬 대형마트
    cherry_T = db.Column(db.Float, nullable=False)  # 체리 시장
    cherry_M = db.Column(db.Float, nullable=False)  # 체리 대형마트
    raisin_T = db.Column(db.Float, nullable=False)  # 건포도 시장
    raisin_M = db.Column(db.Float, nullable=False)  # 건포도 대형마트
    dried_blueberries_T = db.Column(db.Float, nullable=False)  # 건블루베리 시장
    dried_blueberries_M = db.Column(db.Float, nullable=False)  # 건블루베리 대형마트
    mango_T = db.Column(db.Float, nullable=False)  # 망고 시장
    mango_M = db.Column(db.Float, nullable=False)  # 망고 대형마트

    # 수산물
    mackerelL_T = db.Column(db.Float, nullable=False)  # 고등어(생물) 시장
    mackerelL_M = db.Column(db.Float, nullable=False)  # 고등어(생물) 대형마트
    mackerelF_T = db.Column(db.Float, nullable=False)  # 고등어(냉동) 시장
    mackerelF_M = db.Column(db.Float, nullable=False)  # 고등어(냉동) 대형마트
    mackerelS_T = db.Column(db.Float, nullable=False)  # 고등어(염장) 시장
    mackerelS_M = db.Column(db.Float, nullable=False)  # 고등어(염장) 대형마트
    saury_T = db.Column(db.Float, nullable=False)  # 꽁치 시장
    saury_M = db.Column(db.Float, nullable=False)  # 꽁치 대형마트
    cutlassfishL_T = db.Column(db.Float, nullable=False)  # 갈치(생물) 시장
    cutlassfishL_M = db.Column(db.Float, nullable=False)  # 갈치(생물) 대형마트
    cutlassfishF_T = db.Column(db.Float, nullable=False)  # 갈치(냉동) 시장
    cutlassfishF_M = db.Column(db.Float, nullable=False)  # 갈치(냉동) 대형마트
    pollock_T = db.Column(db.Float, nullable=False)  # 명태 시장
    pollock_M = db.Column(db.Float, nullable=False)  # 명태 대형마트
    squidL_T = db.Column(db.Float, nullable=False)  # 물오징어(생선) 시장
    squidL_M = db.Column(db.Float, nullable=False)  # 물오징어(생선) 대형마트
    squidF_T = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 시장
    squidF_M = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 대형마트
    dried_anchovies_T = db.Column(db.Float, nullable=False)  # 건멸치 시장
    dried_anchovies_M = db.Column(db.Float, nullable=False)  # 건멸치 대형마트
    dried_squid_T = db.Column(db.Float, nullable=False)  # 건오징어 시장
    dried_squid_M = db.Column(db.Float, nullable=False)  # 건오징어 대형마트
    seaweedD_T = db.Column(db.Float, nullable=False)  # 김(마른김) 시장
    seaweedD_M = db.Column(db.Float, nullable=False)  # 김(마른김) 대형마트
    seaweedF_T = db.Column(db.Float, nullable=False)  # 김(구운김) 시장
    seaweedF_M = db.Column(db.Float, nullable=False)  # 김(구운김) 대형마트
    dried_seaweed_T = db.Column(db.Float, nullable=False)  # 건미역 시장
    dried_seaweed_M = db.Column(db.Float, nullable=False)  # 건미역 대형마트
    oyster_T = db.Column(db.Float, nullable=False)  # 굴 시장
    oyster_M = db.Column(db.Float, nullable=False)  # 굴 대형마트
    yellow_corbina_T = db.Column(db.Float, nullable=False)  # 수입조기 시장
    yellow_corbina_M = db.Column(db.Float, nullable=False)  # 수입조기 대형마트
    salted_shrimp_T = db.Column(db.Float, nullable=False)  # 새우젓 시장
    salted_shrimp_M = db.Column(db.Float, nullable=False)  # 새우젓 대형마트
    anchovy_fish_sauce_T = db.Column(db.Float, nullable=False)  # 멸치액젓 시장
    anchovy_fish_sauce_M = db.Column(db.Float, nullable=False)  # 멸치액젓 대형마트
    salt_T = db.Column(db.Float, nullable=False)  # 굵은소금 시장
    salt_M = db.Column(db.Float, nullable=False)  # 굵은소금 대형마트
    abalone_T = db.Column(db.Float, nullable=False)  # 전복 시장
    abalone_M = db.Column(db.Float, nullable=False)  # 전복 대형마트
    shrimp_T = db.Column(db.Float, nullable=False)  # 흰다리새우 시장
    shrimp_M = db.Column(db.Float, nullable=False)  # 흰다리새우 대형마트


## 인천 소매
class Incheon_retail(db.Model):
    date = db.Column(db.Integer, primary_key=True, nullable=False)  # 일자

    # 식량작물
    rice_T = db.Column(db.Float, nullable=False)  # 쌀 시장
    rice_M = db.Column(db.Float, nullable=False)  # 쌀 대형마트
    riceF_T = db.Column(db.Float, nullable=False)  # 햇쌀 시장
    riceF_M = db.Column(db.Float, nullable=False)  # 햇쌀 대형마트
    glutinous_rice_T = db.Column(db.Float, nullable=False)  # 찹쌀 시장
    glutinous_rice_M = db.Column(db.Float, nullable=False)  # 찹쌀 대형마트
    bean_T = db.Column(db.Float, nullable=False)  # 콩 시장
    bean_M = db.Column(db.Float, nullable=False)  # 콩 대형마트
    red_bean_T = db.Column(db.Float, nullable=False)  # 팥 시장
    red_bean_M = db.Column(db.Float, nullable=False)  # 팥 대형마트
    green_beans_T = db.Column(db.Float, nullable=False)  # 녹두 시장
    green_beans_M = db.Column(db.Float, nullable=False)  # 녹두 대형마트
    sweet_potato_T = db.Column(db.Float, nullable=False)  # 고구마 시장
    sweet_potato_M = db.Column(db.Float, nullable=False)  # 고구마 대형마트
    potato_T = db.Column(db.Float, nullable=False)  # 감자 시장
    potato_M = db.Column(db.Float, nullable=False)  # 감자 대형마트

    # 채소류
    napa_cabbageF_T = db.Column(db.Float, nullable=False)  # 배추(가을) 시장
    napa_cabbageF_M = db.Column(db.Float, nullable=False)  # 배추(가을) 대형마트
    napa_cabbageW_T = db.Column(db.Float, nullable=False)  # 배추(월동) 시장
    napa_cabbageW_M = db.Column(db.Float, nullable=False)  # 배추(월동) 대형마트
    napa_cabbageS_T = db.Column(db.Float, nullable=False)  # 배추(봄) 시장
    napa_cabbageS_M = db.Column(db.Float, nullable=False)  # 배추(봄) 대형마트
    napa_cabbageH_T = db.Column(db.Float, nullable=False)  # 배추(고랭지) 시장
    napa_cabbageH_M = db.Column(db.Float, nullable=False)  # 배추(고랭지) 대형마트
    cabbage_T = db.Column(db.Float, nullable=False)  # 양배추 시장
    cabbage_M = db.Column(db.Float, nullable=False)  # 양배추 대형마트
    spinach_T = db.Column(db.Float, nullable=False)  # 시금치 시장
    spinach_M = db.Column(db.Float, nullable=False)  # 시금치 대형마트
    lettuceR_T = db.Column(db.Float, nullable=False)  # 상추(적) 시장
    lettuceR_M = db.Column(db.Float, nullable=False)  # 상추(적) 대형마트
    lettuceB_T = db.Column(db.Float, nullable=False)  # 상추(청) 시장
    lettuceB_M = db.Column(db.Float, nullable=False)  # 상추(청) 대형마트
    winter_cabbage_T = db.Column(db.Float, nullable=False)  # 얼갈이배추 시장
    winter_cabbage_M = db.Column(db.Float, nullable=False)  # 얼갈이배추 대형마트
    leaf_mustard_T = db.Column(db.Float, nullable=False)  # 갓 시장
    leaf_mustard_M = db.Column(db.Float, nullable=False)  # 갓 대형마트
    watermelon_T = db.Column(db.Float, nullable=False)  # 수박 시장
    watermelon_M = db.Column(db.Float, nullable=False)  # 수박 대형마트
    korean_melon_T = db.Column(db.Float, nullable=False)  # 참외 시장
    korean_melon_M = db.Column(db.Float, nullable=False)  # 참외 대형마트
    cucumberS_T = db.Column(db.Float, nullable=False)  # 오이(가시계통) 시장
    cucumberS_M = db.Column(db.Float, nullable=False)  # 오이(가시계통) 대형마트
    cucumberD_T = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 시장
    cucumberD_M = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 대형마트
    cucumberW_T = db.Column(db.Float, nullable=False)  # 오이(취청) 시장
    cucumberW_M = db.Column(db.Float, nullable=False)  # 오이(취청) 대형마트
    squash_T = db.Column(db.Float, nullable=False)  # 애호박 시장
    squash_M = db.Column(db.Float, nullable=False)  # 애호박 대형마트
    zucchini_T = db.Column(db.Float, nullable=False)  # 주키니 시장
    zucchini_M = db.Column(db.Float, nullable=False)  # 주키니 대형마트
    tomato_T = db.Column(db.Float, nullable=False)  # 토마토 시장
    tomato_M = db.Column(db.Float, nullable=False)  # 토마토 대형마트
    strawberry_T = db.Column(db.Float, nullable=False)  # 딸기 시장
    strawberry_M = db.Column(db.Float, nullable=False)  # 딸기 대형마트
    radishF_T = db.Column(db.Float, nullable=False)  # 무(가을) 시장
    radishF_M = db.Column(db.Float, nullable=False)  # 무(가을) 대형마트
    radishW_T = db.Column(db.Float, nullable=False)  # 무(월동) 시장
    radishW_M = db.Column(db.Float, nullable=False)  # 무(월동) 대형마트
    radishS_T = db.Column(db.Float, nullable=False)  # 무(봄) 시장
    radishS_M = db.Column(db.Float, nullable=False)  # 무(봄) 대형마트
    radishH_T = db.Column(db.Float, nullable=False)  # 무(고랭지) 시장
    radishH_M = db.Column(db.Float, nullable=False)  # 무(고랭지) 대형마트
    carrot_T = db.Column(db.Float, nullable=False)  # 당근 시장
    carrot_M = db.Column(db.Float, nullable=False)  # 당근 대형마트
    yeol_radish_T = db.Column(db.Float, nullable=False)  # 열무 시장
    yeol_radish_M = db.Column(db.Float, nullable=False)  # 열무 대형마트
    dried_red_pepperD_T = db.Column(db.Float, nullable=False)  # 건고추(화건) 시장
    dried_red_pepperD_M = db.Column(db.Float, nullable=False)  # 건고추(화건) 대형마트
    dried_red_pepperS_T = db.Column(db.Float, nullable=False)  # 건고추(양건) 시장
    dried_red_pepperS_M = db.Column(db.Float, nullable=False)  # 건고추(양양건) 대형마트
    pepper_T = db.Column(db.Float, nullable=False)  # 풋고추 시장
    pepper_M = db.Column(db.Float, nullable=False)  # 풋고추 대형마트
    chilli_pepper_T = db.Column(db.Float, nullable=False)  # 꽈리고추 시장
    chilli_pepper_M = db.Column(db.Float, nullable=False)  # 꽈리고추 대형마트
    cheongyang_pepper_T = db.Column(db.Float, nullable=False)  # 청양고추 시장
    cheongyang_pepper_M = db.Column(db.Float, nullable=False)  # 청양고추 대형마트
    red_pepper_T = db.Column(db.Float, nullable=False)  # 붉은고추 시장
    red_pepper_M = db.Column(db.Float, nullable=False)  # 붉은고추 대형마트
    onion_T = db.Column(db.Float, nullable=False)  # 양파 시장
    onion_M = db.Column(db.Float, nullable=False)  # 양파 대형마트
    green_onion_T = db.Column(db.Float, nullable=False)  # 대파 시장
    green_onion_M = db.Column(db.Float, nullable=False)  # 대파 대형마트
    chives_T = db.Column(db.Float, nullable=False)  # 쪽파 시장
    chives_M = db.Column(db.Float, nullable=False)  # 쪽파 대형마트
    ginger_T = db.Column(db.Float, nullable=False)  # 생강 시장
    ginger_M = db.Column(db.Float, nullable=False)  # 생강 대형마트
    chili_powder_T = db.Column(db.Float, nullable=False)  # 고추가루 시장
    chili_powder_M = db.Column(db.Float, nullable=False)  # 고추가루 대형마트
    parsley_T = db.Column(db.Float, nullable=False)  # 미나리 시장
    parsley_M = db.Column(db.Float, nullable=False)  # 미나리 대형마트
    sesame_leaf_T = db.Column(db.Float, nullable=False)  # 깻잎 시장
    sesame_leaf_M = db.Column(db.Float, nullable=False)  # 깻잎 대형마트
    pimento_T = db.Column(db.Float, nullable=False)  # 피망 시장
    pimento_M = db.Column(db.Float, nullable=False)  # 피망 대형마트
    paprika_T = db.Column(db.Float, nullable=False)  # 파프리카 시장
    paprika_M = db.Column(db.Float, nullable=False)  # 파프리카 대형마트
    melon_T = db.Column(db.Float, nullable=False)  # 멜론 시장
    melon_M = db.Column(db.Float, nullable=False)  # 멜론 대형마트
    garlic_T = db.Column(db.Float, nullable=False)  # 깐마늘 시장
    garlic_M = db.Column(db.Float, nullable=False)  # 깐마늘 대형마트
    cherry_tomato_T = db.Column(db.Float, nullable=False)  # 방울토마토 시장
    cherry_tomato_M = db.Column(db.Float, nullable=False)  # 방울토마토 대형마트
    jujube_cherry_tomato_T = db.Column(db.Float, nullable=False)  # 대추방울토마토 시장
    jujube_cherry_tomato_M = db.Column(db.Float, nullable=False)  # 대추방울토마토 대형마트

    # 특용작물
    sesame_T = db.Column(db.Float, nullable=False)  # 참깨 시장
    sesame_M = db.Column(db.Float, nullable=False)  # 참깨 대형마트
    peanut_T = db.Column(db.Float, nullable=False)  # 땅콩 시장
    peanut_M = db.Column(db.Float, nullable=False)  # 땅콩 대형마트
    oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 느타리버섯 시장
    oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 느타리버섯 대형마트
    oyster_mushroomA_T = db.Column(db.Float, nullable=False)  # 애느타리버섯 시장
    oyster_mushroomA_M = db.Column(db.Float, nullable=False)  # 애느타리버섯 대형마트
    enoki_mushroom_T = db.Column(db.Float, nullable=False)  # 팽이버섯 시장
    enoki_mushroom_M = db.Column(db.Float, nullable=False)  # 팽이버섯 대형마트
    king_oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 새송이버섯 시장
    king_oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 새송이버섯 대형마트
    walnut_T = db.Column(db.Float, nullable=False)  # 호두 시장
    walnut_M = db.Column(db.Float, nullable=False)  # 호두 대형마트
    almond_T = db.Column(db.Float, nullable=False)  # 아몬드 시장
    almond_M = db.Column(db.Float, nullable=False)  # 아몬드 대형마트

    # 과일류
    appleF_T = db.Column(db.Float, nullable=False)  # 사과(후지) 시장
    appleF_M = db.Column(db.Float, nullable=False)  # 사과(후지) 대형마트
    appleT_T = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 시장
    appleT_M = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 대형마트
    appleR_T = db.Column(db.Float, nullable=False)  # 사과(홍로) 시장
    appleR_M = db.Column(db.Float, nullable=False)  # 사과(홍로) 대마트
    pearS_T = db.Column(db.Float, nullable=False)  # 배(신고) 시장
    pearS_M = db.Column(db.Float, nullable=False)  # 배(신고) 대형마트
    pearW_T = db.Column(db.Float, nullable=False)  # 배(원황) 시장
    pearW_M = db.Column(db.Float, nullable=False)  # 배(원황) 대형마트
    peach_T = db.Column(db.Float, nullable=False)  # 복숭아 시장
    peach_M = db.Column(db.Float, nullable=False)  # 복숭아 대형마트
    grapeC_T = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 시장
    grapeC_M = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 대형마트
    grapeG_T = db.Column(db.Float, nullable=False)  # 포도(거봉) 시장
    grapeG_M = db.Column(db.Float, nullable=False)  # 포도(거봉) 대형마트
    grapeM_T = db.Column(db.Float, nullable=False)  # 포도(MBA) 시장
    grapeM_M = db.Column(db.Float, nullable=False)  # 포도(MBA) 대형마트
    grapeS_T = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 시장
    grapeS_M = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 대형마트
    grapeR_T = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 시장
    grapeR_M = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 대형마트
    citrusR_T = db.Column(db.Float, nullable=False)  # 감귤(노지) 시장
    citrusR_M = db.Column(db.Float, nullable=False)  # 감귤(노지) 대형마트
    citrusH_T = db.Column(db.Float, nullable=False)  # 감귤(시설) 시장
    citrusH_M = db.Column(db.Float, nullable=False)  # 감귤(시설) 대형마트
    persimmon_T = db.Column(db.Float, nullable=False)  # 단감 시장
    persimmon_M = db.Column(db.Float, nullable=False)  # 단감 대형마트
    banana_T = db.Column(db.Float, nullable=False)  # 바나나 시장
    banana_M = db.Column(db.Float, nullable=False)  # 바나나 대형마트
    kiwiN_T = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 시장
    kiwiN_M = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 대형마트
    kiwiK_T = db.Column(db.Float, nullable=False)  # 참다래(국산) 시장
    kiwiK_M = db.Column(db.Float, nullable=False)  # 참다래(국산) 대형마트
    pineapple_T = db.Column(db.Float, nullable=False)  # 파인애플 시장
    pineapple_M = db.Column(db.Float, nullable=False)  # 파인애플 대형마트
    orangeU_T = db.Column(db.Float, nullable=False)  # 오렌지(미국) 시장
    orangeU_M = db.Column(db.Float, nullable=False)  # 오렌지(미국) 대형마트
    orangeA_T = db.Column(db.Float, nullable=False)  # 오렌지(호주) 시장
    orangeA_M = db.Column(db.Float, nullable=False)  # 오렌지(호주) 대형마트
    lemon_T = db.Column(db.Float, nullable=False)  # 레몬 시장
    lemon_M = db.Column(db.Float, nullable=False)  # 레몬 대형마트
    cherry_T = db.Column(db.Float, nullable=False)  # 체리 시장
    cherry_M = db.Column(db.Float, nullable=False)  # 체리 대형마트
    raisin_T = db.Column(db.Float, nullable=False)  # 건포도 시장
    raisin_M = db.Column(db.Float, nullable=False)  # 건포도 대형마트
    dried_blueberries_T = db.Column(db.Float, nullable=False)  # 건블루베리 시장
    dried_blueberries_M = db.Column(db.Float, nullable=False)  # 건블루베리 대형마트
    mango_T = db.Column(db.Float, nullable=False)  # 망고 시장
    mango_M = db.Column(db.Float, nullable=False)  # 망고 대형마트

    # 수산물
    mackerelL_T = db.Column(db.Float, nullable=False)  # 고등어(생물) 시장
    mackerelL_M = db.Column(db.Float, nullable=False)  # 고등어(생물) 대형마트
    mackerelF_T = db.Column(db.Float, nullable=False)  # 고등어(냉동) 시장
    mackerelF_M = db.Column(db.Float, nullable=False)  # 고등어(냉동) 대형마트
    mackerelS_T = db.Column(db.Float, nullable=False)  # 고등어(염장) 시장
    mackerelS_M = db.Column(db.Float, nullable=False)  # 고등어(염장) 대형마트
    saury_T = db.Column(db.Float, nullable=False)  # 꽁치 시장
    saury_M = db.Column(db.Float, nullable=False)  # 꽁치 대형마트
    cutlassfishL_T = db.Column(db.Float, nullable=False)  # 갈치(생물) 시장
    cutlassfishL_M = db.Column(db.Float, nullable=False)  # 갈치(생물) 대형마트
    cutlassfishF_T = db.Column(db.Float, nullable=False)  # 갈치(냉동) 시장
    cutlassfishF_M = db.Column(db.Float, nullable=False)  # 갈치(냉동) 대형마트
    pollock_T = db.Column(db.Float, nullable=False)  # 명태 시장
    pollock_M = db.Column(db.Float, nullable=False)  # 명태 대형마트
    squidL_T = db.Column(db.Float, nullable=False)  # 물오징어(생선) 시장
    squidL_M = db.Column(db.Float, nullable=False)  # 물오징어(생선) 대형마트
    squidF_T = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 시장
    squidF_M = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 대형마트
    dried_anchovies_T = db.Column(db.Float, nullable=False)  # 건멸치 시장
    dried_anchovies_M = db.Column(db.Float, nullable=False)  # 건멸치 대형마트
    dried_squid_T = db.Column(db.Float, nullable=False)  # 건오징어 시장
    dried_squid_M = db.Column(db.Float, nullable=False)  # 건오징어 대형마트
    seaweedD_T = db.Column(db.Float, nullable=False)  # 김(마른김) 시장
    seaweedD_M = db.Column(db.Float, nullable=False)  # 김(마른김) 대형마트
    seaweedF_T = db.Column(db.Float, nullable=False)  # 김(구운김) 시장
    seaweedF_M = db.Column(db.Float, nullable=False)  # 김(구운김) 대형마트
    dried_seaweed_T = db.Column(db.Float, nullable=False)  # 건미역 시장
    dried_seaweed_M = db.Column(db.Float, nullable=False)  # 건미역 대형마트
    oyster_T = db.Column(db.Float, nullable=False)  # 굴 시장
    oyster_M = db.Column(db.Float, nullable=False)  # 굴 대형마트
    yellow_corbina_T = db.Column(db.Float, nullable=False)  # 수입조기 시장
    yellow_corbina_M = db.Column(db.Float, nullable=False)  # 수입조기 대형마트
    salted_shrimp_T = db.Column(db.Float, nullable=False)  # 새우젓 시장
    salted_shrimp_M = db.Column(db.Float, nullable=False)  # 새우젓 대형마트
    anchovy_fish_sauce_T = db.Column(db.Float, nullable=False)  # 멸치액젓 시장
    anchovy_fish_sauce_M = db.Column(db.Float, nullable=False)  # 멸치액젓 대형마트
    salt_T = db.Column(db.Float, nullable=False)  # 굵은소금 시장
    salt_M = db.Column(db.Float, nullable=False)  # 굵은소금 대형마트
    abalone_T = db.Column(db.Float, nullable=False)  # 전복 시장
    abalone_M = db.Column(db.Float, nullable=False)  # 전복 대형마트
    shrimp_T = db.Column(db.Float, nullable=False)  # 흰다리새우 시장
    shrimp_M = db.Column(db.Float, nullable=False)  # 흰다리새우 대형마트


## 대전 소매
class Daejeon_retail(db.Model):
    date = db.Column(db.Integer, primary_key=True, nullable=False)  # 일자

    # 식량작물
    rice_T = db.Column(db.Float, nullable=False)  # 쌀 시장
    rice_M = db.Column(db.Float, nullable=False)  # 쌀 대형마트
    riceF_T = db.Column(db.Float, nullable=False)  # 햇쌀 시장
    riceF_M = db.Column(db.Float, nullable=False)  # 햇쌀 대형마트
    glutinous_rice_T = db.Column(db.Float, nullable=False)  # 찹쌀 시장
    glutinous_rice_M = db.Column(db.Float, nullable=False)  # 찹쌀 대형마트
    bean_T = db.Column(db.Float, nullable=False)  # 콩 시장
    bean_M = db.Column(db.Float, nullable=False)  # 콩 대형마트
    red_bean_T = db.Column(db.Float, nullable=False)  # 팥 시장
    red_bean_M = db.Column(db.Float, nullable=False)  # 팥 대형마트
    green_beans_T = db.Column(db.Float, nullable=False)  # 녹두 시장
    green_beans_M = db.Column(db.Float, nullable=False)  # 녹두 대형마트
    sweet_potato_T = db.Column(db.Float, nullable=False)  # 고구마 시장
    sweet_potato_M = db.Column(db.Float, nullable=False)  # 고구마 대형마트
    potato_T = db.Column(db.Float, nullable=False)  # 감자 시장
    potato_M = db.Column(db.Float, nullable=False)  # 감자 대형마트

    # 채소류
    napa_cabbageF_T = db.Column(db.Float, nullable=False)  # 배추(가을) 시장
    napa_cabbageF_M = db.Column(db.Float, nullable=False)  # 배추(가을) 대형마트
    napa_cabbageW_T = db.Column(db.Float, nullable=False)  # 배추(월동) 시장
    napa_cabbageW_M = db.Column(db.Float, nullable=False)  # 배추(월동) 대형마트
    napa_cabbageS_T = db.Column(db.Float, nullable=False)  # 배추(봄) 시장
    napa_cabbageS_M = db.Column(db.Float, nullable=False)  # 배추(봄) 대형마트
    napa_cabbageH_T = db.Column(db.Float, nullable=False)  # 배추(고랭지) 시장
    napa_cabbageH_M = db.Column(db.Float, nullable=False)  # 배추(고랭지) 대형마트
    cabbage_T = db.Column(db.Float, nullable=False)  # 양배추 시장
    cabbage_M = db.Column(db.Float, nullable=False)  # 양배추 대형마트
    spinach_T = db.Column(db.Float, nullable=False)  # 시금치 시장
    spinach_M = db.Column(db.Float, nullable=False)  # 시금치 대형마트
    lettuceR_T = db.Column(db.Float, nullable=False)  # 상추(적) 시장
    lettuceR_M = db.Column(db.Float, nullable=False)  # 상추(적) 대형마트
    lettuceB_T = db.Column(db.Float, nullable=False)  # 상추(청) 시장
    lettuceB_M = db.Column(db.Float, nullable=False)  # 상추(청) 대형마트
    winter_cabbage_T = db.Column(db.Float, nullable=False)  # 얼갈이배추 시장
    winter_cabbage_M = db.Column(db.Float, nullable=False)  # 얼갈이배추 대형마트
    leaf_mustard_T = db.Column(db.Float, nullable=False)  # 갓 시장
    leaf_mustard_M = db.Column(db.Float, nullable=False)  # 갓 대형마트
    watermelon_T = db.Column(db.Float, nullable=False)  # 수박 시장
    watermelon_M = db.Column(db.Float, nullable=False)  # 수박 대형마트
    korean_melon_T = db.Column(db.Float, nullable=False)  # 참외 시장
    korean_melon_M = db.Column(db.Float, nullable=False)  # 참외 대형마트
    cucumberS_T = db.Column(db.Float, nullable=False)  # 오이(가시계통) 시장
    cucumberS_M = db.Column(db.Float, nullable=False)  # 오이(가시계통) 대형마트
    cucumberD_T = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 시장
    cucumberD_M = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 대형마트
    cucumberW_T = db.Column(db.Float, nullable=False)  # 오이(취청) 시장
    cucumberW_M = db.Column(db.Float, nullable=False)  # 오이(취청) 대형마트
    squash_T = db.Column(db.Float, nullable=False)  # 애호박 시장
    squash_M = db.Column(db.Float, nullable=False)  # 애호박 대형마트
    zucchini_T = db.Column(db.Float, nullable=False)  # 주키니 시장
    zucchini_M = db.Column(db.Float, nullable=False)  # 주키니 대형마트
    tomato_T = db.Column(db.Float, nullable=False)  # 토마토 시장
    tomato_M = db.Column(db.Float, nullable=False)  # 토마토 대형마트
    strawberry_T = db.Column(db.Float, nullable=False)  # 딸기 시장
    strawberry_M = db.Column(db.Float, nullable=False)  # 딸기 대형마트
    radishF_T = db.Column(db.Float, nullable=False)  # 무(가을) 시장
    radishF_M = db.Column(db.Float, nullable=False)  # 무(가을) 대형마트
    radishW_T = db.Column(db.Float, nullable=False)  # 무(월동) 시장
    radishW_M = db.Column(db.Float, nullable=False)  # 무(월동) 대형마트
    radishS_T = db.Column(db.Float, nullable=False)  # 무(봄) 시장
    radishS_M = db.Column(db.Float, nullable=False)  # 무(봄) 대형마트
    radishH_T = db.Column(db.Float, nullable=False)  # 무(고랭지) 시장
    radishH_M = db.Column(db.Float, nullable=False)  # 무(고랭지) 대형마트
    carrot_T = db.Column(db.Float, nullable=False)  # 당근 시장
    carrot_M = db.Column(db.Float, nullable=False)  # 당근 대형마트
    yeol_radish_T = db.Column(db.Float, nullable=False)  # 열무 시장
    yeol_radish_M = db.Column(db.Float, nullable=False)  # 열무 대형마트
    dried_red_pepperD_T = db.Column(db.Float, nullable=False)  # 건고추(화건) 시장
    dried_red_pepperD_M = db.Column(db.Float, nullable=False)  # 건고추(화건) 대형마트
    dried_red_pepperS_T = db.Column(db.Float, nullable=False)  # 건고추(양건) 시장
    dried_red_pepperS_M = db.Column(db.Float, nullable=False)  # 건고추(양양건) 대형마트
    pepper_T = db.Column(db.Float, nullable=False)  # 풋고추 시장
    pepper_M = db.Column(db.Float, nullable=False)  # 풋고추 대형마트
    chilli_pepper_T = db.Column(db.Float, nullable=False)  # 꽈리고추 시장
    chilli_pepper_M = db.Column(db.Float, nullable=False)  # 꽈리고추 대형마트
    cheongyang_pepper_T = db.Column(db.Float, nullable=False)  # 청양고추 시장
    cheongyang_pepper_M = db.Column(db.Float, nullable=False)  # 청양고추 대형마트
    red_pepper_T = db.Column(db.Float, nullable=False)  # 붉은고추 시장
    red_pepper_M = db.Column(db.Float, nullable=False)  # 붉은고추 대형마트
    onion_T = db.Column(db.Float, nullable=False)  # 양파 시장
    onion_M = db.Column(db.Float, nullable=False)  # 양파 대형마트
    green_onion_T = db.Column(db.Float, nullable=False)  # 대파 시장
    green_onion_M = db.Column(db.Float, nullable=False)  # 대파 대형마트
    chives_T = db.Column(db.Float, nullable=False)  # 쪽파 시장
    chives_M = db.Column(db.Float, nullable=False)  # 쪽파 대형마트
    ginger_T = db.Column(db.Float, nullable=False)  # 생강 시장
    ginger_M = db.Column(db.Float, nullable=False)  # 생강 대형마트
    chili_powder_T = db.Column(db.Float, nullable=False)  # 고추가루 시장
    chili_powder_M = db.Column(db.Float, nullable=False)  # 고추가루 대형마트
    parsley_T = db.Column(db.Float, nullable=False)  # 미나리 시장
    parsley_M = db.Column(db.Float, nullable=False)  # 미나리 대형마트
    sesame_leaf_T = db.Column(db.Float, nullable=False)  # 깻잎 시장
    sesame_leaf_M = db.Column(db.Float, nullable=False)  # 깻잎 대형마트
    pimento_T = db.Column(db.Float, nullable=False)  # 피망 시장
    pimento_M = db.Column(db.Float, nullable=False)  # 피망 대형마트
    paprika_T = db.Column(db.Float, nullable=False)  # 파프리카 시장
    paprika_M = db.Column(db.Float, nullable=False)  # 파프리카 대형마트
    melon_T = db.Column(db.Float, nullable=False)  # 멜론 시장
    melon_M = db.Column(db.Float, nullable=False)  # 멜론 대형마트
    garlic_T = db.Column(db.Float, nullable=False)  # 깐마늘 시장
    garlic_M = db.Column(db.Float, nullable=False)  # 깐마늘 대형마트
    cherry_tomato_T = db.Column(db.Float, nullable=False)  # 방울토마토 시장
    cherry_tomato_M = db.Column(db.Float, nullable=False)  # 방울토마토 대형마트
    jujube_cherry_tomato_T = db.Column(db.Float, nullable=False)  # 대추방울토마토 시장
    jujube_cherry_tomato_M = db.Column(db.Float, nullable=False)  # 대추방울토마토 대형마트

    # 특용작물
    sesame_T = db.Column(db.Float, nullable=False)  # 참깨 시장
    sesame_M = db.Column(db.Float, nullable=False)  # 참깨 대형마트
    peanut_T = db.Column(db.Float, nullable=False)  # 땅콩 시장
    peanut_M = db.Column(db.Float, nullable=False)  # 땅콩 대형마트
    oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 느타리버섯 시장
    oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 느타리버섯 대형마트
    oyster_mushroomA_T = db.Column(db.Float, nullable=False)  # 애느타리버섯 시장
    oyster_mushroomA_M = db.Column(db.Float, nullable=False)  # 애느타리버섯 대형마트
    enoki_mushroom_T = db.Column(db.Float, nullable=False)  # 팽이버섯 시장
    enoki_mushroom_M = db.Column(db.Float, nullable=False)  # 팽이버섯 대형마트
    king_oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 새송이버섯 시장
    king_oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 새송이버섯 대형마트
    walnut_T = db.Column(db.Float, nullable=False)  # 호두 시장
    walnut_M = db.Column(db.Float, nullable=False)  # 호두 대형마트
    almond_T = db.Column(db.Float, nullable=False)  # 아몬드 시장
    almond_M = db.Column(db.Float, nullable=False)  # 아몬드 대형마트

    # 과일류
    appleF_T = db.Column(db.Float, nullable=False)  # 사과(후지) 시장
    appleF_M = db.Column(db.Float, nullable=False)  # 사과(후지) 대형마트
    appleT_T = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 시장
    appleT_M = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 대형마트
    appleR_T = db.Column(db.Float, nullable=False)  # 사과(홍로) 시장
    appleR_M = db.Column(db.Float, nullable=False)  # 사과(홍로) 대마트
    pearS_T = db.Column(db.Float, nullable=False)  # 배(신고) 시장
    pearS_M = db.Column(db.Float, nullable=False)  # 배(신고) 대형마트
    pearW_T = db.Column(db.Float, nullable=False)  # 배(원황) 시장
    pearW_M = db.Column(db.Float, nullable=False)  # 배(원황) 대형마트
    peach_T = db.Column(db.Float, nullable=False)  # 복숭아 시장
    peach_M = db.Column(db.Float, nullable=False)  # 복숭아 대형마트
    grapeC_T = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 시장
    grapeC_M = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 대형마트
    grapeG_T = db.Column(db.Float, nullable=False)  # 포도(거봉) 시장
    grapeG_M = db.Column(db.Float, nullable=False)  # 포도(거봉) 대형마트
    grapeM_T = db.Column(db.Float, nullable=False)  # 포도(MBA) 시장
    grapeM_M = db.Column(db.Float, nullable=False)  # 포도(MBA) 대형마트
    grapeS_T = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 시장
    grapeS_M = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 대형마트
    grapeR_T = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 시장
    grapeR_M = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 대형마트
    citrusR_T = db.Column(db.Float, nullable=False)  # 감귤(노지) 시장
    citrusR_M = db.Column(db.Float, nullable=False)  # 감귤(노지) 대형마트
    citrusH_T = db.Column(db.Float, nullable=False)  # 감귤(시설) 시장
    citrusH_M = db.Column(db.Float, nullable=False)  # 감귤(시설) 대형마트
    persimmon_T = db.Column(db.Float, nullable=False)  # 단감 시장
    persimmon_M = db.Column(db.Float, nullable=False)  # 단감 대형마트
    banana_T = db.Column(db.Float, nullable=False)  # 바나나 시장
    banana_M = db.Column(db.Float, nullable=False)  # 바나나 대형마트
    kiwiN_T = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 시장
    kiwiN_M = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 대형마트
    kiwiK_T = db.Column(db.Float, nullable=False)  # 참다래(국산) 시장
    kiwiK_M = db.Column(db.Float, nullable=False)  # 참다래(국산) 대형마트
    pineapple_T = db.Column(db.Float, nullable=False)  # 파인애플 시장
    pineapple_M = db.Column(db.Float, nullable=False)  # 파인애플 대형마트
    orangeU_T = db.Column(db.Float, nullable=False)  # 오렌지(미국) 시장
    orangeU_M = db.Column(db.Float, nullable=False)  # 오렌지(미국) 대형마트
    orangeA_T = db.Column(db.Float, nullable=False)  # 오렌지(호주) 시장
    orangeA_M = db.Column(db.Float, nullable=False)  # 오렌지(호주) 대형마트
    lemon_T = db.Column(db.Float, nullable=False)  # 레몬 시장
    lemon_M = db.Column(db.Float, nullable=False)  # 레몬 대형마트
    cherry_T = db.Column(db.Float, nullable=False)  # 체리 시장
    cherry_M = db.Column(db.Float, nullable=False)  # 체리 대형마트
    raisin_T = db.Column(db.Float, nullable=False)  # 건포도 시장
    raisin_M = db.Column(db.Float, nullable=False)  # 건포도 대형마트
    dried_blueberries_T = db.Column(db.Float, nullable=False)  # 건블루베리 시장
    dried_blueberries_M = db.Column(db.Float, nullable=False)  # 건블루베리 대형마트
    mango_T = db.Column(db.Float, nullable=False)  # 망고 시장
    mango_M = db.Column(db.Float, nullable=False)  # 망고 대형마트

    # 수산물
    mackerelL_T = db.Column(db.Float, nullable=False)  # 고등어(생물) 시장
    mackerelL_M = db.Column(db.Float, nullable=False)  # 고등어(생물) 대형마트
    mackerelF_T = db.Column(db.Float, nullable=False)  # 고등어(냉동) 시장
    mackerelF_M = db.Column(db.Float, nullable=False)  # 고등어(냉동) 대형마트
    mackerelS_T = db.Column(db.Float, nullable=False)  # 고등어(염장) 시장
    mackerelS_M = db.Column(db.Float, nullable=False)  # 고등어(염장) 대형마트
    saury_T = db.Column(db.Float, nullable=False)  # 꽁치 시장
    saury_M = db.Column(db.Float, nullable=False)  # 꽁치 대형마트
    cutlassfishL_T = db.Column(db.Float, nullable=False)  # 갈치(생물) 시장
    cutlassfishL_M = db.Column(db.Float, nullable=False)  # 갈치(생물) 대형마트
    cutlassfishF_T = db.Column(db.Float, nullable=False)  # 갈치(냉동) 시장
    cutlassfishF_M = db.Column(db.Float, nullable=False)  # 갈치(냉동) 대형마트
    pollock_T = db.Column(db.Float, nullable=False)  # 명태 시장
    pollock_M = db.Column(db.Float, nullable=False)  # 명태 대형마트
    squidL_T = db.Column(db.Float, nullable=False)  # 물오징어(생선) 시장
    squidL_M = db.Column(db.Float, nullable=False)  # 물오징어(생선) 대형마트
    squidF_T = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 시장
    squidF_M = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 대형마트
    dried_anchovies_T = db.Column(db.Float, nullable=False)  # 건멸치 시장
    dried_anchovies_M = db.Column(db.Float, nullable=False)  # 건멸치 대형마트
    dried_squid_T = db.Column(db.Float, nullable=False)  # 건오징어 시장
    dried_squid_M = db.Column(db.Float, nullable=False)  # 건오징어 대형마트
    seaweedD_T = db.Column(db.Float, nullable=False)  # 김(마른김) 시장
    seaweedD_M = db.Column(db.Float, nullable=False)  # 김(마른김) 대형마트
    seaweedF_T = db.Column(db.Float, nullable=False)  # 김(구운김) 시장
    seaweedF_M = db.Column(db.Float, nullable=False)  # 김(구운김) 대형마트
    dried_seaweed_T = db.Column(db.Float, nullable=False)  # 건미역 시장
    dried_seaweed_M = db.Column(db.Float, nullable=False)  # 건미역 대형마트
    oyster_T = db.Column(db.Float, nullable=False)  # 굴 시장
    oyster_M = db.Column(db.Float, nullable=False)  # 굴 대형마트
    yellow_corbina_T = db.Column(db.Float, nullable=False)  # 수입조기 시장
    yellow_corbina_M = db.Column(db.Float, nullable=False)  # 수입조기 대형마트
    salted_shrimp_T = db.Column(db.Float, nullable=False)  # 새우젓 시장
    salted_shrimp_M = db.Column(db.Float, nullable=False)  # 새우젓 대형마트
    anchovy_fish_sauce_T = db.Column(db.Float, nullable=False)  # 멸치액젓 시장
    anchovy_fish_sauce_M = db.Column(db.Float, nullable=False)  # 멸치액젓 대형마트
    salt_T = db.Column(db.Float, nullable=False)  # 굵은소금 시장
    salt_M = db.Column(db.Float, nullable=False)  # 굵은소금 대형마트
    abalone_T = db.Column(db.Float, nullable=False)  # 전복 시장
    abalone_M = db.Column(db.Float, nullable=False)  # 전복 대형마트
    shrimp_T = db.Column(db.Float, nullable=False)  # 흰다리새우 시장
    shrimp_M = db.Column(db.Float, nullable=False)  # 흰다리새우 대형마트


## 대구 소매
class Daegu_retail(db.Model):
    date = db.Column(db.Integer, primary_key=True, nullable=False)  # 일자

    # 식량작물
    rice_T = db.Column(db.Float, nullable=False)  # 쌀 시장
    rice_M = db.Column(db.Float, nullable=False)  # 쌀 대형마트
    riceF_T = db.Column(db.Float, nullable=False)  # 햇쌀 시장
    riceF_M = db.Column(db.Float, nullable=False)  # 햇쌀 대형마트
    glutinous_rice_T = db.Column(db.Float, nullable=False)  # 찹쌀 시장
    glutinous_rice_M = db.Column(db.Float, nullable=False)  # 찹쌀 대형마트
    bean_T = db.Column(db.Float, nullable=False)  # 콩 시장
    bean_M = db.Column(db.Float, nullable=False)  # 콩 대형마트
    red_bean_T = db.Column(db.Float, nullable=False)  # 팥 시장
    red_bean_M = db.Column(db.Float, nullable=False)  # 팥 대형마트
    green_beans_T = db.Column(db.Float, nullable=False)  # 녹두 시장
    green_beans_M = db.Column(db.Float, nullable=False)  # 녹두 대형마트
    sweet_potato_T = db.Column(db.Float, nullable=False)  # 고구마 시장
    sweet_potato_M = db.Column(db.Float, nullable=False)  # 고구마 대형마트
    potato_T = db.Column(db.Float, nullable=False)  # 감자 시장
    potato_M = db.Column(db.Float, nullable=False)  # 감자 대형마트

    # 채소류
    napa_cabbageF_T = db.Column(db.Float, nullable=False)  # 배추(가을) 시장
    napa_cabbageF_M = db.Column(db.Float, nullable=False)  # 배추(가을) 대형마트
    napa_cabbageW_T = db.Column(db.Float, nullable=False)  # 배추(월동) 시장
    napa_cabbageW_M = db.Column(db.Float, nullable=False)  # 배추(월동) 대형마트
    napa_cabbageS_T = db.Column(db.Float, nullable=False)  # 배추(봄) 시장
    napa_cabbageS_M = db.Column(db.Float, nullable=False)  # 배추(봄) 대형마트
    napa_cabbageH_T = db.Column(db.Float, nullable=False)  # 배추(고랭지) 시장
    napa_cabbageH_M = db.Column(db.Float, nullable=False)  # 배추(고랭지) 대형마트
    cabbage_T = db.Column(db.Float, nullable=False)  # 양배추 시장
    cabbage_M = db.Column(db.Float, nullable=False)  # 양배추 대형마트
    spinach_T = db.Column(db.Float, nullable=False)  # 시금치 시장
    spinach_M = db.Column(db.Float, nullable=False)  # 시금치 대형마트
    lettuceR_T = db.Column(db.Float, nullable=False)  # 상추(적) 시장
    lettuceR_M = db.Column(db.Float, nullable=False)  # 상추(적) 대형마트
    lettuceB_T = db.Column(db.Float, nullable=False)  # 상추(청) 시장
    lettuceB_M = db.Column(db.Float, nullable=False)  # 상추(청) 대형마트
    winter_cabbage_T = db.Column(db.Float, nullable=False)  # 얼갈이배추 시장
    winter_cabbage_M = db.Column(db.Float, nullable=False)  # 얼갈이배추 대형마트
    leaf_mustard_T = db.Column(db.Float, nullable=False)  # 갓 시장
    leaf_mustard_M = db.Column(db.Float, nullable=False)  # 갓 대형마트
    watermelon_T = db.Column(db.Float, nullable=False)  # 수박 시장
    watermelon_M = db.Column(db.Float, nullable=False)  # 수박 대형마트
    korean_melon_T = db.Column(db.Float, nullable=False)  # 참외 시장
    korean_melon_M = db.Column(db.Float, nullable=False)  # 참외 대형마트
    cucumberS_T = db.Column(db.Float, nullable=False)  # 오이(가시계통) 시장
    cucumberS_M = db.Column(db.Float, nullable=False)  # 오이(가시계통) 대형마트
    cucumberD_T = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 시장
    cucumberD_M = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 대형마트
    cucumberW_T = db.Column(db.Float, nullable=False)  # 오이(취청) 시장
    cucumberW_M = db.Column(db.Float, nullable=False)  # 오이(취청) 대형마트
    squash_T = db.Column(db.Float, nullable=False)  # 애호박 시장
    squash_M = db.Column(db.Float, nullable=False)  # 애호박 대형마트
    zucchini_T = db.Column(db.Float, nullable=False)  # 주키니 시장
    zucchini_M = db.Column(db.Float, nullable=False)  # 주키니 대형마트
    tomato_T = db.Column(db.Float, nullable=False)  # 토마토 시장
    tomato_M = db.Column(db.Float, nullable=False)  # 토마토 대형마트
    strawberry_T = db.Column(db.Float, nullable=False)  # 딸기 시장
    strawberry_M = db.Column(db.Float, nullable=False)  # 딸기 대형마트
    radishF_T = db.Column(db.Float, nullable=False)  # 무(가을) 시장
    radishF_M = db.Column(db.Float, nullable=False)  # 무(가을) 대형마트
    radishW_T = db.Column(db.Float, nullable=False)  # 무(월동) 시장
    radishW_M = db.Column(db.Float, nullable=False)  # 무(월동) 대형마트
    radishS_T = db.Column(db.Float, nullable=False)  # 무(봄) 시장
    radishS_M = db.Column(db.Float, nullable=False)  # 무(봄) 대형마트
    radishH_T = db.Column(db.Float, nullable=False)  # 무(고랭지) 시장
    radishH_M = db.Column(db.Float, nullable=False)  # 무(고랭지) 대형마트
    carrot_T = db.Column(db.Float, nullable=False)  # 당근 시장
    carrot_M = db.Column(db.Float, nullable=False)  # 당근 대형마트
    yeol_radish_T = db.Column(db.Float, nullable=False)  # 열무 시장
    yeol_radish_M = db.Column(db.Float, nullable=False)  # 열무 대형마트
    dried_red_pepperD_T = db.Column(db.Float, nullable=False)  # 건고추(화건) 시장
    dried_red_pepperD_M = db.Column(db.Float, nullable=False)  # 건고추(화건) 대형마트
    dried_red_pepperS_T = db.Column(db.Float, nullable=False)  # 건고추(양건) 시장
    dried_red_pepperS_M = db.Column(db.Float, nullable=False)  # 건고추(양양건) 대형마트
    pepper_T = db.Column(db.Float, nullable=False)  # 풋고추 시장
    pepper_M = db.Column(db.Float, nullable=False)  # 풋고추 대형마트
    chilli_pepper_T = db.Column(db.Float, nullable=False)  # 꽈리고추 시장
    chilli_pepper_M = db.Column(db.Float, nullable=False)  # 꽈리고추 대형마트
    cheongyang_pepper_T = db.Column(db.Float, nullable=False)  # 청양고추 시장
    cheongyang_pepper_M = db.Column(db.Float, nullable=False)  # 청양고추 대형마트
    red_pepper_T = db.Column(db.Float, nullable=False)  # 붉은고추 시장
    red_pepper_M = db.Column(db.Float, nullable=False)  # 붉은고추 대형마트
    onion_T = db.Column(db.Float, nullable=False)  # 양파 시장
    onion_M = db.Column(db.Float, nullable=False)  # 양파 대형마트
    green_onion_T = db.Column(db.Float, nullable=False)  # 대파 시장
    green_onion_M = db.Column(db.Float, nullable=False)  # 대파 대형마트
    chives_T = db.Column(db.Float, nullable=False)  # 쪽파 시장
    chives_M = db.Column(db.Float, nullable=False)  # 쪽파 대형마트
    ginger_T = db.Column(db.Float, nullable=False)  # 생강 시장
    ginger_M = db.Column(db.Float, nullable=False)  # 생강 대형마트
    chili_powder_T = db.Column(db.Float, nullable=False)  # 고추가루 시장
    chili_powder_M = db.Column(db.Float, nullable=False)  # 고추가루 대형마트
    parsley_T = db.Column(db.Float, nullable=False)  # 미나리 시장
    parsley_M = db.Column(db.Float, nullable=False)  # 미나리 대형마트
    sesame_leaf_T = db.Column(db.Float, nullable=False)  # 깻잎 시장
    sesame_leaf_M = db.Column(db.Float, nullable=False)  # 깻잎 대형마트
    pimento_T = db.Column(db.Float, nullable=False)  # 피망 시장
    pimento_M = db.Column(db.Float, nullable=False)  # 피망 대형마트
    paprika_T = db.Column(db.Float, nullable=False)  # 파프리카 시장
    paprika_M = db.Column(db.Float, nullable=False)  # 파프리카 대형마트
    melon_T = db.Column(db.Float, nullable=False)  # 멜론 시장
    melon_M = db.Column(db.Float, nullable=False)  # 멜론 대형마트
    garlic_T = db.Column(db.Float, nullable=False)  # 깐마늘 시장
    garlic_M = db.Column(db.Float, nullable=False)  # 깐마늘 대형마트
    cherry_tomato_T = db.Column(db.Float, nullable=False)  # 방울토마토 시장
    cherry_tomato_M = db.Column(db.Float, nullable=False)  # 방울토마토 대형마트
    jujube_cherry_tomato_T = db.Column(db.Float, nullable=False)  # 대추방울토마토 시장
    jujube_cherry_tomato_M = db.Column(db.Float, nullable=False)  # 대추방울토마토 대형마트

    # 특용작물
    sesame_T = db.Column(db.Float, nullable=False)  # 참깨 시장
    sesame_M = db.Column(db.Float, nullable=False)  # 참깨 대형마트
    peanut_T = db.Column(db.Float, nullable=False)  # 땅콩 시장
    peanut_M = db.Column(db.Float, nullable=False)  # 땅콩 대형마트
    oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 느타리버섯 시장
    oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 느타리버섯 대형마트
    oyster_mushroomA_T = db.Column(db.Float, nullable=False)  # 애느타리버섯 시장
    oyster_mushroomA_M = db.Column(db.Float, nullable=False)  # 애느타리버섯 대형마트
    enoki_mushroom_T = db.Column(db.Float, nullable=False)  # 팽이버섯 시장
    enoki_mushroom_M = db.Column(db.Float, nullable=False)  # 팽이버섯 대형마트
    king_oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 새송이버섯 시장
    king_oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 새송이버섯 대형마트
    walnut_T = db.Column(db.Float, nullable=False)  # 호두 시장
    walnut_M = db.Column(db.Float, nullable=False)  # 호두 대형마트
    almond_T = db.Column(db.Float, nullable=False)  # 아몬드 시장
    almond_M = db.Column(db.Float, nullable=False)  # 아몬드 대형마트

    # 과일류
    appleF_T = db.Column(db.Float, nullable=False)  # 사과(후지) 시장
    appleF_M = db.Column(db.Float, nullable=False)  # 사과(후지) 대형마트
    appleT_T = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 시장
    appleT_M = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 대형마트
    appleR_T = db.Column(db.Float, nullable=False)  # 사과(홍로) 시장
    appleR_M = db.Column(db.Float, nullable=False)  # 사과(홍로) 대마트
    pearS_T = db.Column(db.Float, nullable=False)  # 배(신고) 시장
    pearS_M = db.Column(db.Float, nullable=False)  # 배(신고) 대형마트
    pearW_T = db.Column(db.Float, nullable=False)  # 배(원황) 시장
    pearW_M = db.Column(db.Float, nullable=False)  # 배(원황) 대형마트
    peach_T = db.Column(db.Float, nullable=False)  # 복숭아 시장
    peach_M = db.Column(db.Float, nullable=False)  # 복숭아 대형마트
    grapeC_T = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 시장
    grapeC_M = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 대형마트
    grapeG_T = db.Column(db.Float, nullable=False)  # 포도(거봉) 시장
    grapeG_M = db.Column(db.Float, nullable=False)  # 포도(거봉) 대형마트
    grapeM_T = db.Column(db.Float, nullable=False)  # 포도(MBA) 시장
    grapeM_M = db.Column(db.Float, nullable=False)  # 포도(MBA) 대형마트
    grapeS_T = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 시장
    grapeS_M = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 대형마트
    grapeR_T = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 시장
    grapeR_M = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 대형마트
    citrusR_T = db.Column(db.Float, nullable=False)  # 감귤(노지) 시장
    citrusR_M = db.Column(db.Float, nullable=False)  # 감귤(노지) 대형마트
    citrusH_T = db.Column(db.Float, nullable=False)  # 감귤(시설) 시장
    citrusH_M = db.Column(db.Float, nullable=False)  # 감귤(시설) 대형마트
    persimmon_T = db.Column(db.Float, nullable=False)  # 단감 시장
    persimmon_M = db.Column(db.Float, nullable=False)  # 단감 대형마트
    banana_T = db.Column(db.Float, nullable=False)  # 바나나 시장
    banana_M = db.Column(db.Float, nullable=False)  # 바나나 대형마트
    kiwiN_T = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 시장
    kiwiN_M = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 대형마트
    kiwiK_T = db.Column(db.Float, nullable=False)  # 참다래(국산) 시장
    kiwiK_M = db.Column(db.Float, nullable=False)  # 참다래(국산) 대형마트
    pineapple_T = db.Column(db.Float, nullable=False)  # 파인애플 시장
    pineapple_M = db.Column(db.Float, nullable=False)  # 파인애플 대형마트
    orangeU_T = db.Column(db.Float, nullable=False)  # 오렌지(미국) 시장
    orangeU_M = db.Column(db.Float, nullable=False)  # 오렌지(미국) 대형마트
    orangeA_T = db.Column(db.Float, nullable=False)  # 오렌지(호주) 시장
    orangeA_M = db.Column(db.Float, nullable=False)  # 오렌지(호주) 대형마트
    lemon_T = db.Column(db.Float, nullable=False)  # 레몬 시장
    lemon_M = db.Column(db.Float, nullable=False)  # 레몬 대형마트
    cherry_T = db.Column(db.Float, nullable=False)  # 체리 시장
    cherry_M = db.Column(db.Float, nullable=False)  # 체리 대형마트
    raisin_T = db.Column(db.Float, nullable=False)  # 건포도 시장
    raisin_M = db.Column(db.Float, nullable=False)  # 건포도 대형마트
    dried_blueberries_T = db.Column(db.Float, nullable=False)  # 건블루베리 시장
    dried_blueberries_M = db.Column(db.Float, nullable=False)  # 건블루베리 대형마트
    mango_T = db.Column(db.Float, nullable=False)  # 망고 시장
    mango_M = db.Column(db.Float, nullable=False)  # 망고 대형마트

    # 수산물
    mackerelL_T = db.Column(db.Float, nullable=False)  # 고등어(생물) 시장
    mackerelL_M = db.Column(db.Float, nullable=False)  # 고등어(생물) 대형마트
    mackerelF_T = db.Column(db.Float, nullable=False)  # 고등어(냉동) 시장
    mackerelF_M = db.Column(db.Float, nullable=False)  # 고등어(냉동) 대형마트
    mackerelS_T = db.Column(db.Float, nullable=False)  # 고등어(염장) 시장
    mackerelS_M = db.Column(db.Float, nullable=False)  # 고등어(염장) 대형마트
    saury_T = db.Column(db.Float, nullable=False)  # 꽁치 시장
    saury_M = db.Column(db.Float, nullable=False)  # 꽁치 대형마트
    cutlassfishL_T = db.Column(db.Float, nullable=False)  # 갈치(생물) 시장
    cutlassfishL_M = db.Column(db.Float, nullable=False)  # 갈치(생물) 대형마트
    cutlassfishF_T = db.Column(db.Float, nullable=False)  # 갈치(냉동) 시장
    cutlassfishF_M = db.Column(db.Float, nullable=False)  # 갈치(냉동) 대형마트
    pollock_T = db.Column(db.Float, nullable=False)  # 명태 시장
    pollock_M = db.Column(db.Float, nullable=False)  # 명태 대형마트
    squidL_T = db.Column(db.Float, nullable=False)  # 물오징어(생선) 시장
    squidL_M = db.Column(db.Float, nullable=False)  # 물오징어(생선) 대형마트
    squidF_T = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 시장
    squidF_M = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 대형마트
    dried_anchovies_T = db.Column(db.Float, nullable=False)  # 건멸치 시장
    dried_anchovies_M = db.Column(db.Float, nullable=False)  # 건멸치 대형마트
    dried_squid_T = db.Column(db.Float, nullable=False)  # 건오징어 시장
    dried_squid_M = db.Column(db.Float, nullable=False)  # 건오징어 대형마트
    seaweedD_T = db.Column(db.Float, nullable=False)  # 김(마른김) 시장
    seaweedD_M = db.Column(db.Float, nullable=False)  # 김(마른김) 대형마트
    seaweedF_T = db.Column(db.Float, nullable=False)  # 김(구운김) 시장
    seaweedF_M = db.Column(db.Float, nullable=False)  # 김(구운김) 대형마트
    dried_seaweed_T = db.Column(db.Float, nullable=False)  # 건미역 시장
    dried_seaweed_M = db.Column(db.Float, nullable=False)  # 건미역 대형마트
    oyster_T = db.Column(db.Float, nullable=False)  # 굴 시장
    oyster_M = db.Column(db.Float, nullable=False)  # 굴 대형마트
    yellow_corbina_T = db.Column(db.Float, nullable=False)  # 수입조기 시장
    yellow_corbina_M = db.Column(db.Float, nullable=False)  # 수입조기 대형마트
    salted_shrimp_T = db.Column(db.Float, nullable=False)  # 새우젓 시장
    salted_shrimp_M = db.Column(db.Float, nullable=False)  # 새우젓 대형마트
    anchovy_fish_sauce_T = db.Column(db.Float, nullable=False)  # 멸치액젓 시장
    anchovy_fish_sauce_M = db.Column(db.Float, nullable=False)  # 멸치액젓 대형마트
    salt_T = db.Column(db.Float, nullable=False)  # 굵은소금 시장
    salt_M = db.Column(db.Float, nullable=False)  # 굵은소금 대형마트
    abalone_T = db.Column(db.Float, nullable=False)  # 전복 시장
    abalone_M = db.Column(db.Float, nullable=False)  # 전복 대형마트
    shrimp_T = db.Column(db.Float, nullable=False)  # 흰다리새우 시장
    shrimp_M = db.Column(db.Float, nullable=False)  # 흰다리새우 대형마트


## 광주 소매
class Gwangju_retail(db.Model):
    date = db.Column(db.Integer, primary_key=True, nullable=False)  # 일자

    # 식량작물
    rice_T = db.Column(db.Float, nullable=False)  # 쌀 시장
    rice_M = db.Column(db.Float, nullable=False)  # 쌀 대형마트
    riceF_T = db.Column(db.Float, nullable=False)  # 햇쌀 시장
    riceF_M = db.Column(db.Float, nullable=False)  # 햇쌀 대형마트
    glutinous_rice_T = db.Column(db.Float, nullable=False)  # 찹쌀 시장
    glutinous_rice_M = db.Column(db.Float, nullable=False)  # 찹쌀 대형마트
    bean_T = db.Column(db.Float, nullable=False)  # 콩 시장
    bean_M = db.Column(db.Float, nullable=False)  # 콩 대형마트
    red_bean_T = db.Column(db.Float, nullable=False)  # 팥 시장
    red_bean_M = db.Column(db.Float, nullable=False)  # 팥 대형마트
    green_beans_T = db.Column(db.Float, nullable=False)  # 녹두 시장
    green_beans_M = db.Column(db.Float, nullable=False)  # 녹두 대형마트
    sweet_potato_T = db.Column(db.Float, nullable=False)  # 고구마 시장
    sweet_potato_M = db.Column(db.Float, nullable=False)  # 고구마 대형마트
    potato_T = db.Column(db.Float, nullable=False)  # 감자 시장
    potato_M = db.Column(db.Float, nullable=False)  # 감자 대형마트

    # 채소류
    napa_cabbageF_T = db.Column(db.Float, nullable=False)  # 배추(가을) 시장
    napa_cabbageF_M = db.Column(db.Float, nullable=False)  # 배추(가을) 대형마트
    napa_cabbageW_T = db.Column(db.Float, nullable=False)  # 배추(월동) 시장
    napa_cabbageW_M = db.Column(db.Float, nullable=False)  # 배추(월동) 대형마트
    napa_cabbageS_T = db.Column(db.Float, nullable=False)  # 배추(봄) 시장
    napa_cabbageS_M = db.Column(db.Float, nullable=False)  # 배추(봄) 대형마트
    napa_cabbageH_T = db.Column(db.Float, nullable=False)  # 배추(고랭지) 시장
    napa_cabbageH_M = db.Column(db.Float, nullable=False)  # 배추(고랭지) 대형마트
    cabbage_T = db.Column(db.Float, nullable=False)  # 양배추 시장
    cabbage_M = db.Column(db.Float, nullable=False)  # 양배추 대형마트
    spinach_T = db.Column(db.Float, nullable=False)  # 시금치 시장
    spinach_M = db.Column(db.Float, nullable=False)  # 시금치 대형마트
    lettuceR_T = db.Column(db.Float, nullable=False)  # 상추(적) 시장
    lettuceR_M = db.Column(db.Float, nullable=False)  # 상추(적) 대형마트
    lettuceB_T = db.Column(db.Float, nullable=False)  # 상추(청) 시장
    lettuceB_M = db.Column(db.Float, nullable=False)  # 상추(청) 대형마트
    winter_cabbage_T = db.Column(db.Float, nullable=False)  # 얼갈이배추 시장
    winter_cabbage_M = db.Column(db.Float, nullable=False)  # 얼갈이배추 대형마트
    leaf_mustard_T = db.Column(db.Float, nullable=False)  # 갓 시장
    leaf_mustard_M = db.Column(db.Float, nullable=False)  # 갓 대형마트
    watermelon_T = db.Column(db.Float, nullable=False)  # 수박 시장
    watermelon_M = db.Column(db.Float, nullable=False)  # 수박 대형마트
    korean_melon_T = db.Column(db.Float, nullable=False)  # 참외 시장
    korean_melon_M = db.Column(db.Float, nullable=False)  # 참외 대형마트
    cucumberS_T = db.Column(db.Float, nullable=False)  # 오이(가시계통) 시장
    cucumberS_M = db.Column(db.Float, nullable=False)  # 오이(가시계통) 대형마트
    cucumberD_T = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 시장
    cucumberD_M = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 대형마트
    cucumberW_T = db.Column(db.Float, nullable=False)  # 오이(취청) 시장
    cucumberW_M = db.Column(db.Float, nullable=False)  # 오이(취청) 대형마트
    squash_T = db.Column(db.Float, nullable=False)  # 애호박 시장
    squash_M = db.Column(db.Float, nullable=False)  # 애호박 대형마트
    zucchini_T = db.Column(db.Float, nullable=False)  # 주키니 시장
    zucchini_M = db.Column(db.Float, nullable=False)  # 주키니 대형마트
    tomato_T = db.Column(db.Float, nullable=False)  # 토마토 시장
    tomato_M = db.Column(db.Float, nullable=False)  # 토마토 대형마트
    strawberry_T = db.Column(db.Float, nullable=False)  # 딸기 시장
    strawberry_M = db.Column(db.Float, nullable=False)  # 딸기 대형마트
    radishF_T = db.Column(db.Float, nullable=False)  # 무(가을) 시장
    radishF_M = db.Column(db.Float, nullable=False)  # 무(가을) 대형마트
    radishW_T = db.Column(db.Float, nullable=False)  # 무(월동) 시장
    radishW_M = db.Column(db.Float, nullable=False)  # 무(월동) 대형마트
    radishS_T = db.Column(db.Float, nullable=False)  # 무(봄) 시장
    radishS_M = db.Column(db.Float, nullable=False)  # 무(봄) 대형마트
    radishH_T = db.Column(db.Float, nullable=False)  # 무(고랭지) 시장
    radishH_M = db.Column(db.Float, nullable=False)  # 무(고랭지) 대형마트
    carrot_T = db.Column(db.Float, nullable=False)  # 당근 시장
    carrot_M = db.Column(db.Float, nullable=False)  # 당근 대형마트
    yeol_radish_T = db.Column(db.Float, nullable=False)  # 열무 시장
    yeol_radish_M = db.Column(db.Float, nullable=False)  # 열무 대형마트
    dried_red_pepperD_T = db.Column(db.Float, nullable=False)  # 건고추(화건) 시장
    dried_red_pepperD_M = db.Column(db.Float, nullable=False)  # 건고추(화건) 대형마트
    dried_red_pepperS_T = db.Column(db.Float, nullable=False)  # 건고추(양건) 시장
    dried_red_pepperS_M = db.Column(db.Float, nullable=False)  # 건고추(양양건) 대형마트
    pepper_T = db.Column(db.Float, nullable=False)  # 풋고추 시장
    pepper_M = db.Column(db.Float, nullable=False)  # 풋고추 대형마트
    chilli_pepper_T = db.Column(db.Float, nullable=False)  # 꽈리고추 시장
    chilli_pepper_M = db.Column(db.Float, nullable=False)  # 꽈리고추 대형마트
    cheongyang_pepper_T = db.Column(db.Float, nullable=False)  # 청양고추 시장
    cheongyang_pepper_M = db.Column(db.Float, nullable=False)  # 청양고추 대형마트
    red_pepper_T = db.Column(db.Float, nullable=False)  # 붉은고추 시장
    red_pepper_M = db.Column(db.Float, nullable=False)  # 붉은고추 대형마트
    onion_T = db.Column(db.Float, nullable=False)  # 양파 시장
    onion_M = db.Column(db.Float, nullable=False)  # 양파 대형마트
    green_onion_T = db.Column(db.Float, nullable=False)  # 대파 시장
    green_onion_M = db.Column(db.Float, nullable=False)  # 대파 대형마트
    chives_T = db.Column(db.Float, nullable=False)  # 쪽파 시장
    chives_M = db.Column(db.Float, nullable=False)  # 쪽파 대형마트
    ginger_T = db.Column(db.Float, nullable=False)  # 생강 시장
    ginger_M = db.Column(db.Float, nullable=False)  # 생강 대형마트
    chili_powder_T = db.Column(db.Float, nullable=False)  # 고추가루 시장
    chili_powder_M = db.Column(db.Float, nullable=False)  # 고추가루 대형마트
    parsley_T = db.Column(db.Float, nullable=False)  # 미나리 시장
    parsley_M = db.Column(db.Float, nullable=False)  # 미나리 대형마트
    sesame_leaf_T = db.Column(db.Float, nullable=False)  # 깻잎 시장
    sesame_leaf_M = db.Column(db.Float, nullable=False)  # 깻잎 대형마트
    pimento_T = db.Column(db.Float, nullable=False)  # 피망 시장
    pimento_M = db.Column(db.Float, nullable=False)  # 피망 대형마트
    paprika_T = db.Column(db.Float, nullable=False)  # 파프리카 시장
    paprika_M = db.Column(db.Float, nullable=False)  # 파프리카 대형마트
    melon_T = db.Column(db.Float, nullable=False)  # 멜론 시장
    melon_M = db.Column(db.Float, nullable=False)  # 멜론 대형마트
    garlic_T = db.Column(db.Float, nullable=False)  # 깐마늘 시장
    garlic_M = db.Column(db.Float, nullable=False)  # 깐마늘 대형마트
    cherry_tomato_T = db.Column(db.Float, nullable=False)  # 방울토마토 시장
    cherry_tomato_M = db.Column(db.Float, nullable=False)  # 방울토마토 대형마트
    jujube_cherry_tomato_T = db.Column(db.Float, nullable=False)  # 대추방울토마토 시장
    jujube_cherry_tomato_M = db.Column(db.Float, nullable=False)  # 대추방울토마토 대형마트

    # 특용작물
    sesame_T = db.Column(db.Float, nullable=False)  # 참깨 시장
    sesame_M = db.Column(db.Float, nullable=False)  # 참깨 대형마트
    peanut_T = db.Column(db.Float, nullable=False)  # 땅콩 시장
    peanut_M = db.Column(db.Float, nullable=False)  # 땅콩 대형마트
    oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 느타리버섯 시장
    oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 느타리버섯 대형마트
    oyster_mushroomA_T = db.Column(db.Float, nullable=False)  # 애느타리버섯 시장
    oyster_mushroomA_M = db.Column(db.Float, nullable=False)  # 애느타리버섯 대형마트
    enoki_mushroom_T = db.Column(db.Float, nullable=False)  # 팽이버섯 시장
    enoki_mushroom_M = db.Column(db.Float, nullable=False)  # 팽이버섯 대형마트
    king_oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 새송이버섯 시장
    king_oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 새송이버섯 대형마트
    walnut_T = db.Column(db.Float, nullable=False)  # 호두 시장
    walnut_M = db.Column(db.Float, nullable=False)  # 호두 대형마트
    almond_T = db.Column(db.Float, nullable=False)  # 아몬드 시장
    almond_M = db.Column(db.Float, nullable=False)  # 아몬드 대형마트

    # 과일류
    appleF_T = db.Column(db.Float, nullable=False)  # 사과(후지) 시장
    appleF_M = db.Column(db.Float, nullable=False)  # 사과(후지) 대형마트
    appleT_T = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 시장
    appleT_M = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 대형마트
    appleR_T = db.Column(db.Float, nullable=False)  # 사과(홍로) 시장
    appleR_M = db.Column(db.Float, nullable=False)  # 사과(홍로) 대마트
    pearS_T = db.Column(db.Float, nullable=False)  # 배(신고) 시장
    pearS_M = db.Column(db.Float, nullable=False)  # 배(신고) 대형마트
    pearW_T = db.Column(db.Float, nullable=False)  # 배(원황) 시장
    pearW_M = db.Column(db.Float, nullable=False)  # 배(원황) 대형마트
    peach_T = db.Column(db.Float, nullable=False)  # 복숭아 시장
    peach_M = db.Column(db.Float, nullable=False)  # 복숭아 대형마트
    grapeC_T = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 시장
    grapeC_M = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 대형마트
    grapeG_T = db.Column(db.Float, nullable=False)  # 포도(거봉) 시장
    grapeG_M = db.Column(db.Float, nullable=False)  # 포도(거봉) 대형마트
    grapeM_T = db.Column(db.Float, nullable=False)  # 포도(MBA) 시장
    grapeM_M = db.Column(db.Float, nullable=False)  # 포도(MBA) 대형마트
    grapeS_T = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 시장
    grapeS_M = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 대형마트
    grapeR_T = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 시장
    grapeR_M = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 대형마트
    citrusR_T = db.Column(db.Float, nullable=False)  # 감귤(노지) 시장
    citrusR_M = db.Column(db.Float, nullable=False)  # 감귤(노지) 대형마트
    citrusH_T = db.Column(db.Float, nullable=False)  # 감귤(시설) 시장
    citrusH_M = db.Column(db.Float, nullable=False)  # 감귤(시설) 대형마트
    persimmon_T = db.Column(db.Float, nullable=False)  # 단감 시장
    persimmon_M = db.Column(db.Float, nullable=False)  # 단감 대형마트
    banana_T = db.Column(db.Float, nullable=False)  # 바나나 시장
    banana_M = db.Column(db.Float, nullable=False)  # 바나나 대형마트
    kiwiN_T = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 시장
    kiwiN_M = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 대형마트
    kiwiK_T = db.Column(db.Float, nullable=False)  # 참다래(국산) 시장
    kiwiK_M = db.Column(db.Float, nullable=False)  # 참다래(국산) 대형마트
    pineapple_T = db.Column(db.Float, nullable=False)  # 파인애플 시장
    pineapple_M = db.Column(db.Float, nullable=False)  # 파인애플 대형마트
    orangeU_T = db.Column(db.Float, nullable=False)  # 오렌지(미국) 시장
    orangeU_M = db.Column(db.Float, nullable=False)  # 오렌지(미국) 대형마트
    orangeA_T = db.Column(db.Float, nullable=False)  # 오렌지(호주) 시장
    orangeA_M = db.Column(db.Float, nullable=False)  # 오렌지(호주) 대형마트
    lemon_T = db.Column(db.Float, nullable=False)  # 레몬 시장
    lemon_M = db.Column(db.Float, nullable=False)  # 레몬 대형마트
    cherry_T = db.Column(db.Float, nullable=False)  # 체리 시장
    cherry_M = db.Column(db.Float, nullable=False)  # 체리 대형마트
    raisin_T = db.Column(db.Float, nullable=False)  # 건포도 시장
    raisin_M = db.Column(db.Float, nullable=False)  # 건포도 대형마트
    dried_blueberries_T = db.Column(db.Float, nullable=False)  # 건블루베리 시장
    dried_blueberries_M = db.Column(db.Float, nullable=False)  # 건블루베리 대형마트
    mango_T = db.Column(db.Float, nullable=False)  # 망고 시장
    mango_M = db.Column(db.Float, nullable=False)  # 망고 대형마트

    # 수산물
    mackerelL_T = db.Column(db.Float, nullable=False)  # 고등어(생물) 시장
    mackerelL_M = db.Column(db.Float, nullable=False)  # 고등어(생물) 대형마트
    mackerelF_T = db.Column(db.Float, nullable=False)  # 고등어(냉동) 시장
    mackerelF_M = db.Column(db.Float, nullable=False)  # 고등어(냉동) 대형마트
    mackerelS_T = db.Column(db.Float, nullable=False)  # 고등어(염장) 시장
    mackerelS_M = db.Column(db.Float, nullable=False)  # 고등어(염장) 대형마트
    saury_T = db.Column(db.Float, nullable=False)  # 꽁치 시장
    saury_M = db.Column(db.Float, nullable=False)  # 꽁치 대형마트
    cutlassfishL_T = db.Column(db.Float, nullable=False)  # 갈치(생물) 시장
    cutlassfishL_M = db.Column(db.Float, nullable=False)  # 갈치(생물) 대형마트
    cutlassfishF_T = db.Column(db.Float, nullable=False)  # 갈치(냉동) 시장
    cutlassfishF_M = db.Column(db.Float, nullable=False)  # 갈치(냉동) 대형마트
    pollock_T = db.Column(db.Float, nullable=False)  # 명태 시장
    pollock_M = db.Column(db.Float, nullable=False)  # 명태 대형마트
    squidL_T = db.Column(db.Float, nullable=False)  # 물오징어(생선) 시장
    squidL_M = db.Column(db.Float, nullable=False)  # 물오징어(생선) 대형마트
    squidF_T = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 시장
    squidF_M = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 대형마트
    dried_anchovies_T = db.Column(db.Float, nullable=False)  # 건멸치 시장
    dried_anchovies_M = db.Column(db.Float, nullable=False)  # 건멸치 대형마트
    dried_squid_T = db.Column(db.Float, nullable=False)  # 건오징어 시장
    dried_squid_M = db.Column(db.Float, nullable=False)  # 건오징어 대형마트
    seaweedD_T = db.Column(db.Float, nullable=False)  # 김(마른김) 시장
    seaweedD_M = db.Column(db.Float, nullable=False)  # 김(마른김) 대형마트
    seaweedF_T = db.Column(db.Float, nullable=False)  # 김(구운김) 시장
    seaweedF_M = db.Column(db.Float, nullable=False)  # 김(구운김) 대형마트
    dried_seaweed_T = db.Column(db.Float, nullable=False)  # 건미역 시장
    dried_seaweed_M = db.Column(db.Float, nullable=False)  # 건미역 대형마트
    oyster_T = db.Column(db.Float, nullable=False)  # 굴 시장
    oyster_M = db.Column(db.Float, nullable=False)  # 굴 대형마트
    yellow_corbina_T = db.Column(db.Float, nullable=False)  # 수입조기 시장
    yellow_corbina_M = db.Column(db.Float, nullable=False)  # 수입조기 대형마트
    salted_shrimp_T = db.Column(db.Float, nullable=False)  # 새우젓 시장
    salted_shrimp_M = db.Column(db.Float, nullable=False)  # 새우젓 대형마트
    anchovy_fish_sauce_T = db.Column(db.Float, nullable=False)  # 멸치액젓 시장
    anchovy_fish_sauce_M = db.Column(db.Float, nullable=False)  # 멸치액젓 대형마트
    salt_T = db.Column(db.Float, nullable=False)  # 굵은소금 시장
    salt_M = db.Column(db.Float, nullable=False)  # 굵은소금 대형마트
    abalone_T = db.Column(db.Float, nullable=False)  # 전복 시장
    abalone_M = db.Column(db.Float, nullable=False)  # 전복 대형마트
    shrimp_T = db.Column(db.Float, nullable=False)  # 흰다리새우 시장
    shrimp_M = db.Column(db.Float, nullable=False)  # 흰다리새우 대형마트


## 울산 소매
class Ulsan_retail(db.Model):
    date = db.Column(db.Integer, primary_key=True, nullable=False)  # 일자

    # 식량작물
    rice_T = db.Column(db.Float, nullable=False)  # 쌀 시장
    rice_M = db.Column(db.Float, nullable=False)  # 쌀 대형마트
    riceF_T = db.Column(db.Float, nullable=False)  # 햇쌀 시장
    riceF_M = db.Column(db.Float, nullable=False)  # 햇쌀 대형마트
    glutinous_rice_T = db.Column(db.Float, nullable=False)  # 찹쌀 시장
    glutinous_rice_M = db.Column(db.Float, nullable=False)  # 찹쌀 대형마트
    bean_T = db.Column(db.Float, nullable=False)  # 콩 시장
    bean_M = db.Column(db.Float, nullable=False)  # 콩 대형마트
    red_bean_T = db.Column(db.Float, nullable=False)  # 팥 시장
    red_bean_M = db.Column(db.Float, nullable=False)  # 팥 대형마트
    green_beans_T = db.Column(db.Float, nullable=False)  # 녹두 시장
    green_beans_M = db.Column(db.Float, nullable=False)  # 녹두 대형마트
    sweet_potato_T = db.Column(db.Float, nullable=False)  # 고구마 시장
    sweet_potato_M = db.Column(db.Float, nullable=False)  # 고구마 대형마트
    potato_T = db.Column(db.Float, nullable=False)  # 감자 시장
    potato_M = db.Column(db.Float, nullable=False)  # 감자 대형마트

    # 채소류
    napa_cabbageF_T = db.Column(db.Float, nullable=False)  # 배추(가을) 시장
    napa_cabbageF_M = db.Column(db.Float, nullable=False)  # 배추(가을) 대형마트
    napa_cabbageW_T = db.Column(db.Float, nullable=False)  # 배추(월동) 시장
    napa_cabbageW_M = db.Column(db.Float, nullable=False)  # 배추(월동) 대형마트
    napa_cabbageS_T = db.Column(db.Float, nullable=False)  # 배추(봄) 시장
    napa_cabbageS_M = db.Column(db.Float, nullable=False)  # 배추(봄) 대형마트
    napa_cabbageH_T = db.Column(db.Float, nullable=False)  # 배추(고랭지) 시장
    napa_cabbageH_M = db.Column(db.Float, nullable=False)  # 배추(고랭지) 대형마트
    cabbage_T = db.Column(db.Float, nullable=False)  # 양배추 시장
    cabbage_M = db.Column(db.Float, nullable=False)  # 양배추 대형마트
    spinach_T = db.Column(db.Float, nullable=False)  # 시금치 시장
    spinach_M = db.Column(db.Float, nullable=False)  # 시금치 대형마트
    lettuceR_T = db.Column(db.Float, nullable=False)  # 상추(적) 시장
    lettuceR_M = db.Column(db.Float, nullable=False)  # 상추(적) 대형마트
    lettuceB_T = db.Column(db.Float, nullable=False)  # 상추(청) 시장
    lettuceB_M = db.Column(db.Float, nullable=False)  # 상추(청) 대형마트
    winter_cabbage_T = db.Column(db.Float, nullable=False)  # 얼갈이배추 시장
    winter_cabbage_M = db.Column(db.Float, nullable=False)  # 얼갈이배추 대형마트
    leaf_mustard_T = db.Column(db.Float, nullable=False)  # 갓 시장
    leaf_mustard_M = db.Column(db.Float, nullable=False)  # 갓 대형마트
    watermelon_T = db.Column(db.Float, nullable=False)  # 수박 시장
    watermelon_M = db.Column(db.Float, nullable=False)  # 수박 대형마트
    korean_melon_T = db.Column(db.Float, nullable=False)  # 참외 시장
    korean_melon_M = db.Column(db.Float, nullable=False)  # 참외 대형마트
    cucumberS_T = db.Column(db.Float, nullable=False)  # 오이(가시계통) 시장
    cucumberS_M = db.Column(db.Float, nullable=False)  # 오이(가시계통) 대형마트
    cucumberD_T = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 시장
    cucumberD_M = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 대형마트
    cucumberW_T = db.Column(db.Float, nullable=False)  # 오이(취청) 시장
    cucumberW_M = db.Column(db.Float, nullable=False)  # 오이(취청) 대형마트
    squash_T = db.Column(db.Float, nullable=False)  # 애호박 시장
    squash_M = db.Column(db.Float, nullable=False)  # 애호박 대형마트
    zucchini_T = db.Column(db.Float, nullable=False)  # 주키니 시장
    zucchini_M = db.Column(db.Float, nullable=False)  # 주키니 대형마트
    tomato_T = db.Column(db.Float, nullable=False)  # 토마토 시장
    tomato_M = db.Column(db.Float, nullable=False)  # 토마토 대형마트
    strawberry_T = db.Column(db.Float, nullable=False)  # 딸기 시장
    strawberry_M = db.Column(db.Float, nullable=False)  # 딸기 대형마트
    radishF_T = db.Column(db.Float, nullable=False)  # 무(가을) 시장
    radishF_M = db.Column(db.Float, nullable=False)  # 무(가을) 대형마트
    radishW_T = db.Column(db.Float, nullable=False)  # 무(월동) 시장
    radishW_M = db.Column(db.Float, nullable=False)  # 무(월동) 대형마트
    radishS_T = db.Column(db.Float, nullable=False)  # 무(봄) 시장
    radishS_M = db.Column(db.Float, nullable=False)  # 무(봄) 대형마트
    radishH_T = db.Column(db.Float, nullable=False)  # 무(고랭지) 시장
    radishH_M = db.Column(db.Float, nullable=False)  # 무(고랭지) 대형마트
    carrot_T = db.Column(db.Float, nullable=False)  # 당근 시장
    carrot_M = db.Column(db.Float, nullable=False)  # 당근 대형마트
    yeol_radish_T = db.Column(db.Float, nullable=False)  # 열무 시장
    yeol_radish_M = db.Column(db.Float, nullable=False)  # 열무 대형마트
    dried_red_pepperD_T = db.Column(db.Float, nullable=False)  # 건고추(화건) 시장
    dried_red_pepperD_M = db.Column(db.Float, nullable=False)  # 건고추(화건) 대형마트
    dried_red_pepperS_T = db.Column(db.Float, nullable=False)  # 건고추(양건) 시장
    dried_red_pepperS_M = db.Column(db.Float, nullable=False)  # 건고추(양양건) 대형마트
    pepper_T = db.Column(db.Float, nullable=False)  # 풋고추 시장
    pepper_M = db.Column(db.Float, nullable=False)  # 풋고추 대형마트
    chilli_pepper_T = db.Column(db.Float, nullable=False)  # 꽈리고추 시장
    chilli_pepper_M = db.Column(db.Float, nullable=False)  # 꽈리고추 대형마트
    cheongyang_pepper_T = db.Column(db.Float, nullable=False)  # 청양고추 시장
    cheongyang_pepper_M = db.Column(db.Float, nullable=False)  # 청양고추 대형마트
    red_pepper_T = db.Column(db.Float, nullable=False)  # 붉은고추 시장
    red_pepper_M = db.Column(db.Float, nullable=False)  # 붉은고추 대형마트
    onion_T = db.Column(db.Float, nullable=False)  # 양파 시장
    onion_M = db.Column(db.Float, nullable=False)  # 양파 대형마트
    green_onion_T = db.Column(db.Float, nullable=False)  # 대파 시장
    green_onion_M = db.Column(db.Float, nullable=False)  # 대파 대형마트
    chives_T = db.Column(db.Float, nullable=False)  # 쪽파 시장
    chives_M = db.Column(db.Float, nullable=False)  # 쪽파 대형마트
    ginger_T = db.Column(db.Float, nullable=False)  # 생강 시장
    ginger_M = db.Column(db.Float, nullable=False)  # 생강 대형마트
    chili_powder_T = db.Column(db.Float, nullable=False)  # 고추가루 시장
    chili_powder_M = db.Column(db.Float, nullable=False)  # 고추가루 대형마트
    parsley_T = db.Column(db.Float, nullable=False)  # 미나리 시장
    parsley_M = db.Column(db.Float, nullable=False)  # 미나리 대형마트
    sesame_leaf_T = db.Column(db.Float, nullable=False)  # 깻잎 시장
    sesame_leaf_M = db.Column(db.Float, nullable=False)  # 깻잎 대형마트
    pimento_T = db.Column(db.Float, nullable=False)  # 피망 시장
    pimento_M = db.Column(db.Float, nullable=False)  # 피망 대형마트
    paprika_T = db.Column(db.Float, nullable=False)  # 파프리카 시장
    paprika_M = db.Column(db.Float, nullable=False)  # 파프리카 대형마트
    melon_T = db.Column(db.Float, nullable=False)  # 멜론 시장
    melon_M = db.Column(db.Float, nullable=False)  # 멜론 대형마트
    garlic_T = db.Column(db.Float, nullable=False)  # 깐마늘 시장
    garlic_M = db.Column(db.Float, nullable=False)  # 깐마늘 대형마트
    cherry_tomato_T = db.Column(db.Float, nullable=False)  # 방울토마토 시장
    cherry_tomato_M = db.Column(db.Float, nullable=False)  # 방울토마토 대형마트
    jujube_cherry_tomato_T = db.Column(db.Float, nullable=False)  # 대추방울토마토 시장
    jujube_cherry_tomato_M = db.Column(db.Float, nullable=False)  # 대추방울토마토 대형마트

    # 특용작물
    sesame_T = db.Column(db.Float, nullable=False)  # 참깨 시장
    sesame_M = db.Column(db.Float, nullable=False)  # 참깨 대형마트
    peanut_T = db.Column(db.Float, nullable=False)  # 땅콩 시장
    peanut_M = db.Column(db.Float, nullable=False)  # 땅콩 대형마트
    oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 느타리버섯 시장
    oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 느타리버섯 대형마트
    oyster_mushroomA_T = db.Column(db.Float, nullable=False)  # 애느타리버섯 시장
    oyster_mushroomA_M = db.Column(db.Float, nullable=False)  # 애느타리버섯 대형마트
    enoki_mushroom_T = db.Column(db.Float, nullable=False)  # 팽이버섯 시장
    enoki_mushroom_M = db.Column(db.Float, nullable=False)  # 팽이버섯 대형마트
    king_oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 새송이버섯 시장
    king_oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 새송이버섯 대형마트
    walnut_T = db.Column(db.Float, nullable=False)  # 호두 시장
    walnut_M = db.Column(db.Float, nullable=False)  # 호두 대형마트
    almond_T = db.Column(db.Float, nullable=False)  # 아몬드 시장
    almond_M = db.Column(db.Float, nullable=False)  # 아몬드 대형마트

    # 과일류
    appleF_T = db.Column(db.Float, nullable=False)  # 사과(후지) 시장
    appleF_M = db.Column(db.Float, nullable=False)  # 사과(후지) 대형마트
    appleT_T = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 시장
    appleT_M = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 대형마트
    appleR_T = db.Column(db.Float, nullable=False)  # 사과(홍로) 시장
    appleR_M = db.Column(db.Float, nullable=False)  # 사과(홍로) 대마트
    pearS_T = db.Column(db.Float, nullable=False)  # 배(신고) 시장
    pearS_M = db.Column(db.Float, nullable=False)  # 배(신고) 대형마트
    pearW_T = db.Column(db.Float, nullable=False)  # 배(원황) 시장
    pearW_M = db.Column(db.Float, nullable=False)  # 배(원황) 대형마트
    peach_T = db.Column(db.Float, nullable=False)  # 복숭아 시장
    peach_M = db.Column(db.Float, nullable=False)  # 복숭아 대형마트
    grapeC_T = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 시장
    grapeC_M = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 대형마트
    grapeG_T = db.Column(db.Float, nullable=False)  # 포도(거봉) 시장
    grapeG_M = db.Column(db.Float, nullable=False)  # 포도(거봉) 대형마트
    grapeM_T = db.Column(db.Float, nullable=False)  # 포도(MBA) 시장
    grapeM_M = db.Column(db.Float, nullable=False)  # 포도(MBA) 대형마트
    grapeS_T = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 시장
    grapeS_M = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 대형마트
    grapeR_T = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 시장
    grapeR_M = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 대형마트
    citrusR_T = db.Column(db.Float, nullable=False)  # 감귤(노지) 시장
    citrusR_M = db.Column(db.Float, nullable=False)  # 감귤(노지) 대형마트
    citrusH_T = db.Column(db.Float, nullable=False)  # 감귤(시설) 시장
    citrusH_M = db.Column(db.Float, nullable=False)  # 감귤(시설) 대형마트
    persimmon_T = db.Column(db.Float, nullable=False)  # 단감 시장
    persimmon_M = db.Column(db.Float, nullable=False)  # 단감 대형마트
    banana_T = db.Column(db.Float, nullable=False)  # 바나나 시장
    banana_M = db.Column(db.Float, nullable=False)  # 바나나 대형마트
    kiwiN_T = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 시장
    kiwiN_M = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 대형마트
    kiwiK_T = db.Column(db.Float, nullable=False)  # 참다래(국산) 시장
    kiwiK_M = db.Column(db.Float, nullable=False)  # 참다래(국산) 대형마트
    pineapple_T = db.Column(db.Float, nullable=False)  # 파인애플 시장
    pineapple_M = db.Column(db.Float, nullable=False)  # 파인애플 대형마트
    orangeU_T = db.Column(db.Float, nullable=False)  # 오렌지(미국) 시장
    orangeU_M = db.Column(db.Float, nullable=False)  # 오렌지(미국) 대형마트
    orangeA_T = db.Column(db.Float, nullable=False)  # 오렌지(호주) 시장
    orangeA_M = db.Column(db.Float, nullable=False)  # 오렌지(호주) 대형마트
    lemon_T = db.Column(db.Float, nullable=False)  # 레몬 시장
    lemon_M = db.Column(db.Float, nullable=False)  # 레몬 대형마트
    cherry_T = db.Column(db.Float, nullable=False)  # 체리 시장
    cherry_M = db.Column(db.Float, nullable=False)  # 체리 대형마트
    raisin_T = db.Column(db.Float, nullable=False)  # 건포도 시장
    raisin_M = db.Column(db.Float, nullable=False)  # 건포도 대형마트
    dried_blueberries_T = db.Column(db.Float, nullable=False)  # 건블루베리 시장
    dried_blueberries_M = db.Column(db.Float, nullable=False)  # 건블루베리 대형마트
    mango_T = db.Column(db.Float, nullable=False)  # 망고 시장
    mango_M = db.Column(db.Float, nullable=False)  # 망고 대형마트

    # 수산물
    mackerelL_T = db.Column(db.Float, nullable=False)  # 고등어(생물) 시장
    mackerelL_M = db.Column(db.Float, nullable=False)  # 고등어(생물) 대형마트
    mackerelF_T = db.Column(db.Float, nullable=False)  # 고등어(냉동) 시장
    mackerelF_M = db.Column(db.Float, nullable=False)  # 고등어(냉동) 대형마트
    mackerelS_T = db.Column(db.Float, nullable=False)  # 고등어(염장) 시장
    mackerelS_M = db.Column(db.Float, nullable=False)  # 고등어(염장) 대형마트
    saury_T = db.Column(db.Float, nullable=False)  # 꽁치 시장
    saury_M = db.Column(db.Float, nullable=False)  # 꽁치 대형마트
    cutlassfishL_T = db.Column(db.Float, nullable=False)  # 갈치(생물) 시장
    cutlassfishL_M = db.Column(db.Float, nullable=False)  # 갈치(생물) 대형마트
    cutlassfishF_T = db.Column(db.Float, nullable=False)  # 갈치(냉동) 시장
    cutlassfishF_M = db.Column(db.Float, nullable=False)  # 갈치(냉동) 대형마트
    pollock_T = db.Column(db.Float, nullable=False)  # 명태 시장
    pollock_M = db.Column(db.Float, nullable=False)  # 명태 대형마트
    squidL_T = db.Column(db.Float, nullable=False)  # 물오징어(생선) 시장
    squidL_M = db.Column(db.Float, nullable=False)  # 물오징어(생선) 대형마트
    squidF_T = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 시장
    squidF_M = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 대형마트
    dried_anchovies_T = db.Column(db.Float, nullable=False)  # 건멸치 시장
    dried_anchovies_M = db.Column(db.Float, nullable=False)  # 건멸치 대형마트
    dried_squid_T = db.Column(db.Float, nullable=False)  # 건오징어 시장
    dried_squid_M = db.Column(db.Float, nullable=False)  # 건오징어 대형마트
    seaweedD_T = db.Column(db.Float, nullable=False)  # 김(마른김) 시장
    seaweedD_M = db.Column(db.Float, nullable=False)  # 김(마른김) 대형마트
    seaweedF_T = db.Column(db.Float, nullable=False)  # 김(구운김) 시장
    seaweedF_M = db.Column(db.Float, nullable=False)  # 김(구운김) 대형마트
    dried_seaweed_T = db.Column(db.Float, nullable=False)  # 건미역 시장
    dried_seaweed_M = db.Column(db.Float, nullable=False)  # 건미역 대형마트
    oyster_T = db.Column(db.Float, nullable=False)  # 굴 시장
    oyster_M = db.Column(db.Float, nullable=False)  # 굴 대형마트
    yellow_corbina_T = db.Column(db.Float, nullable=False)  # 수입조기 시장
    yellow_corbina_M = db.Column(db.Float, nullable=False)  # 수입조기 대형마트
    salted_shrimp_T = db.Column(db.Float, nullable=False)  # 새우젓 시장
    salted_shrimp_M = db.Column(db.Float, nullable=False)  # 새우젓 대형마트
    anchovy_fish_sauce_T = db.Column(db.Float, nullable=False)  # 멸치액젓 시장
    anchovy_fish_sauce_M = db.Column(db.Float, nullable=False)  # 멸치액젓 대형마트
    salt_T = db.Column(db.Float, nullable=False)  # 굵은소금 시장
    salt_M = db.Column(db.Float, nullable=False)  # 굵은소금 대형마트
    abalone_T = db.Column(db.Float, nullable=False)  # 전복 시장
    abalone_M = db.Column(db.Float, nullable=False)  # 전복 대형마트
    shrimp_T = db.Column(db.Float, nullable=False)  # 흰다리새우 시장
    shrimp_M = db.Column(db.Float, nullable=False)  # 흰다리새우 대형마트


## 부산 소매
class Busan_retail(db.Model):
    date = db.Column(db.Integer, primary_key=True, nullable=False)  # 일자

    # 식량작물
    rice_T = db.Column(db.Float, nullable=False)  # 쌀 시장
    rice_M = db.Column(db.Float, nullable=False)  # 쌀 대형마트
    riceF_T = db.Column(db.Float, nullable=False)  # 햇쌀 시장
    riceF_M = db.Column(db.Float, nullable=False)  # 햇쌀 대형마트
    glutinous_rice_T = db.Column(db.Float, nullable=False)  # 찹쌀 시장
    glutinous_rice_M = db.Column(db.Float, nullable=False)  # 찹쌀 대형마트
    bean_T = db.Column(db.Float, nullable=False)  # 콩 시장
    bean_M = db.Column(db.Float, nullable=False)  # 콩 대형마트
    red_bean_T = db.Column(db.Float, nullable=False)  # 팥 시장
    red_bean_M = db.Column(db.Float, nullable=False)  # 팥 대형마트
    green_beans_T = db.Column(db.Float, nullable=False)  # 녹두 시장
    green_beans_M = db.Column(db.Float, nullable=False)  # 녹두 대형마트
    sweet_potato_T = db.Column(db.Float, nullable=False)  # 고구마 시장
    sweet_potato_M = db.Column(db.Float, nullable=False)  # 고구마 대형마트
    potato_T = db.Column(db.Float, nullable=False)  # 감자 시장
    potato_M = db.Column(db.Float, nullable=False)  # 감자 대형마트

    # 채소류
    napa_cabbageF_T = db.Column(db.Float, nullable=False)  # 배추(가을) 시장
    napa_cabbageF_M = db.Column(db.Float, nullable=False)  # 배추(가을) 대형마트
    napa_cabbageW_T = db.Column(db.Float, nullable=False)  # 배추(월동) 시장
    napa_cabbageW_M = db.Column(db.Float, nullable=False)  # 배추(월동) 대형마트
    napa_cabbageS_T = db.Column(db.Float, nullable=False)  # 배추(봄) 시장
    napa_cabbageS_M = db.Column(db.Float, nullable=False)  # 배추(봄) 대형마트
    napa_cabbageH_T = db.Column(db.Float, nullable=False)  # 배추(고랭지) 시장
    napa_cabbageH_M = db.Column(db.Float, nullable=False)  # 배추(고랭지) 대형마트
    cabbage_T = db.Column(db.Float, nullable=False)  # 양배추 시장
    cabbage_M = db.Column(db.Float, nullable=False)  # 양배추 대형마트
    spinach_T = db.Column(db.Float, nullable=False)  # 시금치 시장
    spinach_M = db.Column(db.Float, nullable=False)  # 시금치 대형마트
    lettuceR_T = db.Column(db.Float, nullable=False)  # 상추(적) 시장
    lettuceR_M = db.Column(db.Float, nullable=False)  # 상추(적) 대형마트
    lettuceB_T = db.Column(db.Float, nullable=False)  # 상추(청) 시장
    lettuceB_M = db.Column(db.Float, nullable=False)  # 상추(청) 대형마트
    winter_cabbage_T = db.Column(db.Float, nullable=False)  # 얼갈이배추 시장
    winter_cabbage_M = db.Column(db.Float, nullable=False)  # 얼갈이배추 대형마트
    leaf_mustard_T = db.Column(db.Float, nullable=False)  # 갓 시장
    leaf_mustard_M = db.Column(db.Float, nullable=False)  # 갓 대형마트
    watermelon_T = db.Column(db.Float, nullable=False)  # 수박 시장
    watermelon_M = db.Column(db.Float, nullable=False)  # 수박 대형마트
    korean_melon_T = db.Column(db.Float, nullable=False)  # 참외 시장
    korean_melon_M = db.Column(db.Float, nullable=False)  # 참외 대형마트
    cucumberS_T = db.Column(db.Float, nullable=False)  # 오이(가시계통) 시장
    cucumberS_M = db.Column(db.Float, nullable=False)  # 오이(가시계통) 대형마트
    cucumberD_T = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 시장
    cucumberD_M = db.Column(db.Float, nullable=False)  # 오이(다다기계통) 대형마트
    cucumberW_T = db.Column(db.Float, nullable=False)  # 오이(취청) 시장
    cucumberW_M = db.Column(db.Float, nullable=False)  # 오이(취청) 대형마트
    squash_T = db.Column(db.Float, nullable=False)  # 애호박 시장
    squash_M = db.Column(db.Float, nullable=False)  # 애호박 대형마트
    zucchini_T = db.Column(db.Float, nullable=False)  # 주키니 시장
    zucchini_M = db.Column(db.Float, nullable=False)  # 주키니 대형마트
    tomato_T = db.Column(db.Float, nullable=False)  # 토마토 시장
    tomato_M = db.Column(db.Float, nullable=False)  # 토마토 대형마트
    strawberry_T = db.Column(db.Float, nullable=False)  # 딸기 시장
    strawberry_M = db.Column(db.Float, nullable=False)  # 딸기 대형마트
    radishF_T = db.Column(db.Float, nullable=False)  # 무(가을) 시장
    radishF_M = db.Column(db.Float, nullable=False)  # 무(가을) 대형마트
    radishW_T = db.Column(db.Float, nullable=False)  # 무(월동) 시장
    radishW_M = db.Column(db.Float, nullable=False)  # 무(월동) 대형마트
    radishS_T = db.Column(db.Float, nullable=False)  # 무(봄) 시장
    radishS_M = db.Column(db.Float, nullable=False)  # 무(봄) 대형마트
    radishH_T = db.Column(db.Float, nullable=False)  # 무(고랭지) 시장
    radishH_M = db.Column(db.Float, nullable=False)  # 무(고랭지) 대형마트
    carrot_T = db.Column(db.Float, nullable=False)  # 당근 시장
    carrot_M = db.Column(db.Float, nullable=False)  # 당근 대형마트
    yeol_radish_T = db.Column(db.Float, nullable=False)  # 열무 시장
    yeol_radish_M = db.Column(db.Float, nullable=False)  # 열무 대형마트
    dried_red_pepperD_T = db.Column(db.Float, nullable=False)  # 건고추(화건) 시장
    dried_red_pepperD_M = db.Column(db.Float, nullable=False)  # 건고추(화건) 대형마트
    dried_red_pepperS_T = db.Column(db.Float, nullable=False)  # 건고추(양건) 시장
    dried_red_pepperS_M = db.Column(db.Float, nullable=False)  # 건고추(양양건) 대형마트
    pepper_T = db.Column(db.Float, nullable=False)  # 풋고추 시장
    pepper_M = db.Column(db.Float, nullable=False)  # 풋고추 대형마트
    chilli_pepper_T = db.Column(db.Float, nullable=False)  # 꽈리고추 시장
    chilli_pepper_M = db.Column(db.Float, nullable=False)  # 꽈리고추 대형마트
    cheongyang_pepper_T = db.Column(db.Float, nullable=False)  # 청양고추 시장
    cheongyang_pepper_M = db.Column(db.Float, nullable=False)  # 청양고추 대형마트
    red_pepper_T = db.Column(db.Float, nullable=False)  # 붉은고추 시장
    red_pepper_M = db.Column(db.Float, nullable=False)  # 붉은고추 대형마트
    onion_T = db.Column(db.Float, nullable=False)  # 양파 시장
    onion_M = db.Column(db.Float, nullable=False)  # 양파 대형마트
    green_onion_T = db.Column(db.Float, nullable=False)  # 대파 시장
    green_onion_M = db.Column(db.Float, nullable=False)  # 대파 대형마트
    chives_T = db.Column(db.Float, nullable=False)  # 쪽파 시장
    chives_M = db.Column(db.Float, nullable=False)  # 쪽파 대형마트
    ginger_T = db.Column(db.Float, nullable=False)  # 생강 시장
    ginger_M = db.Column(db.Float, nullable=False)  # 생강 대형마트
    chili_powder_T = db.Column(db.Float, nullable=False)  # 고추가루 시장
    chili_powder_M = db.Column(db.Float, nullable=False)  # 고추가루 대형마트
    parsley_T = db.Column(db.Float, nullable=False)  # 미나리 시장
    parsley_M = db.Column(db.Float, nullable=False)  # 미나리 대형마트
    sesame_leaf_T = db.Column(db.Float, nullable=False)  # 깻잎 시장
    sesame_leaf_M = db.Column(db.Float, nullable=False)  # 깻잎 대형마트
    pimento_T = db.Column(db.Float, nullable=False)  # 피망 시장
    pimento_M = db.Column(db.Float, nullable=False)  # 피망 대형마트
    paprika_T = db.Column(db.Float, nullable=False)  # 파프리카 시장
    paprika_M = db.Column(db.Float, nullable=False)  # 파프리카 대형마트
    melon_T = db.Column(db.Float, nullable=False)  # 멜론 시장
    melon_M = db.Column(db.Float, nullable=False)  # 멜론 대형마트
    garlic_T = db.Column(db.Float, nullable=False)  # 깐마늘 시장
    garlic_M = db.Column(db.Float, nullable=False)  # 깐마늘 대형마트
    cherry_tomato_T = db.Column(db.Float, nullable=False)  # 방울토마토 시장
    cherry_tomato_M = db.Column(db.Float, nullable=False)  # 방울토마토 대형마트
    jujube_cherry_tomato_T = db.Column(db.Float, nullable=False)  # 대추방울토마토 시장
    jujube_cherry_tomato_M = db.Column(db.Float, nullable=False)  # 대추방울토마토 대형마트

    # 특용작물
    sesame_T = db.Column(db.Float, nullable=False)  # 참깨 시장
    sesame_M = db.Column(db.Float, nullable=False)  # 참깨 대형마트
    peanut_T = db.Column(db.Float, nullable=False)  # 땅콩 시장
    peanut_M = db.Column(db.Float, nullable=False)  # 땅콩 대형마트
    oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 느타리버섯 시장
    oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 느타리버섯 대형마트
    oyster_mushroomA_T = db.Column(db.Float, nullable=False)  # 애느타리버섯 시장
    oyster_mushroomA_M = db.Column(db.Float, nullable=False)  # 애느타리버섯 대형마트
    enoki_mushroom_T = db.Column(db.Float, nullable=False)  # 팽이버섯 시장
    enoki_mushroom_M = db.Column(db.Float, nullable=False)  # 팽이버섯 대형마트
    king_oyster_mushroom_T = db.Column(db.Float, nullable=False)  # 새송이버섯 시장
    king_oyster_mushroom_M = db.Column(db.Float, nullable=False)  # 새송이버섯 대형마트
    walnut_T = db.Column(db.Float, nullable=False)  # 호두 시장
    walnut_M = db.Column(db.Float, nullable=False)  # 호두 대형마트
    almond_T = db.Column(db.Float, nullable=False)  # 아몬드 시장
    almond_M = db.Column(db.Float, nullable=False)  # 아몬드 대형마트

    # 과일류
    appleF_T = db.Column(db.Float, nullable=False)  # 사과(후지) 시장
    appleF_M = db.Column(db.Float, nullable=False)  # 사과(후지) 대형마트
    appleT_T = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 시장
    appleT_M = db.Column(db.Float, nullable=False)  # 사과(쓰가루) 대형마트
    appleR_T = db.Column(db.Float, nullable=False)  # 사과(홍로) 시장
    appleR_M = db.Column(db.Float, nullable=False)  # 사과(홍로) 대마트
    pearS_T = db.Column(db.Float, nullable=False)  # 배(신고) 시장
    pearS_M = db.Column(db.Float, nullable=False)  # 배(신고) 대형마트
    pearW_T = db.Column(db.Float, nullable=False)  # 배(원황) 시장
    pearW_M = db.Column(db.Float, nullable=False)  # 배(원황) 대형마트
    peach_T = db.Column(db.Float, nullable=False)  # 복숭아 시장
    peach_M = db.Column(db.Float, nullable=False)  # 복숭아 대형마트
    grapeC_T = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 시장
    grapeC_M = db.Column(db.Float, nullable=False)  # 포도(캠벨얼리) 대형마트
    grapeG_T = db.Column(db.Float, nullable=False)  # 포도(거봉) 시장
    grapeG_M = db.Column(db.Float, nullable=False)  # 포도(거봉) 대형마트
    grapeM_T = db.Column(db.Float, nullable=False)  # 포도(MBA) 시장
    grapeM_M = db.Column(db.Float, nullable=False)  # 포도(MBA) 대형마트
    grapeS_T = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 시장
    grapeS_M = db.Column(db.Float, nullable=False)  # 포도(샤인머스켓) 대형마트
    grapeR_T = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 시장
    grapeR_M = db.Column(db.Float, nullable=False)  # 포도(레드글로브) 대형마트
    citrusR_T = db.Column(db.Float, nullable=False)  # 감귤(노지) 시장
    citrusR_M = db.Column(db.Float, nullable=False)  # 감귤(노지) 대형마트
    citrusH_T = db.Column(db.Float, nullable=False)  # 감귤(시설) 시장
    citrusH_M = db.Column(db.Float, nullable=False)  # 감귤(시설) 대형마트
    persimmon_T = db.Column(db.Float, nullable=False)  # 단감 시장
    persimmon_M = db.Column(db.Float, nullable=False)  # 단감 대형마트
    banana_T = db.Column(db.Float, nullable=False)  # 바나나 시장
    banana_M = db.Column(db.Float, nullable=False)  # 바나나 대형마트
    kiwiN_T = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 시장
    kiwiN_M = db.Column(db.Float, nullable=False)  # 참다래(뉴질랜드) 대형마트
    kiwiK_T = db.Column(db.Float, nullable=False)  # 참다래(국산) 시장
    kiwiK_M = db.Column(db.Float, nullable=False)  # 참다래(국산) 대형마트
    pineapple_T = db.Column(db.Float, nullable=False)  # 파인애플 시장
    pineapple_M = db.Column(db.Float, nullable=False)  # 파인애플 대형마트
    orangeU_T = db.Column(db.Float, nullable=False)  # 오렌지(미국) 시장
    orangeU_M = db.Column(db.Float, nullable=False)  # 오렌지(미국) 대형마트
    orangeA_T = db.Column(db.Float, nullable=False)  # 오렌지(호주) 시장
    orangeA_M = db.Column(db.Float, nullable=False)  # 오렌지(호주) 대형마트
    lemon_T = db.Column(db.Float, nullable=False)  # 레몬 시장
    lemon_M = db.Column(db.Float, nullable=False)  # 레몬 대형마트
    cherry_T = db.Column(db.Float, nullable=False)  # 체리 시장
    cherry_M = db.Column(db.Float, nullable=False)  # 체리 대형마트
    raisin_T = db.Column(db.Float, nullable=False)  # 건포도 시장
    raisin_M = db.Column(db.Float, nullable=False)  # 건포도 대형마트
    dried_blueberries_T = db.Column(db.Float, nullable=False)  # 건블루베리 시장
    dried_blueberries_M = db.Column(db.Float, nullable=False)  # 건블루베리 대형마트
    mango_T = db.Column(db.Float, nullable=False)  # 망고 시장
    mango_M = db.Column(db.Float, nullable=False)  # 망고 대형마트

    # 수산물
    mackerelL_T = db.Column(db.Float, nullable=False)  # 고등어(생물) 시장
    mackerelL_M = db.Column(db.Float, nullable=False)  # 고등어(생물) 대형마트
    mackerelF_T = db.Column(db.Float, nullable=False)  # 고등어(냉동) 시장
    mackerelF_M = db.Column(db.Float, nullable=False)  # 고등어(냉동) 대형마트
    mackerelS_T = db.Column(db.Float, nullable=False)  # 고등어(염장) 시장
    mackerelS_M = db.Column(db.Float, nullable=False)  # 고등어(염장) 대형마트
    saury_T = db.Column(db.Float, nullable=False)  # 꽁치 시장
    saury_M = db.Column(db.Float, nullable=False)  # 꽁치 대형마트
    cutlassfishL_T = db.Column(db.Float, nullable=False)  # 갈치(생물) 시장
    cutlassfishL_M = db.Column(db.Float, nullable=False)  # 갈치(생물) 대형마트
    cutlassfishF_T = db.Column(db.Float, nullable=False)  # 갈치(냉동) 시장
    cutlassfishF_M = db.Column(db.Float, nullable=False)  # 갈치(냉동) 대형마트
    pollock_T = db.Column(db.Float, nullable=False)  # 명태 시장
    pollock_M = db.Column(db.Float, nullable=False)  # 명태 대형마트
    squidL_T = db.Column(db.Float, nullable=False)  # 물오징어(생선) 시장
    squidL_M = db.Column(db.Float, nullable=False)  # 물오징어(생선) 대형마트
    squidF_T = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 시장
    squidF_M = db.Column(db.Float, nullable=False)  # 물오징어(냉동) 대형마트
    dried_anchovies_T = db.Column(db.Float, nullable=False)  # 건멸치 시장
    dried_anchovies_M = db.Column(db.Float, nullable=False)  # 건멸치 대형마트
    dried_squid_T = db.Column(db.Float, nullable=False)  # 건오징어 시장
    dried_squid_M = db.Column(db.Float, nullable=False)  # 건오징어 대형마트
    seaweedD_T = db.Column(db.Float, nullable=False)  # 김(마른김) 시장
    seaweedD_M = db.Column(db.Float, nullable=False)  # 김(마른김) 대형마트
    seaweedF_T = db.Column(db.Float, nullable=False)  # 김(구운김) 시장
    seaweedF_M = db.Column(db.Float, nullable=False)  # 김(구운김) 대형마트
    dried_seaweed_T = db.Column(db.Float, nullable=False)  # 건미역 시장
    dried_seaweed_M = db.Column(db.Float, nullable=False)  # 건미역 대형마트
    oyster_T = db.Column(db.Float, nullable=False)  # 굴 시장
    oyster_M = db.Column(db.Float, nullable=False)  # 굴 대형마트
    yellow_corbina_T = db.Column(db.Float, nullable=False)  # 수입조기 시장
    yellow_corbina_M = db.Column(db.Float, nullable=False)  # 수입조기 대형마트
    salted_shrimp_T = db.Column(db.Float, nullable=False)  # 새우젓 시장
    salted_shrimp_M = db.Column(db.Float, nullable=False)  # 새우젓 대형마트
    anchovy_fish_sauce_T = db.Column(db.Float, nullable=False)  # 멸치액젓 시장
    anchovy_fish_sauce_M = db.Column(db.Float, nullable=False)  # 멸치액젓 대형마트
    salt_T = db.Column(db.Float, nullable=False)  # 굵은소금 시장
    salt_M = db.Column(db.Float, nullable=False)  # 굵은소금 대형마트
    abalone_T = db.Column(db.Float, nullable=False)  # 전복 시장
    abalone_M = db.Column(db.Float, nullable=False)  # 전복 대형마트
    shrimp_T = db.Column(db.Float, nullable=False)  # 흰다리새우 시장
    shrimp_M = db.Column(db.Float, nullable=False)  # 흰다리새우 대형마트


## 제철 정보
class Seasonal_food(db.Model):
    no = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)  # 갯수 카운트
    Month = db.Column(db.String(3, 'utf8mb4_unicode_ci'), nullable=False)
    Name = db.Column(db.String(10, 'utf8mb4_unicode_ci'), nullable=False)
    Period = db.Column(db.String(10, 'utf8mb4_unicode_ci'), nullable=False)


## 직거래 정보
class Direct_dealing(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    userid = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False)
    nickname = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False)
    product = db.Column(db.String(100, 'utf8mb4_unicode_ci'), nullable=False)
    infoshort = db.Column(db.String(100, 'utf8mb4_unicode_ci'), nullable=False)
    info = db.Column(db.String(3000, 'utf8mb4_unicode_ci'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100, 'utf8mb4_unicode_ci'), nullable=False)
