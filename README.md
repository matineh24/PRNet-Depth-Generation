# PRNet-Depth-Generation 

---

## Introduction

A implementaion of depth generation based on [PRNet](https://github.com/YadiraF/PRNet), which was used in the paper [Exploiting Temporal and Depth Information for Multi-frame Face Anti-spoofing](https://arxiv.org/abs/1811.05118)

## Prerequisite

* Python 3.6 (numpy, skimage, scipy)

* TensorFlow >= 1.4

  Optional:

* dlib (for detecting face.  You do not have to install if you can provide bounding box information. Other face detectors are ok if you want.)

* opencv2 (for showing results)

* Download the PRN trained model at [BaiduDrive](https://pan.baidu.com/s/10vuV7m00OHLcsihaC-Adsw) or [GoogleDrive](https://drive.google.com/file/d/1UoE-XuW1SDLUjZmJPkIZ1MLxvQFgmTFH/view?usp=sharing), and put it into `Data/net-data`

## Test

> python Generate_Depth_Image.py

## Generate data for Major project:

If you are working with new data (not OULU-NPU protocol 1), then first you need to divide your data into three different folders for photo attacks, video attacks and real samples. Then first run the following script. The details of the arguments are given in the script itself.

> python adjust_new_data_names.py rename_file photo_attack_folder video_attack_folder real_folder

Then to convert the videos into frames run the following script (The details of the arguments are given in the script itself): 

> run python make_frames_from_videos.py originpath destpath isFull

Then you can run create_depth.py but is is very time consuming. So a rescale is needed. There are two ways of rescaling. 

The fist one is running the following script. The value of rescale_size is the new height of the images and the width will be rescaled with the same ratio to height changes.
The folderpath here is the destpath of the previous step

> rescale.py folderpath rescale_size 

The second way is to use [this file](https://github.com/matineh24/PRNet-Depth-Generation/blob/master/extract_faces.ipynb) to extract faces out of the images and save them with the dimention of 300\*300\*3. To make it work, simply change the path of the folder given in the notebook with the destpath from previous step.

Finally create a folder to keep depth maps. change [these two lines](https://github.com/matineh24/PRNet-Depth-Generation/blob/48a94e498ab8385006565c649beb8737372ba4b3/create_depth.py#L17) with destpath and new created folder and run the python file to get the depth maps.





## License

Code: under MIT license.

## Citation

If you use this code, please consider citing:

```
@inProceedings{wang2018fastd,
  title     = {Exploiting Temporal and Depth Information for Multi-frame Face Anti-spoofing},
  author    = {Zezheng Wang, Chenxu Zhao, Yunxiao Qin, Qiusheng Zhou, Guojun Qi, Jun Wan, Zhen Lei},
  booktitle = {arXiv:1811.05118},
  year      = {2018}
}
@inProceedings{feng2018prn,
  title     = {Joint 3D Face Reconstruction and Dense Alignment with Position Map Regression Network},
  author    = {Yao Feng, Fan Wu, Xiaohu Shao, Yanfeng Wang, Xi Zhou},
  booktitle = {ECCV},
  year      = {2018}
}
```

## Acknowledgements
Thanks *Yao Feng etc.* for their [PRNet](https://github.com/YadiraF/PRNet).
