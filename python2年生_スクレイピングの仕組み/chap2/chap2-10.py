import requests
from bs4 import BeautifulSoup
import urllib

#webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

#ファイルを書き込みモードで開く
filename = "chap2-10 linklist.txt"
with open(filename,"w") as f:       #ファイルを開いて
    #すべてのaタグを検索し、リンクを絶対ＵＲＬで書きだす
    for element in soup.find_all("a"):
        url = element.get("href")
        link_url = urllib.parse.urljoin(load_url,url)
        f.write(element.text+"\n")
        f.write(link_url+"\n")
        f.write("\n")
