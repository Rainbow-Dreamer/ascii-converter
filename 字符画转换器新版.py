with open('config.py', encoding='utf-8-sig') as f:
    text = f.read()
    exec(text, globals())
var_counter = 1


def get_all_config_options(text):
    result = []
    N = len(text)
    for i in range(N):
        current = text[i]
        if current == '\n':
            if i + 1 < N:
                next_character = text[i + 1]
                if next_character.isalpha():
                    inds = text[i + 1:].index('=') - 1
                    current_config_options = text[i + 1:i + 1 + inds]
                    result.append(current_config_options)
    return result


def change(var, new, is_str=True):
    text = open('config.py', encoding='utf-8-sig').read()
    text_ls = list(text)
    var_len = len(var) + 1
    var_ind = text.index('\n' + var) + var_len
    next_line = text[var_ind:].index('\n')
    if is_str:
        text_ls[var_ind:var_ind + next_line] = f' = {repr(new)}'
    else:
        text_ls[var_ind:var_ind + next_line] = f" = {new}"
    with open('config.py', 'w', encoding='utf-8-sig') as f:
        f.write(''.join(text_ls))


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Ascii Converter 字符画转换器")
        self.minsize(800, 500)
        self.resizable(0, 0)
        self.value_dict = {}
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        font=('微软雅黑', 12))
        style.map('TButton', foreground=[('active', 'white')])
        style.configure('TEntry',
                        fieldbackground='black',
                        foreground='white',
                        insertcolor='white')
        style.configure('TLabelframe',
                        background='black',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        font=('微软雅黑', 12))
        style.configure('TLabelframe.Label',
                        background='black',
                        foreground='white',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        font=('微软雅黑', 12))
        style.configure('TLabel',
                        background='black',
                        foreground='white',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        font=('微软雅黑', 12))
        style.configure('New.TLabel',
                        background='black',
                        foreground='white',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        font=('微软雅黑', 10))
        style.configure('TCheckbutton',
                        background='black',
                        foreground='white',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        inactiveselectbackground='black',
                        font=('微软雅黑', 12))
        style.configure('TScrollbar', background='white')
        self.button_img = ImageTk.PhotoImage(
            Image.open('resources/button.png').resize((200, 107)))
        self.button_img2 = ImageTk.PhotoImage(
            Image.open('resources/button.png').resize((100, 40)))
        bg_image = Image.open('resources/5072612.jpg')
        ratio = 800 / bg_image.width
        self.bg_image = ImageTk.PhotoImage(
            bg_image.resize((800, int(bg_image.height * ratio))))
        self.bg_label = ttk.Label(
            self,
            image=self.bg_image,
            text='\n' * 15 +
            'made by Rainbow Dreamer\nqq: 2180502841\nB站账号: Rainbow_Dreamer\ngithub账号: Rainbow Dreamer',
            compound=CENTER)
        self.bg_label.configure(font=('微软雅黑', 10), foreground='white')
        self.bg_label.place(x=0, y=0)
        title_image = Image.open('resources/title.png')
        self.title_image = ImageTk.PhotoImage(title_image.resize((200, 60)))
        self.title_label = ttk.Label(self,
                                     image=self.title_image,
                                     text='字符画转换器',
                                     compound=CENTER)
        self.title_label.configure(font=('微软雅黑', 15), foreground='white')
        self.title_label.place(x=280, y=10)
        self.img_to_ascii_img_button = ttk.Button(
            self,
            text='图片转字符画图片',
            image=self.button_img,
            compound=CENTER,
            command=self.img_to_ascii_img_window)
        self.img_to_ascii_img_button.place(x=140, y=100, width=200, height=107)
        self.video_to_ascii_video_button = ttk.Button(
            self,
            text='视频转字符画视频',
            image=self.button_img,
            compound=CENTER,
            command=self.video_to_ascii_video_window)
        self.video_to_ascii_video_button.place(x=440,
                                               y=100,
                                               width=200,
                                               height=107)
        self.video_to_ascii_img_button = ttk.Button(
            self,
            text='视频按帧数转换\n字符画图片',
            image=self.button_img,
            compound=CENTER,
            command=self.video_to_ascii_img_window)
        self.video_to_ascii_img_button.place(x=140,
                                             y=250,
                                             width=200,
                                             height=107)
        self.change_settings_button = ttk.Button(
            self,
            text='更改设置',
            image=self.button_img,
            compound=CENTER,
            command=self.change_settings_window)
        self.change_settings_button.place(x=440, y=250, width=200, height=107)
        self.frame_info = StringVar()
        self.frame_show = ttk.Label(self,
                                    textvariable=self.frame_info,
                                    style='New.TLabel',
                                    anchor='nw')
        global all_config_options
        all_config_options = get_all_config_options(text)
        self.value_dict = {i: eval(i) for i in all_config_options}

    def quit_main_window(self):
        self.img_to_ascii_img_button.place_forget()
        self.video_to_ascii_video_button.place_forget()
        self.video_to_ascii_img_button.place_forget()
        self.change_settings_button.place_forget()

    def reset_main_window(self):
        self.img_to_ascii_img_button.place(x=140, y=100, width=200, height=107)
        self.video_to_ascii_video_button.place(x=440,
                                               y=100,
                                               width=200,
                                               height=107)
        self.video_to_ascii_img_button.place(x=140,
                                             y=250,
                                             width=200,
                                             height=107)
        self.change_settings_button.place(x=440, y=250, width=200, height=107)

    def img_to_ascii_img_window(self):
        global 演示模式
        演示模式 = 0
        self.quit_main_window()
        self.current_widgets = []

        self.go_back_button = ttk.Button(self,
                                         text='返回',
                                         command=self.go_back_main_window,
                                         image=self.button_img2,
                                         compound=CENTER)
        self.go_back_button.place(x=600, y=420)
        self.current_widgets.append(self.go_back_button)

        self.current_widgets += self.set_value('图片路径', '图片路径', True, 600, 50,
                                               0, 100, True)
        self.current_widgets += self.set_value('缩放倍数', '缩放倍数', False, 80, 28,
                                               0, 200)
        self.current_widgets += self.set_value('比特数', '比特数', False, 80, 28, 0,
                                               300)

        ascii_save_as_image_widgets = self.set_value('字符画保存为图片',
                                                     '字符画保存为图片',
                                                     False,
                                                     160,
                                                     40,
                                                     200,
                                                     260,
                                                     mode=1)
        self.ascii_save_as_image = ascii_save_as_image_widgets[0]
        self.current_widgets += ascii_save_as_image_widgets

        ascii_save_as_text_widgets = self.set_value('字符画保存为文本文件',
                                                    '字符画保存为文本文件',
                                                    False,
                                                    200,
                                                    40,
                                                    200,
                                                    200,
                                                    mode=1)
        self.ascii_save_as_text = ascii_save_as_text_widgets[0]
        self.current_widgets += ascii_save_as_text_widgets

        show_percentage_widgets = self.set_value('显示转换进度',
                                                 '显示转换进度',
                                                 False,
                                                 150,
                                                 40,
                                                 450,
                                                 200,
                                                 mode=1)
        self.show_percentage = show_percentage_widgets[0]
        self.current_widgets += show_percentage_widgets

        self.current_widgets += self.set_value('图片宽度比例', '图片宽度比例', False, 100,
                                               28, 400, 260)
        self.current_widgets += self.set_value('图片高度比例', '图片高度比例', False, 100,
                                               28, 550, 260)

        self.save_button = ttk.Button(self,
                                      text='保存当前配置',
                                      command=self.save_current,
                                      image=self.button_img2,
                                      compound=CENTER)
        self.save_button.place(x=600, y=350)
        self.current_widgets.append(self.save_button)

        self.picture_color = IntVar()
        img_color = eval('输出图片为彩色')
        self.picture_color.set(1 if img_color else 0)
        self.output_picture_color = Checkbutton(
            self,
            text='输出图片为彩色',
            variable=self.picture_color,
            command=lambda: self.change_bool('输出图片为彩色'),
            background='black',
            foreground='white',
            borderwidth=0,
            highlightthickness=0,
            font=('微软雅黑', 12),
            selectcolor='black',
            activebackground='white')
        self.output_picture_color.var = self.picture_color
        self.output_picture_color.place(x=620, y=200, width=150, height=40)
        self.value_dict['输出图片为彩色'] = [
            self.output_picture_color, img_color, False
        ]
        self.current_widgets.append(self.output_picture_color)

        self.playing = ttk.Button(self,
                                  text='运行',
                                  command=self.play,
                                  image=self.button_img2,
                                  compound=CENTER)
        self.playing.place(x=150, y=330)
        self.current_widgets.append(self.playing)

        self.frame_info.set('暂无读取帧')
        self.frame_show.place(x=0, y=400, width=290, height=70)
        self.current_widgets.append(self.frame_show)

    def change_settings_window(self):
        self.quit_main_window()
        self.go_back_button = ttk.Button(self,
                                         text='返回',
                                         command=self.go_back_main_window,
                                         image=self.button_img2,
                                         compound=CENTER)
        self.go_back_button.place(x=600, y=420)
        self.config_options_bar = ttk.Scrollbar(self)
        self.config_options_bar.place(x=228, y=121, height=183, anchor=CENTER)
        self.choose_config_options = Listbox(
            self,
            yscrollcommand=self.config_options_bar.set,
            background='black',
            foreground='white')
        self.choose_config_options.bind('<<ListboxSelect>>',
                                        self.show_current_config_options)
        self.options_num = len(all_config_options)
        global all_config_options_ind
        all_config_options_ind = {
            all_config_options[i]: i
            for i in range(self.options_num)
        }
        global config_original
        config_original = all_config_options.copy()
        all_config_options.sort(key=lambda s: s.lower())
        global alpha_config
        alpha_config = all_config_options.copy()
        for k in all_config_options:
            self.choose_config_options.insert(END, k)
        self.choose_config_options.place(x=0, y=30, width=220)
        self.config_options_bar.config(
            command=self.choose_config_options.yview)
        self.config_name = ttk.Label(self, text='')
        self.already_place_config_name = False
        self.config_contents = Text(self,
                                    undo=True,
                                    autoseparators=True,
                                    maxundo=-1)
        self.config_contents.bind('<KeyRelease>', self.config_change)
        self.config_contents.place(x=380, y=120, width=400, height=200)
        self.choose_filename_button = ttk.Button(self,
                                                 text='选择文件路径',
                                                 command=self.choose_filename)
        self.choose_directory_button = ttk.Button(
            self, text='选择文件夹路径', command=self.choose_directory)
        self.choose_filename_button.place(x=0, y=250)
        self.choose_directory_button.place(x=0, y=300)
        self.save = ttk.Button(self, text='保存当前配置', command=self.save_current)
        self.save.place(x=0, y=350)
        self.saved_text = ttk.Label(self, text='saved')
        self.search_text = ttk.Label(self, text='搜索设置参数')
        self.search_text.place(x=0, y=425)
        self.search_contents = StringVar()
        self.search_contents.trace_add('write', self.search)
        self.search_entry = Entry(self, textvariable=self.search_contents)
        self.search_entry.place(x=0, y=450)
        self.search_inds = 0
        self.up_button = ttk.Button(
            self,
            text='上一个',
            command=lambda: self.change_search_inds(-1),
            width=8)
        self.down_button = ttk.Button(
            self,
            text='下一个',
            command=lambda: self.change_search_inds(1),
            width=8)
        self.up_button.place(x=160, y=450)
        self.down_button.place(x=250, y=450)
        self.search_inds_list = []
        self.choose_bool1 = ttk.Button(
            self, text='True', command=lambda: self.insert_bool('True'))
        self.choose_bool2 = ttk.Button(
            self, text='False', command=lambda: self.insert_bool('False'))
        self.choose_bool1.place(x=140, y=270)
        self.choose_bool2.place(x=260, y=270)
        self.change_sort_button = ttk.Button(self,
                                             text="以出现先后排序",
                                             command=self.change_sort)
        self.sort_mode = 0
        self.change_sort()
        self.change_sort_button.place(x=150, y=320)
        self.frame_show.place(x=500, y=330, width=290, height=70)
        self.current_widgets = [
            self.go_back_button, self.config_options_bar,
            self.choose_config_options, self.config_contents,
            self.choose_filename_button, self.choose_directory_button,
            self.save, self.saved_text, self.search_text, self.search_entry,
            self.up_button, self.down_button, self.choose_bool1,
            self.choose_bool2, self.change_sort_button, self.config_name,
            self.frame_show
        ]
        self.frame_info.set('目前暂无动作')
        self.choose_config_options.selection_set(0)
        self.choose_config_options.selection_anchor(0)
        self.show_current_config_options(0)

    def video_to_ascii_video_window(self):
        global 演示模式
        演示模式 = 1
        self.quit_main_window()
        self.current_widgets = []

        self.go_back_button = ttk.Button(self,
                                         text='返回',
                                         command=self.go_back_main_window,
                                         image=self.button_img2,
                                         compound=CENTER)
        self.go_back_button.place(x=600, y=420)
        self.current_widgets.append(self.go_back_button)

        self.current_widgets += self.set_value('视频路径', '视频路径', True, 600, 50,
                                               0, 100, True)
        self.current_widgets += self.set_value('缩放倍数', '缩放倍数', False, 80, 28,
                                               0, 200)
        self.current_widgets += self.set_value('比特数', '比特数', False, 80, 28, 0,
                                               300)

    def video_to_ascii_img_window(self):
        pass

    def go_back_main_window(self):
        for i in self.current_widgets:
            i.place_forget()
        self.reset_main_window()
        global var_counter
        var_counter = 1

    def change_sort(self):
        global all_config_options
        if self.sort_mode == 0:
            self.sort_mode = 1
            self.change_sort_button.config(text='以出现先后排序')
            all_config_options = config_original.copy()
            self.choose_config_options.delete(0, END)
            for k in all_config_options:
                self.choose_config_options.insert(END, k)
        else:
            self.sort_mode = 0
            self.change_sort_button.config(text='以字母或笔画排序')
            all_config_options = alpha_config.copy()
            self.choose_config_options.delete(0, END)
            for k in all_config_options:
                self.choose_config_options.insert(END, k)
        self.search()

    def insert_bool(self, content):
        self.config_contents.delete('1.0', END)
        self.config_contents.insert(END, content)
        self.config_change(0)

    def config_change(self, e):
        current_config = self.choose_config_options.get(ANCHOR)
        try:
            current = self.config_contents.get('1.0', 'end-1c')
            current_new = '"' + current.replace('"', '\\"') + '"'
            self.value_dict[current_config] = current
        except Exception as e:
            print(str(e))
            pass

    def change_search_inds(self, num):
        self.search_inds += num
        if self.search_inds < 0:
            self.search_inds = 0
        if self.search_inds_list:
            search_num = len(self.search_inds_list)
            if self.search_inds >= search_num:
                self.search_inds = search_num - 1
            first = self.search_inds_list[self.search_inds]
            self.choose_config_options.selection_clear(0, END)
            self.choose_config_options.selection_set(first)
            self.choose_config_options.selection_anchor(first)
            self.choose_config_options.see(first)
            self.show_current_config_options(0)

    def search(self, *args):
        current = self.search_contents.get()
        if not current:
            return
        self.search_inds_list = [
            i for i in range(self.options_num)
            if current in all_config_options[i]
        ]
        if self.search_inds_list:
            self.search_inds = 0
            first = self.search_inds_list[self.search_inds]
            self.choose_config_options.selection_clear(0, END)
            self.choose_config_options.selection_set(first)
            self.choose_config_options.selection_anchor(first)
            self.choose_config_options.see(first)
            self.show_current_config_options(0)
        else:
            self.choose_config_options.selection_clear(0, END)

    def show_current_config_options(self, e):
        if not self.already_place_config_name:
            self.already_place_config_name = True
            self.config_name.place(x=380, y=84, height=35)
        current_config = self.choose_config_options.get(ANCHOR)
        if current_config:
            self.config_name.configure(text=current_config)
            self.config_contents.delete('1.0', END)
            current_config_value = self.value_dict[current_config]
            if type(current_config_value) == list:
                current_config_value = current_config_value[1]
            try:
                current_config_value = eval(current_config_value)
            except:
                pass
            self.config_contents.insert(END, str(current_config_value))

    def choose_filename(self):
        filename = filedialog.askopenfilename(initialdir='.',
                                              title="选择文件路径",
                                              filetype=(("all files",
                                                         "*.*"), ))
        self.config_contents.delete('1.0', END)
        self.config_contents.insert(END, f"'{filename}'")
        self.config_change(0)

    def choose_directory(self):
        directory = filedialog.askdirectory(
            initialdir='.',
            title="选择文件夹路径",
        )
        self.config_contents.delete('1.0', END)
        self.config_contents.insert(END, f"'{directory}'")
        self.config_change(0)

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
                  path_enable=False,
                  mode=0):
        current_widgets = []
        global var_counter
        if mode == 0:
            value_label = ttk.Label(self, text=value_name)
            value_label.place(x=x1, y=y1, width=width, height=25)
            value_entry = Text(self,
                               undo=True,
                               autoseparators=True,
                               maxundo=-1,
                               background='black',
                               foreground='white',
                               insertbackground='white')
            before_value = self.value_dict[real_value]
            if type(before_value) != list:
                before_value = str(before_value)
            else:
                before_value = eval(repr(before_value[1]))
            if before_value == 'None':
                before_value = ''
            value_entry.insert(END, before_value)
            value_entry.configure(font=('微软雅黑', 12))
            value_entry.place(x=x1, y=y1 + 25, width=width, height=height)
            self.value_dict[real_value] = [value_entry, before_value, is_str]
            current_widgets.append(value_label)
            current_widgets.append(value_entry)
            value_entry.func = lambda e: self.save_current_contents(
                value_entry, real_value, is_str)
            value_entry.bind('<KeyRelease>', value_entry.func)
        elif mode == 1:
            exec(f"self.checkvar{var_counter} = IntVar()")
            checkvar = eval(f"self.checkvar{var_counter}")
            var_counter += 1
            before_value = self.value_dict[real_value]
            if type(before_value) == list:
                before_value = before_value[1]
            checkvar.set(1 if before_value else 0)
            value_checkbutton = Checkbutton(
                self,
                text=value_name,
                variable=checkvar,
                command=lambda: self.change_bool(value_name),
                background='black',
                foreground='white',
                borderwidth=0,
                highlightthickness=0,
                font=('微软雅黑', 12),
                selectcolor='black',
                activebackground='white')
            value_checkbutton.var = checkvar
            self.value_dict[real_value] = [
                value_checkbutton, before_value, is_str
            ]
            value_checkbutton.place(x=x1, y=y1, width=width, height=height)
            current_widgets.append(value_checkbutton)
        if path_enable:
            path_button = ttk.Button(
                self,
                text='更改',
                command=lambda: self.search_path(value_entry),
                image=self.button_img2,
                compound=CENTER)
            path_button.place(x=x1 + width + 10, y=y1 + 5)
            current_widgets.append(path_button)
        return current_widgets

    def change_bool(self, value_name):
        self.value_dict[value_name][1] = not self.value_dict[value_name][1]

    def save_current_contents(self, current_entry, real_value, is_str):
        try:
            self.value_dict[real_value][1] = current_entry.get('1.0', 'end-1c')
        except Exception as e:
            print(str(e))
            pass

    def search_path(self, obj):
        filename = filedialog.askopenfilename(initialdir='.',
                                              title="选择文件",
                                              filetype=(("所有文件", "*.*"), ))
        if filename:
            obj.delete('1.0', END)
            obj.insert(END, filename)
            obj.func(1)

    def show_saved(self):
        self.frame_info.set('当前配置保存完成')

    def save_current(self):
        changed = False
        for each in self.value_dict:
            current_value = self.value_dict[each]
            if type(current_value) != list:
                before_value = eval(each)
                try:
                    current_value = eval(current_value)
                    current_is_str = False
                except:
                    current_is_str = True
                if current_value != before_value:
                    change(each, current_value, current_is_str)
                    changed = True
                    if current_is_str:
                        current_value = repr(current_value)
                    exec(f"{each} = {current_value}", globals(), globals())
            else:
                if type(current_value[1]) == bool:
                    current = current_value[0].var.get()
                    current = True if current else False
                    if current != eval(each):
                        change(each, current, str_msg)
                        changed = True
                        exec(f"{each} = {current}", globals(), globals())
                else:
                    current = current_value[0].get('1.0', 'end-1c')
                    str_msg = current_value[2]
                    if current == '':
                        current = None
                    if not str_msg:
                        current = eval(current)
                    if current in ['', 'None']:
                        current = None
                        str_msg = False
                    if current != eval(each):
                        change(each, current, str_msg)
                        changed = True
                        exec(
                            f"{each} = {repr(current) if str_msg else current}",
                            globals(), globals())
        if changed:
            self.show_saved()
        else:
            self.frame_info.set('当前配置暂无变动')


def plays():
    current_value_dict = deepcopy({
        i: (j[1] if type(j) == list else j)
        for i, j in root.value_dict.items()
    })
    current_value_dict = {
        i: eval(j) if (type(eval(i)) != str and eval(i) != None
                       and type(j) == str and j not in ['', 'None']) else j
        for i, j in current_value_dict.items()
    }
    current_value_dict = {
        i: (None if j in ['', 'None'] else j)
        for i, j in current_value_dict.items()
    }
    length = len(current_value_dict['字符集'])
    K = 2**current_value_dict['比特数']
    unit = (K + 1) / length

    def get_char(r, g, b, alpha=K):
        if alpha == 0:
            return " "
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        return current_value_dict['字符集'][int(gray / unit)]

    def img_to_ascii(im, show_percentage=False):
        WIDTH = int((im.width * current_value_dict['图片宽度比例'] / 6) /
                    current_value_dict['缩放倍数'])
        HEIGHT = int((im.height * current_value_dict['图片高度比例'] / 12) /
                     current_value_dict['缩放倍数'])
        if show_percentage:
            whole_count = WIDTH * HEIGHT
            count = 0
        im_resize = im.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        txt = ""
        if is_color and (current_value_dict['字符画保存为图片']
                         or current_value_dict['导出视频']):
            im_txt = Image.new("RGB",
                               (int(im.width / current_value_dict['缩放倍数']),
                                int(im.height / current_value_dict['缩放倍数'])),
                               (2**current_value_dict['比特数'] - 1,
                                2**current_value_dict['比特数'] - 1,
                                2**current_value_dict['比特数'] - 1))
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

    if current_value_dict['演示模式'] == 1:
        if current_value_dict['视频帧图路径']:
            os.chdir(current_value_dict['视频帧图路径'])
            frames = []
            count = 0
            file_ls = os.listdir()
            for i in file_ls:
                frames.append(Image.open(i))
                count += 1
                root.frame_info.set(f'正在读取视频帧{count}')
                root.update()
        else:
            vidcap = cv2.VideoCapture(current_value_dict['视频路径'])
            is_read, img = vidcap.read()
            if not is_read:
                root.frame_info.set('视频路径不存在或者为空')
                root.update()
                return
            frames = []
            count = 0
            if current_value_dict['视频导出帧图片到文件夹']:
                os.mkdir(current_value_dict['视频帧图片保存路径'])
                os.chdir(current_value_dict['视频帧图片保存路径'])
                start_frame = 0
                if not current_value_dict['视频转换帧数区间']:
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
                    start_frame, to_frame = current_value_dict['视频转换帧数区间']
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
                if not current_value_dict['视频转换帧数区间']:
                    while is_read:
                        frames.append(
                            Image.fromarray(
                                cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
                        is_read, img = vidcap.read()
                        count += 1
                        root.frame_info.set(f'正在读取视频帧{count}')
                        root.update()
                else:
                    start_frame, to_frame = current_value_dict['视频转换帧数区间']
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
        if current_value_dict['导出视频']:
            try:
                os.mkdir('temp_video_images')
            except:
                pass
            os.chdir('temp_video_images')
            num_frames = len(frames)
            n = len(str(num_frames))
            try:
                font = ImageFont.truetype(current_value_dict['字体路径'],
                                          size=current_value_dict['字体大小'])
            except:
                font = ImageFont.load_default()
            font_x_len, font_y_len = font.getsize(current_value_dict['字符集'][1])
            font_y_len = int(font_y_len * 1.37)
            if is_color == 0:
                for i in range(num_frames):
                    root.frame_info.set(f'正在转换第{start_frame + i + 1}帧')
                    root.update()
                    im = frames[i]
                    text_str = img_to_ascii(im)
                    im_txt = Image.new(
                        "L", (int(im.width / current_value_dict['缩放倍数']),
                              int(im.height / current_value_dict['缩放倍数'])),
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
            file_name = os.path.splitext(
                os.path.basename(current_value_dict['视频路径']))[0]
            output_filename = f'ascii_{file_name}.mp4'
            if output_filename in os.listdir():
                os.remove(output_filename)
            ffmpeg.input(f'temp_video_images/%{n}d.png',
                         framerate=current_value_dict['视频输出帧数']).output(
                             output_filename).run()
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
            im = Image.open(current_value_dict['图片路径'])
            text_str_output = img_to_ascii(im, current_value_dict['显示转换进度'])
            if type(text_str_output) != str:
                text_str = text_str_output[0]
            else:
                text_str = text_str_output
        except Exception as e:
            print(str(e))
            root.frame_info.set('图片路径不存在或者为空')
            root.update()
            return
        root.frame_info.set('图片转换完成')
        root.update()
        file_name = os.path.splitext(
            os.path.basename(current_value_dict['图片路径']))[0]
        if current_value_dict['字符画保存为文本文件']:
            root.frame_info.set('图片转换完成，正在写入字符画为\n文本文件...')
            root.update()
            with open(f'ascii_{file_name}.txt', 'w',
                      encoding='utf-8-sig') as f:
                f.write(text_str)
            root.frame_info.set('已成功写入文本文件')
            root.update()
        if current_value_dict['字符画保存为图片']:
            root.frame_info.set('图片转换完成，正在输出字符画为图片...')
            root.update()
            try:
                font = ImageFont.truetype(current_value_dict['字体路径'],
                                          size=current_value_dict['字体大小'])
            except:
                font = ImageFont.load_default()
            font_x_len, font_y_len = font.getsize(current_value_dict['字符集'][1])
            font_y_len = int(font_y_len * 1.37)
            if is_color == 0:
                im_txt = Image.new(
                    "L", (int(im.width / current_value_dict['缩放倍数']),
                          int(im.height / current_value_dict['缩放倍数'])),
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