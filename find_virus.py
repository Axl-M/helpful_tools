"""
Ищет вновьсозданные файлы на хостинге
вероятно являются вредоносными
которые закинули злоумышленики после взлома вашего сайта
"""
import os
import time

# где искать
CHECK_DIRECTORY = r"D:\test"
# журнал со списком подозрительных файлов
FILE_LOG = r"D:\test\Test\find_virus\log.txt"
# временной ограничитель - день назад
TIME_BORDER = 86400


def find_virus(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            # если файл менялся
            if check_file(file_path):
                print(file_path)



def check_file(file):
    current_ts = time.time()
    print(current_ts)
    change_time = get_change_time(file)
    print(change_time)

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



if __name__ == '__main__':
    find_virus(CHECK_DIRECTORY)