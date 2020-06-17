import os
import math
import random
path = r'./data'
output = r"./test"

for folder in os.listdir(path):
  loc = os.path.join(path, folder)

  out_folder = os.path.join(output, folder)
  if not os.path.exists(out_folder):
    os.makedirs(out_folder)
  
  files_in_folder = []
  for f in os.listdir(loc):
      files_in_folder.append(f)
  
  random.shuffle(files_in_folder)

  for f in files_in_folder[:math.floor(len(files_in_folder)*0.2)]:
    os.rename(os.path.join(loc, f), os.path.join(out_folder, f))
