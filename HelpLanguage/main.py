"""
Морфологический анализатор - приводит слово к нормальной форме.

"""
import os
import re
# Анализ текста на часто используемые слова (со 2-й версией проблемы)
import pymorphy3


FIND_DIRECTORY = 'Test'

morph = pymorphy3.MorphAnalyzer()

def walk(directory):
    """
    получить содержимое каждого файла в искомой директории
    :param directory:
    :return:
    """
    for root, dirs, files in os.walk(directory):
        for name in files:
            file = os.path.join(root, name)
            with open(file, encoding='utf-8') as f:
                analysis(f.read())
            # print(file)


def analysis(content):
    frequency = {}
    # получить список слов
    # найти слова начинающиеся с любой из букв русского алфавита, состоящие минимум из одной буквы (+)
    matches = re.findall(r'\b[а-я]+\b', content, re.IGNORECASE)  # \b - граница слова
    # print(content)
    for word in matches:
        word = word.lower()
        # получить нормальную форму слова (именительный падеж, единственное число ....)
        word = morph.parse(word)[0].normal_form
        # word = morph.parse(word)[0].normal_form
        # print(morph.parse(word)[0].normal_form)
        # получить количество для слова, если его еще нет присвоить количеству 0
        count = frequency.get(word, 0)
        # Записать в словарь количество дл каждого слова увеличив его на 1
        frequency[word] = count + 1
    print(frequency)


if __name__ == '__main__':
    walk(FIND_DIRECTORY)

