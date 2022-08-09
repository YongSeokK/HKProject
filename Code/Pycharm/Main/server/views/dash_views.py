import pandas as pd
import pymysql
from flask import Blueprint, request, render_template, url_for, session, flash
from requests import request
from werkzeug.utils import redirect

from config import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME, csv_FolderPath
from server.models import Food_recipe, Wholesale_quantity, Wholesale_price, Total_retail
from server.views.category import Category_List, Category_Kor

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
            dt_r = Total_retail.query[-14:]
            dt_wp = Wholesale_price.query[-14:]
            dt_wq = Wholesale_quantity.query[-14:]
            dt_wp_q = Wholesale_price.query.all()
            dt_wq_q = Wholesale_quantity.query.all()
            # 소매가 날짜 불러오기
            dt_r_date = []
            for i in dt_r:
                dt_r_date.append(str(i.date)[4:6] + '.' + str(i.date)[6:8])

            # 도매 날짜, 가격, 물량 불러오기
            dt_wq_date = []
            for i in dt_wq:
                dt_wq_date.append(str(i.date)[4:6] + '.' + str(i.date)[6:8])

            dt_wp_potato = []
            for i in dt_wp:
                dt_wp_potato.append(round(i.potato, -1))

            dt_wq_potato = []
            for i in dt_wq:
                dt_wq_potato.append(i.potato / 1000)

            # DB_source 파일의 csv potato 가져오기
            test_df = pd.read_csv(csv_FolderPath + '20220804_wholesale_potato.csv')
            p_days = []
            ds_val = test_df['ds'].values.tolist()
            for i in ds_val:
                p_days.append(str(i)[5:7] + '.' + str(i)[8:10])
            yhat_val = round(test_df['yhat'], -1).values.tolist()
            yhat_l_val = round(test_df['yhat_lower'], -1).values.tolist()
            yhat_u_val = round(test_df['yhat_upper'], -1).values.tolist()
            print(p_days)
            print('평균')
            print(yhat_val)
            print('최소')
            print(yhat_l_val)
            print('최대')
            print(yhat_u_val)

            # 18년 1분기 ~ 22년 3분기까지 전부 - 식량작물 감자 평균가격

            potato_p_list = []
            wholesale_pp_list = {
                'sql_18_1': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20180102 and 20180331;",
                'sql_18_2': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20180402 and 20180630;",
                'sql_18_3': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20180702 and 20180929;",
                'sql_18_4': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20181001 and 20181231;",
                'sql_19_1': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20190102 and 20190330;",
                'sql_19_2': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20190401 and 20190629;",
                'sql_19_3': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20190701 and 20190930;",
                'sql_19_4': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20191001 and 20191231;",
                'sql_20_1': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20200102 and 20200331;",
                'sql_20_2': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20200302 and 20200630;",
                'sql_20_3': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20200701 and 20200929;",
                'sql_20_4': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20201005 and 20201231;",
                'sql_21_1': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20210102 and 20210331;",
                'sql_21_2': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20210401 and 20210630;",
                'sql_21_3': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20210701 and 20210930;",
                'sql_21_4': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20211001 and 20211231;",
                'sql_22_1': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20220103 and 20220331;",
                'sql_22_2': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20220401 and 20220630;",
                'sql_22_3': "SELECT sum(potato), count(potato) FROM wholesale_price WHERE date between 20220701 and 20220730;"
            }

            for i in wholesale_pp_list.values():
                cursor.execute(i)
                result = cursor.fetchall()
                print('---', result[0])
                days = result[0][1]
                total_price = result[0][0]
                potato_p_list.append(round((total_price / days), -1))
            print(potato_p_list)

            # 18년 1분기 ~ 22년 3분기까지 전부 - 식량작물 감자 총 판매량

            potato_q_list = []
            wholesale_pq_list = {
                'sql_18_1': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20180102 and 20180331;",
                'sql_18_2': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20180402 and 20180630;",
                'sql_18_3': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20180702 and 20180929;",
                'sql_18_4': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20181001 and 20181231;",
                'sql_19_1': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20190102 and 20190330;",
                'sql_19_2': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20190401 and 20190629;",
                'sql_19_3': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20190701 and 20190930;",
                'sql_19_4': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20191001 and 20191231;",
                'sql_20_1': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20200102 and 20200331;",
                'sql_20_2': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20200302 and 20200630;",
                'sql_20_3': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20200701 and 20200929;",
                'sql_20_4': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20201005 and 20201231;",
                'sql_21_1': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20210102 and 20210331;",
                'sql_21_2': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20210401 and 20210630;",
                'sql_21_3': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20210701 and 20210930;",
                'sql_21_4': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20211001 and 20211231;",
                'sql_22_1': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20220103 and 20220331;",
                'sql_22_2': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20220401 and 20220630;",
                'sql_22_3': "SELECT sum(potato) FROM wholesale_quantity WHERE date between 20220701 and 20220730;"
            }

            for i in wholesale_pq_list.values():
                cursor.execute(i)
                result = cursor.fetchall()
                potato_q_list.append(round(result[0][0] / 1000))
            print(potato_q_list)

            # return render_template('dash/compare.html', )
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
                return render_template('dash/wholesale.html', category=category, radio_check=radio_check,
                                       dt_r_date=dt_r_date, dt_wq_date=dt_wq_date, dt_wp_potato=dt_wp_potato,
                                       dt_wq_potato=dt_wq_potato, potato_q_list=potato_q_list,
                                       potato_p_list=potato_p_list, p_days=p_days, yhat_val=yhat_val,
                                       yhat_l_val=yhat_l_val, yhat_u_val=yhat_u_val)
            else:
                category = request.form.get('category')
                print('도매: ' + category)
                dic_set = Category_List[Category_Kor.index(category)]
                radio_check = dic_set.copy()
                keys_list = list(radio_check.keys())
                radio_check[keys_list[0]] = ' checked="checked" '
                return render_template('dash/wholesale.html', category=category, radio_check=radio_check,
                                       dt_r_date=dt_r_date, dt_wq_date=dt_wq_date, dt_wp_potato=dt_wp_potato,
                                       dt_wq_potato=dt_wq_potato, potato_q_list=potato_q_list,
                                       potato_p_list=potato_p_list, p_days=p_days, yhat_val=yhat_val,
                                       yhat_l_val=yhat_l_val, yhat_u_val=yhat_u_val)


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
@bp.route('/compare2/<category>', methods=('GET', 'POST'))
def compare2(category):
    user_nickname = session.get('user_nickname')
    if user_nickname is None:
        flash("로그인이 필요합니다.")
        return redirect(url_for('main.login'))
    else:
        z=request.args
        print(z)
        return render_template('dash/compare2.html',category=category)


# chart
@bp.route('/chart')
def chart():
    return render_template('dash/chart.html')


# table
@bp.route('/table')
def table():
    dt = Food_recipe.query.filter(Food_recipe.dish == '김치찌개').all()
    return render_template('dash/table.html', dt=dt)
