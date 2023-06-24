"""
Парсинг Excel файла
Вывести минимальный и максимальный расход
"""

import xlrd3 as xlrd

FILE = "Test.xls"

def parsing(file):
    """
    пример парсинга
    :param file:
    :return:
    """
    book = xlrd.open_workbook(file)
    sh = book.sheet_by_index(0)
    print(sh)
    # вывести содержимое каждой ячейки
    for row_number in range(sh.nrows):
        for col_number in range(sh.ncols):
            print(sh.cell_value(rowx=row_number, colx=col_number))


def do(file):
    articles = []
    expenses = []
    book = xlrd.open_workbook(file)
    sh = book.sheet_by_index(0)
    for row_number in range(sh.nrows):
        # возвращает массив/список содержимого столбцов
        row = sh.row_values(row_number)
        # вывести только те строки где СТАТЬЯ РАСХОДА и СУММА (исключить заголовки таблицы и ИТОГО)
        if row[1]:  # если есть 2-й столбец
            # исключить последнюю строку ИТОГО, и те где 2-й столбец не число
            if row[0] != 'Итого:' and isinstance(row[1], float):
                # print(row)
                articles.append(row[0])
                expenses.append(row[1])

    print_result(articles, expenses)


def print_result(articles, expenses):
    # print(articles)
    # print(expenses)
    index_min = get_extreme_key(expenses, min)
    index_max = get_extreme_key(expenses, max)
    print('Минимальный расход:')
    print('Статья:', articles[index_min], '\n',  'Сумма:', expenses[index_min], 'руб.')
    print('-' * 20)
    print('Максимальный расход:')
    print('Статья:', articles[index_max], '\n',  'Сумма:', expenses[index_max], 'руб.')


def get_extreme_key(array, compare):
    extreme_index = 0
    extreme = array[0]
    i = 1
    while i < len(array):
        if compare(array[i], extreme) == array[i]:  # array[i] > extreme
            extreme = array[i]
            extreme_index = i
        i += 1

    return extreme_index




if __name__ == "__main__":
    do(FILE)