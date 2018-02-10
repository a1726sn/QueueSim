import math
import random as rnd
from Node import Node

''' メインメソッド '''
if __name__=='__main__':

  # 準備
  totalTime = 60*60*24*100                       # シミュレーション時間（秒）
  s = 4                                          # 窓口数
  mu = 2                                         # サービス平均時間（分）
  dist_type = "expotential"                      # 指数分布
  node1 = Node("node1", mu, s, dist_type)        # 店を生成
  lam = 1                                        # 客の到着平均間隔（分)
  arrival = -lam * 60 * math.log(rnd.random())   # 客到着残時間（指数分布）

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

  # 結果算出表示
  print("L =", node1.l/totalTime)
  print("Lq =", node1.lq/totalTime)

''' ************************************************************ '''
