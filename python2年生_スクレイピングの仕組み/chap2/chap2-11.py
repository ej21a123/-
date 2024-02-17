import requests

#画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

#urlから最後のファイル名を取り出す
filename = image_url.split("/")[-1]     #ファイル名を取得

#画像データを、ファイルに書き出す
with open(filename,mode="wb") as f:     #バイナリー書き込みモードで開いて
    f.write(imgdata.content)             #画像データを書き込む
