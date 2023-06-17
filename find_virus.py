"""
Ищет вновьсозданные файлы на хостинге
вероятно являются вредоносными
которые закинули злоумышленики после взлома вашего сайта
записать в cron для запуска ежедневно
"""
import os
import sys
import time
from datetime import datetime

# где искать по умолчанию (если путь к папке не передали аргументом)
CHECK_DIRECTORY = r"D:\test"
# журнал со списком подозрительных файлов
FILE_LOG = r"D:\test\find_virus\log.txt"
# временной ограничитель - день назад
TIME_BORDER = 86400
DATE_FORMAT = '%d.%m.%Y %H:%M'


def find_virus(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            # если файл менялся
            if check_file(file_path):
                # print(file_path)
                add_to_log(file_path)


def clear_log(FILE_LOG):
    with open(FILE_LOG, 'w') as f:
        print('Журнал очищен')


def check_file(file):
    """
    былл ли файл создан в пределах ограниченного константой промежутка времени
    :param file:
    :return:
    """
    current_ts = time.time()
    # print(current_ts)
    change_time = get_change_time(file)
    # print(change_time)
    return current_ts - change_time < TIME_BORDER

def get_change_time(file):
    """
    возвращает время когда файл был изменен или создан
    :param file:
    :return:
    """
    m_time = os.stat(file).st_mtime
    a_time = os.stat(file).st_atime
    c_time = os.stat(file).st_ctime
    return max(m_time, a_time, c_time)

def add_to_log(file):
    """
    добавляет имя файла в журнал
    и время его создания / изменения
    :param file:
    :return:
    """
    added_string = file + ": " + datetime.fromtimestamp(get_change_time(file)).strftime(DATE_FORMAT) + "\n"
    with open(FILE_LOG, 'a') as f:
        f.write(added_string)



if __name__ == '__main__':
    clear_log(FILE_LOG)
    # проверять ту директорию если она была передана аргументом в командной строке
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        find_virus(directory)
    else:
        find_virus(CHECK_DIRECTORY)