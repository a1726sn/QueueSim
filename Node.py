import math
import random as rnd
from collections import deque

class Node:

  ''' コンストラクタ '''
  def __init__(self, name, mu, s, dist_type, next_node=None):
    self.name = name            # ノード名
    self.queue = deque([])      # 待ちキュー
    self.mu = mu                # サービス平均時間（分）
    self.service = [0]*s        # サービス受け残時間（× 窓口数）
    self.next_node = next_node  # 次のノード（配列）
    self.l = 0                  # 系内客数の合計値
    self.lq = 0                 # 待ち客数の合計値
    self.dist_type = dist_type  # 使用する分布

  ''' 分布 '''
  def distribution(self, dist):  
    if self.dist_type == "expotential":             # 指数分布
      return -self.mu * 60 * math.log(rnd.random())
    elif self.dist_type == "uniform":               # 一様分布
      return self.mu * 2 * 60 * rnd.random()
    else:                                           # 一定分布
      return self.mu
    
  ''' 待ちキューに追加 '''
  def enqeueu(self):
    self.queue.append(self.distribution(self.dist_type))

  ''' 待ちキューから取り出す '''
  def deqeueu(self, i):
    # 待ちキューから取り出す
    self.service[i] = self.queue.popleft()

    # もし次のノードがあれば、次のノードの中で一番空いている待ちキューに追加
    if self.next_node != None:
      min_node = self.next_node[0]
      for node in self.next_node:
        if len(node.queue) < len(min_node.queue):
          min_node = node
      min_node.enqeueu()
    
  ''' 1秒間のシミュレーション処理 '''
  def sim(self):
    # 窓口ごとにシミュレーション処理を実行
    for i in range(len(self.service)):
      # サービス受け残時間を1秒減らす
      if self.service[i] > 0:
        self.service[i] -= 1

      # 窓口に客がおらず、待ち行列に待っている人がいる時
      if self.service[i] <= 0 and len(self.queue) > 0:
        self.deqeueu(i)

      # 窓口に客が残っている場合、窓口の客数を合計値に追加
      if self.service[i] > 0:
        self.l += 1

      self.l += len(self.queue)    # 系内客数の合計値に待ち客数を追加
      self.lq += len(self.queue)   # 待ち客数の合計値に待ち客数を追加

''' ************************************************************ '''
