import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QPushButton, QLabel, QLineEdit
# from PyQt6.QtCore import Qt
# from PyQt6 import QtWidgets, QtCore

class RemoveTextWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 450, 200)
        self.setWindowTitle('Удаление текста из имён файлов     =by AXL-M=')

        self.select_dir_button = QPushButton('Выбрать каталог', self)
        self.select_dir_button.setGeometry(10, 10, 300, 30)
        self.select_dir_button.clicked.connect(self.select_directory)

        self.remove_text_label = QLabel('Часть имени которую нужно удалить', self)
        self.remove_text_label.setGeometry(10, 50, 300, 20)

        self.remove_text_edit = QLineEdit(self)
        self.remove_text_edit.setGeometry(10, 80, 300, 30)

        self.apply_button = QPushButton('Применить', self)
        self.apply_button.setGeometry(10, 120, 100, 30)
        self.apply_button.clicked.connect(self.remove_text)

        self.cancel_button = QPushButton('Отмена', self)
        self.cancel_button.setGeometry(120, 120, 100, 30)
        self.cancel_button.clicked.connect(self.close)

    def select_directory(self): ##########################################
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # directory = QFileDialog.getExistingDirectory(self, 'Выбор каталога', options=options)

        directory = QFileDialog.getExistingDirectory(parent=None, caption='Выбор каталога')
        if directory:
            self.directory = directory

    def remove_text(self):
        if not hasattr(self, 'directory'):
            QMessageBox.warning(self, 'Ошибка', 'не выбран каталог')
            return

        remove_text = self.remove_text_edit.text()

        if not remove_text:
            QMessageBox.warning(self, 'Ошибка', 'не указана часть имени для удаления')
            return

        counter = 0
        for current_dir, subdirs, files in os.walk(self.directory):
            for file in files:
                if remove_text in file:
                    old_file_path = os.path.join(current_dir, file)
                    new_file_name = file.replace(remove_text, '')
                    new_file_path = os.path.join(current_dir, new_file_name)
                    counter += 1


                    if new_file_name != file:
                        os.rename(old_file_path, new_file_path)
                        print(f'{old_file_path} renamed {new_file_path}')

            for dirname in subdirs:
                if remove_text in dirname:
                    old_path = os.path.join(current_dir, dirname)
                    new_path = os.path.join(current_dir, dirname.replace(remove_text, ''))
                    os.rename(old_path, new_path)
                    print(f'{old_path} renamed {new_path}')
                    counter += 1

        QMessageBox.information(self, 'Успех', f'Часть имени успешно удалена из {counter} файлов')


if __name__ == '__main__':
    app = QApplication([])
    remove_text_window = RemoveTextWindow()
    remove_text_window.show()
    app.exec()


