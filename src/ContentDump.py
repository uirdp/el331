# こっちはtkinterでウィンドウを表示させるのがいいかも
import tkinter as tk
import re

def text_dump(text):
    root = tk.Tk()
    root.geometry('500x500')

    label = tk.Label(root, text=text)
    label.pack()

    root.mainloop()


def text_dump_with_keyword(text, keyword):
    root = tk.Tk()
    root.geometry('500x500')
    root.title("Text Highlight")

    text_widget = tk.Text(root, wrap='word')
    text_widget.pack(expand=1, fill='both')

    # Configure tags
    text_widget.tag_configure("highlight", foreground="red")
    text_widget.tag_configure("normal", foreground="black")

    # Insert text with appropriate tags
    start_idx = 0
    while start_idx < len(text):
        # Find the next occurrence of the keyword
        keyword_idx = text.find(keyword, start_idx)

        if keyword_idx == -1:
            # Insert the rest of the text as normal
            text_widget.insert(tk.END, text[start_idx:], "normal")
            break

        # Insert the text before the keyword
        if start_idx != keyword_idx:
            text_widget.insert(tk.END, text[start_idx:keyword_idx], "normal")

        # Insert the keyword with the highlight tag
        end_idx = keyword_idx + len(keyword)
        text_widget.insert(tk.END, text[keyword_idx:end_idx], "highlight")

        # Update the start index
        start_idx = end_idx

    root.mainloop()

def search_token(text : str, key):
    words = re.findall(r'\w+|[.,]', text)
    ind = words.index(key)

    start = max(0, ind - 10)

    # 20 words after the keyword
    end = min(len(words), ind + 11)

    substr_words = words[start:end]

    substr = ""
    for word in substr_words:
        if word in [",", "."]:
            substr = substr.rstrip() + word
        else:
            substr += " " + word

    substr = substr.lstrip()  # Remove leading space
    print(substr)

    text_dump_with_keyword(substr, key)
    return substr
