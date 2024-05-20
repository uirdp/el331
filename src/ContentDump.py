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

    # Use regex to find whole word matches only
    pattern = re.compile(r'\b' + re.escape(keyword) + r'\b')

    start_idx = 0
    while start_idx < len(text):
        match = pattern.search(text, start_idx)

        if not match:
            # Insert the rest of the text as normal
            text_widget.insert(tk.END, text[start_idx:], "normal")
            break

        # Insert the text before the keyword
        text_widget.insert(tk.END, text[start_idx:match.start()], "normal")

        # Insert the keyword with the highlight tag
        text_widget.insert(tk.END, text[match.start():match.end()], "highlight")

        # Update the start index
        start_idx = match.end()

    root.mainloop()


def search_token(text: str, key: str):
    # Split into lists
    words = re.findall(r'\w+|[.,]', text)

    # Find the index of the keyword
    if key not in words:
        print(f"Keyword '{key}' not found in text.")
        return

    ind = words.index(key)

    # 20 words before the keyword
    start = max(0, ind - 20)

    # 20 words after the keyword
    end = min(len(words), ind + 21)  # ind + 21 to include the keyword

    # Extract the relevant portion
    substr_words = words[start:end]

    # Reconstruct the string with proper spaces
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