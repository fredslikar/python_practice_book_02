"""Determines the readability of the text, i.e. how difficult or easy the given text is to understand,
    calculates the main indicators of the text,
    determines readability scores and print results."""


import Odyssey


def count_pointers(text):
    """Counts punctuation marks in text"""

    pointers = " ,./\:'|!?;"
    count = 0
    for letters in text:
        if letters in pointers:
            count += 1
    return count


def count_letters(text):
    """Counts punctuation letters in text"""

    pointers = " ,./\:'|!?;"
    count = 0
    for letters in text:
        if not letters in pointers:
            count += 1
    return count


def count_sentences(text):
    """Counts the number of sentences in the text,
    orienting to the presence of such signs,
    which usually stand at the end of sentences..."""

    count = 0
    points = '.?!'
    for char in text:
        if char in points:
            count += 1
    return count


def count_syllables(words):
    """Counts the number of syllables in the text."""

    count = 0
    for word in words:
        word_count = count_syllables_in_word(word)
        count += word_count
    return count


def count_syllables_in_word(word):
    """Counts the number of syllables in one word,
    based on a number of conditional rules (approximate number)."""

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
    """Determines the level of complexity of the text and prints result."""

    if score >= 90:
        print("This level of readability is suitable even for 5th graders!")
    elif score >= 80:
        print("This level of readability is suitable even for 6th graders!")
    elif score >= 70:
        print("This level of readability is suitable even for 7th graders!")
    elif score >= 60:
        print("This level of readability is suitable even for 8-9th graders!")
    elif score >= 50:
        print("This level of readability is suitable even for 10-11th graders!")
    elif score >= 30:
        print("This level of readability is quite complex and suitable for university students!")
    else:
        print("Most likely, this is a specialized text, "
              "optimized for some specific tasks, and is suitable only for graduates of specialized universities!")


def readability(text):
    """Determines the readability of the text, i.e. how difficult or easy the given text is to understand,
    calculates the main indicators of the text,
    determines readability scores and print results."""

    total_letters = 0
    total_pointers = 0
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    total_pointers = count_pointers(text)
    total_letters = count_letters(text)
    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)

    score = (206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words))

    print(total_pointers, " punctuation marks in this text!")
    print(total_letters, " letters in this text!")
    print(total_words, " words in this text!")
    print(total_sentences, " sentences in this text!")
    print(total_syllables, ' syllables in this text!')
    print(score, " points for ease of reading this text!")
    readability_level(score)


readability(Odyssey.text)
