import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("test.csv")

#条件に合うデータを抽出する
data_a = df[df["数学"] >= 90]
print("数学が90点以上\n",data_a)

print("")

data_b = df[df["英語"] <70]
print("英語が70点未満\n",data_b)

print("")
#集計（最大値、最小値、平均値、中央値、合計等）を表示
print("数学の最高点 = ",df["数学"].max())
print("数学の最低点 = ",df["数学"].min())
print("数学の平均値 = ",df["数学"].mean())
print("数学の中央値 = ",df["数学"].median())
print("数学の合計点 = ",df["数学"].sum())
