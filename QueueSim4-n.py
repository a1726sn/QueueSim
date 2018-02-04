import math
import random as rnd
from Node import Node

''' メインメソッド '''
if __name__=='__main__':

  # 準備
  totalTime = 60*60*24*3                             # シミュレーション時間（秒）
  s = 4                                              # 窓口数
  mu = 2                                             # サービス平均時間（分）
  dist_type = "expotential"                          # 指数分布
  n = 6                                            # N段数
  nodes = []                                         # ノードの配列
  prev = Node("node1", mu, s, dist_type)             # ノード1を生成
  nodes.append(prev)                                 # ノードの配列にノード1を追加
  for i in range(1, n):                              # ノードをN段直列に接続
    node = Node("node"+str(i+1), mu, s, dist_type)
    prev.next_node = [node]
    prev = node
    nodes.append(node)

  net= ""                                            # ネットワークを確認
  for node in nodes:
    net += node.name
    if node.next_node != None:
      net += " -> "
  print(net)
  
  lam = 1                                            # 客の到着平均間隔（分)
  arrival = -lam * 60 * math.log(rnd.random())       # 客到着残時間（指数分布）
  
  # シミュレーション
  for i in range(0, totalTime):
    # 客到着残時間を1秒減らす
    arrival -= 1

    # 新たな客が到着した時
    if arrival <= 0:
      arrival = -lam * 60 * math.log(rnd.random())
      nodes[0].enqeueu()
      
    # 各ノードで1秒進める
    for idx, node in enumerate(nodes):
      node.sim()

  # 結果算出表示
  l_sum = 0          # 系内客数のすべてのノードの合計値
  lq_sum = 0         # 待ち客数のすべてのノードの合計値
  for node in nodes:
    l_sum += node.l
    lq_sum += node.lq
    
  print("L =", l_sum/totalTime)
  print("Lq =", lq_sum/totalTime)

''' ************************************************************ '''
