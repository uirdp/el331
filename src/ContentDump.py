# こっちはtkinterでウィンドウを表示させるのがいいかも
import tkinter as tk


def text_dump(text):
    root = tk.Tk()
    root.geometry('500x500')

    label = tk.Label(root, text=text)
    label.pack()

    root.mainloop()


def search_token(text, key):
    ind = text.find(key)

    start = ind - 10
    if start < 0:
        start = 0

    end = ind + 10
    if end > len(text):
        end = len(text)

    substr = text[start:end]
    text_dump(substr)