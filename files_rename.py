# Переименовать все файлы в каталоге.
# Пройтись по всем файлам и подкаталогам в указанном каталоге
# и заменить все вхождения строки 'old_string' на строку 'new_string'
# При этом сохранить структуру каталогов

import os

def rename_files(path, old_substr, new_substr):
    """
    Функция переименования файлов и каталогов в заданном каталоге и его подкаталогах
    :param path: путь к каталогу
    :param old_substr: строка, которую нужно заменить
    :param new_substr: строка, на которую нужно заменить
    :return: None
    """
    for dirpath, dirnames, filenames in os.walk(path):
        # print(dirpath, dirnames, filenames)
        # переименовывание файлов
        for filename in filenames:
            if old_substr in filename:
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, filename.replace(old_substr, new_substr))
                os.rename(old_path, new_path)

        # переименовывание подкаталогов в текущем каталоге
        for dirname in dirnames:
            if old_substr in dirname:
                old_path = os.path.join(dirpath, dirname)
                new_path = os.path.join(dirpath, dirname.replace(old_substr, new_substr))
                os.rename(old_path, new_path)

    print("===> Завершено.")


# rename_files('C:/path/to/dir', 'old_string', 'new_string')

path_to_dir = "X:\=НОВОЕ=\=Pro-14 способов заработка на своем сайте (2023) _[Юлия Литвина] — копия"
old_string = "[S1.SLIV.ONE] "
new_string = ""
rename_files(path_to_dir, old_string, new_string)