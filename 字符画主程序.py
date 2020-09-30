with open('config.py', encoding='utf-8') as f:
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
        self.minsize(900, 600)

        self.value_dict = {}
        self.set_value('字符集', '字符集', True, 600, 100, 0, 0)
        self.set_value('背景图片', '背景图片', True, 600, 40, 0, 120, True)
        self.set_value('缩放倍数', '缩放倍数', False, 80, 40, 0, 180)
        self.set_value('字体', '字体', True, 140, 40, 0, 230)
        self.set_value('字体大小', '字体大小', False, 140, 40, 0, 280)
        self.set_value('比特数', '比特数', False, 80, 40, 0, 330)
        self.set_value('演示模式', '演示模式', False, 80, 40, 0, 380)
        self.set_value('图片路径', '图片路径', True, 600, 40, 0, 430, True)
        self.set_value('视频路径', '视频路径', True, 500, 50, 100, 180, True)
        self.set_value('视频帧图路径', '视频帧图路径', True, 500, 50, 150, 250, True)
        self.set_value('视频帧图片保存路径', '视频帧图片保存路径', True, 500, 50, 150, 310, True)
        self.set_value('视频导出帧图片到文件夹', '视频导出帧图片到文件夹', False, 150, 40, 150, 370)
        self.set_value('颜色', '颜色', False, 150, 40, 0, 490)
        self.set_value('帧数', '帧数', False, 150, 40, 0, 540)
        self.set_value('视频转换帧数区间', '视频转换帧数区间', False, 150, 40, 200, 490)
        self.set_value('字符画保存为图片', '字符画保存为图片', False, 150, 40, 200, 540)
        self.set_value('屏幕宽度', '屏幕宽度', False, 70, 40, 320, 370)
        self.set_value('屏幕高度', '屏幕高度', False, 70, 40, 410, 370)
        self.set_value('字符画保存为文本文件', '字符画保存为文本文件', False, 150, 40, 500, 370)
        self.set_value('显示图片或者视频', '显示图片或者视频', False, 150, 40, 680, 370)
        self.set_value('图片转换显示进度', '图片转换显示进度', False, 150, 40, 730, 450)
        self.set_value('导出视频', '导出视频', False, 150, 40, 730, 510)
        self.save = ttk.Button(self, text="save", command=self.save_current)
        self.save.place(x=500, y=500)
        self.saved_text = ttk.Label(self, text='saved')
        self.playing = ttk.Button(self, text='运行', command=self.play)
        self.playing.place(x=600, y=500)
        self.frame_info = StringVar()
        self.frame_info.set('暂无读取帧')
        self.frame_show = ttk.Label(self, textvariable=self.frame_info)
        self.frame_show.place(x=500, y=550)
        self.msg_label = ttk.Label(
            self,
            text=
            '每次运行之前要记得先\n点击save按钮保存配置哦~\n演示模式为0：转换图片为ascii字符画\n演示模式为1：转换视频为ascii字符画视频'
        )
        self.msg_label.place(x=620, y=50)

    def play(self):
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
        value_entry = Text(value_label, height=10)
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
        self.saved_text.place(x=620, y=530)
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
        WIDTH = int(im.width * 1.1 / 缩放倍数)
        HEIGHT = int(im.height * 0.6 / 缩放倍数)
        if show_percentage:
            whole_count = WIDTH * HEIGHT
            count = 0
        im = im.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        txt = ""
        for i in range(HEIGHT):
            for j in range(WIDTH):
                pixel = im.getpixel((j, i))
                txt += get_char(*pixel)
                if show_percentage:
                    count += 1
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
                        root.frame_info.set(f'正在读取视频帧{count}')
                        root.update()
                else:
                    for k in range(*视频转换帧数区间):
                        if is_read:
                            cv2.imwrite(f"{count}.jpg", img)
                            frames.append(Image.fromarray(img))
                            is_read, img = vidcap.read()
                            count += 1
                            root.frame_info.set(f'正在读取视频帧{count}')
                            root.update()
                        else:
                            break
            else:
                if not 视频转换帧数区间:
                    while is_read:
                        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        frames.append(Image.fromarray(img))
                        is_read, img = vidcap.read()
                        count += 1
                        root.frame_info.set(f'正在读取视频帧{count}')
                        root.update()
                else:
                    for k in range(视频转换帧数区间[1]):
                        if is_read:
                            frames.append(Image.fromarray(img))
                            is_read, img = vidcap.read()
                            count += 1
                            root.frame_info.set(f'正在读取视频帧{count}')
                            root.update()
                        else:
                            break
                    frames = frames[视频转换帧数区间[0]:]
        root.frame_info.set('视频帧读取完成，开始转换')
        root.update()
        counter = 0
        if 导出视频:
            img_ls = []
            for i in range(len(frames)):
                root.frame_info.set(f'正在转换第{i+1}帧')
                root.update()
                current_img = convert(img_to_ascii(frames[i]),
                                      'current.png',
                                      not_save=True)
                if i == 0:
                    size = (int(current_img.width), int(current_img.height))
                img_ls.append(
                    np.array(current_img.convert('RGB'))[:, :, ::-1].copy())
            file_name = os.path.splitext(os.path.basename(视频路径))[0]
            out = cv2.VideoWriter('output.avi',
                                  cv2.VideoWriter_fourcc(*'XVID'), fps, size)
            for j in range(len(img_ls)):
                root.frame_info.set(f'正在写入视频第{j+1}帧')
                root.update()
                out.write(img_ls[j])
            out.release()
            root.frame_info.set(f'已成功输出为视频')
            root.update()

        text_str = img_to_ascii(frames[0])
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
                    label.text = img_to_ascii(frames[counter])
                except:
                    frames.clear()

            def update(dt):
                pass

            pyglet.clock.schedule_interval(update, 1 / 帧数)
            pyglet.app.run()
    else:
        root.frame_info.set('图片转换中')
        root.update()
        text_str = img_to_ascii(Image.open(图片路径), 图片转换显示进度)
        root.frame_info.set('图片转换完成')
        root.update()
        file_name = os.path.splitext(os.path.basename(图片路径))[0]
        if 字符画保存为文本文件:
            root.frame_info.set('图片转换完成，正在写入字符画为文本文件...')
            root.update()
            with open(f'ascii_{file_name}.txt', 'w') as f:
                f.write(text_str)
            root.frame_info.set('已成功写入文本文件')
            root.update()
        if 字符画保存为图片:
            root.frame_info.set('图片转换完成，正在输出字符画为图片...')
            root.update()
            convert(text_str, f'ascii_{file_name}.png')
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