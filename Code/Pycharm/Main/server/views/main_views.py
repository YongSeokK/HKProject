from flask import Flask, Blueprint, request, render_template, url_for, session, g, flash
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from server.forms import UserCreateForm
from server.model import Members, Food_recipe, Wholesale_quantity
from server import db

bp = Blueprint('main', __name__, url_prefix='/')
app = Flask(__name__)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = user_id


@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')


@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Members.query.filter_by(userid=form.userid.data).first()
        if not user:
            user = Members(userid=form.userid.data,
                           userpw=form.password.data,
                           name=form.name.data,
                           email=form.email.data,
                           phone=form.phone.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.login'))
        else:
            print('이미 존재하는 유저')
    return render_template('signup.html', form=form)


@bp.route('/logout')
def logout():
    session.clear()
    flash("로그아웃 되었습니다.")
    return redirect(url_for('main.index'))


@bp.route('/login', methods=('GET', 'POST'))
def login():
    print(request.form.get('id'))
    print(request.form.get('pw'))
    if request.method == 'POST':
        if request.form.get('signup'):
            return redirect(url_for('main.signup'))
        else:
            user = Members.query.filter_by(userid=request.form.get('id')).first()
            if not user:
                flash('존재하지 않는 유저입니다')
            elif user.userpw != request.form.get('pw'):
                flash('정확한 비밀번호를 입력해주세요.')
            elif user.userpw == request.form.get('pw'):
                session.clear()
                session['user_id'] = user.userid
                print('login success')
                return redirect(url_for('main.index'))
            else:
                return render_template('login.html')
    return render_template('login.html')


@bp.route('/dash')
def dash():
    dt = Food_recipe.query.filter(Food_recipe.dish == '김치찌개').all()
    # <>
    return render_template('dash.html', dt=dt)
