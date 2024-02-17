import requests
from pathlib import Path

#保存用フォルダを作る
out_folder = Path("chap2-12download")
out_folder.mkdir(exist_ok=True)         #chap2-12downloadフォルダを作成

#画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

#urlから最後のファイル名を取り出して、保存フォルダ名とつなげる
filename = image_url.split("/")[-1]
out_path = out_folder.joinpath(filename)        #フォルダ名と連結

#画像データを、ファイルに書き出す
with open(out_path,mode="wb") as f:
    f.write(imgdata.content)
