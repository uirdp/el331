# こっちはtkinterでウィンドウを表示させるのがいいかも
import tkinter as tk
import re

def text_dump(text):
    root = tk.Tk()
    root.geometry('500x500')

    label = tk.Label(root, text=text)
    label.pack()

    root.mainloop()


def text_dump_with_keyword(substrings, keyword):
    root = tk.Tk()
    root.geometry('500x500')
    root.title("Text Highlight")

    text_widget = tk.Text(root, wrap='word')
    text_widget.pack(expand=1, fill='both')

    # Configure tags
    text_widget.tag_configure("highlight", foreground="red")
    text_widget.tag_configure("normal", foreground="black")

    pattern = re.compile(keyword)
    print(pattern)

    for word in substrings:
        start_idx = 0

        match = pattern.fullmatch(word)
        start_idx += 1
        if match is None:
            text_widget.insert(tk.END, word + ' ', "normal")

        if match :
            text_widget.insert(tk.END, word + ' ', "highlight")

            print("match: " + word[match.start():match.end()])
            #text_widget.insert(tk.END, word[match.start():match.end()], "highlight")

        text_widget.insert(tk.END, "")  # Add a newline between different substrings

    root.mainloop()


def search_token(text: str, key: str):
    # Split into lists
    words = re.findall(r'\w+|[.,]', text)

    # Find all indices of the keyword
    indices = [i for i, word in enumerate(words) if word == key]

    if not indices:
        print(f"Keyword '{key}' not found in text.")
        return

    substrs = []
    for ind in indices:
        # 5 words before the keyword
        start = max(0, ind - 5)

        # 5 words after the keyword
        end = min(len(words), ind + 6)  # ind + 6 to include the keyword

        # Extract the relevant portion
        substr_words = words[start:end]

        # Reconstruct the string with proper spaces
        substr = ""
        for word in substr_words:
            if word in [",", "."]:
                substr = substr.rstrip() + word
            else:
                substr += " " + word

        substrs.append(substr.lstrip())  # Remove leading space

        print(substrs)
        text_dump_with_keyword(substr_words, key)