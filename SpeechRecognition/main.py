"""
Распознование речи
Транскрибаци аудио-файла в текст
"""
import speech_recognition as sr

FILE = 'audio.wav'

r = sr.Recognizer()
with sr.AudioFile(FILE) as source:
    audio = r.record(source)

# или так (НЕ ДЕЛАТЬ ТАК - файл не закрывается)
# source = sr.AudioFile(FILE).__enter__()
# audio = r.record(source)

try:
    # обязательно указать язык (по умолчанию пытается распознать англ - будет ошибка)
    text = r.recognize_google(audio, language='ru-RU')
    print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


'''
class TestWith:
    # вызывается в начале оператора with
    def __enter__(self):
        print('Вход')
        return 1    # запишется в test

    # выполняется по окончанию with
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Выход')


with TestWith as test:
    print('Выполнение кода внутри with')
    print(test)

'''