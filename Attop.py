from cookie import COOKIE
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse as parse
import time

class Attop(object):
    def __init__(self):
        self.__version__ = 1.0
        self.cookie = COOKIE
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'cookie': self.cookie
        }
        self.r = requests.Session()
        self.r.headers=self.headers

        d_url = 'http://www.attop.com/wk/'
        url = 'http://www.attop.com/wk/learn.htm?id=74'
        comments = []

        def get_comment(url):
            html = requests.get(url, timeout=20, headers=self.headers).text
            soup = BeautifulSoup(html, 'lxml')
            liTags = soup.find_all('li', attrs={'id': re.compile('j_20[0-9]*')})
            for li in liTags:
                try:
                    aTags = li.find_all('a')
                    for a in aTags:
                        href = a.get("href")
                        comments.append(href)
                except Exception as e:
                    print(e)

        get_comment(url=url)
        urls_map = map(lambda x: d_url + x, comments)
        self.urls = list(urls_map)

    def post_all(self, num):
        def post_1(num):
            url = 'http://www.attop.com/js/ajax/call/plaincall/__System.pageLoaded.dwr'
            params = {
                "callCount": 1,
                "windowName": "",
                "c0-scriptName": "__System",
                "c0-methodName": "pageLoaded",
                "c0-id": 0,
                "batchId": 0,
                "instanceId": 0,
                "page": f"%2Fwk%2Fmedia_pop.htm%3Fid%3D{num}",
                "scriptSessionId": "D3dTxqr639g6YPSb4tTZAF5g1rm/Pe5h1rm-A4N5tX3td"
            }
            try:
                self.r.post(url=url, data=params)
            except Exception as e:
                print(e)

        def post_2(num):
            url = 'http://www.attop.com/js/ajax/call/plaincall/zsClass.dotAjax.dwr'
            params = {'callCount': 1, 'windowName': '', 'c0-scriptName': 'zsClass', 'c0-methodName': 'dotAjax',
                      'c0-id': 0,
                      'c0-param0': 'string:doWkMediaPj', 'c0-e1': f'number:{num}', 'c0-e2': 'number:3',
                      'c0-param1': 'Object_Object:{id:reference:c0-e1, type:reference:c0-e2}',
                      'c0-param2': 'string:doWkMediaPj', 'batchId': 1, 'instanceId': 0,
                      'page': f'%2Fwk%2Fmedia_pop.htm%3Fid%3D{num}',
                      'scriptSessionId': 'D3dTxqr639g6YPSb4tTZAF5g1rm/Pe5h1rm-A4N5tX3td'}
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'cookie': self.cookie,
                'Referer': f'http://www.attop.com/wk/media_pop.htm?id={num}'
            }
            self.r.headers = headers

            try:
                self.r.post(url=url, data=params)
            except Exception as e:
                print(e)

        def post_3():
            url = 'http://www.attop.com/js/ajax/call/plaincall/zsClass.commonAjax.dwr'
            params = {'callCount': 1, 'windowName': '', 'c0-scriptName': 'zsClass', 'c0-methodName': 'commonAjax',
                      'c0-id': 0,
                      'c0-param0': 'string:getTopDhNum', 'c0-param1': 'Object_Object:{}',
                      'c0-param2': 'string:doGetTopDhNum',
                      'batchId': 10, 'instanceId': 0, 'page': '%2Fuser%2Fstudy.htm',
                      'scriptSessionId': 'D3dTxqr639g6YPSb4tTZAF5g1rm/eUbg1rm-btMEtv2Ij'}

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'cookie': self.cookie,
                'Referer': 'http://www.attop.com/user/study.htm'
            }
            self.r.headers = headers

            try:
                self.r.post(url=url, data=params)
            except Exception as e:
                print(e)

        def post_4():
            url = 'http://www.attop.com/js/ajax/call/plaincall/zsClass.commonAjax.dwr'
            params = {'callCount': 1, 'windowName': '', 'c0-scriptName': 'zsClass', 'c0-methodName': 'commonAjax',
                      'c0-id': 0,
                      'c0-param0': 'string:getAjaxList', 'c0-e1': f'string:id%3D{self.id}%26jid%3D{self.jid}',
                      'c0-e2': 'string:learn.htm',
                      'c0-e3': 'number:1', 'c0-e4': 'string:showajaxinfo',
                      'c0-param1': 'Object_Object:{param:reference:c0-e1, pagename:reference:c0-e2, currentpage:reference:c0-e3, showmsg:reference:c0-e4}',
                      'c0-param2': 'string:doGetAjaxList', 'batchId': 5, 'instanceId': 0,
                      'page': f'%2Fwk%2Flearn.htm%3Fid%3D{self.id}%26jid%3D{self.jid}',
                      'scriptSessionId': 'D3dTxqr639g6YPSb4tTZAF5g1rm/PZ2h1rm-Fzku8t615'}

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'cookie': self.cookie,
                'Referer': f'http://www.attop.com/wk/learn.htm?id={self.id}&jid={self.jid}'
            }
            self.r.headers = headers

            try:
                self.r.post(url=url, data=params)
            except Exception as e:
                print(e)

        post_1(num)
        post_2(num)
        post_3()
        post_4()
        print(f'- 评价{num}成功')

    def get_nums(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'cookie': self.cookie,
            'Referer': f'http://www.attop.com/wk/learn.htm?id={self.id}&jid={self.jid}'
        }
        self.r.headers = headers
        params = {'callCount': 1, 'windowName': '', 'c0-scriptName': 'zsClass', 'c0-methodName': 'commonAjax',
                  'c0-id': 0, 'c0-param0': 'string:getAjaxList', 'c0-e1': f'string:id%3D{self.id}%26jid%3D{self.jid}',
                  'c0-e2': 'string:learn.htm', 'c0-e3': 'number:1', 'c0-e4': 'string:showajaxinfo',
                  'c0-param1': 'Object_Object:{param:reference:c0-e1, pagename:reference:c0-e2, currentpage:reference:c0-e3, showmsg:reference:c0-e4}',
                  'c0-param2': 'string:doGetAjaxList', 'batchId': 2, 'instanceId': 0,
                  'page': f'%2Fwk%2Flearn.htm%3Fid%3D{self.id}%26jid%3D{self.jid}',
                  'scriptSessionId': 'D3dTxqr639g6YPSb4tTZAF5g1rm/7FXQ3rm-rPukkaJT5'}

        url = 'http://www.attop.com/js/ajax/call/plaincall/zsClass.commonAjax.dwr'
        try:
            res = self.r.post(url, data=params)
            use = res.text.encode('utf8').decode('unicode_escape')
            all_num = re.findall(r'media_([0-9]*)', use)
            print(all_num)
            return all_num
        except Exception as e:
            print(e)

    def comment(self):
        for each in self.urls:
            self.id = parse.parse_qs(parse.urlparse(each).query)['id'][0]
            self.jid = parse.parse_qs(parse.urlparse(each).query)['jid'][0]
            for num in self.get_nums():
                self.post_all(int(num))

    def watch(self):
        r = requests.Session()
        r.headers = self.headers
        print("begin")
        try:
            for url in self.urls:
                r.post(url)
                print("正在刷 {}".format(url))
            print("ok,等个十分钟")
            for i in range(600):
                time.sleep(1)
                print("{}/600秒".format(i))
        except:
            raise Exception("error")
