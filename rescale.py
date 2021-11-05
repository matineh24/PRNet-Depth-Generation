from skimage.transform import rescale
import cv2
from os import walk
from skimage.io import imread, imsave
import sys

try:
    write_path = sys.argv[1] + '/'
    rescale_size = float(sys.argv[2])
except:
    write_path = './test1/'
    rescale_size = 400.0

'''
Rescale files if the depth map creation is taking long

To use this file, run python rescale.py A B 
A: 
    Path of the folder containing images
B: 
    An integer specifying the rescaled image's height 

'''

f = []
for (dirpath, dirnames, filenames) in walk(write_path):

    for i in filenames:
        image = imread(dirpath+'/' + i)
        r = rescale_size / image.shape[0]
        dim = (int(image.shape[1] * r), int(rescale_size))
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        path = dirpath +'/'+ i
        cv2.imwrite(path, cv2.cvtColor(resized, cv2.COLOR_RGB2BGR))





