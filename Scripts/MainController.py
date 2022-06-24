import datetime
from PIL import ImageGrab

import ImageUtil

class MainController:
    def __init__(self, view):
        self.View = view
        self.Images = []

        # Viewのボタンに処理を紐づけ
        view.SetButtonCommand('Load', self.LoadFromClipboard)
        view.SetButtonCommand('Clear', self.Clear)
        view.SetButtonCommand('Save', self.Save)

    def LoadFromClipboard(self):
        img = ImageUtil.GetStatusView(ImageGrab.grabclipboard())
        if not img is None:
            self.Images.append(img)
            self.Image = ImageUtil.GetOrganizedStatus(self.Images)
            self.View.SetPreviewImage(self.Image)

    def Clear(self):
        self.Images = []
        self.View.SetPreviewImage(None)

    def Save(self):
        self.Image.save(datetime.datetime.now().strftime('../Output/%Y%m%d_%H%M%S.png'))
