import math
import random as rnd
from Node import Node
import numpy as np
import matplotlib.pyplot as plt

''' メインメソッド '''
if __name__=='__main__':

  # 準備
  totalTime = 60*60*24*3                       # シミュレーション時間（秒）
  s = 2                                        # 窓口数
  mu = 2                                       # サービス平均時間（分）
  dist_type = "expotential"                    # 指数分布
  node4 = Node("node4", mu, s, dist_type)                  # ノード4を生成
  node3 = Node("node3", mu, s, dist_type, [node4])         # ノード3を生成
  node2 = Node("node2", mu, s, dist_type, [node4])         # ノード2を生成
  node1 = Node("node1", mu, s, dist_type, [node2, node3])  # ノード1を生成
  nodes = [node1, node2, node3, node4]                     # ノードの配列
  lam = 2                                            # 客の到着平均間隔（分)
  arrival = [-lam * 60 * math.log(rnd.random())]*2   # 客到着残時間２つ（指数分布）

  x_scale = 10                               # X軸の縮尺（10分区切り）
  x = np.arange(0, totalTime/60, x_scale)    # グラフ出力用X軸配列
  y = []                                     # グラフ出力用Y軸配列（ノード分）
  for i in range(len(nodes)):
    y.append([])
    
  # シミュレーション
  for i in range(0, totalTime):
    # 各客到着経路で実行
    for idx, n in enumerate(arrival):
      # 客到着残時間を1秒減らす
      arrival[idx] -= 1

      # 新たな客が到着した時、先頭のノードの待ちキューに追加
      if arrival[idx] <= 0:
        arrival[idx] = -lam * 60 * math.log(rnd.random())
        node1.enqeueu()
      
    # 各ノードで1秒進める
    for idx, node in enumerate(nodes):
      node.sim()
      # グラフ出力用にx_scale分ごとの待ちキューの客数を記録
      if i % (60*x_scale) == 0:
        y[idx].append(len(node.queue))

  # 結果算出表示
  l_sum = 0          # 系内客数のすべてのノードの合計値
  lq_sum = 0         # 待ち客数のすべてのノードの合計値
  for node in nodes:
    l_sum += node.l
    lq_sum += node.lq
    
  print("L =", l_sum/totalTime)
  print("Lq =", lq_sum/totalTime)

  # グラフ表示
  for idx, sub in enumerate(y):
    plt.plot(x, sub, label=nodes[idx].name)
  plt.legend()
  plt.title("Simulation_5")
  plt.xlabel("Time (min)")
  plt.ylabel("L")
  plt.grid()
  plt.xlim([0, totalTime/60])
  plt.ylim([0, max(np.array(y).flatten())*1.2])
  plt.show()

''' ************************************************************ '''
