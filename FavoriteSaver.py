
import tkinter as tk
from tkinter.simpledialog import askstring
import webbrowser

class FavoriteSaverUI:
    def __init__(self, root):
        self.root = root
        root.title("즐겨찾기 저장소")

        self.label = tk.Label(root, text="Open URLs")
        self.label.pack()

        self.listbox = tk.Listbox(root)
        self.listbox.pack()

        self.add_button = tk.Button(root, text="Add URL", command=self.add_url)
        self.add_button.pack()

        self.open_button = tk.Button(root, text="Open URLs", command=self.open_urls)
        self.open_button.pack()

        self.load_urls()

    def add_url(self):
        url = askstring("Add URL", "Enter the URL:")
        if url:
            self.listbox.insert(tk.END, url)
            self.save_urls()

    def open_urls(self):
        urls = list(self.listbox.get(0, tk.END))
        for url in urls:
            try:
                webbrowser.open(url)
            except Exception as e:
                print(f"Error opening URL: {e}")

    def save_urls(self):
        with open("urls.txt", "w") as file:
            urls = self.listbox.get(0, tk.END)
            for url in urls:
                file.write(url + "\n")

    def load_urls(self):
        try:
            with open("urls.txt", "r") as file:
                urls = file.readlines()
                for url in urls:
                    self.listbox.insert(tk.END, url.strip())
        except FileNotFoundError:
            pass

# Tkinter 애플리케이션 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = FavoriteSaverUI(root)
    root.mainloop()
