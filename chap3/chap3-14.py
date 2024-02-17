import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("test.csv")

#グラフを作って表示する
df.plot()
plt.show()
