"""First make list with results and list with serial numbers,
then sort both lists: results and serial number,
then select the first few values from the already sorted lists"""

scores_bulbs = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31,
                57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
solution_numbers = range(len(scores_bulbs))
solution_numbers = list(solution_numbers)


def ezy_sorted(scores, numbers):
    """Sort both lists: results and serial number"""

    re_renge = True
    coun_moves = 0
    while re_renge:
        re_renge = False
        for i in range(0, len(scores) - 1):
            if scores[i] < scores[i + 1]:
                move = scores[i]
                scores[i] = scores[i + 1]
                scores[i + 1] = move
                move = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = move
                coun_moves += 1
                re_renge = True
    print(coun_moves)


def print_first_x(scores, numbers, x=5):
    """Select the first few values from the lists"""

    print('First places for ' + str(x) + ' pretenders are:')
    for i in range(x):
        print(str(i + 1) + '.' + ' pretender # ' + str(numbers[i]) + ' with result: ', scores[i])


ezy_sorted(scores_bulbs, solution_numbers)
print_first_x(scores_bulbs, solution_numbers, 7)
print(scores_bulbs)
print(solution_numbers)
