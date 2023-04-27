"""Finds the average age of friends"""

users = {}

users['Kim'] = {'el.post': 'kim@gmail.com', 'gender': 'f', 'age': 27, 'frends': ['Jon', 'Josh']}
users['Jon'] = {'el.post': 'jon@gmail.com', 'gender': 'm', 'age': 24, 'frends': ['Kim', 'Josh']}
users['Josh'] = {'el.post': 'josh@gmail.com', 'gender': 'm', 'age': 32, 'frends': ['Kim']}


def averege_age(name):
    """Finds the average age of friends"""

    user = users[name]
    age = []
    for i in user['frends']:
        frend = users[i]
        age.append(frend['age'])
    ave_age = sum(age) / len(age)
    return ave_age


print(averege_age('Kim'))
print(averege_age('Jon'))
print(averege_age('Josh'))
