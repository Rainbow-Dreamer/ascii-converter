#-*- coding:utf-8 -*-
with open('config.py', encoding='utf-8') as f:
    exec(f.read())
import cv2
import pyglet
import os
from PIL import Image, ImageFont, ImageDraw



length = len(字符集)
K = 2**比特数+1
unit = K/length
def get_char(r,g,b,alpha=None):
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return 字符集[int(gray/unit)]

def img_to_ascii(im):
    WIDTH = int(im.width*1.1/缩放倍数)
    HEIGHT = int(im.height*0.6/缩放倍数)
    im = im.resize((WIDTH,HEIGHT),Image.ANTIALIAS)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            pixel = im.getpixel((j,i))
            txt += get_char(*pixel)       
        txt += '\n' 
    return txt

if 演示模式 == 1:
    if 视频帧图路径:
    
        os.chdir(视频帧图路径)
        frames = []
        count = 0
        file_ls = os.listdir()
        for i in file_ls:
            frames.append(Image.open(i))
            count += 1
            print(f'loading frame {count}')
    else:
        vidcap = cv2.VideoCapture(视频路径)
        is_read, img = vidcap.read()
        frames = []
        count = 0
        if 视频导出帧图片到文件夹:
            os.mkdir(视频帧图片保存路径)
            os.chdir(视频帧图片保存路径)
            if not 视频转换帧数区间:
                while is_read:
                    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    cv2.imwrite(f"{count}.jpg", img)
                    frames.append(Image.fromarray(img))
                    is_read, img = vidcap.read()
                    count += 1
                    print(f'loading frame {count}')
            else:
                for k in range(*视频转换帧数区间):
                    if is_read:
                        cv2.imwrite(f"{count}.jpg", img)
                        frames.append(Image.fromarray(img))
                        is_read, img = vidcap.read()
                        count += 1
                        print(f'loading frame {count}')
                    else:
                        break
        else:
            if not 视频转换帧数区间:
                while is_read:
                    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    frames.append(Image.fromarray(img))
                    is_read, img = vidcap.read()
                    count += 1
                    print(f'loading frame {count}')  
            else:
                for k in range(*视频转换帧数区间):
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
    window = pyglet.window.Window(width=屏幕宽度, height=屏幕高度)
    pyglet.resource.path = ['']
    pyglet.resource.reindex()
    image = pyglet.resource.image(背景图片)
    image.width, image.height = 屏幕宽度, 屏幕高度
    label = pyglet.text.Label(text_str,
                              font_size=字体大小,
                              font_name=字体,
                              x=0,
                              y=屏幕高度//2,
                              anchor_x='left',
                              anchor_y='center',
                              color=颜色,
                              width=屏幕宽度,
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
    
    
    pyglet.clock.schedule_interval(update, 1/帧数)    
else:
    text_str = img_to_ascii(Image.open(图片路径))
    if 字符画保存为图片:
        from txt_to_image import convert
        convert(text_str, 'result.png')
    window = pyglet.window.Window(width=屏幕宽度, height=屏幕高度)
    pyglet.resource.path = ['']
    pyglet.resource.reindex()
    image = pyglet.resource.image(背景图片)
    image.width, image.height = 屏幕宽度, 屏幕高度
    label = pyglet.text.Label(text_str,
                              font_size=字体大小,
                              font_name=字体,
                              x=0,
                              y=屏幕高度,
                              anchor_x='left',
                              anchor_y='top',
                              color=颜色,
                              width=屏幕宽度,
                              multiline=True)
        
    @window.event
    def on_draw():
        global counter
        window.clear()
        image.blit(0, 0)
        label.draw()      



pyglet.app.run()