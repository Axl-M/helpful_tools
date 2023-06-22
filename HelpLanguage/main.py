"""
Анализирует тексты во всех файлах в указанной директории
и выводит отчет о частотности для каждого слова (в порядке убывания)

Морфологический анализатор - приводит каждое слово к нормальной форме.

Можно использовать для составления списка слов необходимых для изучения
иностранного языка исходя из частоты использования данных слов

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
    frequency = {}
    for root, dirs, files in os.walk(directory):
        for name in files:
            file = os.path.join(root, name)
            with open(file, encoding='utf-8') as f:
                # получить анализ частотности для данного файла
                new_frequency = analysis(f.read())

            # объединить анализы частотности в общий словарь
            for word in new_frequency:
                count = frequency.get(word, 0)
                frequency[word] = count + new_frequency.get(word)

    print_result(frequency)


def analysis(content: str) -> dict:
    """
    :param content: Содержимое файла (текст)
    :return: Возвращает словарь {начальна форма слова: количество вхождений этого слова в тексте}
    """
    frequency = {}
    # получить список слов где каждое
    # найденное слово начинается с любой из букв русского алфавита, состоящие минимум из одной буквы (+)
    matches = re.findall(r'\b[а-я]+\b', content, re.IGNORECASE)  # \b - граница слова
    # print(content)
    for word in matches:
        word = word.lower()
        # получить нормальную форму слова (именительный падеж, единственное число ....)
        word = morph.parse(word)[0].normal_form
        # получить количество для слова, если его еще нет присвоить количеству 0
        count = frequency.get(word, 0)
        # Записать в словарь количество дл каждого слова увеличив его на 1
        frequency[word] = count + 1
    return frequency


def print_result(frequency: dict) -> None:
    """
    вывести содержимое словаря построчно
    :param frequency:
    :return:
    """
    frequency = sort(frequency)  # остортировать содержимое словаря
    # print(frequency)
    for word in frequency:
        print(f'{word} -- {frequency[word]}')


def sort(dictionary: dict) -> dict:
    """
    отсортировать словарь по частотности значений
    :param dictionary: словарь для сортировки
    :return: отсортированный по значениям словарь (в порядке убывания)
    """
    sorted_dict = {}
    sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)
    for key in sorted_keys:
        sorted_dict[key] = dictionary[key]
    return sorted_dict


if __name__ == '__main__':
    walk(FIND_DIRECTORY)
