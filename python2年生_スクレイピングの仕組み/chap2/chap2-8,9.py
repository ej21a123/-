import requests
from bs4 import BeautifulSoup
import urllib

#webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

#全てのaタグを検索して、リンクを表示する
for element in soup.find_all("a"):      #全てのaタグを検索
    print(element.text)
    url = element.get("href")       #href属性を取り出す
    link_url = urllib.parse.urljoin(load_url,url)     #絶対urlを取得
    print(link_url)
