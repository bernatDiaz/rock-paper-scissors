# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import keras
import numpy
from utils import N_prev, encode, intercalate, pad_data, decode, counter

def player(prev_play, model=[], opponent_history = [], ai_history = []):
  if not model:
    model.append(keras.models.load_model("initial_model.h5"))
  
  opponent_history.append(prev_play)
  last_plays_opponent = opponent_history[-N_prev:]
  last_plays_ai = ai_history[-N_prev:]

  last_plays_opponent = list(map(encode, last_plays_opponent))
  last_plays_ai = list(map(encode, last_plays_ai))

  last_plays_opponent.reverse()
  last_plays_ai.reverse()

  last_plays = intercalate(last_plays_opponent, last_plays_ai)

  if len(last_plays) < N_prev * 2:
    last_plays = pad_data(last_plays)
  
  prediction = model[0].predict([last_plays])
  opponent_play_code = numpy.argmax(prediction)
  opponent_play = decode(opponent_play_code)
  play = counter(opponent_play)
  ai_history.append(play)
  return play
