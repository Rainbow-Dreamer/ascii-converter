from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2
import os
import sys
from PIL import Image, ImageFont, ImageDraw, ImageTk
import numpy as np
import ffmpeg
from ast import literal_eval
from copy import deepcopy

abs_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(abs_path)
sys.path.append(abs_path)
with open('字符画转换器.py', encoding='utf-8-sig') as f:
    exec(f.read(), globals())
