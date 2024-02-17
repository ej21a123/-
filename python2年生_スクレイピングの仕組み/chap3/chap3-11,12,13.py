import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("test.csv")

#ソート（国語の点数が高いもの順)
kokugo = df.sort_values("国語",ascending=False)

#CSVファイルに出力する
kokugo.to_csv("export1.csv")
#CSVファイルにし、インデックスを削除して出力
kokugo.to_csv("export2.csv",index=False)
#CSVファイルにし、インデックスとヘッダーを削除にて出力
kokugo.to_csv("export3.csv",index=False,header=False)

