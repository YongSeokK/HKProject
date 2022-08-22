import copy

import pymysql
from flask import Blueprint, request, render_template, url_for, session, flash
from werkzeug.utils import redirect

from config import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME, csv_Folder_Path, Category_Kor, Category_Eng, Region_Dict, \
    Category_List_W, Category_radioList_W, Category_List_R, Category_radioList_R, Produce_Num
from server.define.chart_data import Chartdata_W, Chartdata_R
from server.define.dict import Retail_Dict
from server.models import Food_recipe

bp = Blueprint('dash', __name__, url_prefix='/')

# DB 초기 설정
mydb = pymysql.Connect(host=DB_HOST, user=DB_USERNAME,
                       password=DB_PASSWORD, database=DB_NAME)
cursor = mydb.cursor()

retail_dict = Retail_Dict(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME)
result_dict = retail_dict.RetailDict()


# Dashboard
@bp.route('/dash', methods=('GET', 'POST'))
def board():
    y = request.form.get('region')
    z = request.form.get('category')
    print(y, z)
    return render_template('dash/dash.html')


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
                dic_set = Category_radioList_W[Category_Kor.index(category)]
                radio_check = copy.deepcopy(dic_set)  # 딕셔너리 깊은 복사
                key_produce = option[1]  # 농산물
                radio_check[key_produce] = ' checked="checked" '

                MyChart = Chartdata_W(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME,
                                      csv_Folder_Path, Category_Kor, Category_List_W, category, key_produce)

                chart = MyChart.Wholesale()

                return render_template('dash/wholesale.html',
                                       category=category, key_produce=key_produce, radio_check=radio_check,
                                       date=chart['1']['date'], price=chart['1']['price'], deal=chart['1']['deal'],
                                       max_price=chart['1']['max_price'], stepSize_price=chart['1']['stepSize_price'],
                                       max_deal=chart['1']['max_deal'], stepSize_deal=chart['1']['stepSize_deal'],
                                       date_f=chart['2']['date_f'], yhat=chart['2']['yhat'],
                                       yhat_l=chart['2']['yhat_l'], yhat_u=chart['2']['yhat_u'],
                                       max_yhat=chart['2']['max_yhat'], stepSize_yhat=chart['2']['stepSize_yhat'],
                                       price_quarter=chart['3']['price_quarter'],
                                       deal_quarter=chart['3']['deal_quarter'],
                                       max_price_quarter=chart['3']['max_price_quarter'],
                                       stepSize_price_quarter=chart['3']['stepSize_price_quarter'],
                                       max_deal_quarter=chart['3']['max_deal_quarter'],
                                       stepSize_deal_quarter=chart['3']['stepSize_deal_quarter'])
            else:
                category = request.form.get('category')
                print('도매: ' + category)
                dic_set = Category_radioList_W[Category_Kor.index(category)]
                radio_check = copy.deepcopy(dic_set)
                keys_list = list(radio_check.keys())
                key_produce = keys_list[0]
                radio_check[key_produce] = ' checked="checked" '

                MyChart = Chartdata_W(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME,
                                      csv_Folder_Path, Category_Kor, Category_List_W, category, key_produce)
                chart = MyChart.Wholesale()

                return render_template('dash/wholesale.html',
                                       category=category, key_produce=key_produce, radio_check=radio_check,
                                       date=chart['1']['date'], price=chart['1']['price'], deal=chart['1']['deal'],
                                       max_price=chart['1']['max_price'], stepSize_price=chart['1']['stepSize_price'],
                                       max_deal=chart['1']['max_deal'], stepSize_deal=chart['1']['stepSize_deal'],
                                       date_f=chart['2']['date_f'], yhat=chart['2']['yhat'],
                                       yhat_l=chart['2']['yhat_l'], yhat_u=chart['2']['yhat_u'],
                                       max_yhat=chart['2']['max_yhat'], stepSize_yhat=chart['2']['stepSize_yhat'],
                                       price_quarter=chart['3']['price_quarter'],
                                       deal_quarter=chart['3']['deal_quarter'],
                                       max_price_quarter=chart['3']['max_price_quarter'],
                                       stepSize_price_quarter=chart['3']['stepSize_price_quarter'],
                                       max_deal_quarter=chart['3']['max_deal_quarter'],
                                       stepSize_deal_quarter=chart['3']['stepSize_deal_quarter'])


# print(result_dict['total']['Vegetable']['M'][20211013])

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
                dic_set = Category_radioList_R[Category_Kor.index(category)]
                radio_check = copy.deepcopy(dic_set)
                key_produce = option[2]
                radio_check[key_produce] = ' checked="checked" '

                MyChart = Chartdata_R(result_dict, csv_Folder_Path, Category_Kor, Category_Eng,
                                      Region_Dict, Category_List_R, Produce_Num,
                                      region, category, key_produce)
                chart = MyChart.Retail()

                return render_template('dash/retail.html',
                                       region=region, category=category, key_produce=key_produce,
                                       radio_check=radio_check, date=chart['1']['date'],
                                       result_t=chart['1']['result_t'],
                                       result_t_total=chart['1']['result_t_total'],
                                       yhat_l_T=chart['1']['yhat_l_T'], yhat_u_T=chart['1']['yhat_u_T'],
                                       result_m=chart['2']['result_m'],
                                       result_m_total=chart['2']['result_m_total'],
                                       yhat_l_M=chart['2']['yhat_l_M'], yhat_u_M=chart['2']['yhat_u_M'],
                                       month_List=chart['3']['month_List'],
                                       month_price_T=chart['3']['month_price_T'],
                                       month_price_M=chart['3']['month_price_M'])
            else:
                region = request.form.get('region')
                category = request.form.get('category')
                print('소매: ' + region + '_' + category)
                dic_set = Category_radioList_R[Category_Kor.index(category)]
                radio_check = copy.deepcopy(dic_set)
                keys_list = list(radio_check.keys())
                key_produce = keys_list[0]
                radio_check[key_produce] = ' checked="checked" '

                MyChart = Chartdata_R(result_dict, csv_Folder_Path, Category_Kor, Category_Eng,
                                      Region_Dict, Category_List_R, Produce_Num,
                                      region, category, key_produce)
                chart = MyChart.Retail()

                return render_template('dash/retail.html',
                                       region=region, category=category, key_produce=key_produce,
                                       radio_check=radio_check, date=chart['1']['date'],
                                       result_t=chart['1']['result_t'],
                                       result_t_total=chart['1']['result_t_total'],
                                       yhat_l_T=chart['1']['yhat_l_T'], yhat_u_T=chart['1']['yhat_u_T'],
                                       result_m=chart['2']['result_m'],
                                       result_m_total=chart['2']['result_m_total'],
                                       yhat_l_M=chart['2']['yhat_l_M'], yhat_u_M=chart['2']['yhat_u_M'],
                                       month_List=chart['3']['month_List'],
                                       month_price_T=chart['3']['month_price_T'],
                                       month_price_M=chart['3']['month_price_M'])


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
        print(category)
        temp = request.args.get('search')
        print(temp)
        # dt = Food_recipe.query.filter(Food_recipe.dish == category).all()
        return render_template('dash/compare2.html')#, category=category)


# chart
@bp.route('/chart')
def chart():
    quarter = {'1Q': ['01', '03'], '2Q': ['04', '06'],
               '3Q': ['07', '09'], '4Q': ['10', '12']}
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    now = datetime.now()
    sql_end = "SELECT date FROM wholesale_quantity WHERE date " + "ORDER BY date DESC LIMIT 1;"
    cursor.execute(sql_end)
    end_db = cursor.fetchall()
    end_date = end_db[0][0]
    quarter_List = []
    for minus in range(4, -1, -1):
        calculation = now - relativedelta(years=minus)
        year = calculation.strftime("%Y")
        q_y = []
        for i, j in quarter.items():
            q = []
            sql_first = "SELECT date FROM wholesale_quantity WHERE date LIKE '" + year + j[0] + "%' LIMIT 1;"
            cursor.execute(sql_first)
            first_db = cursor.fetchall()
            q.append(first_db[0][0])
            if int(year) == now.year and (int(str(end_date)[:6]) - int(year + j[1])) < 0:
                sql_last = "SELECT date FROM wholesale_quantity WHERE date= '" + str(end_date) + "';"
                cursor.execute(sql_last)
                last_db = cursor.fetchall()
                q.append(last_db[0][0])
                q_y.append(q)
                break

            sql_last = "SELECT date FROM wholesale_quantity WHERE date LIKE '" + \
                       year + j[1] + "%' ORDER BY date DESC LIMIT 1;"
            # sql = "SELECT sum(" + button + ") FROM wholesale_quantity WHERE date between 20180102 and 20180331;"
            cursor.execute(sql_last)
            last_db = cursor.fetchall()
            q.append(last_db[0][0])
            q_y.append(q)
        quarter_List.append(q_y)
    return render_template('dash/chart.html')


# table
@bp.route('/table/<ingredient>', methods=('GET', 'POST'))
def table(ingredient):
    # dt = Food_recipe.query.filter(Food_recipe.dish == keyword).all()
    sql_t = 'SELECT * FROM food_recipe WHERE dish LIKE "%{}%" ORDER BY views DESC LIMIT 10;'.format(ingredient)
    cursor.execute(sql_t)
    dt = cursor.fetchall()
    return render_template('dash/table.html', dt=dt)
