
import os

def print_directory_contents(path, depth):
    """
    Вывод содержимого директории и всех ее вложенных поддиректорий
    до указанной глубины вложенности
    :param path: путь к директории
    :param depth: глубина рекурсии
    :return:
    """
    # если глубина=0, выводить только имя директории
    if depth == 0:
        print(os.path.basename(path))
        return
    else:
        # вывести путь к текущей директории
        print(path)
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                # рекурсивно вызвать ф-цию для каждой поддиректории
                print_directory_contents(item_path, depth - 1)

# путь к директории
path = r'X:\fleshka'

# глубина рекурсии
# если = 0, выводит только имя директории и выходит из ф-ции
# если = 1, выводит только имена подпапок (ффалы в этой папке не выводятся)
# если > 1, выводит путь к текущей директории, а затем дл каждого вложенного элемента,
# если он является поддиректорией рекурсивно вызываем ту же функцию и уменьшаем глубину рекурсии
depth = 2

print_directory_contents(path, depth)