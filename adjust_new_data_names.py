import os
from os import walk
import sys

try:
    rename_file = sys.argv[1]
    photo_attack_folder = sys.argv[2]
    video_attack_folder = sys.argv[3]
    real_folder = sys.argv[4]
except:
    rename_file = 'Test.txt'
    photo_attack_folder = 'self_created/photo_attack'
    video_attack_folder = 'self_created/video_attack'
    real_folder = 'self_created/real'


'''
Rename files based on Dev.txt and Test.txt. These two text files contain OULU-NPU protocol 1
file names. If the file name ends with 4, and 5 it is a video attack and if it ends with 2 
and 3 it is a photo attack. If it ends with 1 it is a real sample. 

To use this file, run python adjust_new_data_names.py A B C D 
A: 
    Test.txt if you want to rename files based on test protocol of OULU NPU
    Dev.txt if you want to rename files based on dev protocol of OULU NPU
B: 
    The address of the folder containing photo attack videos
C:
    The address of the folder containing video attack videos
D: 
    The address of the folder containing real sample videos
    
'''
def rename_files(path, file_names):
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)

    for i in range(len(f)):
        if f[i].split('.')[-1] == 'mp4':
            os.rename(os.path.join(path, f[i]), os.path.join(path, file_names[i] +'.'+ f[i].split('.')[-1]))


def get_file_names(path):
    lines = []
    with open(path) as f:
        lines = f.readlines()
    live_file_names = []
    fake_photo_file_names = []
    fake_video_file_names = []
    for line in lines:
        x = line.split(',')
        if x[0] == '+1':
            live_file_names.append(str(x[1][:8]))
        else:
            if x[1].split('_')[-1] == '5\n' or x[1].split('_')[-1] == '4\n':
                fake_video_file_names.append(str(x[1][:8]))
            else:
                fake_photo_file_names.append(str(x[1][:8]))
    return live_file_names, fake_video_file_names,fake_photo_file_names



live_file_names, fake_video_file_names,fake_photo_file_names = get_file_names(rename_file)
rename_files(photo_attack_folder, fake_photo_file_names)
rename_files(video_attack_folder, fake_video_file_names)
rename_files(real_folder, live_file_names)