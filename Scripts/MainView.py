import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk

class MainView:
    def __init__(self, master):
        mainFrame = ttk.Frame(master)
        mainFrame.pack(expand='true', fill='both', side='top')

        # コマンド領域
        commandFrame = ttk.Frame(mainFrame, width=320)
        commandFrame.pack(anchor=tk.NW, side=tk.LEFT, fill=tk.Y)

        self.Buttons = {}
        
        loadButton = ttk.Button(commandFrame, text='読み込み')
        loadButton.pack()
        self.Buttons['Load'] = loadButton

        clearButton = ttk.Button(commandFrame, text='リセット')
        clearButton.pack()
        self.Buttons['Clear'] = clearButton

        saveButton = ttk.Button(commandFrame, text='Save')
        saveButton.pack()
        self.Buttons['Save'] = saveButton

        # Preview領域
        self.Preview = ttk.Label(mainFrame, padding=10)
        self.Preview.pack(anchor=tk.NW, side=tk.LEFT, ipadx=0, expand=True)

    # ボタンを押した時の挙動を設定
    def SetButtonCommand(self, id, command):
        self.Buttons[id]['command'] = command

    # Previewにイメージをセット
    def SetPreviewImage(self, image):
        if image is None:
            self.PreviewImage = None
            self.Preview['image'] = None
        else:
            self.PreviewImage = ImageTk.PhotoImage(image = image.resize((image.width // 2, image.height // 2)))
            self.Preview['image'] = self.PreviewImage
