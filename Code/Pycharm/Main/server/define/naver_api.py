import json
import re
import traceback
import urllib.request


class Naverapi:

    def __init__(self, pname, client_id, client_secret):
        self.pname = pname
        self.client_id = client_id
        self.client_secret = client_secret

    def Navershop(self):
        try:
            # print(pname)
            encText = urllib.parse.quote(self.pname)
            url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=3&sort=sim&start=1"

            try:
                request = urllib.request.Request(url)
                request.add_header("X-Naver-Client-Id", self.client_id)
                request.add_header("X-Naver-Client-Secret", self.client_secret)
                response = urllib.request.urlopen(request)
                rescode = response.getcode()

                if (rescode == 200):
                    response_body = response.read()
                    response_json = json.loads(response_body)

                    data_List = []
                    for temp in response_json['items']:
                        dictdata = {}
                        dictdata['이름'] = re.sub("<b>|</b>", "", temp['title'])
                        dictdata['최저가격'] = str(format(int(temp['lprice']), ','))
                        dictdata['이미지'] = temp['image']
                        dictdata['url'] = temp['link']
                        data_List.append(dictdata)
                    # print(response_body.decode('utf-8'))
                else:
                    print("Error Code:" + rescode)

            except Exception as e:
                message = traceback.format_exc()
                print(message)
                data_List = []
            return data_List

        except Exception as e:
            message = traceback.format_exc()
            return message


def Navernews(topic):
    # print(topic)
    client_id = "MiUA1cOwkgZ7FPIPBawa"
    client_secret = "sdSR7YXRu8"
    encText = urllib.parse.quote(topic)
    url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=10&sort=date&start=1"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        response_json = json.loads(response_body)

        article_List = []
        dictdata = {}
        for temp in response_json['items']:
            dictdata['제목'] = re.sub("<b>|</b>|&apos;|&quot;", "", temp['title'])
            dictdata['링크'] = temp['originallink']
            article_List.append(dictdata)
        # print(response_body.decode('utf-8'))
        # print(article_list)
    else:
        print("Error Code:" + rescode)
    return article_List
