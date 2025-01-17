from copy import deepcopy

people = [
    {
        'name': 'Person 1',
        'age': 20,
        'hobbies': ['Playing video games', 'Working out']
    },
    {
        'name': 'Person 2',
        'age': 25,
        'hobbies': ['Travelling', 'Playing piano']
    },
    {
        'name': 'Person 3',
        'age': 30,
        'hobbies': ['Playing guitar', 'Running']
    },
    {
        'name': 'Person 4',
        'age': 35,
        'hobbies': ['Playing saxophone', 'Reading']
    },
]

names = [person['name'] for person in people]
print(names)

older_than_twenty = all([person['age'] > 20 for person in people])
print(older_than_twenty)

people_copy = deepcopy(people)
people_copy[0]['name'] = 'Not Person 1'
print(people)
print(people_copy)

person_one, person_two, person_three, person_four = people
print(person_one)
print(person_two)
print(person_three)
print(person_four)
