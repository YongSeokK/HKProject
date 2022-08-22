from datetime import datetime

import pymysql
from flask import Flask, Blueprint, request, render_template, url_for, session, g, flash
from flask_bcrypt import Bcrypt
from werkzeug.utils import redirect, secure_filename

from config import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME, Shop_imgFolder_Path, \
    Client_id, Client_secret, Days, Category_List_W
from server import db
from server.forms import UserCreateForm, UserPwForm
from server.models import Members
from ..define.naver_api import Naverapi

bp = Blueprint('main', __name__, url_prefix='/')
bcrypt = Bcrypt(Flask(__name__))

# DB 초기 설정
mydb = pymysql.Connect(host=DB_HOST, user=DB_USERNAME,
                       password=DB_PASSWORD, database=DB_NAME)
cursor = mydb.cursor(pymysql.cursors.DictCursor)


# 로그인 상태 확인
@bp.before_app_request
def load_logged_in_user():
    user_nickname = session.get('user_nickname')  # 별명
    user_id = session.get('user_id')  # 아이디
    user_grade = session.get('user_grade')  # 아이디
    if user_nickname is None:
        g.nickname = None
        g.user = None
        g.grade = None
    else:
        g.nickname = user_nickname
        g.user = user_id
        g.grade = user_grade


# 메인 홈
@bp.route('/', methods=('GET', 'POST'))
def index():
    # 변동표
    date = []
    data_table = []
    for dictionary in Category_List_W:
        produce_List = list(dictionary.values())  # 품목의 밸류값만 가져와 list로 변경
        translation_Dict = {v: k for k, v in dictionary.items()}  # 영어이름을 대체하기 위해 딕셔너리 키:밸류 도치
        for item in produce_List:
            produce = translation_Dict.get(item)  # item = 품목명 영어, 한글 이름 매칭
            # 거래량
            sql_q = 'SELECT date, ' + item + ' FROM Wholesale_quantity ORDER BY date DESC LIMIT 2;'  # 열 선택 & 열 내림차순 행 제한
            cursor.execute(sql_q)
            dt_quantity = cursor.fetchall()
            before_quantity = int(dt_quantity[1][item])  # 그제
            yesterday_quantity = int(dt_quantity[0][item])  # 어제
            # 가격
            sql_p = 'SELECT date, ' + item + ' FROM Wholesale_price ORDER BY date DESC LIMIT 2;'
            cursor.execute(sql_p)
            dt_price = cursor.fetchall()
            before_price = int(dt_price[1][item])
            yesterday_price = int(dt_price[0][item])
            if before_price == 0 or yesterday_price == 0:
                pass
            else:
                # 차이
                quantity_dif = int(abs(before_quantity - yesterday_quantity))
                price_dif = int(abs(before_price - yesterday_price))
                dt_Dict = {"품목명": produce,
                           "그제_거래량": before_quantity, "어제_거래량": yesterday_quantity,
                           "거래량_변동폭": quantity_dif,
                           "그제_가격": before_price, "어제_가격": yesterday_price,
                           "가격_변동폭": price_dif}
                data_table.append(dt_Dict)
    for d in [dt_quantity[1]['date'], dt_quantity[0]['date']]:
        time = datetime.strptime(str(d), "%Y%m%d")
        day = str(time.month) + '.' + str(time.day) + '(' + Days[time.weekday()] + ')'
        date.append(day)
    # 변동폭 기준 내림차순 정렬, 상위 5개
    data_table = sorted(data_table, key=(lambda x: x["가격_변동폭"]), reverse=True)[0:10]

    # popup 1
    pname = '농산물 물가'
    MyNaver = Naverapi(pname, Client_id, Client_secret)
    article_List = MyNaver.Navernews()

    # popup 3
    now = datetime.now()
    this_month = now.strftime('%m')
    sql_seasonal = 'SELECT * FROM seasonal_food WHERE Month = {}'.format(this_month)
    cursor.execute(sql_seasonal)
    monthly_food = cursor.fetchall()

    return render_template('base/index.html',
                           date=date, data_table=data_table,
                           article_List=article_List, monthly_food=monthly_food)


# 회원 가입
@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Members.query.filter_by(userid=form.userid.data).first()
        if not user:
            print('signup: ', form.userid.data)
            pw_hash = form.password.data
            pw_hash = bcrypt.generate_password_hash(pw_hash.encode('utf-8'))
            pw_hash = pw_hash.decode('utf-8')
            user = Members(userid=form.userid.data,
                           nickname=form.nickname.data,
                           userpw=pw_hash,
                           name=form.name.data,
                           email=form.email.data,
                           phone=form.phone.data,
                           grade=1)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.login'))
        else:
            flash('이미 존재하는 아이디입니다.')
            print('이미 존재하는 아이디입니다.')
            return redirect(url_for('main.login'))
    return render_template('base/signup.html', form=form)


# 로그 인
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        if request.form.get('signup'):
            return redirect(url_for('main.signup'))
        else:
            print('login: ', request.form.get('id'))
            user = Members.query.filter_by(userid=request.form.get('id')).first()
            pw_hash = request.form.get('pw').encode('utf-8')
            if not user:
                flash('존재하지 않는 아이디입니다.')
            else:
                candidate = user.userpw.encode('utf-8')
                if not bcrypt.check_password_hash(candidate, pw_hash):
                    flash('정확한 비밀번호를 입력해주세요.')
                elif bcrypt.check_password_hash(candidate, pw_hash):
                    # elif user.userpw == request.form.get('pw'):
                    session.clear()
                    session['user_nickname'] = user.nickname
                    session['user_id'] = user.userid
                    session['user_grade'] = user.grade
                    print('login success')
                    return redirect(url_for('main.index'))
                else:
                    return render_template('base/login.html')
    return render_template('base/login.html')


# 로그 아웃
@bp.route('/logout')
def logout():
    session.clear()
    flash("로그아웃 되었습니다.")
    return redirect(url_for('main.login'))


# 프로필
@bp.route('/profile', methods=('GET', 'POST'))
def profile():
    user = Members.query.filter_by(userid=g.user).first()
    if request.method == 'POST':
        choice = list(request.form.keys())[0].split('.')[0]
        print('choice: ' + choice)
        return render_template('profile/confirm.html', user=user, choice=choice)
    return render_template('profile/profile.html', user=user)


# 프로필 수정
@bp.route('/change', methods=('GET', 'POST'))
def change():
    user = Members.query.filter_by(userid=g.user).first()
    if request.method == 'POST':
        sql_table = 'UPDATE members SET nickname="' + request.form.get('nickname') + '"' + \
                    ', name="' + request.form.get('name') + '"' + \
                    ', email="' + request.form.get('email') + '"' + \
                    ', phone="' + request.form.get('phone') + '" WHERE ' + 'userid="' + g.user + '"'
        cursor.execute(sql_table)
        mydb.commit()
        session['user_nickname'] = request.form.get('nickname')
        return redirect(url_for('main.profile'))
    return render_template('profile/change.html', user=user)


# 비밀번호 수정
@bp.route('/changepw', methods=('GET', 'POST'))
def changepw():
    form = UserPwForm()
    user = Members.query.filter_by(userid=g.user).first()
    if request.method == 'POST' and form.validate_on_submit():
        pw_hash = form.password.data
        pw_hash = bcrypt.generate_password_hash(pw_hash.encode('utf-8'))
        pw_hash = pw_hash.decode('utf-8')
        text = pw_hash + ',' + g.user
        sql_table = 'UPDATE members SET userpw="{}" WHERE userid="{}"'.format(text)
        cursor.execute(sql_table)
        mydb.commit()
        return redirect(url_for('main.profile'))
    return render_template('profile/changepw.html', user=user, form=form)


# 비밀 번호 확인
@bp.route('/confirm', methods=('GET', 'POST'))
def confirm():
    if request.method == 'POST':
        choice = request.form.to_dict()['check']
        user = Members.query.filter_by(userid=g.user).first()
        pw_hash = request.form.get('pw').encode('utf-8')
        candidate = user.userpw.encode('utf-8')
        if not bcrypt.check_password_hash(candidate, pw_hash):
            # elif user.userpw != request.form.get('pw'):
            flash('정확한 비밀번호를 입력해주세요.')
            return render_template('profile/confirm.html', choice=choice)
        elif bcrypt.check_password_hash(candidate, pw_hash):
            if choice == 'profile':
                return redirect(url_for('main.change'))
            else:
                return redirect(url_for('main.changepw'))
        else:
            return render_template('profile/confirm.html')
    return render_template('profile/confirm.html')


# 팀 _ 숨겨진 페이지
@bp.route('/team', methods=('GET', 'POST'))
def team():
    return render_template('profile/team.html')


# 직거래쇼핑
@bp.route('/shop', methods=('GET', 'POST'))
def shop():
    if request.method == 'POST':
        return redirect(url_for('main.write'))
    else:
        sql_table = "SELECT * FROM direct_dealing ORDER BY id DESC LIMIT 12;"
        cursor.execute(sql_table)
        db = cursor.fetchall()
        for data in db:
            data['pricecomma'] = format(data['price'], ',')
            data['image']
        return render_template('shopping/shop.html', db=db)


# 글쓰기
@bp.route('/shop/write', methods=('GET', 'POST'))
def write():
    user_userid = session.get('user_id')
    user_nickname = session.get('user_nickname')
    user_grade = session.get('user_grade')
    if user_nickname is None:
        flash("로그인이 필요합니다.")
        return redirect(url_for('main.login'))
    else:
        if user_grade == 1:
            flash("판매자 권한이 없습니다.")
            return redirect(url_for('main.shop'))
        else:
            if request.method == 'POST' and request.form.get('write'):
                userid = user_userid
                nickname = user_nickname
                product = request.form.get('product')
                infoshort = request.form.get('infoshort')
                info = request.form.get('info')
                price = request.form.get('price')
                now = datetime.now()
                time = now.strftime("%y%m%d_%H%M%S")
                img_file = userid + '-' + time
                img = request.files['image']
                filename = secure_filename(img.filename)
                # print(filename)
                extension = '.' + filename.split('.')[-1]
                # print(extension)
                img.save(Shop_imgFolder_Path + img_file + extension)
                sql_text = 'userid, nickname, product, infoshort, info, price, image'
                result_text = (userid, nickname, product, infoshort, info, price, img_file + extension)
                sql_table = 'INSERT INTO direct_dealing ({}) VALUES (%s, %s, %s, %s, %s, %s, %s)'.format(sql_text)
                cursor.execute(sql_table, result_text)
                mydb.commit()
                return redirect(url_for('main.shop'))
            else:
                return render_template('shopping/write.html')


@bp.route('/shop/pay/<nickname>/<int:id>', methods=('GET', 'POST'))
def pay(nickname, id):
    sql_table = "SELECT * FROM direct_dealing WHERE nickname='{}' AND id='{}';".format(nickname, id)
    cursor.execute(sql_table)
    trade_db = cursor.fetchall()
    for data in trade_db:
        data['pricecomma'] = format(data['price'], ',')
    print(trade_db)
    return render_template('shopping/pay.html', trade_db=trade_db)


# 레시피
# @bp.route('/recipe', methods=('GET', 'POST'))
# def recipe():
#     return render_template('base/recipe.html')
@bp.route('/recipe/', methods=('GET', 'POST'))
def recipe():
    # dt = Food_recipe.query.filter(Food_recipe.dish == keyword).all()
    temp = request.args
    temp1 = request.form.keys()
    print(temp)
    print(temp1)
    # if temp != None:
    #     ingredient = temp
    sql_t = 'SELECT * FROM food_recipe WHERE dish LIKE "%{}%" ORDER BY views DESC LIMIT 9;'.format(temp)
    cursor.execute(sql_t)
    dt_dish = cursor.fetchall()
    # 여기는 db에서 딕셔너리 형식으로 불러오기 때문에 html에 jinja2로 적용할 때도 딕셔너리 형식으로 활용해야 함.
    return render_template('base/recipe.html', dt_dish=dt_dish)


# 관리자 페이지
@bp.route('/admin', methods=('GET', 'POST'))
def admin():
    sql_table = "SELECT * FROM members;"
    cursor.execute(sql_table)
    members = cursor.fetchall()
    return render_template('base/admin.html', members=members)


# del
@bp.route('/initdel')
def initdel():
    session.clear()
    from server.models import Direct_dealing
    db_del = Direct_dealing.query.all()
    for i in db_del:
        db.session.delete(i)
    db.session.commit()
    print('Del')
    flash("로그아웃 되었습니다.")
    return redirect(url_for('main.login'))


@bp.route('/detail/<category>/<produce>/', methods=('GET', 'POST'))
def detail(category, produce):
    x = request.form.get('content')
    print(x)
    # question = Question.query.filter(Question.id==question_id)
    # question = Members.query.get_or_404(question_id)
    # question_id = request.args.get('question_id')
    # print(question_id)
    print(request.args)
    print(category, produce)
    return '<br><br><br><br><br><br><br><br><br><br><br><br><br>"ok"'
