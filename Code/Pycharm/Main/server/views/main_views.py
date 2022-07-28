from flask import Flask, Blueprint, request, render_template, url_for, session, g, flash, jsonify
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from server.forms import UserCreateForm
from server.model import Members, Food_recipe, Wholesale_quantity
from server import db
import json
import re
from server.yolo5_def import YoloRun
import urllib.request
from glob import glob
import os

bp = Blueprint('main', __name__, url_prefix='/')
bcrypt = Bcrypt(Flask(__name__))


# app = Flask(__name__)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = user_id


# 메인 홈
@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')


# 회원가입
@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Members.query.filter_by(userid=form.userid.data).first()
        if not user:
            pw_hash = form.password.data
            pw_hash = bcrypt.generate_password_hash(pw_hash.encode('utf-8'))
            pw_hash = pw_hash.decode('utf-8')
            user = Members(userid=form.userid.data,
                           userpw=pw_hash,
                           name=form.name.data,
                           email=form.email.data,
                           phone=form.phone.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.login'))
        else:
            print('이미 존재하는 유저')
    return render_template('signup.html', form=form)


# 로그아웃
@bp.route('/logout')
def logout():
    session.clear()
    flash("로그아웃 되었습니다.")
    return redirect(url_for('main.login'))


# 로그인
@bp.route('/login', methods=('GET', 'POST'))
def login():
    print(request.form.get('id'))
    # print(request.form.get('pw'))
    if request.method == 'POST':
        if request.form.get('signup'):
            return redirect(url_for('main.signup'))
        else:
            user = Members.query.filter_by(userid=request.form.get('id')).first()
            pw_hash = request.form.get('pw').encode('utf-8')
            candidate = user.userpw.encode('utf-8')
            if not user:
                flash('존재하지 않는 유저입니다')
            elif not bcrypt.check_password_hash(candidate, pw_hash):
                # elif user.userpw != request.form.get('pw'):
                flash('정확한 비밀번호를 입력해주세요.')
            elif bcrypt.check_password_hash(candidate, pw_hash):
                # elif user.userpw == request.form.get('pw'):
                session.clear()
                session['user_id'] = user.userid
                print('login success')
                return redirect(url_for('main.index'))
            else:
                return render_template('login.html')
    return render_template('login.html')


# Dashboard
@bp.route('/dash')
def dash():
    user_id = session.get('user_id')
    if user_id is None:
        flash("로그인이 필요합니다.")
        return redirect(url_for('main.login'))
    else:
        dt = Food_recipe.query.filter(Food_recipe.dish == '김치찌개').all()
        return render_template('dash.html', dt=dt)


# Chatbot
@bp.route('/hello', methods=['POST', 'GET'])
def hello_pybo():
    print('응답')
    req_json = request.get_json()
    print(req_json)
    print('check1')
    temp = req_json['action']['params']['secureimage']
    temp_json = json.loads(temp)
    img_tmp = temp_json['secureUrls']
    URLList = re.sub('List\(|\)', "", img_tmp).split(',')
    # URLList[0] 은 챗봇에서 사용자가 보낸 사진의 URL주소
    cnt = 1
    # print(URLList)
    for i in URLList:
        urllib.request.urlretrieve(i, "C:\\G_Project\\Code\\Pycharm\\Main\\server\\static\\upload_img\\" + "food" + str(cnt) + ".jpg")
        cnt = cnt + 1
    # a 는 URL주소를 이용하여 로컬피시에 저장
    print('check2')
    h = glob("C:\\G_Project\\Code\\Pycharm\\Main\\server\\static\\upload_img\\*.jpg")
    j = []
    for i in h:
        j.append(i)
    # j는 temp폴더에 있는 사진의 경로

    xx = []
    for i in j:
        x = YoloRun(i)
        xx.append(x)

    # ret 은 챗봇이 사진을 받았을때의 응답
    ret = {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": str(xx)}}]}}
    dir_path = ("C:\\G_Project\\Code\\Pycharm\\Main\\server\\static\\upload_img")
    if os.path.exists(dir_path):
        if len(glob(dir_path + '\\*')) != 0:
            for file in glob(dir_path + '\\*'):
                os.remove(file)
        else:
            print('자료 없음')
    print('----------------------다음---------------------------------------------------------------------------------')
    return jsonify(ret)
