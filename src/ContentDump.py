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

    print(substrings)
    pattern = re.compile(keyword)
    print(pattern)

    index = 0
    for word in substrings:
        index += 1

        print(word)
        if(word == "\n"):
            text_widget.insert(tk.END, "\n")
        match = pattern.fullmatch(word)

        if match is None:
            text_widget.insert(tk.END, word + ' ', "normal")

        if match :
            text_widget.insert(tk.END, word + ' ', "highlight")

            print("match: " + word[match.start():match.end()])

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

    print(indices)

    substrs = []
    substr_words = []

    for ind in indices:
        # 5 words before the keyword
        start = max(0, ind - 5)

        # 5 words after the keyword
        end = min(len(words), ind + 6)  # ind + 6 to include the keyword

        # Extract the relevant portion
        substr_words += words[start:end]
        substr_words.append("\n")

        # Reconstruct the string with proper spaces
        substr = ""
        for word in substr_words:
            if word in [",", "."]:
                substr = substr.rstrip() + word
            else:
                substr += " " + word

        # Remove leading space
        substrs.append(substr.lstrip())


    print(substrs)
    text_dump_with_keyword(substr_words, key)