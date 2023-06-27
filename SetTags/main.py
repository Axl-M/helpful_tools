"""
Замена тегов в аудиофайлах
можно увидеть в експлорере столбцы: название, исполнители, альбом .....
"""
import os
import eyed3

FIND_DIRECTORY = 'Test'


def walk(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            set_tags(os.path.join(root, name))


def set_tags(file):
    print(file)
    # получить имя файла без расширения
    name = os.path.basename(file).split('.')[0]
    print(name)
    audiofile = eyed3.load(file)
    # если тег отсутствует - нужно ИНИЦИАЛИЗИРВАТЬ
    if not audiofile.tag:
        audiofile.initTag()
    # audiofile.tag.title = 'моё Название'
    audiofile.tag.title = name
    #  если им альбома не указано
    if not audiofile.tag.album:
        audiofile.tag.album = 'Other'

    # audiofile.tag.title = "The edge"
    audiofile.tag.save()


if __name__ == '__main__':
    walk(FIND_DIRECTORY)

