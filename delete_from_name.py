# Пройтись по всем файлам в каталоге и его подкаталогах
# и удалить указанную часть из имени файлов.
# Папки не переименовывает !!!

import os

# folder_path = 'my_folder'
# sub_name = '_old'

folder_path = 'X:\=НОВОЕ=\=Pro-14 способов заработка на своем сайте (2023) _[Юлия Литвина] — копия'
sub_name = '[S1.SLIV.ONE] '

for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        # проверем что файл содержит указанную подстроку
        if sub_name in filename:
            # получить полный путь к файлу
            file_path = os.path.join(dirpath, filename)
            # удалем подстроку из имени файла
            new_filename = filename.replace(sub_name, "")
            new_file_path = os.path.join(dirpath, new_filename)
            # переименовывание файла
            os.rename(file_path, new_file_path)
            print((f" Файл {file_path} переименован в {new_file_path}"))