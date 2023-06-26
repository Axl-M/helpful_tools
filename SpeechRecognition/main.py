"""
Распознование речи
Транскрибаци аудио-файла в текст
"""
import speech_recognition as sr

FILE = 'audio.wav'

r = sr.Recognizer()
with sr.AudioFile(FILE) as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio, language='ru-RU')
    print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == "__main__":
    ...