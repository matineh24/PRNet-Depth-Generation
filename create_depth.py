import glob
import os
import sys

import pandas as pd
from skimage.io import imread, imsave

import utils.depth_image as DepthImage
from api import PRN

# from tqdm import tqdm

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

prn = PRN(is_dlib=True, is_opencv=False)

path_image = './test_images_self_created-resize/'
write_path = './test_depth_self_created_resize/'

f = []
folders = glob.glob(os.path.join(path_image, '*'))

for f in folders:
    name_pure = os.path.split(f)[1]
    files = glob.glob(os.path.join(f, '*'))
    for file in files:
        file_name = os.path.split(file)[1].split('scene')[0]
        dirr = write_path + name_pure + '/'
        if os.path.isdir(dirr):
            if os.path.isfile(dirr + file_name + 'depth1D.jpg'):
                continue
        try:
            image = imread(file)
            image_shape = [image.shape[0], image.shape[1]]
            pos, (left, right, top, bottom) = prn.process(image, None, None, image_shape)
            y = top
            x = left
            w = right - left
            h = bottom - top
            kpt = prn.get_landmarks(pos)
            vertices = prn.get_vertices(pos)
            depth_scene_map = DepthImage.generate_depth_image(vertices, kpt, image.shape, isMedFilter=True)
            bbox = pd.DataFrame([y, x, w, h], columns=['ax'])
            bbox.to_csv(os.path.split(file)[0] + '/' + file_name + 'scene.dat')
            dirr = write_path + name_pure + '/'
            new_path = dirr + file_name + 'depth1D.jpg'
            if not os.path.isdir(dirr):
                os.mkdir(dirr)
            imsave(new_path, depth_scene_map)
        except:
            continue

sys.exit()
