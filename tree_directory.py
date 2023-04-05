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


tree_str = ''

def generate_tree(path, n=0):
    global tree_str
    if path.is_file():
        tree_str += '    |' * n + '-' * 4 + path.name + '\n'
    elif path.is_dir():
        tree_str += '    |' * n + '-' * 4 + '[' + str(path.relative_to(path.parent)) + ']' + '\\' + '\n'
        for folder in path.iterdir():
            generate_tree(folder, n + 1)
    return tree_str

def save_to_file(tree, file_out):
    with open(file_out, 'w', encoding='utf-8') as f:
        f.write(tree)

path = Path('X:\ТЕСТОВЫЙ')
file_out = str(path) + '\_tree.txt'
if __name__ == '__main__':
    tree = generate_tree(path)
    print(tree_str)
    save_to_file(tree, file_out)

#
# if __name__ == '__main__':
#         # Количество параметров команды 2 и каталог существует
#     if len(sys.argv) == 2 and Path(sys.argv[1]).exists():
#         generate_tree(Path(sys.argv[1]), 0)
#     # Количество параметров команды 3 и каталог существует
#     if len(sys.argv) == 3 and Path(sys.argv[1]).exists():
#         generate_tree(Path(sys.argv[1]), 0)
#         save_file(tree_str, sys.argv[2])
#     else:  # Текущий путь
#         generate_tree(Path.cwd(), 0)
#     print(tree_str)