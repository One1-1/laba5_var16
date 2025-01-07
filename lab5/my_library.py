def task5_1(seans, quantity_tickets):
    '''
    Дана строка. Если она представляет собой запись целого числа, то вывести 1;
    если вещественного (с дробной частью), то вывести 2; если строку нельзя
    преобразовать в число, то вывести 0

    :param seans: дневной или вечерний сеанс
    :param quantity_tickets: кол-во билетов
    :return: None
    '''

    price_day = 30
    price_evening = 60

    if seans == 'd':
        print(f'Цена: {price_day * quantity_tickets}')
    else:
        print(f'Цена: {price_evening * quantity_tickets}')

def task5_2(text):
    '''
    Дан текст из слов, разделенных пробелами. Определить, где расположено
    самое длинное слово фразы: в первой половине, во второй или посередине.

    :param text: вводимый текст
    :return: None
    '''

    # Разделяем текст на слова
    words = text.split()

    # Находим самое длинное слово
    longest_word = max(words, key=len)
    longest_word_length = len(longest_word)

    # позиции
    first_half = words[:len(words) // 2]
    second_half = words[len(words) // 2:]
    middle_position = len(words) % 2 == 1 and len(words) // 2

    # Проверяем, где находится самое длинное слово
    if longest_word in first_half:
        position = 'в первой половине'
    elif longest_word in second_half:
        position = 'во второй половине'
    elif middle_position and longest_word == words[len(words) // 2]:
        position = 'посередине'
    else:
        position = 'не найдено'

    print(f"Самое длинное слово '{longest_word}' расположено {position}.")

def task5_3(text, substring, insert_word):
    '''
    После каждого слова текста, заканчивающегося заданной подстрокой, вставить указанное слово.

    :param text: вводимый текст
    :param substring: слово, которое надо вставить
    :return: result
    '''


    # Разбиваем текст на слова
    words = text.split()

    # Список для хранения измененных слов
    new_words = []

    # Проходим по каждому слову в тексте
    for word in words:
        # Проверяем, заканчивается ли слово на заданную подстроку
        if word.endswith(substring):
            new_words.append(word + ' ' + insert_word)  # Вставляем слово
        else:
            new_words.append(word)  # Оставляем слово без изменений

    # Объединяем слова обратно в строку
    result = ' '.join(new_words)

    return result

def task5_4(text, start_char, end_char):
    '''
    В тексте исключить подстроку максимальной длины, начинающуюся и заканчивающуюся заданными символами.

    :param text: вводимый текст
    :param start_char: первый символ слова
    :param end_char: последний символ слова
    :return result: результат
    '''


    max_length = 0
    start_index = -1
    end_index = -1

    # Поиск подстроки максимальной длины
    for i in range(len(text)):
        if text[i] == start_char:
            for j in range(i + 1, len(text)):
                if text[j] == end_char:
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        start_index = i
                        end_index = j
                    break

    # Исключение найденной подстроки
    if start_index != -1 and end_index != -1:
        result = text[:start_index] + text[end_index + 1:]
    else:
        result = text

    return result

def task5_5(number):
    '''
    Написать регулярное выражение, которое подходит для следующих
    вариантов написания вещественных чисел: 3.14529; -255.34; 128; 1.9e10;
    123,340.00 и не подходит для 720p

    :param number:
    :return: None
    '''
    import re

    pattern = r'^[+-]?(\d+(\.\d+)?|\.\d+)([eE][+-]?\d+)?$|^\d{1,3}(,\d{3})*(\.\d+)?$'

    # Проверка каждого числа
    if re.match(pattern, number):
        print(f"{number} подходит")
    else:
        print(f"{number} не подходит")


def task5_6(text):
    '''
    В заданном тексте найти все слова, содержащие символ "@" и заканчивающиеся на ".ru".

    :param text: вводимая строка для проверки
    :return matches: результат
    '''
    import re


    pattern = r'\b\w+@\w+\.ru\b'

    matches = re.findall(pattern, text)

    return matches

def task5_7(text):
    '''
    Дан текст из некоторых слов (разделители – любые знаки препинания и / или пробел). Найти все слова, начинающиеся с «prod»

    :param text: вводиымй текст
    :return matches: результат
    '''

    import re

    pattern = r'\bprod\w*'

    matches = re.findall(pattern, text)

    return matches









