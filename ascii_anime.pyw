#-*- coding:utf-8 -*-
from config import *
import cv2
import pyglet
import os
from PIL import Image, ImageFont, ImageDraw



length = len(ascii_char)
K = 2**bits+1
unit = K/length
def get_char(r,g,b,alpha=None):
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return ascii_char[int(gray/unit)]

def img_to_ascii(im):
    WIDTH = int(im.width*1.1/resize_num)
    HEIGHT = int(im.height*0.6/resize_num)
    im = im.resize((WIDTH,HEIGHT),Image.ANTIALIAS)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            pixel = im.getpixel((j,i))
            txt += get_char(*pixel)       
        txt += '\n' 
    return txt

if show_mode == 1:
    if video_path:
    
        os.chdir(video_path)
        frames = []
        count = 0
        file_ls = os.listdir()
        for i in file_ls:
            frames.append(Image.open(i))
            count += 1
            print(f'loading frame {count}')
    else:
        vidcap = cv2.VideoCapture(video_file)
        is_read, img = vidcap.read()
        frames = []
        count = 0
        if write_img_to_folder:
            os.mkdir(img_save_path)
            os.chdir(img_save_path)
            if not frames_range:
                while is_read:
                    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    cv2.imwrite(f"{count}.jpg", img)
                    frames.append(Image.fromarray(img))
                    is_read, img = vidcap.read()
                    count += 1
                    print(f'loading frame {count}')
            else:
                for k in range(*frames_range):
                    if is_read:
                        cv2.imwrite(f"{count}.jpg", img)
                        frames.append(Image.fromarray(img))
                        is_read, img = vidcap.read()
                        count += 1
                        print(f'loading frame {count}')
                    else:
                        break
        else:
            if not frames_range:
                while is_read:
                    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    frames.append(Image.fromarray(img))
                    is_read, img = vidcap.read()
                    count += 1
                    print(f'loading frame {count}')  
            else:
                for k in range(*frames_range):
                    if is_read:       
                        frames.append(Image.fromarray(img))
                        is_read, img = vidcap.read()
                        count += 1
                        print(f'loading frame {count}')  
                    else:
                        break
    print('loading frames finished', flush=True)
    counter = 0

    text_str = img_to_ascii(frames[0])
    width = text_str.index('\n')
    height = text_str.count('\n')
    test_label = pyglet.text.Label(text_str[:width],font_size=fonts_size,font_name=fonts_name)
    unit_height = test_label.content_height
    unit_width = test_label.content_width
    height *= unit_height
    width *= (fonts_size + 1)
    window = pyglet.window.Window(width=width, height=height)
    pyglet.resource.path = ['']
    pyglet.resource.reindex()
    image = pyglet.resource.image(background_img)
    image.width, image.height = width, height
    label = pyglet.text.Label(text_str,
                              font_size=fonts_size,
                              font_name=fonts_name,
                              x=0,
                              y=height//2,
                              anchor_x='left',
                              anchor_y='center',
                              color=colors,
                              width=width,
                              multiline=True)
    
    @window.event
    def on_draw():
        global counter
        window.clear()
        image.blit(0, 0)
        label.draw()
        counter += 1
        label.text = img_to_ascii(frames[counter])
    def update(dt):
        pass
    
    
    pyglet.clock.schedule_interval(update, 1/fps)    
else:
    text_str = img_to_ascii(Image.open(image_path))
    if save_as_img:
        from txt_to_image import convert
        convert(text_str, 'result.png')
    width = text_str.index('\n')
    height = text_str.count('\n')
    test_label = pyglet.text.Label(text_str[:width],font_size=fonts_size,font_name=fonts_name)
    unit_height = test_label.content_height
    unit_width = test_label.content_width
    height *= unit_height
    width = int(width * (fonts_size + 0.5))
    window = pyglet.window.Window(width=width, height=height)
    pyglet.resource.path = ['']
    pyglet.resource.reindex()
    image = pyglet.resource.image(background_img)
    image.width, image.height = width, height
    label = pyglet.text.Label(text_str,
                              font_size=fonts_size,
                              font_name=fonts_name,
                              x=0,
                              y=height,
                              anchor_x='left',
                              anchor_y='top',
                              color=colors,
                              width=width,
                              multiline=True)
        
    @window.event
    def on_draw():
        global counter
        window.clear()
        image.blit(0, 0)
        label.draw()      



pyglet.app.run()