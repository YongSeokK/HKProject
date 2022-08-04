from flask import Blueprint, request, render_template, url_for, session, flash
from sqlalchemy import and_
from werkzeug.utils import redirect

from server.models import Food_recipe

bp = Blueprint('dash', __name__, url_prefix='/')


# @bp.before_app_request
# def load_logged_in_user():
#     user_id = session.get('user_id')
#     if user_id is None:
#         g.user = None
#     else:
#         g.user = user_id


# Dashboard
@bp.route('/dash')
def board():
    dt = Food_recipe.query.filter(and_(Food_recipe.dish == '김치찌개', Food_recipe.registrant == '김패쓰'))
    return render_template('dash.html', dt=dt)


# Dashboard_가격예측
@bp.route('/forecast', methods=('GET', 'POST'))
def forecast():
    user_nickname = session.get('user_nickname')
    radio_check = {'감자': ' checked="checked" ', '고구마': ''}
    check_list = list(radio_check.values())
    if user_nickname is None:
        flash("로그인이 필요합니다.")
        return redirect(url_for('main.login'))
    else:
        dt = Food_recipe.query.filter(Food_recipe.dish == '김치찌개').all()
        if request.method == 'POST':
            option = request.form.to_dict()['myRadios']
            # print(option)
            radio_check['감자'] = ''
            radio_check[option] = ' checked="checked" '
            check_list = list(radio_check.values())
            print(radio_check)
            return render_template('dash/forecast.html', dt=dt, check_list=check_list)
    return render_template('dash/forecast.html', dt=dt, check_list=check_list)


# Dashboard_가격비교
@bp.route('/compare')
def compare():
    user_nickname = session.get('user_nickname')
    if user_nickname is None:
        flash("로그인이 필요합니다.")
        return redirect(url_for('main.login'))
    else:
        dt = Food_recipe.query.filter(Food_recipe.dish == '김치찌개').all()
        return render_template('dash/compare.html', dt=dt)


# chart
@bp.route('/chart')
def chart():
    return render_template('dash/chart.html')


# table
@bp.route('/table')
def table():
    dt = Food_recipe.query.filter(Food_recipe.dish == '김치찌개').all()
    return render_template('dash/table.html', dt=dt)
