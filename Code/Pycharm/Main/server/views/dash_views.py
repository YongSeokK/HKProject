from flask import Blueprint, request, render_template, url_for, session, flash
from werkzeug.utils import redirect

from server.models import Food_recipe
from server.views.category import Category_List, Category_Kor

bp = Blueprint('dash', __name__, url_prefix='/')


# Dashboard
@bp.route('/dash', methods=('GET', 'POST'))
def board():
    y = request.form.get('region')
    z = request.form.get('category')
    print(y, z)
    return render_template('dash.html')


# Dashboard_도매
@bp.route('/wholesale', methods=('GET', 'POST'))
def wholesale():
    user_nickname = session.get('user_nickname')
    if user_nickname is None:
        flash("로그인이 필요합니다.")
        return redirect(url_for('main.login'))
    else:
        if request.method == 'POST':
            if request.form.get('myRadios'):
                option = request.form.to_dict()['myRadios']
                print('도매: ' + option)
                option = option.split('_')
                category = option[0]
                dic_set = Category_List[Category_Kor.index(category)]
                radio_check = dic_set.copy()
                radio_key = option[1]
                radio_check[radio_key] = ' checked="checked" '
                # print(keys_list)
                return render_template('dash/wholesale.html', category=category, radio_check=radio_check)
            else:
                category = request.form.get('category')
                print('도매: ' + category)
                dic_set = Category_List[Category_Kor.index(category)]
                radio_check = dic_set.copy()
                keys_list = list(radio_check.keys())
                radio_check[keys_list[0]] = ' checked="checked" '
                return render_template('dash/wholesale.html', category=category, radio_check=radio_check)


# Dashboard_가격비교_소매
@bp.route('/compare', methods=('GET', 'POST'))
def compare():
    user_nickname = session.get('user_nickname')
    if user_nickname is None:
        flash("로그인이 필요합니다.")
        return redirect(url_for('main.login'))
    else:
        if request.method == 'POST':
            if request.form.get('myRadios'):
                option = request.form.to_dict()['myRadios']
                print('소매: ' + option)
                option = option.split('_')
                region = option[0]
                category = option[1]
                dic_set = Category_List[Category_Kor.index(category)]
                radio_check = dic_set.copy()
                radio_key = option[2]
                radio_check[radio_key] = ' checked="checked" '
                return render_template('dash/compare.html', region=region, category=category, radio_check=radio_check)
            else:
                region = request.form.get('region')
                category = request.form.get('category')
                print('소매: ' + region + '_' + category)
                dic_set = Category_List[Category_Kor.index(category)]
                radio_check = dic_set.copy()
                keys_list = list(radio_check.keys())
                radio_check[keys_list[0]] = ' checked="checked" '
                return render_template('dash/compare.html', region=region, category=category, radio_check=radio_check)


# Dashboard_가격비교_소매
@bp.route('/compare2', methods=('GET', 'POST'))
def compare2():
    user_nickname = session.get('user_nickname')
    if user_nickname is None:
        flash("로그인이 필요합니다.")
        return redirect(url_for('main.login'))
    else:
        return render_template('dash/compare.html')


# chart
@bp.route('/chart')
def chart():
    return render_template('dash/chart.html')


# table
@bp.route('/table')
def table():
    dt = Food_recipe.query.filter(Food_recipe.dish == '김치찌개').all()
    return render_template('dash/table.html', dt=dt)
