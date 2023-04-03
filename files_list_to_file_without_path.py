# Сохранить в файл ТОЛЬКО имена фалов каталога и его подкаталогов
# в папке 1-го уровня находятся:
#     подпапки (разделы)
# вывести имя каждого раздела и его содержимое


import os

path = "X:\=НОВОЕ=\=Pro-14 способов заработка на своем сайте (2023) _[Юлия Литвина] — копия"
# path = "c:/path/to/dir"

with open(path + '/_files_list.txt', 'w', encoding='utf-8') as f:
    # root - путь до текущей директории
    # dirs - список подпапок этой директории
    # files - список файлов
    for root, dirs, files in os.walk(path):
        print('\nroot: ', root)
        print('dirs: ', dirs)
        print('files: ', files)
        # Выводим имя раздела
        f.write(f'\n==={os.path.basename(root)}===\n')  # basename - только имя директории (без пути к ней)
        print('basename: ', os.path.basename(root))
        # Выводим содержимое раздела
        for dir in dirs:
            print(dir)
            f.write(dir)
            f.write('\n')
        for file in files:
            print(file)
            f.write(file)
            f.write('\n')

print('\n========> [ Завершено ]')
