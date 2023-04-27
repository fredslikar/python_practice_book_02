"""Questions and answers for choosing a style"""

face_style_standard = ['[dark]', '[short]', '[blue]', '[female]', '[yes]', '[yes]']
face_style_question = ['Color of the hair', 'Length of the hair', 'Color of the yes', 'Your gender is',
                       'Do you need a glasses', 'Do you need a beard']
programs_answer = "Your chose is"


def face_style_choice():
    for i in range(len(face_style_question)):
        answer = input(face_style_question[i] + " " + face_style_standard[i] + '? ')
        if answer == '':
            print(programs_answer + ' ' + face_style_standard[i] + '!')
        else:
            print(programs_answer + ' ' + ' [' + answer + ']')


def face_chose(question, standard):
    answer = input(question + ' ' + standard + '?')
    if answer == '':
        print('Your chose is ' + standard)
    else:
        print('Your chose is ' + answer)


# j = 0
# for i in face_style_question:
#     face_chose(i, face_style_standard[j])
#     j += 1

face_style_choice()