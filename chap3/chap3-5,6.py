import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("test.csv")

#1列データを追加
df["美術"] = [68,73,82,77,94,96]
print("列データ（美術）を追加\n",df)

#1行データを追加
df.loc[6] = ["G男",90,92,94,99,92,93]
print("行データを追加\n",df)

print("")

#名前の列を削除
print("名前の列を削除\n",df.drop("名前",axis=1))

#インデックスの行を削除
print("インデックスの行を削除\n",df.drop(2,axis=0))
