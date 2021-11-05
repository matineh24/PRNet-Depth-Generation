import cv2
import os
from os import walk
import time
import sys

try:
    mypath = sys.argv[1] + '/'
    dest = sys.argv[2] + '/'
    isFull = int(sys.argv[3])

except:
    mypath = './test_files_self_created/'
    dest = './test_images_self_created/'
    isFull = 1

'''
This script generates frames out of videos and put them into different folders with the 
organization that could directly be used by create depth script and then in the major project. 

To use this file, run python make_frames_from_videos.py A B C
A: 
    Path of the folder containing all the video files
B: 
    Path of the destination folder
C:
    if C==1 then all of the frames will be extracted (Use for testing OULU-NPU)
    if C==0 then only first 5 frames are extracted (Use for testing with new data)

Example assume we have folder origin and folder dest and we want to save only 5 frames:
     python make_frames_from_videos.py origin dest 0
'''

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    print(filenames)

for x in f:
    if x.split('.')[1] == 'mp4':
        vidcap = cv2.VideoCapture(mypath + x)
        success, image = vidcap.read()
        count = 1
        if isFull:
            while success:
                dirr = dest + x.split('.')[0] + '/'
                new_path = dirr +x.split('.')[0] +'_'+"%03d" % int(count) + "_scene.jpg"
                if not os.path.isdir(dirr):
                    os.mkdir(dirr)

                cv2.imwrite(new_path, image)  # save frame as JPEG file
                success, image = vidcap.read()
                count += 1
        else:
            while count < 6:
                dirr = dest + x.split('.')[0] + '/'
                new_path = dirr + x.split('.')[0] + '_' + "%03d" % int(count) + "_scene.jpg"
                if not os.path.isdir(dirr):
                    os.mkdir(dirr)

                cv2.imwrite(new_path, image)  # save frame as JPEG file
                success, image = vidcap.read()
                count += 1
