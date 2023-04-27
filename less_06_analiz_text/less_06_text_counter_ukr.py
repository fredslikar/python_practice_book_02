"""Визначає рівень читабельності тексту, тобто на скільки приведенний текст є складним або простим для сприйняття...
а також підраховує кількісь розділових знаків, літер, складів, слів, речень"""

def count_pointers(text):
    """Функія яка рахує розділові знаки в тексті"""
    pointers = " ,./\:'|!?;"
    count = 0
    for leters in text:
        if leters in pointers:
            count += 1
    return count

def count_liters (text):
    """Функія яка рахує літери в тексті"""
    pointers = " ,./\:'|!?;"
    count = 0
    for leters in text:
        if not leters in pointers:
            count += 1
    return count

def count_setences(text):
    """підраховує кількість речень у тексті орієнтуючість на наявність таких знаків, що зазвичай стоять в кінці речень..."""
    count = 0
    points = '.?!'
    for char in text:
        if char in points:
            count += 1
    return count

def count_syllables(words):
    """підраховує кількість складів у тексті"""
    count = 0
    for word in words:
        word_count = count_syllables_in_word(word)
        count += word_count
    return count

def count_syllables_in_word(word):
    """підраховує кількість складів в одному слові, орієнтуючись на низку умовних правил(приблизна кількість)"""

    count = 0
    endings = ',./;:?!'
    last_char = word[-1]

    if last_char in endings:
        proces_word = word[0:-1]
    else:
        proces_word = word

    if len(proces_word) <= 3:
        return 1

    if proces_word[-1] in 'eE':
        proces_word = proces_word[0:-1]
    vowels = ('aeiouyAEIOUY')
    prev_char_was_vowel = False
    for i in proces_word:
        if i in vowels:
            if not prev_char_was_vowel:
                count += 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False

    return count

def readability_level(score):
    if score >= 90:
        print("Цей рівень читабельності підійде навіть для учнів 5-го класу!")
    elif score >= 80:
        print("Цей рівень читабельності підійде навіть для учнів 6-го класу!")
    elif score >= 70:
        print("Цей рівень читабельності підійде навіть для учнів 7-го класу!")
    elif score >= 60:
        print("Цей рівень читабельності підійде навіть для учнів 8-9-го класу!")
    elif score >= 50:
        print("Цей рівень читабельності підійде навіть для учнів 10-11-го класу!")
    elif score >= 30:
        print("Цей рівень читабельності доволі складний і підійде для студентів ВУЗів!")
    else:
        print("Скоріш за все - це спеціалізований текст, оптимізований для якихось конкретних задач, і підійде вже тільки для випусників"
              "спеціалізованих ВУЗів!")

def readability(text):
    """функція, що визначає читабельність тексту, тобто на скільки приведенний текст є складним або простим для сприйняття..."""
    total_liters = 0
    total_pointers = 0
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    total_pointers = count_pointers(text)
    total_liters = count_liters(text)

    # визначаємо кількість слів у тексті
    words = text.split()
    total_words = len(words)

    # визначаємо кількість речень у тексті
    total_sentences = count_setences(text)

    # визначаємо кількість складів
    total_syllables = count_syllables(words)

    score = (206.835 - 1.015*(total_words/total_sentences) - 84.6*(total_syllables/total_words))

    # print(total_pointers, " розділових знаків у цьому тексті!")
    # print(total_liters, " літер у цьому тексті!")
    # print(total_words, " слів у цьому тексті!")
    # print(total_sentences, " речень у цьому тексті!")
    # print(total_syllables, ' складів у цьому тексті!')
    print(score, " балів зручності читання цього тексту!")
    readability_level(score)

if __name__ == "__main__":
    from ch6 import Odyssey

    print('"Одисея"')
    readability(Odyssey.text)


