import datetime
import os
import threading
import time
import subprocess
import numpy as np
import pyperclip
from PIL import ImageGrab, Image

import ImageUtil

class MainController:
    def __init__(self, view):
        self.View = view
        self.Image = None
        self.Images = []
        self.LastArray = None

        # Viewのボタンに処理を紐づけ
        view.SetButtonCommand('Load', self.LoadFromClipboard)
        view.SetButtonCommand('Clear', self.Clear)
        view.SetButtonCommand('Save', self.Save)

        # クリップボード監視スレッドを開始
        self.CaptureThread = threading.Thread(target = self.ThreadLoop)
        self.CaptureThread.daemon = True
        self.CaptureThread.start()

    def LoadFromClipboard(self):
        try:
            img = ImageGrab.grabclipboard()
        except:
            img = None
        if type(img) == list:
            if type(img[0]) == Image:
                img = img[0]
            else:
                img = None
        img = ImageUtil.GetStatusView(img)
        if not img is None:
            ary = np.array(img)
            if self.LastArray is None or not np.array_equal(self.LastArray, ary):
                self.LastArray = ary
                self.Images.append(img)
                self.Image = ImageUtil.GetOrganizedStatus(self.Images)
                self.View.SetPreviewImage(self.Image)

    def Clear(self):
        self.Images = []
        self.View.SetPreviewImage(None)

    def Save(self):
        if not self.Image is None:
            self.Image.save(datetime.datetime.now().strftime('./Output/%Y%m%d_%H%M%S.png'))
            subprocess.Popen(['explorer', os.path.abspath('./Output')])

    def ThreadLoop(self):
        # 定期処理
        while(True):
            self.LoadFromClipboard()
            time.sleep(1)
