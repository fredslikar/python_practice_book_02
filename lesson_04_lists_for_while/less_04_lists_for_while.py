"""Checks for presence of coconut in a smoothie"""

smoothies = ['coconut', 'strawberry', 'banana', 'tropical', 'berry']
has_coconut = [True, False, False, True, False]

i = 0
while i < len(smoothies):
    if has_coconut[i]:
        print('drink ' + '"' + smoothies[i] + '"' + ' contains coconut')
    i += 1

for i in range(len(smoothies)):
    if has_coconut[i]:
        print('drink ' + '"' + smoothies[i] + '"' + ' contains coconut')

"""Operations with lists"""

mistery1 = ['secret'] * 5
mistery2 = 'secret ' * 5
mistery3 = list(mistery2)
print(mistery1)
print(mistery2)
print(mistery3)
