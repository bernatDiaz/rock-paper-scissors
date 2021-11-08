N_prev = 10

def encode(play):
  if play == 'R':
    return 0
  if play == 'P':
    return 1
  if play == 'S':
    return 2
  return 3

def decode(code):
  if code == 0:
    return 'R'
  if code == 1:
    return 'P'
  if code == 2:
    return 'S'
  return ''

def pad_trim_data(data):
  if(len(data) < N_prev * 2):
    return pad_data(data)
  else:
    return data[:N_prev * 2]

def pad_data(data):
  return data + [3] * (N_prev * 2 - len(data))

def intercalate(first, second):
  result = []

  if len(first) <= len(second):
    for i in range(len(first)):
      result.append(first[i])
      result.append(second[i])
    for i in range(len(first), len(second)):
      result.append(second[i])
  else:
    for i in range(len(second)):
      result.append(first[i])
      result.append(second[i])
    for i in range(len(second), len(first)):
      result.append(first[i])

  return result
  
def column_names(N_prev):
  columns = []
  for i in range(1, N_prev + 1):
    columns = columns + ["opponent_previous_play"+str(i), "player_previous_play"+str(i)]
  return columns
column_names = column_names(N_prev)

def counter(play):
  if play == 'R':
    return 'P'
  if play == 'P':
    return 'S'
  if play == 'S':
    return 'R'