"""
Замена тегов в аудиофайлах

"""
import os
import eyed3

FIND_DIRECTORY = 'Test'


def walk(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            set_tags(os.path.join(root, name))


def set_tags(file):
    # print(file)
    audiofile = eyed3.load(file)
    audiofile.tag.title = "The edge"
    audiofile.tag.save()


if __name__ == '__main__':
    walk(FIND_DIRECTORY)

