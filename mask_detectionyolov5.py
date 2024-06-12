# -*- coding: utf-8 -*-
"""Mask DetectionYolov5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wspm0WsGbJFKApnfvWuSj2xNwgXaj0bw
"""

# Commented out IPython magic to ensure Python compatibility.
# clone YOLOv5 repository
!git clone https://github.com/ultralytics/yolov5  # clone repo
# %cd yolov5
!git reset --hard 064365d8683fd002e9ad789c1e91fa3d021b44f0

#importing libraries
import os
import shutil
import random

!unzip /content/mask_dataset.zip

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolov5
# !pip install roboflow

# from roboflow import Roboflow
# rf = Roboflow(api_key="d0yjGOmmkoSCrV8DXWCh")
# project = rf.workspace("fast-mtgvi").project("mask-detection-7smsk")
# dataset = project.version(1).download("yolov5")
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="d0yjGOmmkoSCrV8DXWCh")
project = rf.workspace("fast-mtgvi").project("mask1-umvll")
dataset = project.version(1).download("yolov5")

#cloning github repo

!git clone https://github.com/ultralytics/yolov5.git

#installing all requirements

!pip install -r requirements.txt

# Commented out IPython magic to ensure Python compatibility.
# this is the YAML file Roboflow wrote for us that we're loading into this notebook with our data
# %cat {dataset.location}/data.yaml

#download weights

!wget https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5s.pt

!python train.py --img 416 --batch 8 --epochs 200 --data /content/yolov5/Mask1-1/data.yaml --weights /content/yolov5/yolov5s.pt --nosave --cache

# detection on new images
!python detect.py --source /content/yolov5/Mask1-1/valid/images --weights /content/yolov5/runs/train/exp6/weights/last.pt --img 416 --save-txt --save-conf

#display result images

import glob
from IPython.display import Image, display

for imageName in glob.glob('/content/yolov5/runs/detect/exp/*.jpg'): #assuming JPG
    display(Image(filename=imageName))
    print("\n")

# detection on a video
!python detect.py --source /content/video.mp4 --weights /content/yolov5/runs/train/exp6/weights/last.pt --img 416 --save-txt --save-conf --exist-ok

# detection on a video
!python detect.py --source /content/MaskVideo.mp4 --weights /content/yolov5/runs/train/exp6/weights/last.pt --img 416 --save-txt --save-conf --exist-ok

# detection on a video
!python detect.py --source /content/Mask2.mp4 --weights /content/yolov5/runs/train/exp6/weights/last.pt --img 416 --save-txt --save-conf --exist-ok

# detection on a video
!python detect.py --source /content/Mask3.mp4 --weights /content/yolov5/runs/train/exp6/weights/last.pt --img 416 --save-txt --save-conf --exist-ok

