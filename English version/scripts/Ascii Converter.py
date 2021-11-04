with open('scripts/config_en.py', encoding='utf-8-sig') as f:
    text = f.read()
    exec(text, globals())
var_counter = 1
abs_path = os.getcwd()


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
    text = open('scripts/config_en.py', encoding='utf-8-sig').read()
    text_ls = list(text)
    var_len = len(var) + 1
    var_ind = text.index('\n' + var) + var_len
    next_line = text[var_ind:].index('\n')
    if is_str:
        text_ls[var_ind:var_ind + next_line] = f' = {repr(new)}'
    else:
        text_ls[var_ind:var_ind + next_line] = f" = {new}"
    with open('scripts/config_en.py', 'w', encoding='utf-8-sig') as f:
        f.write(''.join(text_ls))


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Ascii Converter")
        self.minsize(800, 500)
        self.resizable(0, 0)
        self.wm_iconbitmap('resources/ascii.ico')
        self.value_dict = {}
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        font=('Consolas', 12))
        style.map('TButton', foreground=[('active', 'white')])
        style.configure('New.TButton',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        font=('Consolas', 10))
        style.configure('New2.TButton',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        font=('Consolas', 8))
        style.configure('TEntry',
                        fieldbackground='black',
                        foreground='white',
                        insertcolor='white')
        style.configure('TLabelframe',
                        background='black',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        font=('Consolas', 12))
        style.configure('TLabelframe.Label',
                        background='black',
                        foreground='white',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        font=('Consolas', 12))
        style.configure('TLabel',
                        background='black',
                        foreground='white',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        font=('Consolas', 12))
        style.configure('New.TLabel',
                        background='black',
                        foreground='white',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        font=('Consolas', 10))
        style.configure('TCheckbutton',
                        background='black',
                        foreground='white',
                        borderwidth=0,
                        focuscolor='none',
                        highlightthickness=0,
                        inactiveselectbackground='black',
                        font=('Consolas', 12))
        style.configure('TScrollbar', background='white')
        self.button_img = ImageTk.PhotoImage(
            Image.open('resources/button.png').resize((180, 100)))
        self.button_img2 = ImageTk.PhotoImage(
            Image.open('resources/button.png').resize((100, 40)))
        self.button_img3 = ImageTk.PhotoImage(
            Image.open('resources/button.png').resize((150, 40)))
        self.button_img4 = ImageTk.PhotoImage(
            Image.open('resources/button.png').resize((150, 30)))
        self.button_img5 = ImageTk.PhotoImage(
            Image.open('resources/button.png').resize((200, 30)))
        bg_image = Image.open('resources/5072612.jpg')
        ratio = 800 / bg_image.width
        self.bg_image = ImageTk.PhotoImage(
            bg_image.resize((800, int(bg_image.height * ratio))))
        self.bg_label = ttk.Label(
            self,
            image=self.bg_image,
            text='\n' * 23 +
            'made by Rainbow Dreamer\nqq: 2180502841\nBiliBili Account: Rainbow_Dreamer\nGithub Account: Rainbow Dreamer',
            compound=CENTER)
        self.bg_label.configure(font=('Consolas', 10), foreground='white')
        self.bg_label.place(x=0, y=0)
        title_image = Image.open('resources/title.png')
        self.title_image = ImageTk.PhotoImage(title_image.resize((240, 100)))
        self.title_label = ttk.Label(self,
                                     image=self.title_image,
                                     text='Ascii Converter',
                                     compound=CENTER)
        self.title_label.configure(font=('Consolas', 15), foreground='white')
        self.title_label.place(x=260, y=10)
        self.img_to_ascii_img_button = ttk.Button(
            self,
            text='Images to Ascii\nImages/Texts',
            image=self.button_img,
            compound=CENTER,
            command=self.img_to_ascii_img_window)
        self.img_to_ascii_img_button.place(x=140, y=140, width=180, height=100)
        self.video_to_ascii_video_button = ttk.Button(
            self,
            text='Videos to\nAscii Videos',
            image=self.button_img,
            compound=CENTER,
            command=self.video_to_ascii_video_window)
        self.video_to_ascii_video_button.place(x=440,
                                               y=140,
                                               width=180,
                                               height=100)
        self.video_to_ascii_img_button = ttk.Button(
            self,
            text='Extract Frames\nFrom Videos',
            image=self.button_img,
            compound=CENTER,
            command=self.video_to_ascii_img_window)
        self.video_to_ascii_img_button.place(x=140,
                                             y=280,
                                             width=180,
                                             height=100)
        self.change_settings_button = ttk.Button(
            self,
            text='Change Settings',
            image=self.button_img,
            compound=CENTER,
            command=self.change_settings_window)
        self.change_settings_button.place(x=440, y=280, width=180, height=100)
        self.frame_info = StringVar()
        self.frame_show = ttk.Label(self,
                                    textvariable=self.frame_info,
                                    style='New.TLabel',
                                    anchor='nw')
        global all_config_options
        all_config_options = get_all_config_options(text)
        self.value_dict = {i: eval(i) for i in all_config_options}
        self.go_back = False

        try:
            with open('browse memory.txt', encoding='utf-8-sig') as f:
                self.last_place = f.read()
        except:
            self.last_place = "."

    def quit_main_window(self):
        self.img_to_ascii_img_button.place_forget()
        self.video_to_ascii_video_button.place_forget()
        self.video_to_ascii_img_button.place_forget()
        self.change_settings_button.place_forget()

    def reset_main_window(self):
        self.img_to_ascii_img_button.place(x=140, y=140, width=180, height=100)
        self.video_to_ascii_video_button.place(x=440,
                                               y=140,
                                               width=180,
                                               height=100)
        self.video_to_ascii_img_button.place(x=140,
                                             y=280,
                                             width=180,
                                             height=100)
        self.change_settings_button.place(x=440, y=280, width=180, height=100)

    def img_to_ascii_img_window(self):
        self.go_back = False
        global convert_mode
        convert_mode = 0
        global output_video
        output_video = False
        self.quit_main_window()
        self.current_widgets = []

        self.go_back_button = ttk.Button(self,
                                         text='Back',
                                         command=self.go_back_main_window,
                                         image=self.button_img2,
                                         compound=CENTER)
        self.go_back_button.place(x=600, y=420)
        self.current_widgets.append(self.go_back_button)

        self.current_widgets += self.set_value('image path', 'image_path',
                                               True, 600, 50, 0, 115, True)
        self.current_widgets += self.set_value('resize ratio', 'resize_ratio',
                                               False, 120, 28, 0, 200)
        self.current_widgets += self.set_value('bit number', 'bit_number',
                                               False, 120, 28, 0, 300)

        self.current_widgets += self.set_value('save as ascii images',
                                               'save_as_ascii_images',
                                               False,
                                               220,
                                               40,
                                               160,
                                               260,
                                               mode=1)

        self.current_widgets += self.set_value('save as ascii text',
                                               'save_as_ascii_text',
                                               False,
                                               200,
                                               40,
                                               200,
                                               200,
                                               mode=1)

        self.current_widgets += self.set_value('show convert percentages',
                                               'show_convert_percentages',
                                               False,
                                               200,
                                               40,
                                               410,
                                               200,
                                               mode=1,
                                               font_size=10)

        self.current_widgets += self.set_value('image width ratio',
                                               'image_width_ratio', False, 160,
                                               28, 400, 260)
        self.current_widgets += self.set_value('image height ratio',
                                               'image_height_ratio', False,
                                               170, 28, 580, 260)

        self.save_button = ttk.Button(self,
                                      text='Save Current Settings',
                                      command=self.save_current,
                                      image=self.button_img4,
                                      compound=CENTER,
                                      style='New2.TButton')
        self.save_button.place(x=600, y=350)
        self.current_widgets.append(self.save_button)

        self.picture_color = IntVar()
        img_color = self.value_dict['colored_images']
        if type(img_color) == list:
            img_color = img_color[1]
        self.picture_color.set(1 if img_color else 0)
        self.output_picture_color = Checkbutton(
            self,
            text='colored images',
            variable=self.picture_color,
            command=lambda: self.change_bool('colored_images'),
            background='black',
            foreground='white',
            borderwidth=0,
            highlightthickness=0,
            font=('Consolas', 12),
            selectcolor='black',
            activebackground='white')
        self.output_picture_color.var = self.picture_color
        self.output_picture_color.place(x=620, y=200, width=160, height=40)
        self.value_dict['colored_images'] = [
            self.output_picture_color, img_color, False
        ]
        self.current_widgets.append(self.output_picture_color)

        self.playing = ttk.Button(self,
                                  text='Start',
                                  command=self.play,
                                  image=self.button_img2,
                                  compound=CENTER)
        self.playing.place(x=150, y=330)
        self.current_widgets.append(self.playing)

        self.frame_info.set('No actions at this time')
        self.frame_show.place(x=0, y=400, width=260, height=70)
        self.current_widgets.append(self.frame_show)

    def change_settings_window(self):
        self.go_back = False
        self.quit_main_window()
        self.go_back_button = ttk.Button(self,
                                         text='Back',
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
        self.config_contents.place(x=400, y=160, width=380, height=170)
        self.choose_filename_button = ttk.Button(self,
                                                 text='Choose filename',
                                                 command=self.choose_filename,
                                                 image=self.button_img4,
                                                 compound=CENTER,
                                                 style='New.TButton')
        self.choose_directory_button = ttk.Button(
            self,
            text='Choose directory',
            command=self.choose_directory,
            image=self.button_img4,
            compound=CENTER,
            style='New.TButton')
        self.choose_filename_button.place(x=0, y=230)
        self.choose_directory_button.place(x=0, y=300)
        self.save = ttk.Button(self,
                               text='Save Current Settings',
                               command=self.save_current,
                               image=self.button_img4,
                               compound=CENTER,
                               style='New2.TButton')
        self.save.place(x=0, y=360)
        self.saved_text = ttk.Label(self, text='saved')
        self.search_text = ttk.Label(self, text='Search Settings')
        self.search_text.place(x=0, y=425)
        self.search_contents = StringVar()
        self.search_contents.trace_add('write', self.search)
        self.search_entry = Entry(self, textvariable=self.search_contents)
        self.search_entry.place(x=0, y=450)
        self.search_inds = 0
        self.up_button = ttk.Button(
            self,
            text='Previous',
            command=lambda: self.change_search_inds(-1),
            width=8,
            image=self.button_img2,
            compound=CENTER,
            style='New.TButton')
        self.down_button = ttk.Button(
            self,
            text='Next',
            command=lambda: self.change_search_inds(1),
            width=8,
            image=self.button_img2,
            compound=CENTER,
            style='New.TButton')
        self.up_button.place(x=160, y=395)
        self.down_button.place(x=160, y=450)
        self.search_inds_list = []
        self.choose_bool1 = ttk.Button(
            self,
            text='True',
            command=lambda: self.insert_bool('True'),
            image=self.button_img2,
            compound=CENTER)
        self.choose_bool2 = ttk.Button(
            self,
            text='False',
            command=lambda: self.insert_bool('False'),
            image=self.button_img2,
            compound=CENTER)
        self.choose_bool1.place(x=160, y=270)
        self.choose_bool2.place(x=280, y=270)
        self.change_sort_button = ttk.Button(
            self,
            text="Sort in order of appearance",
            command=self.change_sort,
            image=self.button_img5,
            compound=CENTER,
            style='New2.TButton')
        self.sort_mode = 0
        self.change_sort()
        self.change_sort_button.place(x=160, y=340)
        self.frame_show.place(x=500, y=330, width=280, height=70)
        self.current_widgets = [
            self.go_back_button, self.config_options_bar,
            self.choose_config_options, self.config_contents,
            self.choose_filename_button, self.choose_directory_button,
            self.save, self.saved_text, self.search_text, self.search_entry,
            self.up_button, self.down_button, self.choose_bool1,
            self.choose_bool2, self.change_sort_button, self.config_name,
            self.frame_show
        ]
        self.frame_info.set('No actions at this time')
        self.choose_config_options.selection_set(0)
        self.choose_config_options.selection_anchor(0)
        self.show_current_config_options(0)

    def video_to_ascii_video_window(self):
        self.go_back = False
        global convert_mode
        convert_mode = 1
        global output_video
        output_video = True
        global output_video_frames
        output_video_frames = False
        self.quit_main_window()
        self.current_widgets = []

        self.go_back_button = ttk.Button(self,
                                         text='Back',
                                         command=self.go_back_main_window,
                                         image=self.button_img2,
                                         compound=CENTER)
        self.go_back_button.place(x=630, y=420)
        self.current_widgets.append(self.go_back_button)

        self.current_widgets += self.set_value('video path', 'video_path',
                                               True, 600, 50, 0, 115, True)
        self.current_widgets += self.set_value('resize ratio', 'resize_ratio',
                                               False, 120, 28, 0, 200)
        self.current_widgets += self.set_value('bit number', 'bit_number',
                                               False, 120, 28, 0, 300)
        self.current_widgets += self.set_value('video frames interval',
                                               'video_frames_interval', False,
                                               200, 28, 140, 200)
        self.current_widgets += self.set_value('video frame path',
                                               'video_frame_path',
                                               True,
                                               300,
                                               28,
                                               350,
                                               200,
                                               True,
                                               path_mode=1)
        self.current_widgets += self.set_value('font path', 'font_path', True,
                                               100, 28, 150, 270)
        self.current_widgets += self.set_value('font size', 'font_size', False,
                                               100, 28, 270, 270)
        self.current_widgets += self.set_value('video frame rate',
                                               'video_frame_rate', False, 160,
                                               28, 450, 270)
        self.current_widgets += self.set_value('image width ratio',
                                               'image_width_ratio', False, 160,
                                               28, 270, 330)
        self.current_widgets += self.set_value('image height ratio',
                                               'image_height_ratio', False,
                                               170, 28, 450, 330)

        self.save_button = ttk.Button(self,
                                      text='Save Current Settings',
                                      command=self.save_current,
                                      image=self.button_img4,
                                      compound=CENTER,
                                      style='New2.TButton')
        self.save_button.place(x=630, y=350)
        self.current_widgets.append(self.save_button)

        self.picture_color = IntVar()
        img_color = self.value_dict['colored_images']
        if type(img_color) == list:
            img_color = img_color[1]
        self.picture_color.set(1 if img_color else 0)
        self.output_picture_color = Checkbutton(
            self,
            text='colored images',
            variable=self.picture_color,
            command=lambda: self.change_bool('colored_images'),
            background='black',
            foreground='white',
            borderwidth=0,
            highlightthickness=0,
            font=('Consolas', 12),
            selectcolor='black',
            activebackground='white')
        self.output_picture_color.var = self.picture_color
        self.output_picture_color.place(x=620, y=280, width=160, height=40)
        self.value_dict['colored_images'] = [
            self.output_picture_color, img_color, False
        ]
        self.current_widgets.append(self.output_picture_color)

        self.playing = ttk.Button(self,
                                  text='Start',
                                  command=self.play,
                                  image=self.button_img2,
                                  compound=CENTER)
        self.playing.place(x=150, y=340)
        self.current_widgets.append(self.playing)

        self.frame_info.set('No actions at this time')
        self.frame_show.place(x=0, y=400, width=260, height=70)
        self.current_widgets.append(self.frame_show)

    def video_to_ascii_img_window(self):
        self.go_back = False
        global convert_mode
        convert_mode = 1
        global output_video
        output_video = False
        global output_video_frames
        output_video_frames = True
        self.quit_main_window()
        self.current_widgets = []

        self.go_back_button = ttk.Button(self,
                                         text='Back',
                                         command=self.go_back_main_window,
                                         image=self.button_img2,
                                         compound=CENTER)
        self.go_back_button.place(x=630, y=420)
        self.current_widgets.append(self.go_back_button)

        self.current_widgets += self.set_value('video path', 'video_path',
                                               True, 600, 50, 0, 115, True)
        self.current_widgets += self.set_value('video frames interval',
                                               'video_frames_interval', False,
                                               200, 28, 70, 200)
        self.current_widgets += self.set_value('video frames save path',
                                               'video_frames_save_path',
                                               False,
                                               300,
                                               28,
                                               300,
                                               200,
                                               True,
                                               path_mode=1)
        self.picture_color = IntVar()
        self.picture_color.set(1)
        self.save_button = ttk.Button(self,
                                      text='Save Current Settings',
                                      command=self.save_current,
                                      image=self.button_img4,
                                      compound=CENTER,
                                      style='New2.TButton')
        self.save_button.place(x=630, y=350)
        self.current_widgets.append(self.save_button)

        self.playing = ttk.Button(self,
                                  text='Start',
                                  command=self.play,
                                  image=self.button_img2,
                                  compound=CENTER)
        self.playing.place(x=150, y=320)
        self.current_widgets.append(self.playing)

        self.frame_info.set('No actions at this time')
        self.frame_show.place(x=0, y=400, width=260, height=70)
        self.current_widgets.append(self.frame_show)

    def go_back_main_window(self):
        os.chdir(abs_path)
        self.go_back = True
        global output_video
        output_video = False
        global output_video_frames
        output_video_frames = False
        for i in self.current_widgets:
            i.place_forget()
        self.reset_main_window()
        global var_counter
        var_counter = 1

    def change_sort(self):
        global all_config_options
        if self.sort_mode == 0:
            self.sort_mode = 1
            self.change_sort_button.config(text='Sort in order of appearance')
            all_config_options = config_original.copy()
            self.choose_config_options.delete(0, END)
            for k in all_config_options:
                self.choose_config_options.insert(END, k)
        else:
            self.sort_mode = 0
            self.change_sort_button.config(text='Sort in alphabetical order')
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
            self.config_name.place(x=400, y=124, height=35)
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
        filename = filedialog.askopenfilename(initialdir=self.last_place,
                                              title="Choose filename",
                                              filetype=(("All files",
                                                         "*.*"), ))
        self.config_contents.delete('1.0', END)
        self.config_contents.insert(END, f"'{filename}'")
        self.config_change(0)

    def choose_directory(self):
        directory = filedialog.askdirectory(
            initialdir=self.last_place,
            title="Choose directory",
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
                  path_mode=0,
                  mode=0,
                  font_size=12):
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
            value_entry.configure(font=('Consolas', 12))
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
                command=lambda: self.change_bool(real_value),
                background='black',
                foreground='white',
                borderwidth=0,
                highlightthickness=0,
                font=('Consolas', font_size),
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
                text='change',
                command=lambda: self.search_path(value_entry, path_mode),
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

    def search_path(self, obj, mode=0):
        if mode == 0:
            filename = filedialog.askopenfilename(initialdir=self.last_place,
                                                  title="Choose filename",
                                                  filetype=(("All files",
                                                             "*.*"), ))
        elif mode == 1:
            filename = filedialog.askdirectory(initialdir=self.last_place,
                                               title="Choose directory")
        if filename:
            obj.delete('1.0', END)
            obj.insert(END, filename)
            obj.func(1)
            memory = os.path.dirname(filename)
            with open('browse memory.txt', 'w', encoding='utf-8-sig') as f:
                f.write(memory)
            self.last_place = memory

    def show_saved(self):
        self.frame_info.set('Current settings are saved')

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
                    if not str_msg and current is not None:
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
            self.frame_info.set('There\'s no changes in\ncurrent settings')


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
    length = len(current_value_dict['ascii_character_set'])
    K = 2**current_value_dict['bit_number']
    unit = (K + 1) / length

    def get_char(r, g, b, alpha=K):
        if alpha == 0:
            return " "
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        return current_value_dict['ascii_character_set'][int(gray / unit)]

    def img_to_ascii(im, show_percentage=False):
        WIDTH = int((im.width * current_value_dict['image_width_ratio'] / 6) /
                    current_value_dict['resize_ratio'])
        HEIGHT = int(
            (im.height * current_value_dict['image_height_ratio'] / 12) /
            current_value_dict['resize_ratio'])
        if show_percentage:
            whole_count = WIDTH * HEIGHT
            count = 0
        im_resize = im.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        txt = ""
        if is_color and (current_value_dict['save_as_ascii_images']
                         or output_video):
            im_txt = Image.new(
                "RGB", (int(im.width / current_value_dict['resize_ratio']),
                        int(im.height / current_value_dict['resize_ratio'])),
                (2**current_value_dict['bit_number'] - 1,
                 2**current_value_dict['bit_number'] - 1,
                 2**current_value_dict['bit_number'] - 1))
            colors = []
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    pixel = im_resize.getpixel((j, i))
                    colors.append(pixel)
                    txt += get_char(*pixel)
                if show_percentage:
                    count += WIDTH
                    root.frame_info.set(
                        f'Conversion progress:  {round((count/whole_count)*100, 3)}%'
                    )
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
                        f'Conversion progress:  {round((count/whole_count)*100, 3)}%'
                    )
                    root.update()
                txt += '\n'
            return txt

    if convert_mode == 1:
        video_frames_path = current_value_dict['video_frame_path']
        if video_frames_path:
            os.chdir(video_frames_path)
            file_ls = [f for f in os.listdir() if os.path.isfile(f)]
            file_ls.sort(key=lambda x: int(os.path.splitext(x)[0]))
            frames = (Image.open(i) for i in file_ls)
            start_frame = 0
        else:
            if not current_value_dict['video_path']:
                return
            vidcap = cv2.VideoCapture(current_value_dict['video_path'])
            count = 0
            if output_video_frames:
                try:
                    os.chdir(current_value_dict['video_frames_save_path'])
                except:
                    if not os.path.exists('video_frame_ascii_images'):
                        os.mkdir('video_frame_ascii_images')
                    os.chdir('video_frame_ascii_images')
                    for each in os.listdir():
                        os.remove(each)
                start_frame = 0
                if not current_value_dict['video_frames_interval']:
                    whole_frame_number = int(
                        vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
                    frames = (Image.fromarray(
                        cv2.cvtColor(vidcap.read()[1], cv2.COLOR_BGR2RGB))
                              for k in range(whole_frame_number))
                    is_read, img = vidcap.read()
                    while is_read:
                        if root.go_back:
                            break
                        cv2.imwrite(f"{count}.png", img)
                        is_read, img = vidcap.read()
                        count += 1
                        root.frame_info.set(
                            f'Reading and exporting video frame {count}')
                        root.update()
                    vidcap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                else:
                    start_frame, to_frame = current_value_dict[
                        'video_frames_interval']
                    no_of_frames = to_frame - start_frame
                    vidcap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
                    frames = (Image.fromarray(
                        cv2.cvtColor(vidcap.read()[1], cv2.COLOR_BGR2RGB))
                              for k in range(no_of_frames))
                    is_read, img = vidcap.read()
                    for k in range(no_of_frames):
                        if root.go_back:
                            break
                        if is_read:
                            cv2.imwrite(f"{count}.png", img)
                            is_read, img = vidcap.read()
                            count += 1
                            root.frame_info.set(
                                f'Reading and exporting video frame {start_frame + count}'
                            )
                            root.update()
                        else:
                            break
                    vidcap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
                os.chdir(abs_path)
                root.frame_info.set(
                    'Video frames are successfully\nexported as images')
                root.update()
                return
            else:
                start_frame = 0
                if not current_value_dict['video_frames_interval']:
                    whole_frame_number = int(
                        vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
                    frames = (Image.fromarray(
                        cv2.cvtColor(vidcap.read()[1], cv2.COLOR_BGR2RGB))
                              for k in range(whole_frame_number))
                    frame_length = whole_frame_number
                else:
                    start_frame, to_frame = current_value_dict[
                        'video_frames_interval']
                    no_of_frames = to_frame - start_frame
                    frame_length = no_of_frames
                    vidcap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
                    frames = (Image.fromarray(
                        cv2.cvtColor(vidcap.read()[1], cv2.COLOR_BGR2RGB))
                              for k in range(no_of_frames))
        if output_video:
            if video_frames_path:
                file_name = os.path.splitext(
                    os.path.basename(video_frames_path))[0]
            else:
                file_name = os.path.splitext(
                    os.path.basename(current_value_dict['video_path']))[0]
            output_filename = filedialog.asksaveasfilename(
                initialdir='.',
                initialfile=f'ascii_{file_name}.mp4',
                title="Choose the file path of the exported video",
                filetype=(("All files", "*.*"), ))
            if not output_filename:
                return
            if video_frames_path:
                os.chdir(abs_path)
            if not os.path.exists('temp_video_images'):
                os.mkdir('temp_video_images')
            os.chdir('temp_video_images')
            for each in os.listdir():
                os.remove(each)
            num_frames = frame_length
            n = len(str(num_frames))
            try:
                font = ImageFont.truetype(current_value_dict['font_path'],
                                          size=current_value_dict['font_size'])
            except:
                font = ImageFont.load_default()
            font_x_len, font_y_len = font.getsize(
                current_value_dict['ascii_character_set'][1])
            font_y_len = int(font_y_len * 1.37)
            if is_color == 0:
                for i in range(num_frames):
                    if root.go_back:
                        break
                    root.frame_info.set(
                        f'Converting video frame {start_frame + i + 1}/{start_frame + num_frames + 1}'
                    )
                    root.update()
                    try:
                        im = next(frames)
                    except:
                        break
                    text_str = img_to_ascii(im)
                    im_txt = Image.new(
                        "L",
                        (int(im.width / current_value_dict['resize_ratio']),
                         int(im.height / current_value_dict['resize_ratio'])),
                        'white')
                    dr = ImageDraw.Draw(im_txt)
                    x = y = 0
                    for j in range(len(text_str)):
                        if text_str[j] == "\n":
                            x = 0
                            y += font_y_len
                        dr.text((x, y), text_str[j], fill='black', font=font)
                        x += font_x_len
                    if root.go_back:
                        break
                    im_txt.save(f'{i:0{n}d}.png')
            else:
                for i in range(num_frames):
                    if root.go_back:
                        break
                    root.frame_info.set(
                        f'Converting video frame {start_frame + i + 1}/{start_frame + num_frames + 1}'
                    )
                    root.update()
                    try:
                        text_str_output = img_to_ascii(next(frames))
                    except:
                        break
                    txt, colors, im_txt = text_str_output
                    dr = ImageDraw.Draw(im_txt)
                    x = y = 0
                    for j in range(len(txt)):
                        if txt[j] == "\n":
                            x = 0
                            y += font_y_len
                        dr.text((x, y), txt[j], fill=colors[j], font=font)
                        x += font_x_len
                    if root.go_back:
                        break
                    im_txt.save(f'{i:0{n}d}.png')
            root.frame_info.set(
                'Conversion are finished,\nstart to export video..')
            root.update()
            os.chdir(abs_path)
            if root.go_back:
                return
            current_framerate = current_value_dict['video_frame_rate']
            if not current_framerate:
                current_framerate = vidcap.get(cv2.CAP_PROP_FPS)
            ffmpeg.input(f'temp_video_images/%{n}d.png',
                         framerate=current_framerate).output(
                             output_filename, pix_fmt='yuv420p').run()
            root.frame_info.set('Video has been successfully exported')
            root.update()
    else:
        root.frame_info.set('Converting images..')
        root.update()
        try:
            im = Image.open(current_value_dict['image_path'])
            text_str_output = img_to_ascii(
                im, current_value_dict['show_convert_percentages'])
            if type(text_str_output) != str:
                text_str = text_str_output[0]
            else:
                text_str = text_str_output
        except Exception as e:
            print(str(e))
            root.frame_info.set('This image path does not exist')
            root.update()
            return
        root.frame_info.set('Converting images are finished')
        root.update()
        file_name = os.path.splitext(
            os.path.basename(current_value_dict['image_path']))[0]
        if current_value_dict['save_as_ascii_text']:
            root.frame_info.set(
                'Converting images are finished,\nwriting ascii result to text...'
            )
            root.update()
            output_filename = filedialog.asksaveasfilename(
                initialdir='.',
                initialfile=f'ascii_{file_name}.txt',
                title="Choose the file path of the exported ASCII text file",
                filetype=(("All files", "*.*"), ))
            if not output_filename:
                return
            with open(output_filename, 'w', encoding='utf-8-sig') as f:
                f.write(text_str)
            root.frame_info.set('Successfully writing to text file')
            root.update()
        if current_value_dict['save_as_ascii_images']:
            root.frame_info.set(
                'Converting images are finished,\nwriting ascii result to image...'
            )
            root.update()
            output_filename = filedialog.asksaveasfilename(
                initialdir='.',
                initialfile=f'ascii_{file_name}.png',
                title="Choose the file path of the exported ASCII image file",
                filetype=(("All files", "*.*"), ))
            if not output_filename:
                return
            try:
                font = ImageFont.truetype(current_value_dict['font_path'],
                                          size=current_value_dict['font_size'])
            except:
                font = ImageFont.load_default()
            font_x_len, font_y_len = font.getsize(
                current_value_dict['ascii_character_set'][1])
            font_y_len = int(font_y_len * 1.37)
            if is_color == 0:
                im_txt = Image.new(
                    "L", (int(im.width / current_value_dict['resize_ratio']),
                          int(im.height / current_value_dict['resize_ratio'])),
                    'white')
                dr = ImageDraw.Draw(im_txt)
                x = y = 0
                for i in range(len(text_str)):
                    if text_str[i] == "\n":
                        x = 0
                        y += font_y_len
                    dr.text((x, y), text_str[i], fill='black', font=font)
                    x += font_x_len
                im_txt.save(output_filename)

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
                im_txt.save(output_filename)

            root.frame_info.set('Successfully writing to image file')
            root.update()


root = Root()
root.mainloop()