with open('config.py', encoding='utf-8') as f:
    exec(f.read(), globals())
txt_to_image.update(font_path, font_size)


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
        self.set_value('字体', '字体', True, 140, 40, 0, 190)
        self.set_value('字体大小', '字体大小', False, 140, 40, 0, 240)
        self.set_value('比特数', '比特数', False, 80, 40, 0, 290)
        self.set_value('演示模式', '演示模式', False, 80, 40, 0, 340)
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
        self.set_value('显示图片或者视频', '显示图片或者视频', False, 150, 40, 680, 330)
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
        self.color_scale = 6
        self.color_scale_entry = ttk.Entry(self)
        self.color_scale_entry.place(x=600, y=650)
        self.color_scale_entry.insert(END, self.color_scale)
        self.color_scale_label = ttk.Label(self, text='彩色字符画字体缩放倍数')
        self.color_scale_label.place(x=600, y=625)

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
        global color_scale
        is_color = self.picture_color.get()
        self.color_scale = int(self.color_scale_entry.get())
        color_scale = self.color_scale
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
        if is_color and (字符画保存为图片 or 导出视频):
            WIDTH = int(im.width / 缩放倍数)
            HEIGHT = int(im.height / 缩放倍数)
        else:
            WIDTH = int(im.width * width_resize / 缩放倍数)
            HEIGHT = int(im.height * height_resize / 缩放倍数)
        if show_percentage:
            whole_count = WIDTH * HEIGHT
            count = 0
        im = im.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        txt = ""
        if is_color and (字符画保存为图片 or 导出视频):
            im_txt = Image.new("RGB", (im.width, im.height),
                               (2**比特数 - 1, 2**比特数 - 1, 2**比特数 - 1))
            colors = []
            txt = []
            for i in range(HEIGHT):
                current_color = []
                current_line = ''
                for j in range(WIDTH):
                    pixel = im.getpixel((j, i))
                    current_color.append((pixel[0], pixel[1], pixel[2]))
                    current_line += get_char(*pixel)
                if show_percentage:
                    count += WIDTH
                    root.frame_info.set(
                        f'转换进度:  {round((count/whole_count)*100, 3)}%')
                    root.update()
                txt.append(current_line)
                colors.append(current_color)
            return txt, colors, im_txt
        else:
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    pixel = im.getpixel((j, i))
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
                    for k in range(*视频转换帧数区间):
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
            if is_color == 0:
                for i in range(num_frames):
                    root.frame_info.set(f'正在转换第{start_frame + i + 1}帧')
                    root.update()
                    convert(img_to_ascii(frames[i]),
                            f'{i:0{n}d}.png',
                            font_size=font_size)
            else:
                try:
                    font = ImageFont.truetype(font_path, size=font_size)
                except IOError:
                    font = ImageFont.load_default()
                font_x_len, font_y_len = font.getsize(' ')
                font_x_len = int(font_x_len / color_scale)
                font_y_len = int(font_y_len / color_scale)
                for i in range(num_frames):
                    root.frame_info.set(f'正在转换第{start_frame + i + 1}帧')
                    root.update()
                    text_str_output = img_to_ascii(frames[i])
                    txt, colors, im_txt = text_str_output
                    dr = ImageDraw.Draw(im_txt)
                    for j in range(len(txt)):
                        for k in range(len(txt[0])):
                            dr.text((k * font_x_len, j * font_y_len),
                                    txt[j][k], colors[j][k])
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
            text_str = '\n'.join(text_str_output[0])
        else:
            text_str = text_str_output
        if 显示图片或者视频:
            window = pyglet.window.Window(width=屏幕宽度, height=屏幕高度)
            pyglet.resource.path = [abs_path]
            pyglet.resource.reindex()
            image = pyglet.resource.image(背景图片)
            image.width, image.height = 屏幕宽度, 屏幕高度
            label = pyglet.text.Label(text_str,
                                      font_size=字体大小,
                                      font_name=字体,
                                      x=0,
                                      y=屏幕高度 // 2,
                                      anchor_x='left',
                                      anchor_y='center',
                                      color=颜色,
                                      width=屏幕宽度,
                                      multiline=True)

            @window.event
            def on_draw():
                nonlocal counter
                window.clear()
                image.blit(0, 0)
                label.draw()
                counter += 1
                try:
                    text_str_output = img_to_ascii(frames[counter])
                    if type(text_str_output) != str:
                        text_str = '\n'.join(text_str_output[0])
                    else:
                        text_str = text_str_output
                    label.text = text_str
                except:
                    frames.clear()

            def update(dt):
                pass

            pyglet.clock.schedule_interval(update, 1 / 帧数)
            pyglet.app.run()
    else:
        root.frame_info.set('图片转换中')
        root.update()
        try:
            text_str_output = img_to_ascii(Image.open(图片路径), 图片转换显示进度)
            if type(text_str_output) != str:
                text_str = '\n'.join(text_str_output[0])
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
            if is_color == 0:
                convert(text_str,
                        f'ascii_{file_name}.png',
                        font_size=font_size)
            else:
                txt, colors, im_txt = text_str_output
                dr = ImageDraw.Draw(im_txt)
                try:
                    font = ImageFont.truetype(font_path, size=字体大小)
                except IOError:
                    font = ImageFont.load_default()
                font_x_len, font_y_len = font.getsize(' ')
                for j in range(len(txt)):
                    for i in range(len(txt[0])):
                        dr.text((i * font_x_len, j * font_y_len), txt[j][i],
                                colors[j][i])
                im_txt.save(f'ascii_{file_name}.png')

            root.frame_info.set('已成功输出为图片')
            root.update()
        if 显示图片或者视频:
            window = pyglet.window.Window(width=屏幕宽度, height=屏幕高度)
            pyglet.resource.path = [abs_path]
            pyglet.resource.reindex()
            image = pyglet.image.load(背景图片)
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
                nonlocal counter
                window.clear()
                image.blit(0, 0)
                label.draw()

            pyglet.app.run()


root = Root()
root.mainloop()