from pathlib import Path

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
        tree_str += '    |' * n + '-' * 4 + str(path.relative_to(path.parent)) + '\\' + '\n'
        for cp in path.iterdir():
            generate_tree(cp, n + 1)


path = Path('X:\ТЕСТОВЫЙ')
if __name__ == '__main__':
    generate_tree(path)
    print(tree_str)