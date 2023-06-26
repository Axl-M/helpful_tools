"""
Изменить все изображения в папке
Оптимизировать размер текстур
Понизить разрешение изображений
"""
import os

from PIL import Image

DIRECTORY = 'Test'
FROM_EXTENSION = '.jpg'
TO_EXTENSION = '.png'
MAX_SIZE = (1024, 1024)


def walk(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            conversion(os.path.join(root, name))


def conversion(file):
    resize(file)
    name, extension = os.path.splitext(file)
    if extension == FROM_EXTENSION:
        img = Image.open(file)
        img.save(name + TO_EXTENSION)
        os.remove(file)


def resize(file):
    img = Image.open(file)
    # img.thumbnail(MAX_SIZE, Image.ANTIALIAS) # ANTIALIAS - упразднено
    img.thumbnail(MAX_SIZE, Image.LANCZOS)
    img.save(file)


if __name__ == "__main__":
    walk(DIRECTORY)
