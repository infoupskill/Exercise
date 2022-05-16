#nest for loop

person = {
    'first_name': 'Akash',
    'last_name': 'Kumar',
    'age': 25,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)