import json
import re
import urllib.request


def Navershop(pname):
    # print(pname)

    client_id = "MiUA1cOwkgZ7FPIPBawa"
    client_secret = "sdSR7YXRu8"
    encText = urllib.parse.quote(pname)
    url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=1&sort=sim&start=1"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        response_json = json.loads(response_body)

        dictdata = {}
        for temp in response_json['items']:
            dictdata['이름'] = re.sub("<b>|</b>", "", temp['title'])
            dictdata['최저가격'] = temp['lprice']
            dictdata['이미지'] = temp['image']
            dictdata['url'] = temp['link']

        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    return dictdata
