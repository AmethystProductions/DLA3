import os
import matplotlib.pyplot as plt
# from keras.preprocessing import image
import cv2
import math

path = r"./simpsons_testdataset"
output = r"./data/test"

for folder in os.listdir(path):
  loc = os.path.join(path, folder)

  out_folder = os.path.join(output, folder)
  if not os.path.exists(out_folder):
    os.makedirs(out_folder)

  for f in os.listdir(loc):
      img = cv2.imread(os.path.join(loc, f))
      if img is None or "gif" in f:
        continue
      print(os.path.join(loc, f))

      width, height = img.shape[0:2]
      # print("({}, {}) -> ".format(width, height), end="")
      height = math.ceil(height/2)
      width = math.ceil(width/2)
      size = max(width, height)

      img_padded = cv2.copyMakeBorder(
        img, 
        (size-width), 
        (size-width), 
        (size-height), 
        (size-height), 
        cv2.BORDER_CONSTANT)
      # print("[{}, {}]".format(img_padded[0], img_padded[1]))

      out_file = os.path.join(out_folder, f)
      cv2.imwrite(out_file, img_padded)
      
      