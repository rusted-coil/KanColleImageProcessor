from MainView import MainView
from MainController import MainController

class Window:
    def __init__(self, master=None):
        self.Master = master

        # Window設定
        master.title('KanColle ImageProcessor')
        master.geometry('1280x720')

        # MainViewを作成
        self.View = MainView(master)

        # MainControllerを作成
        self.Controller = MainController(self.View)

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
