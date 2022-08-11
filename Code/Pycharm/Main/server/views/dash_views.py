import copy

import pymysql
from flask import Blueprint, request, render_template, url_for, session, flash
from werkzeug.utils import redirect

from config import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME, csv_FolderPath, Category_Kor, Category_List, Category_List2
from server.define.chart_data import ChartData
from server.models import Food_recipe

bp = Blueprint('dash', __name__, url_prefix='/')

# DB 초기 설정
mydb = pymysql.Connect(host=DB_HOST, user=DB_USERNAME,
                       password=DB_PASSWORD, database=DB_NAME)
cursor = mydb.cursor()


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
                category = option[0]  # 카테고리
                dic_set = Category_List2[Category_Kor.index(category)]
                radio_check = copy.deepcopy(dic_set)  # 딕셔너리 깊은 복사
                radio_key = option[1]  # 농산물
                radio_check[radio_key] = ' checked="checked" '
                # print(keys_list)

                # def chart_data 리턴 값 순차대로 대입
                # List: 날짜, 가격, 거래량, 미래 날짜, 예측 중간, 최소, 최대, 가격 분기, 거래량 분기
                MyChart = ChartData(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME,
                                    csv_FolderPath, Category_Kor, Category_List, category, radio_key)
                date, price, deal, date_f, yhat, yhat_l, yhat_u, price_quarter, deal_quarter = MyChart.Wholesale()

                # date, price, deal, date_f, yhat, yhat_l, yhat_u, price_quarter, deal_quarter = chart_data(category,
                #                                                                                           radio_key)
                return render_template('dash/wholesale.html', category=category, radio_key=radio_key,
                                       radio_check=radio_check, date=date, price=price, deal=deal, date_f=date_f,
                                       yhat=yhat, yhat_l=yhat_l, yhat_u=yhat_u,
                                       price_quarter=price_quarter, deal_quarter=deal_quarter)
            else:
                category = request.form.get('category')
                print('도매: ' + category)
                dic_set = Category_List2[Category_Kor.index(category)]
                radio_check = copy.deepcopy(dic_set)
                keys_list = list(radio_check.keys())
                radio_key = keys_list[0]
                radio_check[radio_key] = ' checked="checked" '

                MyChart = ChartData(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME,
                                    csv_FolderPath, Category_Kor, Category_List, category, radio_key)
                date, price, deal, date_f, yhat, yhat_l, yhat_u, price_quarter, deal_quarter = MyChart.Wholesale()
                return render_template('dash/wholesale.html', category=category, radio_key=radio_key,
                                       radio_check=radio_check, date=date, price=price, deal=deal, date_f=date_f,
                                       yhat=yhat, yhat_l=yhat_l, yhat_u=yhat_u,
                                       price_quarter=price_quarter, deal_quarter=deal_quarter)


# Dashboard_소매
@bp.route('/retail', methods=('GET', 'POST'))
def retail():
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
                dic_set = Category_List2[Category_Kor.index(category)]
                radio_check = copy.deepcopy(dic_set)
                radio_key = option[2]
                radio_check[radio_key] = ' checked="checked" '

                MyChart = ChartData(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME,
                                    csv_FolderPath, Category_Kor, Category_List, category, radio_key)
                date, price, deal, date_f, yhat, yhat_l, yhat_u, price_quarter, deal_quarter = MyChart.Wholesale()
                return render_template('dash/retail.html', region=region, category=category, radio_key=radio_key,
                                       radio_check=radio_check, date=date, price=price, deal=deal, date_f=date_f,
                                       yhat=yhat, yhat_l=yhat_l, yhat_u=yhat_u,
                                       price_quarter=price_quarter, deal_quarter=deal_quarter)
            else:
                region = request.form.get('region')
                category = request.form.get('category')
                print('소매: ' + region + '_' + category)
                dic_set = Category_List2[Category_Kor.index(category)]
                radio_check = copy.deepcopy(dic_set)
                keys_list = list(radio_check.keys())
                radio_key = keys_list[0]
                radio_check[radio_key] = ' checked="checked" '

                MyChart = ChartData(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME,
                                    csv_FolderPath, Category_Kor, Category_List, category, radio_key)
                date, price, deal, date_f, yhat, yhat_l, yhat_u, price_quarter, deal_quarter = MyChart.Wholesale()
                return render_template('dash/retail.html', region=region, category=category, radio_key=radio_key,
                                       radio_check=radio_check, date=date, price=price, deal=deal, date_f=date_f,
                                       yhat=yhat, yhat_l=yhat_l, yhat_u=yhat_u,
                                       price_quarter=price_quarter, deal_quarter=deal_quarter)


# Dashboard_가격비교_소매
@bp.route('/compare2/<category>', methods=('GET', 'POST'))
def compare2(category):
    user_nickname = session.get('user_nickname')
    if user_nickname is None:
        flash("로그인이 필요합니다.")
        return redirect(url_for('main.login'))
    else:
        z = request.args
        print(z)
        return render_template('dash/compare2.html', category=category)


# chart
@bp.route('/chart')
def chart():
    return render_template('dash/chart.html')


# table
@bp.route('/table')
def table():
    dt = Food_recipe.query.filter(Food_recipe.dish == '김치찌개').all()
    return render_template('dash/table.html', dt=dt)
