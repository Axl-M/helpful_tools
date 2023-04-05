from pathlib import Path
# import sys

'''
path = Path('X:\ТЕСТОВЫЙ')
print(path)    # полный путь   X:\ТЕСТОВЫЙ
print(path.name)   # только имя    ТЕСТОВЫЙ

folders = path.iterdir()    # генератор всех папок с полными путями
for i in folders:
    print(i)

# Определите, является ли path файлом
print(path.is_file())

# Определите, является ли path каталогом
print(path.is_dir())
'''

class DirectoryTree(object):
    """
    Создает дерево каталогов
    путь: целевой каталог
    filename: им файла для сохранения
    """

    def __init__(self, path='.', filename='_tree.txt'):
        super(DirectoryTree, self).__init__()
        self.path = Path(path)
        self.filename = filename
        self.tree = ''

    # def set_path(self, path):
    #     self.path = Path(path)
    #
    # def set_filename(self, filename):
    #     self.filename = filename


    def generate_tree(self, n=0):
        if self.path.is_file():
            self.tree += '    |' * n + '-' * 4 + self.path.name + '\n'
        elif self.path.is_dir():
            self.tree += '    |' * n + '-' * 4 + '[' + str(self.path.relative_to(self.path.parent)) + ']' + '\\' + '\n'
            for folder in self.path.iterdir():
                self.path = Path(folder)
                self.generate_tree( n + 1)
        # return tree_str

    def save_to_file(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(self.tree)

path = Path('X:\ТЕСТОВЫЙ')
file_out = str(path) + '\_tree.txt'
if __name__ == '__main__':
    dir_tree = DirectoryTree(path=path, filename=file_out)
    dir_tree.generate_tree()
    print(dir_tree.tree)
    dir_tree.save_to_file()




# __name__ == '__main__':
#     dirtree = DirectionTree()
#     # Количество параметров команды равно 1, и создается дерево каталогов текущего каталога
#     if len(sys.argv) == 1:
#         dirtree.set_path(Path.cwd())
#         dirtree.generate_tree()
#         print(dirtree.tree)
#     # Количество параметров команды 2 и каталог существует
#     elif len(sys.argv) == 2 and Path(sys.argv[1]).exists():
#         dirtree.set_path(sys.argv[1])
#         dirtree.generate_tree()
#         print(dirtree.tree)
#     # Количество параметров команды 3 и каталог существует
#     elif len(sys.argv) == 3 and Path(sys.argv[1]).exists():
#         dirtree.set_path(sys.argv[1])
#         dirtree.generate_tree()
#         dirtree.set_filename(sys.argv[2])
#         dirtree.save_file()
#     else:  # Слишком много параметров для анализа
#         print(«Слишком много параметров командной строки, проверьте! ')

'''
python dirtree.py 
Распечатать дерево каталогов текущего каталога;

python dirtree.py E:\Programming\Python\applications
Распечатать дерево каталогов указанного каталога;

python dirtree.py E:\Programming\Python\applications dirtree.txt
Распечатать дерево каталогов указанного каталога и сохранить его как файл.
'''