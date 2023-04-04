# Сохранить в файл
# имя каждого раздела (папки) и его содержимое
# отобразить глубину вложенности отступами

import os

def print_directory_contents(path, depth):
    # проход по всем папкам и файлам в заданной директории и ее поддиректорих
    for root, dirs, files in os.walk(path):
        # вывести название раздела
        f.write(f"\n{' ' * depth} - {os.path.basename(root)}\n")
        # вывод содержимого раздела
        for file in files:
            f.write(f"{' ' * (depth + 3)}{file}\n")

        # рекурсивно вызвать функцию для каждой подпапки с увеличенной глубиной на 2
        for subdir in dirs:
            print_directory_contents(os.path.join(root, subdir), depth + 2)




path = r'X:\fleshka'
output = path + '/_file_list.txt'

with open(output, 'w') as f:
    print_directory_contents(path, 0)

print("===> Завершено.")