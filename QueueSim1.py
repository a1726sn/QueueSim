import math
import random as rnd

''' 設定値 '''
totalTime = 60*60*24     # シミュレーション時間（分）
queue = [[], [], []]     # 指数分布、一様分布、一定分布の滞在残時間を持った人を管理する
arrival = [0, 0, 0]      # 入場総人数　（指数分布、一様分布、一定分布）
capacity = 60            # 館内の人数制限
w = 300                  # 滞在残時間（分）

''' 滞在残時間初期値生成メソッド '''
def stay_init(idx):
    if idx == 0:     # 指数分布
        return -w * math.log(rnd.random())
    elif idx == 1:   # 一様分布
        return w * 2 * rnd.random()
    else:            # 一定分布
        return w

''' シミュレーション '''
for t in range(1, totalTime):
    for idx in range(len(arrival)):
        # 一人ずつ退出するか確認
        for i, n in enumerate(queue[idx]):
            if n <= 0:              # 退出するかチェック
                del queue[idx][i]   # 退出する
            else:
                queue[idx][i] -= 1  # 滞在残時間を1分減らす

        # 入場できるかチェック
        if len(queue[idx]) <= capacity:
            queue[idx].append(stay_init(idx)) # 滞在残時間を持った人を一人入場させる
            arrival[idx] += 1       # 入場総人数を1増やす

''' 結果算出、表示 '''
print("指数分布を使用した場合の平均入場間隔:", totalTime / arrival[0])
print("一様分布を使用した場合の平均入場間隔:", totalTime / arrival[1])
print("一定分布を使用した場合の平均入場間隔:", totalTime / arrival[2])

''' ************************************************************ '''
