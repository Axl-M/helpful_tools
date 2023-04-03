import tkinter as tk
from tkinter import filedialog, messagebox
import os

class FileRenamer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("File Renamer")
        self.pack()

        self.label_path = tk.Label(self, text='Выберите папку:')
        self.label_path.pack()
        self.button_select_folder = tk.Button(self, text='Выбрать папку', command=self.select_folder)
        self.button_select_folder.pack()

        self.label_search = tk.Label(self, text='Введите текст который нужно удалить из названий файлов:')
        self.label_search.pack()
        self.entry_search = tk.Entry(self)
        self.entry_search.pack()

        self.label_replace_with = tk.Label(self, text='Введите текст, на который нужно заменить удаленный текст:')
        self.label_replace_with.pack()
        self.entry_replace_with = tk.Entry(self)
        self.entry_replace_with.pack()

        self.button_rename = tk.Button(self, text='Переименовать', command=self.rename_files, state=tk.DISABLED)
        self.button_rename.pack()

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.button_rename.config(state=tk.NORMAL)
            self.folder_path = folder_path

    def rename_files(self):
        search = self.entry_search.get()
        replace_with = self.entry_replace_with.get()

        counter = 0

        for dirname, _, filenames in os.walk(self.folder_path):
            for filename in filenames:
                if search in filename:
                    old_path = os.path.join(dirname, filename)
                    new_path = os.path.join(dirname, filename.replace(search, replace_with))
                    os.rename(old_path, new_path)
                    counter += 1

        messagebox.showinfo("Готово", f"Переименовано {counter} файлов.")

        self.entry_search.delete(0, tk.END)
        self.entry_replace_with.delete(0, tk.END)
        self.button_rename.config(state=tk.DISABLED)

