
import os

f = open('data/train.txt', 'w')
basepath = './flowers/'
for p1 in os.listdir(basepath):
    image = os.path.abspath(basepath + p1)
    f.write(image + '\n')
f.close()

g = open('data/test.txt', 'w')
basepath = './testimages/'
for p in os.listdir(basepath):
    image = os.path.abspath(basepath + p)
    g.write(image + '\n')
g.close()
