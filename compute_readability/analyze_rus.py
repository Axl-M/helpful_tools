# вычисляет индекс удобочитаемости
# по формуле
#  206.835 - 1.015 * (всего слов / к-во предложений) - 84.6 * (слогов / слов)

# ИНДЕКС  УРОВЕНЬ        ПРИМЕЧАНИЕ
# 00-90   5-й класс      Очень легко читается, понятен 1 1 -летнему школьнику
# 90-80   6-й класс      Легко читается, типичный разговорный язык
# 80-70   7-й класс      Относительно легко читается
# 70-60   8-9-й классы   Литературный язык, понятен школьникам 1 3-1 5 лет
# 60-50   1О-11-й классы Относительно тяжело читается
# 50-30   Студент        Тяжело читается
# 30-0    Выпускник вуза Очень тяжело читается, понятен в основном выпускникам вузов

# формула актуальна для русского текста
# import text_eng
import text_rus

def count_syllables(words):
    count = 0
    for word in words:
        # syllables = count_syllables_in_word(word)
        syllables = count_syllables_in_word_rus(word)
        count += syllables
    return count

# def count_syllables_in_word(word):
#     """
#     Примерно подсчитывает количество слогов в слове
#     (актуально для английского языка)
#     :param word: слово
#     :return: количество слогов
#     """
#     count = 0
#     endings = '.,;:?!'
#     last_char = word[-1]
#
#     if last_char in endings:            # убрать знаки препинания
#         processed_word = word[:-1]
#     else:
#         processed_word = word
#
#     if len(processed_word) < 3:
#         return 1
#
#     if processed_word[-1] in 'eE':              # конечная "е" не образует слог
#         processed_word = processed_word[:-1]
#
#     vowels = 'aeiouAEIOU'
#     prev_char_was_vowel = False
#     for char in processed_word:
#         if char in vowels:
#             if not prev_char_was_vowel:
#                 count += 1
#             prev_char_was_vowel = True
#         else:
#             prev_char_was_vowel = False
#
#     if processed_word[-1] in 'yY':
#         count += 1
#
#     return count

def count_syllables_in_word_rus(word):
    """
    Подсчет примерный количества слогов в слове
    для русского языка
    полагаю кол-во слогов примерно = кол-ву гласных
    :param word: слово
    :return: количество слогов
    """
    count = 0
    for char in word:
        if char in 'уеыаоэяиюУЕЫАОЭЯИЮ':
            count += 1
    return count

def count_total_sentences(text):
    count = 0
    for char in text:
        # if char == '.' or char == '?' or char == '!':
        if char in '.?!':
            count += 1
    return count

def output_results(score):
    if score >= 90:
        print(' Уровень 5-го класса')
    elif score >= 80:
        print(' Уровень 6-го класса')
    elif score >= 70:
        print(' Уровень 7-го класса')
    elif score >= 60:
        print(' Уровень 8-9-го класса')
    elif score >= 50:
        print(' Уровень 10-11-го класса')
    elif score >= 30:
        print(' Уровень студента вуза ')
    else:
        print(' Уровень выпускника вуза  ')

def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()
    total_words = len(words)
    total_sentences = count_total_sentences(text)
    total_syllables = count_syllables(words)
    # коэффициенты откорректированы для русскоязычного текста
    score = round(206.835 - 1.52 * (total_words / total_sentences)
             - 65.14 * (total_syllables / total_words))

    print(words)
    print(total_words, "слова")
    print(total_sentences, "предложений")
    print(total_syllables, "слогов")
    print("Удобочитаемость - ", score)

    output_results(score)


RUS = text_rus.text
# ENG = text_eng.text
# compute_readability(ENG)
compute_readability(RUS)
