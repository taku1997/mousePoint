import pyautogui
import time
from datetime import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv


def get_now():
  now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
  return now

def get_cursor_loop(loop_second):
  #0.1秒ずつ指定位置をカーソル位置取得
  #loop_second:int -　データを取得する秒数

  times = []
  position = []
  for _ in range(0, loop_second*10):
    #時刻とカーソル位置の取得
    now = get_now()
    x,y = pyautogui.position()

    #リストに情報を追加
    times.append(now)
    position.append([x,y])
    time.sleep(0.1)
  return times, position

def get_windows_size():
  windows_size = pyautogui.size()
  return windows_size


def write_file(position):
  writeTime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
  with open('data/{}.csv'.format(writeTime),'w') as f:
    writer = csv.writer(f)
    for i in position:
       writer.writerow([i[0],i[1]])
      

if __name__ == "__main__":
    times,position = get_cursor_loop(5)
    windows_size = get_windows_size()
    write_file(position)

    data = np.array(position)
    df = pd.DataFrame(data, columns=['x', 'y'])
    # (0,0)座標が画面の左上なのでy軸のみ順番を反転
    sns.jointplot(data=df, x='x', y='y', xlim=(0, windows_size[0]), ylim=(windows_size[1], 0))
    plt.show()