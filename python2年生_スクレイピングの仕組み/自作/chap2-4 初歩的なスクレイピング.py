import requests
from bs4 import BeautifulSoup

#webページを取得して解析する
load_url = "https://www.eldenring.jp/concept.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

#すべてのimgタグを検索して表示する
for element in soup.find_all("img"):
    print(element)
