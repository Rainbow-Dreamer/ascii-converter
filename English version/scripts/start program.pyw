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
current_path = os.getcwd()
os.chdir(current_path)
sys.path.append(abs_path)
sys.path.append(current_path)
with open('scripts/Ascii Converter.py', encoding='utf-8-sig') as f:
    exec(f.read(), globals())
