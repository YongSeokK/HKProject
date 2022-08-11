import copy

import pymysql
from flask import Blueprint, request, render_template, url_for, session, flash
from werkzeug.utils import redirect

from config import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME, csv_FolderPath, Category_Kor, Category_List, \
    Category_List2
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
                key_produce = option[1]  # 농산물
                radio_check[key_produce] = ' checked="checked" '
                # print(keys_list)

                # def chart_data 리턴 값 순차대로 대입
                # List: 날짜, 가격, 거래량, 미래 날짜, 예측 중간, 최소, 최대, 가격 분기, 거래량 분기
                MyChart = ChartData(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME,
                                    csv_FolderPath, Category_Kor, Category_List, category, key_produce)

                # date, price, deal, date_f, yhat, yhat_l, yhat_u, price_quarter, deal_quarter = chart_data(category,
                #                                                                                           key_produce)

                chart1, chart2, chart3 = MyChart.Wholesale()
                # # chart1: 날짜, 가격, 거래량, 최소 가격, 최대 가격, 가격 크기, 최소 거래량, 최대 거래량, 거래량 크기
                # chart1 = {'date': date, 'price': price, 'deal': deal,
                #           'min_price': min_price, 'max_price': max_price, 'stepSize_price': stepSize_price,
                #           'min_deal': min_deal, 'max_deal': max_deal, 'stepSize_deal': stepSize_deal}
                # # chart2: 예측 날짜, 예측 평균 가격, 최소 평균 예측값, 최대 평균 예측값, 예측 최솟값, 예측 최댓값, 예측 크기
                # chart2 = {'date_f': date_f, 'yhat': yhat, 'yhat_l': yhat_l, 'yhat_u': yhat_u,
                #           'min_yhat': min_yhat, 'max_yhat': max_yhat, 'stepSize_yhat': stepSize_yhat}
                # # chart3: 분기별 가격, 분기별 거래량, 최소 가격, 최대 가격, 가격 크기, 최소 거래량, 최대 거래량, 거래량 크기
                # chart3 = {'price_quarter': price_quarter, 'deal_quarter': deal_quarter,
                #           'min_price_quarter': min_price_quarter, 'max_price_quarter': max_price_quarter,
                #           'stepSize_price_quarter': stepSize_price_quarter,
                #           'min_deal_quarter': min_deal_quarter, 'max_deal_quarter': max_deal_quarter,
                #           'stepSize_deal_quarter': stepSize_deal_quarter}

                return render_template('dash/wholesale.html',
                                       category=category, key_produce=key_produce, radio_check=radio_check,
                                       date=chart1['date'], price=chart1['price'], deal=chart1['deal'],
                                       min_price=chart1['min_price'], max_price=chart1['max_price'],
                                       stepSize_price=chart1['stepSize_price'],
                                       min_deal=chart1['min_deal'], max_deal=chart1['max_deal'],
                                       stepSize_deal=chart1['stepSize_deal'],
                                       date_f=chart2['date_f'],
                                       yhat=chart2['yhat'], yhat_l=chart2['yhat_l'], yhat_u=chart2['yhat_u'],
                                       min_yhat=chart2['min_yhat'], max_yhat=chart2['max_yhat'],
                                       stepSize_yhat=chart2['stepSize_yhat'],
                                       price_quarter=chart3['price_quarter'], deal_quarter=chart3['deal_quarter'],
                                       min_price_quarter=chart3['min_price_quarter'],
                                       max_price_quarter=chart3['max_price_quarter'],
                                       stepSize_price_quarter=chart3['stepSize_price_quarter'],
                                       min_deal_quarter=chart3['min_deal_quarter'],
                                       max_deal_quarter=chart3['max_deal_quarter'],
                                       stepSize_deal_quarter=chart3['stepSize_deal_quarter'])
            else:
                category = request.form.get('category')
                print('도매: ' + category)
                dic_set = Category_List2[Category_Kor.index(category)]
                radio_check = copy.deepcopy(dic_set)
                keys_list = list(radio_check.keys())
                key_produce = keys_list[0]
                radio_check[key_produce] = ' checked="checked" '

                MyChart = ChartData(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME,
                                    csv_FolderPath, Category_Kor, Category_List, category, key_produce)
                chart1, chart2, chart3 = MyChart.Wholesale()

                print("chart1['price']          :" + str(chart1['price']))
                print("chart1['min_price']      :" + str(chart1['min_price']))
                print("chart1['max_price']      :" + str(chart1['max_price']))
                print("chart1['stepSize_price'] :" + str(chart1['stepSize_price']))
                print("chart1['deal']           :" + str(chart1['deal']))
                print("chart1['min_deal']       :" + str(chart1['min_deal']))
                print("chart1['max_deal']       :" + str(chart1['max_deal']))
                print("chart1['stepSize_deal']  :" + str(chart1['stepSize_deal']))

                # print(chart1['date'], chart1['price'], chart1['deal'],
                #                        chart1['min_price'], chart1['max_price'],
                #                        chart1['stepSize_price'],
                #                        chart1['min_deal'], chart1['max_deal'],
                #                        chart1['stepSize_deal'],
                #                        chart2['date_f'],
                #                        chart2['yhat'], chart2['yhat_l'], chart2['yhat_u'],
                #                        chart2['min_yhat'], chart2['max_yhat'],
                #                        chart2['stepSize_yhat'],
                #                        chart3['price_quarter'], chart3['deal_quarter'],
                #                        chart3['min_price_quarter'],
                #                        chart3['max_price_quarter'],
                #                        chart3['stepSize_price_quarter'],
                #                        chart3['min_deal_quarter'],
                #                        chart3['max_deal_quarter'],
                #                        chart3['stepSize_deal_quarter'])

                return render_template('dash/wholesale.html',
                                       category=category, key_produce=key_produce, radio_check=radio_check,
                                       date=chart1['date'], price=chart1['price'], deal=chart1['deal'],
                                       min_price=chart1['min_price'], max_price=chart1['max_price'],
                                       stepSize_price=chart1['stepSize_price'],
                                       min_deal=chart1['min_deal'], max_deal=chart1['max_deal'],
                                       stepSize_deal=chart1['stepSize_deal'],
                                       date_f=chart2['date_f'],
                                       yhat=chart2['yhat'], yhat_l=chart2['yhat_l'], yhat_u=chart2['yhat_u'],
                                       min_yhat=chart2['min_yhat'], max_yhat=chart2['max_yhat'],
                                       stepSize_yhat=chart2['stepSize_yhat'],
                                       price_quarter=chart3['price_quarter'], deal_quarter=chart3['deal_quarter'],
                                       min_price_quarter=chart3['min_price_quarter'],
                                       max_price_quarter=chart3['max_price_quarter'],
                                       stepSize_price_quarter=chart3['stepSize_price_quarter'],
                                       min_deal_quarter=chart3['min_deal_quarter'],
                                       max_deal_quarter=chart3['max_deal_quarter'],
                                       stepSize_deal_quarter=chart3['stepSize_deal_quarter'])


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
                key_produce = option[2]
                radio_check[key_produce] = ' checked="checked" '

                MyChart = ChartData(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME,
                                    csv_FolderPath, Category_Kor, Category_List, category, key_produce)
                date, price, deal, date_f, yhat, yhat_l, yhat_u, price_quarter, deal_quarter = MyChart.Wholesale()
                return render_template('dash/retail.html', region=region, category=category, key_produce=key_produce,
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
                key_produce = keys_list[0]
                radio_check[key_produce] = ' checked="checked" '

                MyChart = ChartData(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME,
                                    csv_FolderPath, Category_Kor, Category_List, category, key_produce)
                date, price, deal, date_f, yhat, yhat_l, yhat_u, price_quarter, deal_quarter = MyChart.Wholesale()
                return render_template('dash/retail.html', region=region, category=category, key_produce=key_produce,
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
