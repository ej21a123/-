import pandas as pd

df = pd.read_csv("test.csv")

#ソート(並べ替え）をして表示
kokugo = df.sort_values("国語",ascending = False)
print("国語の点が高いもの順でソート\n",kokugo)#昇順
print("")
suugaku = df.sort_values("数学")
print("数学の点が低いもの順でソート\n",suugaku)#降順

#行と列を入れ替える
print("行と列を入れ替える\n",df.T)

#データをリスト化する
print("Pythonのリストデータ化\n",df.values)
