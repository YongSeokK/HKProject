from flask import Flask, Blueprint, request, render_template, url_for, session, g, flash, jsonify
from flask_bcrypt import Bcrypt
from werkzeug.utils import redirect
from server.forms import UserCreateForm
from server.models import Members, Food_recipe, Wholesale_quantity
from server import db
import json
import re
import urllib.request
from glob import glob
import os
import pymysql
from config import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME

bp = Blueprint('main', __name__, url_prefix='/')
bcrypt = Bcrypt(Flask(__name__))


# 로그인 상태 확인
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')  # 별명
    user_id2 = session.get('user_id2')  # 아이디
    if user_id is None:
        g.user = None
        g.user2 = None
    else:
        g.user = user_id
        g.user2 = user_id2


# 메인 홈
@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')


# 회원 가입
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
                           nickname=form.nickname.data,
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


# 로그 인
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
                session['user_id'] = user.nickname
                session['user_id2'] = user.userid
                print('login success')
                return redirect(url_for('main.index'))
            else:
                return render_template('login.html')
    return render_template('login.html')


# 로그 아웃
@bp.route('/logout')
def logout():
    session.clear()
    flash("로그아웃 되었습니다.")
    return redirect(url_for('main.login'))


# DB 초기 설정
mydb = pymysql.Connect(host=DB_HOST, user=DB_USERNAME,
                       password=DB_PASSWORD, database=DB_NAME)
cursor = mydb.cursor(pymysql.cursors.DictCursor)


# 프로필
@bp.route('/profile', methods=('GET', 'POST'))
def profile():
    user = Members.query.filter_by(nickname=g.user).first()
    if request.method == 'POST':
        value_key = list(request.form.to_dict().keys())[0].split('.')[0]
        print(value_key)
        return render_template('profile/change.html', value_key=value_key)
    return render_template('profile/profile.html', user=user)


# 프로필 수정
@bp.route('/change', methods=('GET', 'POST'))
def change():
    # print(request.form.get('id'))
    if request.method == 'POST':
        value_key = list(request.form.to_dict().keys())[0].split('.')[0]
        print(value_key)
        x = value_key
        # sql_table = 'SELECT * FROM members WHERE ' + x + ' LIKE "{}" ;'.format(g.user)
        # cursor.execute(sql_table)
        # row = cursor.fetchall()[0]
        # print(row[x])
        # print(request.form.get(x))
        sql_table = 'UPDATE members SET ' + x + '="' + request.form.get(x) + '" WHERE ' + 'userid' + \
                    ' LIKE "{}" ;'.format(g.user2)
        print(str(sql_table))
        cursor.execute(sql_table)
        mydb.commit()
        user = Members.query.filter_by(userid=g.user2).first()
        session['user_id'] = user.nickname
        return redirect(url_for('main.profile'))
    return render_template('profile/change.html')


# 비밀 번호 확인
@bp.route('/confirm', methods=('GET', 'POST'))
def confirm():
    # print(request.form.get('pw'))
    if request.method == 'POST':
        user = Members.query.filter_by(nickname=g.user).first()
        pw_hash = request.form.get('pw').encode('utf-8')
        candidate = user.userpw.encode('utf-8')
        if not bcrypt.check_password_hash(candidate, pw_hash):
            # elif user.userpw != request.form.get('pw'):
            flash('정확한 비밀번호를 입력해주세요.')
        elif bcrypt.check_password_hash(candidate, pw_hash):
            return redirect(url_for('main.profile'))
        else:
            return render_template('profile/confirm.html')
    return render_template('profile/confirm.html')


# del
@bp.route('/initdel')
def initdel():
    session.clear()
    db_del = Members.query.all()
    for i in db_del:
        db.session.delete(i)
    db.session.commit()
    flash("로그아웃 되었습니다.")
    return redirect(url_for('main.login'))
