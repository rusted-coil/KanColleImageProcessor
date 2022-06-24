from MainView import MainView
from MainController import MainController

class Window:
    def __init__(self, master=None):
        # Window設定
        master.title('KanColle ImageProcessor')
        master.geometry('1280x720')

        # MainViewを作成
        view = MainView(master)

        # MainControllerを作成
        controller = MainController(view)
        
if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
