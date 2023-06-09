
import os

def get_files_list(path):
    """
    Возвращает в файл список всех файлов и подкаталогов данного каталога
    с полными путями.
    :param path: путь, к каталогу для которого создать список
    :return: список_файлов
    """
    files_list = []

    # для каждого подкаталога и файла
    for file in os.listdir(path):
        # print(file)
        file_path = os.path.join(path, file)
        # для получения содержимого подкаталога используем рекурсию
        if os.path.isdir(file_path):
            files_list += get_files_list(file_path)
        else:
            files_list.append(file_path)

    return files_list


def write_to_file(files_list):
    """
    Сохраняет в файл переданный список
    :param files_list: список_фалов для сохранения
    :return: None
    """
    with open(path + '\_files_list.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(files_list))


path = "X:\ТЕСТОВЫЙ"
files_list = get_files_list(path)
write_to_file(files_list)