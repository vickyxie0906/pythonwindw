import tkinter as tk  # 引入 tkinter 圖形化工具標準模組
from PIL import Image, ImageTk  # PIL影像處理套件 Tk k小寫
import tkinter.font as tkFont#控制字體大小樣式

class ImageButton(tk.Button):
    def __init__(self,parents,**kwargs):#打包
        super().__init__(parents, **kwargs)#解包裝
        bgImage1 = Image.open("btn1.png")  # 讀取圖片檔
        self.tkImage1 = ImageTk.PhotoImage(bgImage1)
        self.config(image=self.tkImage1,borderwidth=0)




class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #---------建立背景-------
        bgImage = Image.open("bg.jpg")
        self.tkImage = ImageTk.PhotoImage(bgImage)

        mainCanvas = tk.Canvas(self, width=640, height=427)
        mainCanvas.create_image(
            0, 0, anchor=tk.NW, image=self.tkImage)  # self.tkImage要加self否則圖片會消失
        mainCanvas.pack(fill=tk.BOTH, expand=True)
        #---------建立背景end-------

        #---------建立Label-------
        helv36=tkFont.Font(family="Helvetica",size=28,weight="bold")
        tk.Label(mainCanvas, text="職能發展學院",font=helv36, background="#C9C8CD", foreground="#888888").place(x=370, y=50)

        #---------End建立Label-------

        #---------建立ButtonsFrame-------
        buttonFrame=tk.Frame(mainCanvas,width=130,height=300,background="#ffffff")
        buttonFrame.place(x=100,y=50)

        #---------End建立ButtonsFrame-------

        #---------建立Button-------
        
        btn1 = ImageButton(buttonFrame,command=self.btn1Click)
        btn1.pack()

        btn2 = ImageButton(buttonFrame,borderwidth=0)
        btn2.pack()

        #---------End建立Button-------
    def btn1Click(self0):
        print("userClick")

    

        
        
        #tk.Button(mainCanvas, text="click").pack

        # btnbgimage = Image.open('down.png').resize(
        #     (22, 22), Image.ANTIALIAS)  # resize設定大小
        # self.tkbtnbgImage = ImageTk.PhotoImage(btnbgimage)
        # tk.Button(mainCanvas, text="click",
        #           image=self.tkbtnbgImage, compound=tk.TOP,).pack()

        #tk.Entry(mainCanvas, width=20).pack()


def main():
    window = Window()#繼承Window的設定
    window.title("Frame框架")#設定視窗標題
    window.resizable(0,0)#(0,0)可以使滑鼠無法改變視窗大小
    window.geometry("640x427+650+250")  # (設定視窗大小x,視窗顯示螢幕地方+)
    window.mainloop()#運行視窗主程式


if __name__ == "__main__":
    main()
