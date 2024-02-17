import pandas as pd

df = pd.read_csv("test.csv")
print("データの件数：",len(df))
print("項目名：",df.columns.values)
print("インデックス：",df.index.values)

print("")
#1行のデータの表示
print("数学の列データ\n",df["数学"])
#複数行のデータの表示
print("名前、英語、理科の列データ\n",df[["名前","英語","理科"]])   #3つでも[]は2重でOK
