# こっちはtkinterでウィンドウを表示させるのがいいかも
import tkinter as tk


def text_dump(text):
    root = tk.Tk()
    root.geometry('500x500')

    label = tk.Label(root, text=text)
    label.pack()

    root.mainloop()