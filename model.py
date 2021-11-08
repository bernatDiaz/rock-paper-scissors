from tensorflow import keras
from tensorflow.keras import layers
from keras.utils.np_utils import to_categorical
import pandas as pd

from utils import N_prev

def build_model():
  
  model = keras.Sequential()
  model.add(layers.InputLayer(input_shape=(N_prev * 2,)))
  model.add(layers.Embedding(input_dim=4, output_dim=3, input_length=N_prev * 2))
  model.add(layers.Flatten())
  model.add(layers.Dense(64, activation='relu'))
  model.add(layers.Dense(64, activation='relu'))
  model.add(layers.Dense(64, activation='relu'))
  model.add(layers.Dense(3))
  model.add(layers.Softmax())

  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

  return model

def train(file_data, file_model):
  data = pd.read_csv(file_data)
  data = data.sample(frac=1).reset_index(drop=True)

  print("loaded")
  label = data.pop('label')
  data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
  categorical_labels = to_categorical(label, num_classes=3)

  model = build_model()
  model.fit(data, categorical_labels, validation_split=0.2)
  model.save(file_model)