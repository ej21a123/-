import requests

url = "https://www.mc2.osakac.ac.jp/mc2/modules/bulletin/"
response = requests.get(url)         #webページを取得する

response.encoding = response.apparent_encoding      #文字化けしないようにする

#print(response.text)        #取得した文字列データを表示する

filename = "chap1-3 メディアコミュニケーション.txt"

'''
f = open(filename,mode="w")     #ファイルを書き込みモードで開いて

f.write(response.text)      #インターネットから取得したデータを書き込んで

f.close()       #最後にファイルを閉じる
'''

with open(filename,mode="w") as f:      #ファイルを書き込みモードで開いて
    f.write(response.text)          #インターネットから取得したデータを書き込む
