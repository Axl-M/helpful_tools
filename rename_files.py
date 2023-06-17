"""
Переименовать все файлы в директории
согласно нескольким правилам
"""
import os

# директория где находятся файлы для переименования
DIRECTORY = r"D:\test\Test"


def get_file(dir_with_files: str) -> None:
    """
    получить имя каждого файла в дирректории и поддиректориях если они есть
    :param dir_with_files: директория где находятся файлы для переименования
    :return: None
    """
    for root, dirs, files in os.walk(dir_with_files):
        for file_name in files:
            rename_file(root, file_name)


def rename_file(root: str, file_name: str):
    """
    переименовывает файлы
    :param root: директория где находятся файлы
    :param file_name: имя файла
    :return:
    """
    valid_name = get_valid_name(file_name)
    old_file = os.path.join(root, file_name)
    new_file = os.path.join(root, valid_name)
    os.rename(old_file, new_file)


def get_valid_name(name: str) -> str:
    """
    функция с правилами для переименования
    :param name: имя файла
    :return:
    """
    name = name.replace("_Diff.", "_BC.")
    name = name.replace("_Diffuse.", "_BC.")
    name = name.replace("_Normal.", "_N.")
    name = name.replace("_ORM.", "_AORM.")
    name = name.replace("_O.", "_A.")
    if not name.startswith("T_"):
        name = "T_" + name
    return name



if __name__ == '__main__':
    get_file(DIRECTORY)
