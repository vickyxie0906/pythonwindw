
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        bg1Image=Image.open("bg1.jpg")
        self.tkImage=ImageTk.PhotoImage(bg1Image)
        mainCanvas=tk.Canvas(self,width=800,height=534)
        mainCanvas.create_image(0,0,anchor=tk.NW,image=self.tkImage)
        mainCanvas.pack(fill=tk.BOTH, expand=True)

        helv28 = tkFont.Font(family="Helvetica", size=28, weight="bold")
        tk.Label(mainCanvas, text="Blue Sky", font=helv28,
                 background="#f0f8ff", foreground="#0000ff").place(x=330, y=50)


    

def main():
    window=Window()
    window.title("Blue Sky")
    window.resizable(0,0)
    window.geometry("800x534+550+50")
    window.mainloop()



if __name__ == "__main__":
    main()
