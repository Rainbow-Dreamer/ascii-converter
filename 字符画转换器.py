with open('config.py', encoding='utf-8-sig') as f:
    exec(f.read(), globals())


def change(var, new, is_str=True):
    text = open('config.py', encoding='utf-8').read()
    text_ls = list(text)
    var_len = len(var) + 1
    var_ind = text.index('\n' + var) + var_len
    next_line = text[var_ind:].index('\n')
    if is_str:
        text_ls[var_ind:var_ind + next_line] = f' = {repr(new)}'
    else:
        text_ls[var_ind:var_ind + next_line] = f" = {new}"
    with open('config.py', 'w', encoding='utf-8') as f:
        f.write(''.join(text_ls))


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("视频和图片转字符画")
        self.minsize(900, 700)
        self.value_dict = {}
        self.set_value('字符集', '字符集', True, 600, 60, 0, 0)
        self.set_value('背景图片', '背景图片', True, 600, 40, 0, 80, True)
        self.set_value('缩放倍数', '缩放倍数', False, 80, 40, 0, 140)
        self.set_value('比特数', '比特数', False, 80, 40, 0, 240)
        self.set_value('演示模式', '演示模式', False, 80, 40, 0, 290)
        self.set_value('图片路径', '图片路径', True, 600, 40, 0, 390, True)
        self.set_value('视频路径', '视频路径', True, 500, 50, 100, 140, True)
        self.set_value('视频帧图路径', '视频帧图路径', True, 500, 50, 150, 210, True)
        self.set_value('视频帧图片保存路径', '视频帧图片保存路径', True, 500, 50, 150, 270, True)
        self.set_value('视频导出帧图片到文件夹', '视频导出帧图片到文件夹', False, 150, 40, 150, 330)
        self.set_value('颜色', '颜色', False, 150, 40, 0, 450)
        self.set_value('帧数', '帧数', False, 150, 40, 0, 500)
        self.set_value('视频转换帧数区间', '视频转换帧数区间', False, 150, 40, 200, 450)
        self.set_value('字符画保存为图片', '字符画保存为图片', False, 150, 40, 200, 500)
        self.set_value('屏幕宽度', '屏幕宽度', False, 70, 40, 320, 330)
        self.set_value('屏幕高度', '屏幕高度', False, 70, 40, 410, 330)
        self.set_value('字符画保存为文本文件', '字符画保存为文本文件', False, 150, 40, 500, 330)
        self.set_value('图片转换显示进度', '图片转换显示进度', False, 150, 40, 730, 410)
        self.set_value('导出视频', '导出视频', False, 150, 40, 730, 520)
        self.set_value('导出视频帧数', 'fps', False, 100, 40, 350, 580)
        self.set_value('导出视频字体', 'font_path', True, 100, 40, 500, 580)
        self.set_value('导出视频字体大小', 'font_size', False, 120, 40, 650, 580)
        self.set_value('图片宽度比例', 'width_resize', False, 100, 40, 300, 630)
        self.set_value('图片高度比例', 'height_resize', False, 100, 40, 450, 630)
        self.save = ttk.Button(self, text="save", command=self.save_current)
        self.save.place(x=500, y=490)
        self.saved_text = ttk.Label(self, text='saved')
        self.playing = ttk.Button(self, text='运行', command=self.play)
        self.playing.place(x=600, y=490)
        self.frame_info = StringVar()
        self.frame_info.set('暂无读取帧')
        self.frame_show = ttk.Label(self, textvariable=self.frame_info)
        self.frame_show.place(x=500, y=530)
        self.msg_label = ttk.Label(
            self,
            text=
            '每次运行之前要记得先\n点击save按钮保存配置哦~\n演示模式为0：转换图片为ascii字符画\n演示模式为1：转换视频为ascii字符画视频'
        )
        self.msg_label.place(x=620, y=10)
        self.set_true_button = ttk.Button(self,
                                          text='True',
                                          command=lambda: self.insert_value(1),
                                          takefocus=False)
        self.set_false_button = ttk.Button(
            self,
            text='False',
            command=lambda: self.insert_value(0),
            takefocus=False)
        self.set_true_button.place(x=0, y=600)
        self.set_false_button.place(x=100, y=600)
        self.picture_color = IntVar()
        self.output_picture_color = Checkbutton(self,
                                                text='输出图片为彩色',
                                                variable=self.picture_color,
                                                onvalue=1,
                                                offvalue=0)
        self.output_picture_color.place(x=200, y=560)

    def insert_value(self, value):
        if value == 1:
            value = 'True'
        elif value == 0:
            value = 'False'
        current_focus = self.focus_get()
        if 'text' in str(current_focus):
            current_focus.delete('1.0', END)
            current_focus.insert(END, value)

    def play(self):
        global is_color
        is_color = self.picture_color.get()
        plays()

    def set_value(self,
                  value_name,
                  real_value,
                  is_str,
                  width,
                  height,
                  x1,
                  y1,
                  path_enable=False):
        value_label = ttk.LabelFrame(self,
                                     text=value_name,
                                     width=width,
                                     height=height)
        value_label.place(x=x1, y=y1)
        value_entry = Text(value_label,
                           undo=True,
                           autoseparators=True,
                           maxundo=-1)
        before_value = str(eval(real_value))
        if before_value == 'None':
            before_value = ''
        elif before_value == '':
            before_value = "''"
        value_entry.insert(END, before_value)
        value_entry.place(x=0, y=0, width=width)
        self.value_dict[real_value] = [value_entry, before_value, is_str]
        if path_enable:
            path_button = ttk.Button(
                self, text='更改', command=lambda: self.search_path(value_entry))
            path_button.place(x=x1 + width + 10, y=y1 + 20)

    def search_path(self, obj):
        filename = filedialog.askopenfilename(initialdir='.',
                                              title="选择文件",
                                              filetype=(("所有文件", "*.*"), ))
        if filename:
            obj.delete('1.0', END)
            obj.insert(END, filename)

    def show_saved(self):
        self.saved_text.place(x=445, y=495)
        self.after(1000, self.saved_text.place_forget)

    def save_current(self):
        changed = False
        for each in self.value_dict:
            current_value = self.value_dict[each]
            current = current_value[0].get('1.0', END).replace('\n', '')
            str_msg = current_value[2]
            if current != current_value[1]:
                if current in ['', 'None']:
                    current = None
                    str_msg = False
                change(each, current, str_msg)
                self.value_dict[each][1] = current
                changed = True
        if changed:
            self.show_saved()


def plays():
    with open('config.py', encoding='utf-8') as f:
        exec(f.read(), globals())
    length = len(字符集)
    K = 2**比特数
    unit = (K + 1) / length

    def get_char(r, g, b, alpha=K):
        if alpha == 0:
            return " "
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        return 字符集[int(gray / unit)]

    def img_to_ascii(im, show_percentage=False):
        WIDTH = int((im.width * width_resize // 6) / 缩放倍数)
        HEIGHT = int((im.height * height_resize // 15) / 缩放倍数)
        if show_percentage:
            whole_count = WIDTH * HEIGHT
            count = 0
        im_resize = im.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        txt = ""
        if is_color and (字符画保存为图片 or 导出视频):
            im_txt = Image.new("RGB",
                               (int(im.width / 缩放倍数), int(im.height / 缩放倍数)),
                               (2**比特数 - 1, 2**比特数 - 1, 2**比特数 - 1))
            colors = []
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    pixel = im_resize.getpixel((j, i))
                    colors.append(pixel)
                    txt += get_char(*pixel)
                if show_percentage:
                    count += WIDTH
                    root.frame_info.set(
                        f'转换进度:  {round((count/whole_count)*100, 3)}%')
                    root.update()
                txt += '\n'
                colors.append((255, 255, 255))
            return txt, colors, im_txt
        else:
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    pixel = im_resize.getpixel((j, i))
                    txt += get_char(*pixel)
                if show_percentage:
                    count += WIDTH
                    root.frame_info.set(
                        f'转换进度:  {round((count/whole_count)*100, 3)}%')
                    root.update()
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
                root.frame_info.set(f'正在读取视频帧{count}')
                root.update()
        else:
            vidcap = cv2.VideoCapture(视频路径)
            is_read, img = vidcap.read()
            if not is_read:
                root.frame_info.set('视频路径不存在或者为空')
                root.update()
                return
            frames = []
            count = 0
            if 视频导出帧图片到文件夹:
                os.mkdir(视频帧图片保存路径)
                os.chdir(视频帧图片保存路径)
                start_frame = 0
                if not 视频转换帧数区间:
                    while is_read:
                        cv2.imwrite(f"{count}.jpg", img)
                        frames.append(
                            Image.fromarray(
                                cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
                        is_read, img = vidcap.read()
                        count += 1
                        root.frame_info.set(f'正在读取视频帧{count}')
                        root.update()
                else:
                    start_frame, to_frame = 视频转换帧数区间
                    no_of_frames = to_frame - start_frame
                    vidcap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
                    is_read, img = vidcap.read()
                    for k in range(no_of_frames):
                        if is_read:
                            cv2.imwrite(f"{count}.jpg", img)
                            frames.append(
                                Image.fromarray(
                                    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
                            is_read, img = vidcap.read()
                            count += 1
                            root.frame_info.set(
                                f'正在读取视频帧{start_frame + count}')
                            root.update()
                        else:
                            break
            else:
                start_frame = 0
                if not 视频转换帧数区间:
                    while is_read:
                        frames.append(
                            Image.fromarray(
                                cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
                        is_read, img = vidcap.read()
                        count += 1
                        root.frame_info.set(f'正在读取视频帧{count}')
                        root.update()
                else:
                    start_frame, to_frame = 视频转换帧数区间
                    no_of_frames = to_frame - start_frame
                    vidcap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
                    is_read, img = vidcap.read()
                    for k in range(no_of_frames):
                        if is_read:
                            frames.append(
                                Image.fromarray(
                                    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
                            is_read, img = vidcap.read()
                            count += 1
                            root.frame_info.set(
                                f'正在读取视频帧{start_frame + count}')
                            root.update()
                        else:
                            break
        root.frame_info.set('视频帧读取完成，开始转换')
        root.update()
        counter = 0
        if 导出视频:
            try:
                os.mkdir('temp_video_images')
            except:
                pass
            os.chdir('temp_video_images')
            num_frames = len(frames)
            n = len(str(num_frames))
            try:
                font = ImageFont.truetype(font_path, size=font_size)
            except:
                font = ImageFont.load_default()
            font_x_len, font_y_len = font.getsize(字符集[1])
            font_y_len = int(font_y_len * 1.37)
            if is_color == 0:
                for i in range(num_frames):
                    root.frame_info.set(f'正在转换第{start_frame + i + 1}帧')
                    root.update()
                    im = frames[i]
                    text_str = img_to_ascii(im)
                    im_txt = Image.new(
                        "L", (int(im.width / 缩放倍数), int(im.height / 缩放倍数)),
                        'white')
                    dr = ImageDraw.Draw(im_txt)
                    x = y = 0
                    for j in range(len(text_str)):
                        if text_str[j] == "\n":
                            x = 0
                            y += font_y_len
                        dr.text((x, y), text_str[j], fill='black', font=font)
                        x += font_x_len
                    im_txt.save(f'{i:0{n}d}.png')
            else:
                for i in range(num_frames):
                    root.frame_info.set(f'正在转换第{start_frame + i + 1}帧')
                    root.update()
                    text_str_output = img_to_ascii(frames[i])
                    txt, colors, im_txt = text_str_output
                    dr = ImageDraw.Draw(im_txt)
                    x = y = 0
                    for j in range(len(txt)):
                        if txt[j] == "\n":
                            x = 0
                            y += font_y_len
                        dr.text((x, y), txt[j], fill=colors[j], font=font)
                        x += font_x_len
                    im_txt.save(f'{i:0{n}d}.png')

            root.frame_info.set(f'转换完成，开始输出为视频..')
            root.update()
            os.chdir('..')
            file_name = os.path.splitext(os.path.basename(视频路径))[0]
            output_filename = f'ascii_{file_name}.mp4'
            if output_filename in os.listdir():
                os.remove(output_filename)
            ffmpeg.input(f'temp_video_images/%{n}d.png',
                         framerate=fps).output(output_filename).run()
            root.frame_info.set(f'已成功输出为视频')
            root.update()

        text_str_output = img_to_ascii(frames[0])
        if type(text_str_output) != str:
            text_str = text_str_output[0]
        else:
            text_str = text_str_output
    else:
        root.frame_info.set('图片转换中')
        root.update()
        try:
            im = Image.open(图片路径)
            text_str_output = img_to_ascii(im, 图片转换显示进度)
            if type(text_str_output) != str:
                text_str = text_str_output[0]
            else:
                text_str = text_str_output
        except:
            root.frame_info.set('图片路径不存在或者为空')
            root.update()
            return
        root.frame_info.set('图片转换完成')
        root.update()
        file_name = os.path.splitext(os.path.basename(图片路径))[0]
        if 字符画保存为文本文件:
            root.frame_info.set('图片转换完成，正在写入字符画为\n文本文件...')
            root.update()
            with open(f'ascii_{file_name}.txt', 'w') as f:
                f.write(text_str)
            root.frame_info.set('已成功写入文本文件')
            root.update()
        if 字符画保存为图片:
            root.frame_info.set('图片转换完成，正在输出字符画为图片...')
            root.update()
            try:
                font = ImageFont.truetype(font_path, size=font_size)
            except:
                font = ImageFont.load_default()
            font_x_len, font_y_len = font.getsize(字符集[1])
            font_y_len = int(font_y_len * 1.37)
            if is_color == 0:
                im_txt = Image.new(
                    "L", (int(im.width / 缩放倍数), int(im.height / 缩放倍数)),
                    'white')
                dr = ImageDraw.Draw(im_txt)
                x = y = 0
                for i in range(len(text_str)):
                    if text_str[i] == "\n":
                        x = 0
                        y += font_y_len
                    dr.text((x, y), text_str[i], fill='black', font=font)
                    x += font_x_len
                im_txt.save(f'ascii_{file_name}.png')

            else:
                txt, colors, im_txt = text_str_output
                dr = ImageDraw.Draw(im_txt)
                x = y = 0
                for i in range(len(txt)):
                    if txt[i] == "\n":
                        x = 0
                        y += font_y_len
                    dr.text((x, y), txt[i], fill=colors[i], font=font)
                    x += font_x_len
                im_txt.save(f'ascii_{file_name}.png')

            root.frame_info.set('已成功输出为图片')
            root.update()


root = Root()
root.mainloop()