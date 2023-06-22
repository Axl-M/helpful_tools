"""
Ищет строку по всем файлам
И выводит результат (список файлов где она содержится)
Выводит контекст, где эта строка встречается.
"""
import os

DIRECTORY = r'C:\Users\Axl\Projects\Python\Poleznoe\Test'
FIND_STRING = 'обеспече'
# для вывода вхождения. Сколько символов до и после искомой строки показывать
COUNT_ADDED_SYMBOLS = 10
RED = "\x1b[31;1m"
GREEN = "\x1b[32;1m"
CANCEL = "\x1b[0m"


def find(find_dir, find_string):
    for root, dirs, files in os.walk(find_dir):
        for name in files:
            find_string_in_files(os.path.join(root, name), find_string)


def find_string_in_files(file, find_string):
    with open(file, encoding='utf-8') as f:
        content = f.read()
    # print(content)
    index = content.find(find_string)
    if index != -1:
        print_find_info(file, content, find_string, index)


def print_find_info(file, content, find_string, index):
    start_index = index - COUNT_ADDED_SYMBOLS if index >= COUNT_ADDED_SYMBOLS else 0
    end_index = index + len(find_string) + COUNT_ADDED_SYMBOLS
    content = content[start_index:end_index]
    # Выделить цветом вхождение (в уже сформированной строке. Иначе обрезаются управляющие символы)
    content = content.replace(find_string, RED + find_string + CANCEL)
    print(f"{file}:\n {content}")



if __name__ == '__main__':
    """
    30 + (0-черный, 1-красный, 2-зеленый, 3-желтый, 4-синий, 5-магента, 6-циан, 7-белый
    40 + (для бэкграунда)
    1m - жирный
    """
    # print("\x1b[31;1m")  # красный жирный
    # print("\x1b[0m")  # сбросить все атрибуты

    find(DIRECTORY, FIND_STRING)

