import os

path = r"./data"
dic = {}

i = 0
for folder in os.listdir(path):
    dic[i] = folder
    i += 1

print(dic)