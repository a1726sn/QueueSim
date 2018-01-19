import math
import random as rnd
from Node import Node
import numpy as np
import matplotlib.pyplot as plt

''' メインメソッド '''
if __name__=='__main__':

  # 準備
  totalTime = 60*60*24*3                         # シミュレーション時間（秒）
  s = 4                                          # 窓口数
  mu = 2                                         # サービス平均時間（分）
  dist_type = "expotential"                      # 指数分布
  node1 = Node("node1", mu, s, dist_type)        # ノード1を生成
  lam = 1                                        # 客の到着平均間隔（分)
  arrival = -lam * 60 * math.log(rnd.random())   # 客到着残時間（指数分布）

  x_scale = 10                              # X軸の縮尺（10分区切り）
  x = np.arange(0, totalTime/60, x_scale)   # グラフ出力用X軸配列
  y = []                                    # グラフ出力用Y軸配列（ノード分）
  
  # シミュレーション
  for i in range(0, totalTime):
    # 客到着残時間を1秒減らす
    arrival -= 1

    # 新たな客が到着した時
    if arrival <= 0:
      arrival = -lam * 60 * math.log(rnd.random())
      node1.enqeueu()
      
    # ノードで1秒進める
    node1.sim()

    # グラフ出力用にx_scale分ごとの待ちキューの客数を記録
    if i % (60*x_scale) == 0:
      y.append(len(node1.queue))

  # 結果算出表示
  print("L =", node1.l/totalTime)
  print("Lq =", node1.lq/totalTime)

  # グラフ表示
  plt.plot(x, y, label=node1.name)
  plt.legend()
  plt.title("Simulation_3")
  plt.xlabel("Time (min)")
  plt.ylabel("L")
  plt.grid()
  plt.xlim([0, totalTime/60])
  plt.ylim([0, max(y)*1.2])
  plt.show()

''' ************************************************************ '''
