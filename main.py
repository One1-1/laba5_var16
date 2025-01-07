"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""

from lab5.my_library import task5_1, task5_2, task5_3, task5_4, task5_5, task5_6, task5_7


def menu():
    """
    Функция предлагает выбор номера задания\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
    """

    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()

        match choice:

            case 1:
                seans = input('Ввдете какой сеанс d/e: ')
                quantity_tickets = int(input('Введите кол-во билетов: '))

                task5_1(seans, quantity_tickets)

            case 2:
                text = input('Введите текст: ')

                print(task5_2(text))

            case 3:
                text = input('Введите текст: ')
                substring = 'Введите слово после котрого надо вставить другое: '
                insert_word = input('Введите слово для подстановки: ')
                print(task5_3(text, substring, insert_word))

            case 4:
                text = input("Введите текст: ")
                start_char = input("Введите начальный символ: ")
                end_char = input("Введите конечный символ: ")

                print(task5_4(text, start_char, end_char))

            case 5:
                number = input('Введите число: ')

                task5_5(number)

            case 6:
                text = input('Введите текст: ')

                print(task5_6(text))

            case 7:
                text = 'prod1, production, product, test, produce, pro, prod_test, another_prod.'
                print(task5_7(text))

            case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break




