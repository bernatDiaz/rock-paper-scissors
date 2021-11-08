import pandas as pd
from random import randrange

from RPS_game import kris
from utils import encode, decode, pad_trim_data, column_names
from train_bots import quincy_train, mrugesh_train, abbey_train

def build_data(opponent, num_games = 25, plays_per_game = 1000, hasMemory=False):
  data = []
  labels = []
  for i in range(num_games):
    print(i)
    subdata = []
    if hasMemory:
      opponent_play = opponent("", reset=True)
    else:
      opponent_play = opponent("")
    play = decode(randrange(3))
    data.append(pad_trim_data(subdata))
    labels.append(encode(opponent_play))

    for _ in range(plays_per_game - 1):
      subdata = [encode(opponent_play), encode(play)] + subdata
      opponent_play = opponent(play)
      play = decode(randrange(3))
      data.append(pad_trim_data(subdata))
      labels.append(encode(opponent_play))

  df = pd.DataFrame(data, columns=column_names)
  df['label'] = labels

  return df

def build_initial():
  dfs = []
  dfs.append(build_data(kris))
  dfs.append(build_data(quincy_train, hasMemory=True))
  dfs.append(build_data(mrugesh_train, hasMemory=True))
  dfs.append(build_data(abbey_train, hasMemory=True))
  df = pd.concat(dfs)
  df.to_csv("initial_data.csv")
