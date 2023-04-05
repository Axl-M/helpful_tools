# пишет в файл `output.txt` имена всех папок и файлов в указанной директории и ее вложенных поддиректориях
# до указанной глубины. При этом каждый разделитель между папками/файлами будет отступ (2 пробела) для наглядности.

import os
import tkinter as tk
import tkinter.filedialog

root = tk.Tk()
root.title('File explorer   -=-    by Axl-M')
root.geometry("500x200")


# Чтобы выбрать папку, в которой будет проводится поиск, добавим кнопку "Browse" и окно для вывода директории:


folder_path = ''

label_folder = tk.Label(root, text='Выберите папку: ')
label_folder.pack()

frame_folder = tk.Frame(root)
frame_folder.pack()

entry_folder = tk.Entry(frame_folder, textvariable=tk.StringVar(value=os.getcwd()))
entry_folder.pack(side=tk.LEFT)

def browse_folder():
    global folder_path
    folder_path = tk.filedialog.askdirectory()
    entry_folder.delete(0, tk.END)
    entry_folder.insert(0, folder_path)

button_browse = tk.Button(frame_folder, text='Выбрать', command=browse_folder)
button_browse.pack(side=tk.LEFT)

label_depth = tk.Label(root, text='Глубина: ')
label_depth.pack()

intvar_depth = tk.IntVar(value=0)
spin_depth = tk.Spinbox(root, from_=0, to=10, textvariable=intvar_depth)
spin_depth.pack()


# Далее создадим функцию для обхода файлов и папок и записи их имен в файл:


def walk_directory(path, depth, file):
    """
    Функция рекурсивно обходит директории и записывает имена файлов и папок в файл

    :param path: путь к директории
    :param depth: глубина рекурсии
    :param file: файл, в который записываются имена файлов и папок
    """
    if depth == 0:
        print(os.path.basename(path) + '\n')
        file.write(os.path.basename(path) + '\n')
        return
    else:

        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print('=', entry.name)
                    path = os.path.join(path, entry)
                    walk_directory(path, depth-1, file)
                    # print('|- ' + entry.name)
                    # # file.write('| '*(10 - depth) + '|- ' + entry.name + '\n')
                    # file.write('|- ' + entry.name + '\n')
                    # # walk_directory(entry.path, depth - 1, file)
                elif entry.is_file():
                    file.write('|---- ' + entry.name + '\n')
                    print('|---- '  + entry.name)

        # folders = []
        # files = []
        # for entry in sorted(os.scandir(path), key=lambda entry: entry.name):
        #     if entry.is_dir():
        #         folders.append(entry)
        #         # print('|- ' + entry.name)
        #     else:
        #         files.append(entry)
        #         # print('|---- ' + entry.name)
        #
        #
        # print(f"Папки в директории {path}:")
        # for folder in folders:
        #     print(folder.name)
        #
        # print(f"\nФайлы в директории {path}:")
        # for file in files:
        #     print(file.name)

# И наконец, функцию для вывода имен файлов и папок:

def show_directory():
    global folder_path
    folder_path = entry_folder.get()
    depth = intvar_depth.get()
    with open(folder_path + r'\file_explorer.txt', 'w') as file:
        walk_directory(folder_path, depth, file)
    # tk.messagebox.showinfo('File explorer', 'Done')
    print("===> [Выполнено]")

# Теперь добавим кнопку для вывода имен файлов и папок и запустим приложение:


button_show = tk.Button(root, text='Выполнить', command=show_directory)
button_show.pack()

root.mainloop()




#
# import tkinter as tk
# import tkinter.filedialog
# import os
#
# def print_directory_contents(path, depth, file):
#     """
#     Функция выводит содержимое директории и всех ее вложенных поддиректорий до указанной глубины.
#
#     :param path: путь к директории
#     :param depth: глубина рекурсии
#     :param file: объект файла для записи
#     """
#     if depth == 0:  # если глубина рекурсии равна 0, то выводим только имя указанной директории
#         print(os.path.basename(path))
#         file.write('\n===' + os.path.basename(path) + '===\n')
#         return
#     else:
#         print(path)  # выводим путь к текущей директории
#         file.write(path + '\n')
#         for item in os.listdir(path):
#             item_path = os.path.join(path, item)
#             if os.path.isdir(item_path):
#                 print_directory_contents(item_path, depth - 1, file)  # рекурсивно вызываем функцию для каждой поддиректории
#
#
# def browse_folder():
#     global folder_path
#     folder_path = tk.filedialog.askdirectory()
#     entry_path.delete(0, tk.END)
#     entry_path.insert(0, folder_path)
#
#
# def run():
#     path = entry_path.get()  # получаем путь к директории из поля ввода
#     depth = int(entry_depth.get())  # получаем глубину вложенности из поля ввода
#     output = path + '\_output.txt'   # итоговый файл будет создан в той же папке
#
#     with open(output, 'w') as file:
#         print_directory_contents(path, depth, file)  # вызываем функцию с указанными параметрами и объектом файла для записи
#     print(os.getcwd())
#
# # создаем окно
# root = tk.Tk()
#
# # элементы интерфейса
# label_by = tk.Label(text="List of files        by AXL-M")
# label_path = tk.Label(text="Путь к папке:")
# entry_path = tk.Entry()
# button_path = tk.Button(text="Выбрать", command=browse_folder)
#
# label_depth = tk.Label(text="Глубина вложенности:")
# entry_depth = tk.Entry()
#
# button_run = tk.Button(text="Запустить", command=run)
#
# # размещаем элементы на окне
# label_by.pack()
# label_path.pack()
# entry_path.pack()
# button_path.pack()
#
# label_depth.pack()
# entry_depth.pack()
#
# button_run.pack()
#
# # запускаем графический интерфейс
# root.mainloop()
#
#


# import tkinter as tk
# from tkinter import filedialog
# import os
#
# root = tk.Tk()
#
# def select_folder():
#     folder_path = filedialog.askdirectory()
#     if folder_path:
#         path_var.set(folder_path)
#
# def print_directory_contents(path, depth):
#     if depth == 0:
#         output_file.write(os.path.basename(path) + '\n')
#         return
#     else:
#         output_file.write(path + '\n')
#         for item in os.listdir(path):
#             item_path = os.path.join(path, item)
#             if os.path.isdir(item_path):
#                 print_directory_contents(item_path, depth - 1)
#
# def process_directory():
#     folder_path = path_var.get()
#     if not folder_path:
#         return
#     try:
#         depth = int(depth_var.get())
#     except ValueError:
#         return
#     output_filename = output_var.get()
#     if not output_filename:
#         return
#     with open(output_filename, 'w') as output_file:
#         print_directory_contents(folder_path, depth)
#
#
# path_var = tk.StringVar()
# depth_var = tk.StringVar()
# output_var = tk.StringVar()
#
# tk.Label(root, text="Folder:").grid(row=0, column=0)
# tk.Entry(root, textvariable=path_var).grid(row=0, column=1)
# tk.Button(root, text="Select", command=select_folder).grid(row=0, column=2)
# tk.Label(root, text="Depth:").grid(row=1, column=0)
# tk.Entry(root, textvariable=depth_var).grid(row=1, column=1)
# tk.Label(root, text="Output file:").grid(row=2, column=0)
# tk.Entry(root, textvariable=output_var).grid(row=2, column=1)
# tk.Button(root, text="Process", command=process_directory).grid(row=3, columnspan=3)
#
# root.mainloop()
#


# import os
#
# def print_directory_contents(path, depth, output_file):
#     """
#     Функция записывает имя текущей директории и ее содержимое,
#     а также содержимое всех вложенных поддиректорий до указанной глубины в файл.
#
#     :param path: путь к директории
#     :param depth: глубина рекурсии
#     :param output_file: путь к файлу, в который будут записаны результаты
#     """
#     if depth == 0:  # если глубина рекурсии равна 0, то записываем только имя текущей директории
#         with open(output_file, 'a') as f:
#             f.write(os.path.basename(path) + '\n')
#         return
#     else:
#         # записываем имя текущей директории
#         with open(output_file, 'a') as f:
#             f.write(os.path.basename(path) + '\n')
#
#         for item in os.listdir(path):
#             item_path = os.path.join(path, item)
#             if os.path.isdir(item_path):
#                 # рекурсивно вызываем функцию для каждой поддиректории с глубиной на 1 меньше
#                 print_directory_contents(item_path, depth - 1, output_file)
#             else:
#                 # записываем содержимое файла в текущей директории
#                 with open(output_file, 'a') as f:
#                     f.write('  ' + item + '\n')
#
#
# path = '.'  # указываем путь к директории
# depth = 2  # указываем глубину рекурсии
# output_file = 'output.txt'  # указываем путь к файлу для записи результатов
#
# print_directory_contents(path, depth, output_file)  # вызываем функцию