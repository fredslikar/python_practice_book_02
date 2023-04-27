"""Программа, що підставляє замість слів в підготованому раніше тексті
інші слова, які вводить користувач і зберігає змінений текст в новому файлі.
Програма запускається через командний рядок (для цього в прогамі є import sys та перевірка sys.argv.
В командному рядку перейти в корневий каталог програми, написати:
python less_09_crazy_text_ukr.py lib.txt"""

import sys


def crazy_textionary(filename):
    """Пробує відкрити шаблонний файл, порядково обробляє його текст, закриває файл.
    Повертає оброблений (змінений текст)"""

    try:
        file = open(filename, 'r', encoding='UTF-8')
        text = ''
    except:
        print("The file can't be opening")
    for line in file:
        text = text + process_line(line)

    file.close()
    return text


def process_line(line):
    """Пословно перевіряє наявність спецслів в рядку і, при наявності таких,
    пропонує користувачу ввести відповідний тип слова.
    Замінює відповідне слово в рядку. Повертає змінений рядок слів."""

    turn_line = ''
    words = line.split()
    words_for_change = ['ДІЄСЛОВО', 'ІМЕННИК', 'ПРИКМЕТНИК']
    points = '.,:;/?!-'
    for word in words:
        znak = ' '
        for liter in word:
            if liter in points:
                word = word.strip(points)
                znak = liter + ' '
        if word in words_for_change:
            answer = input("Введіть " + word + " будьласка!!!\n")
            turn_line = turn_line + answer + znak
        else:
            turn_line = turn_line + word + znak

    return turn_line + '\n'


def save_crazy_textionary(filename, text):
    """Зберігає змінений текст в новий файл."""

    file = open(filename, 'w', encoding='UTF-8')
    file.write(text)
    file.close()


def main():
    """Перевіряє, що в командному рядку вказано дві назви файлів, якщо так -
    прогама виконується. Зберігається файл зі зміненим текстом 'crazy_'"""

    if len(sys.argv) != 2:
        print('less_09_crazy_text_ukr.py <filename>')
        print(sys.argv)
    else:
        filename = 'lib.txt'
        lib = crazy_textionary(filename)
        if lib != None:
            save_crazy_textionary('crazy_' + filename, lib)


if __name__ == '__main__':
    main()

