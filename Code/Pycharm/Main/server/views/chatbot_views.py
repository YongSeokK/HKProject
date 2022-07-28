from flask import Flask, Blueprint, request, render_template, url_for, session, g, flash, jsonify
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from server.forms import UserCreateForm
from server.models import Members, Food_recipe, Wholesale_quantity
from server import db
import json
import re
from server.yolo5_def import YoloRun
import urllib.request
from glob import glob
import os

bp = Blueprint('kakao_chatbot', __name__, url_prefix='/kakao_chatbot')


# Chatbot_이미지 yolo 입출력
@bp.route('/yolo_img', methods=['POST', 'GET'])
def yolo_img():
    req_json = request.get_json()
    # print('응답')
    # print(req_json)
    response = req_json['action']['params']['secureimage']
    response_json = json.loads(response)
    img_tmp = response_json['secureUrls']
    URLList = re.sub('List\(|\)', "", img_tmp).split(',')
    # URLList[0] 은 챗봇에서 사용자가 보낸 사진의 URL주소
    # print(URLList)
    # url 사진 로컬에 저장
    cnt = 1
    for img_url in URLList:
        urllib.request.urlretrieve(img_url,
                                   "C:\\G_Project\\Code\\Pycharm\\Main\\server\\static\\upload_img\\" + "food" + str(
                                       cnt) + ".jpg")
        cnt = cnt + 1
    img_list = glob("C:\\G_Project\\Code\\Pycharm\\Main\\server\\static\\upload_img\\*.jpg")

    result = []
    for img_path in img_list:
        x = YoloRun(img_path)
        result.append(x)

    # return_message = 사용자에게 표시되는 응답
    return_message = {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": str(result)}}]}}
    dir_path = ("C:\\G_Project\\Code\\Pycharm\\Main\\server\\static\\upload_img")
    if os.path.exists(dir_path):
        if len(glob(dir_path + '\\*')) != 0:
            for file in glob(dir_path + '\\*'):
                os.remove(file)
        else:
            print('자료 없음')
    return jsonify(return_message)
