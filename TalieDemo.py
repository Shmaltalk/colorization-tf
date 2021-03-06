import tensorflow as tf
from utils import *
from net import Net
from skimage.io import imsave
from skimage.transform import resize
import cv2
import os

autocolor = Net(train=False)


saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess, 'models/model.ckpt')
    

    lst = open('./data/test.txt')
    for name in lst:
        name = name.strip()
        #print(name)
        img = cv2.imread(name)
        #print(img)
        if len(img.shape) == 3:
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        img = img[None, :, :, None]
        data_l = (img.astype(dtype=np.float32)) / 255.0 * 100 - 50

        #data_l = tf.placeholder(tf.float32, shape=(None, None, None, 1))

        conv8_313 = autocolor.inference(data_l)
        conv8_313 = sess.run(conv8_313)  
    
        img_rgb = decode(data_l, conv8_313,2.63)
        savename = '/home/taliem/Color/testColor/' + os.path.basename(name)
        imsave(savename, img_rgb)
