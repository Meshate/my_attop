import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'cookie': 'Hm_lvt_276e4ec7ba0aa6e4db3b46c40cde6e63=1540823733; rand=7570; memcached_zz=383531_1528982984127265461nMg56is6Oj6E5bR4YNYroNtlxdZakXSX462knrxMkmKJbrtCxL5Lcqq84UmEBl5A3EWvOgtJfmc8qIfNQJuZw63BKbbtYueWoRCleHqbVTPnZ; dang_username=zaccc; JSESSIONID=A9F00AE476CDEA4BE4DD5DD7DF6817D6; DWRSESSIONID=D3dTxqr639g6YPSb4tTZAF5g1rm; Hm_lpvt_276e4ec7ba0aa6e4db3b46c40cde6e63=1540823982'
}

def d_url_comments():
    d_url = 'http://www.attop.com/wk/'
    url = 'http://www.attop.com/wk/learn.htm?id=74'
    comments = []

    def get_comment(url):
        html = requests.get(url, timeout=20, headers=headers).text
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
    urls = list(urls_map)
    return urls