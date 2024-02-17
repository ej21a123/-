import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

#Webページを取得して解析する
load_url = "https://www.eldenring.jp/concept.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

#保存用フォルダを作る
out_folder = Path("eldenring2")
out_folder.mkdir(exist_ok=True)

#すべてのimgタグを検索し、リンクを取得する
for element in soup.find_all("source"):
    src = element.get("srcset")

    #絶対URLを作って、画像データを取得する
    source_url = urllib.parse.urljoin(load_url,src)
    sourcedata = requests.get(source_url)

    #URLから最後のファイル名を取り出して、保存フォルダ名とつなげる
    filename = source_url.split("/")[-1]
    out_path = out_folder.joinpath(filename)

    #画像データを、ファイルに書き出す
    with open(out_path,mode="wb")as f:
        f.write(sourcedata.content)

    #1回アクセスしたので1秒待つ
    time.sleep(1)
